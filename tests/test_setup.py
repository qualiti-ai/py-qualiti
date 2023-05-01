import os
from dotenv import load_dotenv

load_dotenv()


def test_openai_api_key():
    assert os.getenv("OPENAI_API_KEY") is not None
