from pathlib import Path

import openai
import typer

from attributer import add
from attributer import config
from attributer import utils


app = typer.Typer()
openai.api_key = config.OPENAI_API_KEY


@app.command()
def file(input_path: Path, inplace: bool = True):
    """Add data-testid attributes to HTML elements in the given file

    $ attributer file index.html

    $ attributer file ./src/Components/Nav.tsx --no-inplace
    """
    input_path = utils.validate_file_path(input_path)
    output_path = add.testids_to_file(input_path, inplace)
    typer.secho(f"✅ Saved to {output_path}", fg="bright_green")


@app.command()
def folder(input_path: Path, inplace: bool = True):
    """! NOT IMPLEMENTED YET ! Add data-testid attributes to HTML elements for each file in the given folder

    $ attributer folder ./src/Home/Nav

    $ attributer folder ./src/Components --no-inplace
    """
    input_path = utils.validate_folder_path(input_path)
    # add.testids_to_folder(input_path, output_path)


if __name__ == "__main__":
    app()
