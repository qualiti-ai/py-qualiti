import json
import os
import platform
from pathlib import Path
from typing import Dict

import typer
from dotenv import load_dotenv

from qualiti.async_typer import AsyncTyper

QUALITI_PATH = Path(__file__).parent


def _load_config() -> Dict:
    """Load the configuration file."""
    with (QUALITI_PATH / "qualiti.conf.json").open("r") as file:
        conf = json.load(file)
    return conf


def _set_config(conf: Dict) -> None:
    """Overwrite the entire configuration file."""
    with (QUALITI_PATH / "qualiti.conf.json").open("w") as file:
        json.dump(conf, file, indent=2)


load_dotenv()
config = _load_config()


def get_value(key: str) -> any:
    """Get the value of the given key.

    Looks in environment variables first, then the config of the current session."""
    return os.getenv(key) or config.get(key)


def set_value(key: str, value: str, persist: bool = False) -> None:
    """Set the value for the given key for the current session.

    Args:
        key: The key to set.
        value: The value to set.
        persist: Whether to update the value to the config file permanently.
    """
    config[key] = value

    if persist:
        _set_config(config)


def set_environment_variable(key: str, value: str) -> None:
    """Set the given environment variable in the user's shell configuration file.

    Args:
        key: The name of the environment variable.
        value: The value of the environment variable.
    """
    WINDOWS = "Windows"
    UNIX = ["Darwin", "Linux"]

    # Set the environment variable in the current session
    os.environ[key] = value

    # Get the user's shell configuration file
    if platform.system() == WINDOWS:
        config_file = os.path.expanduser("~\\AppData\\Local\\Microsoft\\Windows\\PowerShell\\profile.ps1")
    elif platform.system() in UNIX:
        shell = os.path.basename(os.environ["SHELL"])
        if shell == "bash":
            config_file = os.path.expanduser("~/.bashrc")
        elif shell == "zsh":
            config_file = os.path.expanduser("~/.zshrc")
        else:
            # Handle other shells here
            config_file = None
    else:
        # Handle other operating systems here
        config_file = None

    # Append the environment variable to the user's shell configuration file
    if config_file:
        with open(config_file, "a") as file:
            if platform.system() == WINDOWS:
                file.write(f'\n$env:{key}="{value}"\n')
            elif platform.system() in UNIX:
                file.write(f'\nexport {key}="{value}"\n')


app = AsyncTyper()


@app.command()
def get_conf(key: str):
    """Get the value of the given key from qualiti.conf.json.

    $ qualiti conf get-conf SUPPORTED_FILES
    """
    value = config.get(key)
    if value:
        typer.secho(f"\n{value}", fg="bright_green")
    else:
        typer.secho("\n❌ Not found in config", fg="bright_yellow")
        typer.secho("Try setting it with: qualiti conf set-conf <key> <value>")


@app.command()
def get_env(key: str):
    """Get the value of the given key from environment variables.

    $ qualiti conf get-env OPENAI_API_KEY
    """
    value = os.getenv(key)
    if value:
        typer.secho(f"\n{value}", fg="bright_green")
    else:
        typer.secho("\n❌ Not found in environment variables", fg="bright_yellow")
        typer.secho("Try setting it with: qualiti conf set-env <key> <value>")


@app.command()
def set_conf(key: str, value: str):
    """Set the given key and value in qualiti.conf.json.

    $ qualiti conf set-conf GLOB_PATTERN "**/*.component.*"
    """
    # TODO: Support non-string values like lists and dictionaries
    set_value(key, value, persist=True)
    typer.secho(f"✅ Config updated: {key}={value}", fg="bright_green")


@app.command()
def set_env(key: str, value: str):
    """Set the given environment variable in your shell's configuration file.

    $ qualiti set-env OPENAI_API_KEY <your-api-key>
    """
    # TODO: Add a check to see if the environment variable is already set
    # to avoid adding duplicate entries to the shell configuration file
    set_environment_variable(key, value)
    typer.secho(f"✅ Environment variable set: {key}={value}", fg="bright_green")


@app.command()
def show_conf():
    """Show the entire configuration file."""
    typer.secho("\nNOTE: API Keys and Secrets are better stored in Environment Variables", fg="bright_blue")
    typer.secho(json.dumps(config, indent=2), fg="bright_green")


if __name__ == "__main__":
    app()
