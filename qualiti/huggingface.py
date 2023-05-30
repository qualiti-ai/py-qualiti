from typing import Dict, List

import config
import requests
from huggingface_hub import login
from rich.console import Console
from sentence_transformers import SentenceTransformer

ACCESS_TOKEN = config.get_value("HUGGINGFACE_ACCESS_TOKEN")
HEADERS = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
login(ACCESS_TOKEN)


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
    """Encode a list of texts into a list of embeddings.

    Args:
        texts: A list of texts to encode.
        model: The model to use for encoding.

    Returns:
        A list of embeddings.
    """
    transformer = SentenceTransformer(model)
    return transformer.encode(texts)


if __name__ == "__main__":
    console = Console()

    # Use the HuggingFace API to get the embeddings for a list of texts
    url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"
    payload = {"inputs": ["User can change their current Account Type to Student or Teacher"], "options": {"wait_for_model": True}}
    output = query(url, payload)

    # You can also use a local model instead
    # output = encode_texts(["User can change their current Account Type to Student or Teacher"])
    console.print(output)
