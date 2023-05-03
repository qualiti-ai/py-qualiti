from pathlib import Path

import typer
from rich.progress import Progress, TextColumn, BarColumn, TaskProgressColumn


def new_progress() -> Progress:
    """Create a new Rich Progress instance."""
    return Progress(TextColumn("[progress.description]{task.description}"), BarColumn(), TaskProgressColumn())


def validate_file_path(path: Path) -> Path:
    """Validate that the given path is a file and that it exists.

    Args:
        path: The path to be validated.

    Returns:
        The validated path.

    Raises:
        typer.BadParameter: If the path is not a file or does not exist.
    """
    typer.secho(f"\n🔍 Validating path: {path}", fg=typer.colors.BRIGHT_CYAN)

    if path is None:
        raise typer.BadParameter("Path cannot be None")
    if not path.exists():
        raise typer.BadParameter(f"Path does not exist: {path}")
    if not path.is_file():
        raise typer.BadParameter(f"Path is not to a file: {path}")

    typer.secho("✅ Path is valid!", fg=typer.colors.BRIGHT_GREEN)
    return path


def validate_folder_path(path: Path) -> Path:
    """Validate that the given path is a folder and that it exists.

    Args:
        path: The path to be validated.

    Returns:
        The validated path.

    Raises:
        typer.BadParameter: If the path is not a folder or does not exist.
    """
    typer.secho(f"\n🔍 Validating path: {path}", fg=typer.colors.BRIGHT_CYAN)

    if path is None:
        raise typer.BadParameter("Path cannot be None")
    if not path.exists():
        raise typer.BadParameter(f"Path does not exist: {path}")
    if not path.is_dir():
        raise typer.BadParameter(f"Path is not a folder: {path}")

    typer.secho("✅ Path is valid!", fg=typer.colors.BRIGHT_GREEN)
    return path
