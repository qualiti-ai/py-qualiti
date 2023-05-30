from pathlib import Path
from typing import Dict, List

import pandas as pd
import requests
import torch
import typer
from datasets import load_dataset
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import semantic_search

from qualiti import config, utils
from qualiti.async_typer import AsyncTyper

ACCESS_TOKEN = config.get_value("HUGGINGFACE_ACCESS_TOKEN")
HEADERS = {"Authorization": f"Bearer {ACCESS_TOKEN}"}


def query(url: str, payload: Dict) -> Dict:
    """Query the HuggingFace API.

    Args:
        url: The URL of the API endpoint.
        payload: The payload to send to the API endpoint.

    Usage:
        ```
        url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"
        payload = {"inputs": ["User can change their current Account Type to Student or Teacher"], "options": {"wait_for_model": True}}
        output = query(url, payload)
        print(output)
        ```
    """
    response = requests.post(url=url, headers=HEADERS, json=payload)
    return response.json()


def encode_texts(texts: List[str], model: str = "sentence-transformers/all-MiniLM-L6-v2") -> List:
    """Encode a list of texts into a list of embeddings using a SentenceTransformer model.

    Args:
        texts: A list of texts to encode.
        model: The model to use for encoding.

    Returns:
        A list of embeddings.
    """
    transformer = SentenceTransformer(model)
    return transformer.encode(texts)


app = AsyncTyper()


@app.command()
def create_test_case_embeddings(test_cases_path: Path, column: str = "Summary", embeddings_path: str = "embeddings.csv"):
    """EXAMPLE: Create embeddings for all Test Case summaries and save them to a CSV file.

    * This is from the notebook example shown here: https://shorturl.at/sD123
    """
    df = pd.read_csv(utils.validate_path(test_cases_path).absolute())
    vectors = encode_texts(df[column].tolist())
    embeddings = pd.DataFrame(vectors)
    embeddings.to_csv(embeddings_path, index=False)
    typer.secho(f"✅ File(s) saved to: {embeddings_path}", fg="bright_green")


@app.command()
def search_test_case_embeddings(test_cases_path: Path, search: str, column: str = "Summary", top_k: int = 5, dataset_path: str = "CarlosKidman/test-cases"):
    """EXAMPLE: Search Test Case summary embeddings.

    * This is from the notebook example shown here: https://shorturl.at/sD123
    """
    # 1. Load Test Cases and Embeddings
    df = pd.read_csv(utils.validate_path(test_cases_path).absolute())
    values = df[column].tolist()
    dataset = load_dataset(dataset_path)
    test_case_embeddings = torch.from_numpy(dataset["train"].to_pandas().to_numpy()).to(torch.float)

    # 2. Convert search query to embedding
    vector = encode_texts([search])
    new_embedding = torch.FloatTensor(vector)

    # 3. Search embeddings
    results = semantic_search(new_embedding, test_case_embeddings, top_k=top_k)[0]

    # 4. Transform to something usable
    typer.secho(f"\nTop {top_k} similar Test Cases:\n", fg="bright_green")
    for i in range(len(results)):
        score = results[i]["score"]
        summary = values[results[i]["corpus_id"]]
        typer.secho(f"{score:.2f}: {summary}", fg="bright_blue")


if __name__ == "__main__":
    app()
