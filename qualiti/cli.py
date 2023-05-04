from pathlib import Path

import openai
import typer

from qualiti import attributer, config, utils

app = typer.Typer()
openai.api_key = config.OPENAI_API_KEY


@app.command()
def add_testids(input_path: Path, inplace: bool = True):
    """Add data-testid attributes to HTML elements to a file or each file in the given directory and its subdirectories.

    $ qualiti add-testids ./examples/StoreView.tsx

    $ qualiti add-testids ./examples/SubComponents
    """
    input_path = utils.validate_path(input_path)
    output_path = attributer.testids(input_path, inplace)
    typer.secho(f"✅ File(s) saved to: {output_path}", fg="bright_green")


@app.command()
def set_env(key: str, value: str):
    """Set the given environment variable in your shell's configuration file.

    $ qualiti set-env OPENAI_API_KEY <your-api-key>
    """
    utils.set_environment_variable(key, value)
    typer.secho(f"✅ Environment variable set: {key}={value}", fg="bright_green")


if __name__ == "__main__":
    app()
