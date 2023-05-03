from pathlib import Path

import openai
import typer

from attributer.utils import new_progress


def get_completion(prompt: str, model="gpt-3.5-turbo") -> str:
    """Get AI completion for a prompt.

    NOTE: Please use good Prompt Engineering practices to ensure the best results.
    You can use ChatGPT to test your prompts before using them in this function.

    Args:
        prompt: The prompt to be completed.

    Returns:
        The AI's completion of the prompt.
    """
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # The degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


def testids_to_file(input_path: Path, inplace: bool = True) -> Path:
    """Add data-testid attributes to HTML elements in a file.

    Args:
        input_path: Path to file to be modified.
        inplace: If True, will overwrite existing file. If False, will save to a new file.
    """
    typer.secho("\n--\n", fg="bright_yellow")

    with new_progress() as progress:
        task1 = progress.add_task("Read File", total=1)
        code = input_path.read_text()
        progress.update(task1, advance=1)

    with new_progress() as progress:
        task2 = progress.add_task("Gen attrs", total=1)
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
        progress.update(task2, advance=0.33)

        completion = get_completion(prompt)
        progress.update(task2, advance=0.66)

        completion = completion.replace("```\n", "")
        completion = completion.replace("```", "")
        progress.update(task2, advance=1)

    with new_progress() as progress:
        task3 = progress.add_task("Save File", total=1)
        if inplace:
            output_path = input_path
        else:
            output_path = input_path.parent / f"{input_path.stem}.testids{input_path.suffix}"

        output_path.write_text(completion)
        progress.update(task3, advance=1)

    typer.secho("\n--\n", fg="bright_yellow")
    return output_path
