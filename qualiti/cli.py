from pathlib import Path

import openai
import typer

from qualiti import add_attrs
from qualiti import config
from qualiti import utils


app = typer.Typer()
openai.api_key = config.OPENAI_API_KEY


@app.command()
def file(input_path: Path, inplace: bool = True):
    """Add data-testid attributes to HTML elements in the given file.

    $ qualiti file index.html

    $ qualiti file ./src/Components/Nav.tsx --no-inplace
    """
    input_path = utils.validate_file_path(input_path)
    output_path = add_attrs.testids_to_file(input_path, inplace)
    typer.secho(f"✅ File saved to: {output_path}", fg="bright_green")


@app.command()
def add_testids(input_path: Path, inplace: bool = True):
    """Add data-testid attributes to HTML elements to each file in the given directory and its subdirectories.

    $ qualiti add-testids ./src/StoreView.tsx

    $ qualiti add-testids ./src/Components
    """
    input_path = utils.validate_path(input_path)
    output_path = add_attrs.testids_to_directory(input_path, inplace)
    typer.secho(f"✅ Files saved in dir: {output_path}", fg="bright_green")


if __name__ == "__main__":
    app()
