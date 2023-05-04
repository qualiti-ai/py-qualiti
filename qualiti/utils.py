import os
import platform
from pathlib import Path
from typing import List

import typer
from click.exceptions import FileError

from qualiti import config


def get_all_files_from_directory(
    path: Path,
    glob: str = config.GLOB_PATTERN,
    supported_files: List[str] = config.SUPPORTED_FILES,
) -> List[Path]:
    """Get all files from the given directory and its subdirectories.

    NOTE: The default for `glob` and `supported_files` are set in `qualiti.conf.json`.

    Args:
        path: The path to the directory to search.
        glob: The glob pattern to use when searching for files (default: all files).
        supported_files: The file extensions to include in the search (default: all supported files).

    Returns:
        A list of all files in the given directory and its subdirectories.
    """
    files = [file for file in path.glob(glob) if file.suffix in supported_files]
    return files


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


def validate_path(path: Path) -> Path:
    """Validate that the given path is a file or directory and that it exists.

    Args:
        path: The path to be validated.

    Returns:
        The validated path.

    Raises:
        typer.BadParameter: If the path is not a file or directory or does not exist.
    """
    typer.secho(f"\n🔍 Validating path: {path}", fg=typer.colors.BRIGHT_CYAN)

    if path is None:
        raise typer.BadParameter("Path cannot be None")
    if not path.exists():
        raise typer.BadParameter(f"Path does not exist: {path}")
    if not path.is_file() and not path.is_dir():  # pragma: no cover
        raise FileError(path, hint="Path is not a valid file or directory object")

    typer.secho("✅ Path is valid!", fg=typer.colors.BRIGHT_GREEN)
    return path
