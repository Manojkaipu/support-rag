from pathlib import Path

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

# USD per million tokens: input, output, cache read, cache write. Used for Anthropic, and for xAI
# only when a response lacks usage.cost_in_usd_ticks (the billed cost).
PRICES = {
    "claude-opus-5": (5.00, 25.00, 0.50, 6.25),
    "claude-opus-4-8": (5.00, 25.00, 0.50, 6.25),  # refusal fallback target
    "claude-sonnet-5": (2.00, 10.00, 0.20, 2.50),
    "claude-haiku-4-5": (1.00, 5.00, 0.10, 1.25),
    "grok-4.7": (2.00, 6.00, 0.50, 2.00),  # prompts under 200k tokens
    "grok-4.3": (1.25, 2.50, 0.20, 1.25),
}

DEFAULT_MODELS = {"anthropic": "claude-opus-5", "xai": "grok-4.7"}


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str
    data_dir: Path = Path("data")
    embed_model: str = "sentence-transformers/all-MiniLM-L6-v2"

    llm_provider: str = "xai"  # xai | anthropic
    xai_api_key: str | None = None  # Anthropic's SDK reads ANTHROPIC_API_KEY itself
    agent_model: str | None = None  # default: the provider's model in DEFAULT_MODELS
    verifier_model: str | None = None
    judge_model: str | None = None
    agent_effort: str = "high"
    verifier_effort: str = "medium"
    max_agent_turns: int = 8
    max_answer_retries: int = 2

    cors_origins: list[str] = ["http://localhost:3000"]

    @model_validator(mode="after")
    def default_models(self):
        default = DEFAULT_MODELS.get(self.llm_provider)
        if default is None:
            raise ValueError(f"llm_provider must be one of {list(DEFAULT_MODELS)}")
        self.agent_model = self.agent_model or default
        self.verifier_model = self.verifier_model or default
        self.judge_model = self.judge_model or default
        return self


settings = Settings()
