"""Load application settings from environment variables."""

from pydantic import BaseSettings

class Settings(BaseSettings):
    """Application settings loaded from a `.env` file or environment variables."""

    api_key: str | None = None
    db_username: str = ""
    db_password: str = ""
    db_host: str = "localhost"

    class Config:
        env_file = ".env"

settings = Settings()

DB_CREDENTIALS = {
    "DB_USERNAME": settings.db_username,
    "DB_PASSWORD": settings.db_password,
    "host": settings.db_host,
}

API_KEY = settings.api_key

__all__ = ["DB_CREDENTIALS", "API_KEY", "settings"]
