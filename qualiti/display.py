from rich.progress import Progress, TextColumn, BarColumn, TaskProgressColumn


def progress_bar() -> Progress:
    """Create a new Rich Progress instance."""
    return Progress(TextColumn("[progress.description]{task.description}"), BarColumn(), TaskProgressColumn())
