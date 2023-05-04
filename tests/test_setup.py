import json
import os

import pytest

from qualiti import config


@pytest.fixture()
def reset_config():
    yield
    config._set_config(
        {
            "OPENAI_API_KEY": "",
            "GLOB_PATTERN": "**/*",
            "SUPPORTED_FILES": [".html", ".jsx", ".tsx", ".vue"],
        }
    )


def test_openai_api_key():
    assert os.getenv("OPENAI_API_KEY") is not None


def test_default_qualiti_conf_json():
    assert config.get_value("GLOB_PATTERN") == "**/*"
    assert config.get_value("SUPPORTED_FILES") == [".html", ".jsx", ".tsx", ".vue"]


def test_set_config_value():
    config.set_value("GLOB_PATTERN", "**/.component.*")
    assert config.get_value("GLOB_PATTERN") == "**/.component.*"


def test_set_config_value_and_persist(reset_config):
    config.set_value("GLOB_PATTERN", "**/.component.*", persist=True)
    assert config.get_value("GLOB_PATTERN") == "**/.component.*"

    with open(config.QUALITI_PATH / "qualiti.conf.json") as file:
        conf_file = json.load(file)

    assert conf_file["GLOB_PATTERN"] == "**/.component.*"
