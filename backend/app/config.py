from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_env: str = "development"
    openai_api_key: str = ""
    database_url: str = "postgresql+psycopg://dang:dang@localhost:5432/dang_ai_agent"
    jwt_secret: str = "change-me"
    cors_origins: str = "*"
    text_model: str = "gpt-5.5"
    realtime_model: str = "gpt-realtime-2"
    image_model: str = "gpt-image-2"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @property
    def cors_origin_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()
