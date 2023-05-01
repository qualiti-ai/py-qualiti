import os
from pathlib import Path

import openai
from dotenv import load_dotenv


load_dotenv()


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


def add_data_testids(input_path: str, output_path: str) -> str:
    # 1. Read file
    code = Path(input_path).read_text()

    # 2 Generate prompt
    prompt = f"""
        Given the following code in the backticks ``` below, do the following:

        1. Identify all relevant HTML elements
        2. For each element, add ONLY a unique and helpful `data-testid` attribute if it doesn't already have one
        3. Do NOT add any comments or docstrings
        4. Respond with ONLY the new code

        ```
        {code}
        ```
        """

    # 3. Get AI completion
    completion = get_completion(prompt)
    completion = completion.replace("```\n", "")
    completion = completion.replace("\n```", "")

    # 4. Save as new file
    Path(output_path).write_text(completion)


def main():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    add_data_testids("./examples/StoreView.tsx", "./examples/StoreView.test.tsx")


if __name__ == "__main__":
    main()
