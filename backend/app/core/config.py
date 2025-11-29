from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """App configuration settings."""

    model_config = {"env_prefix": "WEATHER_", "env_file": ".env", "env_file_encoding": "utf-8"}

    PROJECT_NAME: str = "Weather API"
    API_V1_STR: str = "/api/v1"
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://frontend:3000"]

    OPEN_METEO_BASE_URL: AnyHttpUrl = "https://api.open-meteo.com/v1"
    GEOCODING_BASE_URL: AnyHttpUrl = "https://geocoding-api.open-meteo.com/v1"

    CACHE_TTL_SECONDS: int = 300


settings = Settings()
