from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str
    data_dir: Path = Path("data")
    embed_model: str = "sentence-transformers/all-MiniLM-L6-v2"


settings = Settings()
