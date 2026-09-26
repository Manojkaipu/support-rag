from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# USD per million tokens: input, output, cache read, cache write (5-minute TTL)
PRICES = {
    "claude-opus-5": (5.00, 25.00, 0.50, 6.25),
    "claude-opus-4-8": (5.00, 25.00, 0.50, 6.25),  # refusal fallback target
    "claude-sonnet-5": (2.00, 10.00, 0.20, 2.50),
    "claude-haiku-4-5": (1.00, 5.00, 0.10, 1.25),
}


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str
    data_dir: Path = Path("data")
    embed_model: str = "sentence-transformers/all-MiniLM-L6-v2"

    agent_model: str = "claude-opus-5"
    agent_effort: str = "high"
    verifier_model: str = "claude-opus-5"
    verifier_effort: str = "medium"
    judge_model: str = "claude-opus-5"
    max_agent_turns: int = 8
    max_answer_retries: int = 2

    cors_origins: list[str] = ["http://localhost:3000"]


settings = Settings()
