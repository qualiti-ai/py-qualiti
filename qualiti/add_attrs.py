from pathlib import Path

import typer

from qualiti import ai
from qualiti import display
from qualiti import utils


PROMPT = """
    Given the following code in the backticks ``` below, do the following:

    1. Identify all relevant HTML elements
    2. For each element, add ONLY a unique and helpful `data-testid` attribute if it doesn't already have one
    3. Do NOT add any comments or docstrings
    4. Respond with ONLY the new code

    ```
    {0}
    ```
"""


def testids(input_path: Path, inplace: bool = True) -> Path:
    """Add data-testid attributes to HTML elements in a file or folder.

    Args:
        input_path: Path to file or folder to be modified.
        inplace: If True, will overwrite existing file. If False, will save to a new file.

    Returns:
        Path to the modified file or folder.
    """
    if input_path.is_file():
        return testids_to_file(input_path, inplace)
    elif input_path.is_dir():
        return testids_to_directory(input_path, inplace)
    else:
        raise typer.BadParameter(f"Path is not to a file or folder: {input_path}")


def testids_to_file(input_path: Path, inplace: bool = True) -> Path:
    """Add data-testid attributes to HTML elements in a file.

    Args:
        input_path: Path to file to be modified.
        inplace: If True, will overwrite existing file. If False, will save to a new file.

    Returns:
        Path to the modified file.
    """
    typer.secho("\n--\n", fg="bright_yellow")

    with display.progress_bar() as progress:
        task1 = progress.add_task("Read File", total=1)
        code = input_path.read_text()
        progress.update(task1, advance=1)

    with display.progress_bar() as progress:
        task2 = progress.add_task("Gen attrs", total=1)
        # prompt = f"""
        #     Given the following code in the backticks ``` below, do the following:

        #     1. Identify all relevant HTML elements
        #     2. For each element, add ONLY a unique and helpful `data-testid` attribute if it doesn't already have one
        #     3. Do NOT add any comments or docstrings
        #     4. Respond with ONLY the new code

        #     ```
        #     {code}
        #     ```
        #     """
        prompt = PROMPT.format(code)
        progress.update(task2, advance=0.33)

        completion = ai.get_completion(prompt)
        progress.update(task2, advance=0.66)

        completion = completion.replace("```\n", "")
        completion = completion.replace("```", "")
        progress.update(task2, advance=1)

    with display.progress_bar() as progress:
        task3 = progress.add_task("Save File", total=1)
        if inplace:
            output_path = input_path
        else:
            output_path = input_path.parent / f"{input_path.stem}.testids{input_path.suffix}"

        output_path.write_text(completion)
        progress.update(task3, advance=1)

    typer.secho("\n--\n", fg="bright_yellow")
    return output_path


def testids_to_directory(input_path: Path, inplace: bool = True) -> Path:
    """Add data-testid attributes to HTML elements in every file of the given directory and its subdirectories.

    Args:
        input_path: Path to directory to be modified.
        inplace: If True, will overwrite existing files. If False, will save to new files.

    Returns:
        Path to the modified directory.
    """
    typer.secho("\n--\n", fg="bright_yellow")
    files = utils.get_all_files_from_directory(input_path)

    with display.progress_bar() as progress:
        task = progress.add_task("Processing Files...", total=len(files))
        for file in files:
            code = file.read_text()
            prompt = PROMPT.format(code)
            completion = ai.get_completion(prompt)
            completion = completion.replace("```\n", "")
            completion = completion.replace("```", "")
            if inplace:
                output_path = file
            else:
                output_path = file.parent / f"{file.stem}.testids{file.suffix}"

            output_path.write_text(completion)
            progress.update(task, advance=1)

    typer.secho("\n--\n", fg="bright_yellow")
    return input_path
