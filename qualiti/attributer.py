from pathlib import Path

import typer

from qualiti import ai, display, utils
from qualiti.async_typer import AsyncTyper


TESTID_PROMPT = """
    Given the following code in the backticks ``` below, do the following:

    1. Identify all relevant HTML elements
    2. For each element, add ONLY a unique and helpful `data-testid` attribute if it doesn't already have one
    3. Do NOT add any comments or docstrings
    4. Respond with ONLY the new code surrounded by ```

    ```
    {0}
    ```
"""


def testids(input_path: Path, inplace: bool = True, model: str = "gpt-3.5-turbo") -> Path:
    """Add data-testid attributes to HTML elements in a file or all files in a directory and its subdirectories.

    Args:
        input_path: Path to file or directory to be modified.
        inplace: If True, will overwrite each existing file. If False, will save to a new file.
        model: Specify which model to use. If "bing", use BingChat

    Returns:
        Path to the modified file or directory.
    """
    if input_path.is_file():
        return testids_to_file(input_path, inplace, model)
    elif input_path.is_dir():
        return testids_to_directory(input_path, inplace, model)
    else:
        raise typer.BadParameter(f"Path is not to a file or directory: {input_path}")


def testids_to_file(input_path: Path, inplace: bool = True, model: str = "gpt-3.5-turbo") -> Path:
    """Add data-testid attributes to HTML elements in a file.

    Args:
        input_path: Path to file to be modified.
        inplace: If True, will overwrite existing file. If False, will save to a new file.
        model: Specify which model to use. If "bing", use BingChat

    Returns:
        Path to the modified file.
    """
    typer.secho("\n--\n", fg="bright_yellow")

    with display.progress_bar() as progress:
        task1 = progress.add_task("(1/3) Read File", total=1)
        code = input_path.read_text()
        progress.update(task1, advance=1)

    with display.progress_bar() as progress:
        task2 = progress.add_task("(2/3) Gen attrs", total=1)

        prompt = TESTID_PROMPT.format(code)
        progress.update(task2, advance=0.33)

        completion = ai.get_completion(prompt, model=model)
        progress.update(task2, advance=0.66)

        code = utils.extract_code_from_completion(completion)
        progress.update(task2, advance=1)

    with display.progress_bar() as progress:
        task3 = progress.add_task("(3/3) Save File", total=1)
        output_path = _set_output_path(input_path, inplace)
        output_path.write_text(code)
        progress.update(task3, advance=1)

    typer.secho("\n--\n", fg="bright_yellow")
    return output_path


def testids_to_directory(input_path: Path, inplace: bool = True, model: str = "gpt-3.5-turbo") -> Path:
    """Add data-testid attributes to HTML elements in every file of the given directory and its subdirectories.

    Args:
        input_path: Path to directory to be modified.
        inplace: If True, will overwrite each existing file. If False, will save to new files.
        model: Specify which model to use. If "bing", use BingChat

    Returns:
        Path to the modified directory.
    """
    typer.secho("\n--\n", fg="bright_yellow")
    files = utils.get_all_files_from_directory(input_path)

    with display.progress_bar() as progress:
        task = progress.add_task("Generating data-testid attributes...", total=len(files))
        for file in files:
            code = file.read_text()
            prompt = TESTID_PROMPT.format(code)

            completion = ai.get_completion(prompt, model=model)
            code = utils.extract_code_from_completion(completion)

            output_path = _set_output_path(file, inplace)
            output_path.write_text(code)
            progress.update(task, advance=1)

    typer.secho("\n--\n", fg="bright_yellow")
    return input_path


def _set_output_path(input_path: Path, inplace: bool) -> Path:
    """Set the output path, for the file to be saved to, based on the input path and the inplace flag.

    Args:
        input_path: Path to file or directory to be modified.
        inplace: If True, use the existing file name. If False, make a new file name at the same location.

    Returns:
        Path to the modified file.
    """
    if inplace:
        output_path = input_path
    else:
        output_path = input_path.parent / f"{input_path.stem}.testids{input_path.suffix}"
    return output_path


app = AsyncTyper()


@app.command("testid")
def add_testids(input_path: Path, inplace: bool = True, model: str = "gpt-3.5-turbo"):
    """Add data-testid attributes to HTML elements in a file or each file in the given directory and its subdirectories.

    * Default: "gpt-3.5-turbo", but can use "gpt-4" if you have access

    $ qualiti attr testid ./examples/StoryView.tsx

    $ qualiti attr testid ./examples/SubComponents --model "gpt-4"
    """
    input_path = utils.validate_path(input_path)
    output_path = testids(input_path, inplace, model)
    typer.secho(f"✅ File(s) saved to: {output_path}", fg="bright_green")


if __name__ == "__main__":
    app()
