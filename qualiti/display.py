from rich.progress import BarColumn, Progress, TaskProgressColumn, TextColumn


def progress_bar() -> Progress:
    """Create a new Rich Progress instance."""
    return Progress(TextColumn("[progress.description]{task.description}"), BarColumn(), TaskProgressColumn())
