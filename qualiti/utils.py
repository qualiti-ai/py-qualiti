from pathlib import Path
from typing import List

import typer
from click.exceptions import FileError

from qualiti import config


def extract_code_from_completion(completion: str, code_block_seperator="```") -> str:
    # ["```", code, "```"] => [1] is just the code
    completion = completion.split(code_block_seperator)[1]
    if completion.startswith("\n"):
        completion = completion[1:]
    return completion


def get_all_files_from_directory(
    path: Path,
    glob: str = None,
    supported_files: List[str] = None,
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
    glob = glob or config.get_value("GLOB_PATTERN")
    supported_files = supported_files or config.get_value("SUPPORTED_FILES")
    files = [file for file in path.glob(glob) if file.suffix in supported_files]
    return files


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
    if not path.is_file() and not path.is_dir():
        raise FileError(path, hint="Path is not a valid file or directory object")

    typer.secho("✅ Path is valid!", fg=typer.colors.BRIGHT_GREEN)
    return path
