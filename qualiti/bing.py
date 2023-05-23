import asyncio
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List

from EdgeGPT import Chatbot, ConversationStyle
from rich.console import Console

from qualiti import utils

console = Console()


def load_cookies(cookies_path: str) -> List[Dict]:
    path = Path(cookies_path)
    if not path.exists():
        raise FileNotFoundError(f"Could not find cookies file at {cookies_path}")

    with path.open() as file:
        cookies = json.load(file)

    # Add 30 days to today's date and set as expiration date
    thirty_days = 2592000
    expiration = "expirationDate"

    for cookie in cookies:
        if cookie.get(expiration):
            cookie[expiration] = datetime.now().timestamp() + thirty_days

    return cookies


class BingChat:
    """ContextManager for Bing Chatbot.

    Usage:
        ```
        async with BingChat() as bot:
            response = await bot.ask(prompt="Tell me a joke", conversation_style=ConversationStyle.precise)

        print(response)
        ```
    """

    def __init__(self, cookies_path: str = None):
        self.cookies = load_cookies(cookies_path) if cookies_path else None

    async def __aenter__(self):
        self.bot = await Chatbot.create(cookies=self.cookies)
        return self

    async def ask(
        self,
        prompt: str,
        wss_link: str = "wss://sydney.bing.com/sydney/ChatHub",
        conversation_style: ConversationStyle = ConversationStyle.precise,
        options: dict = None,
        webpage_context: str | None = None,
        search_result: bool = False,
    ) -> Dict:
        """Ask a question to the bot and return its response."""
        response = await self.bot.ask(prompt, wss_link, conversation_style, options, webpage_context, search_result)
        return response["item"]["messages"][1]["text"]

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.bot.close()


TESTID_PROMPT = """
    Given the following code in the backticks ``` below, do the following:

    1. Identify all relevant HTML elements
    2. For each element, add ONLY a unique and helpful `data-testid` attribute if it doesn't already have one
    3. Do NOT add any comments or docstrings
    4. Respond with ONLY the new code block surrounded by ```

    ```
    {0}
    ```
"""


async def main():
    """Great for testing out prompts with BingChat.

    Usage:
        ```
        python qualiti/bing.py
        ```
    """
    # 1. Get the code text from a file
    code = Path("examples/plans.component.html").read_text()
    # code = Path("examples/StoryView.tsx").read_text()

    # 2. Ask the bot to add data-testid attributes to the code
    async with BingChat() as bot:
        response = await bot.ask(prompt=TESTID_PROMPT.format(code), conversation_style=ConversationStyle.precise)

    console.print(response)
    console.print("\n")

    # 3. Extract only the code since BingChat doesn't do a great job of "listening" to instructions compared to OpenAI's GPT-3.5-Turbo
    completion = utils.extract_code_from_completion(response, code_block_seperator="```")

    # 4. Do something with the new code (ie save it to a file)
    console.print(completion)


if __name__ == "__main__":
    asyncio.run(main())
