from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine import URL


class Settings(BaseSettings):

    # --- Application metadata ---
    APP_NAME: str = "TriageFlow"
    APP_VERSION: str = "0.1.0"
    ENVIRONMENT: str = "local"

    # --- Server ---
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # --- Logging ---
    LOG_LEVEL: str = "INFO"

    DATABASE_HOST: str = "localhost"
    DATABASE_PORT: int = 3306
    DATABASE_NAME: str = "rtpq"
    DATABASE_USER: str = "rtpq_app"
    DATABASE_PASSWORD: str = "changeme_app_password"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    @property
    def DATABASE_URL(self) -> str:
        return str(
            URL.create(
                drivername="mysql+pymysql",
                username=self.DATABASE_USER,
                password=self.DATABASE_PASSWORD,
                host=self.DATABASE_HOST,
                port=self.DATABASE_PORT,
                database=self.DATABASE_NAME,
            )
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()
