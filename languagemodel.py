from pydantic import BaseModel
from typing import Optional
from enum import Enum


class ModelProvider(str, Enum):
    OPEN_AI = "OPEN_AI"
    ANTHROPIC = "ANTHROPIC"
    GEMINI = "GEMINI"


class ModelId(str, Enum):
    CLAUDE_SONNET_4_5 = "claude-sonnet-4-5-20250929"
    OPEN_AI_GPT_4_1_MINI = "gpt-4.1-mini"
    CLAUDE_HAIKU = "claude-3-5-haiku-latest"
    OPEN_AI_GPT_5_NANO = "gpt-5-nano"
    OPEN_AI_GPT_4_1_NANO = "gpt-4.1-nano"
    OPEN_AI_GPT_4_0_MINI = "gpt-4o-mini"
    OPEN_AI_GPT_5_MINI = "gpt-5-mini"


class LanguageModel(BaseModel):
    model_provider: ModelProvider
    model_id: ModelId
    api_key: Optional[str] = None
    temperature: float = 0.2
