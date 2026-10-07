import os
from typing import Optional

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")


def get_model_config() -> dict:
    return {"api_key": OPENAI_API_KEY, "model": MODEL_NAME}
