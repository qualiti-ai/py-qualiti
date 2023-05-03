import os
import json
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()

QUALITI_PATH = Path(__file__).parent

with (QUALITI_PATH / "qualiti.conf.json").open() as f:
    config = json.load(f)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or config.get("openai_api_key")
GLOB_PATTERN = config["files"]["glob_pattern"]
SUPPORTED_FILES = config["files"]["supported"]
