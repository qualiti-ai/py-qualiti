import openai

from qualiti.async_typer import AsyncTyper
from qualiti import attributer, config


openai.api_key = config.get_value("OPENAI_API_KEY")
app = AsyncTyper()
app.add_typer(attributer.app, name="attr", help="Add attributes to HTML elements.")
app.add_typer(config.app, name="conf", help="Set and Get configuration values.")


if __name__ == "__main__":
    app()
