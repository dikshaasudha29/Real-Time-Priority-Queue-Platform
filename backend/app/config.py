from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Centralized application configuration.
    Values are loaded from environment variables or .env.
    """

    # Application Settings
    APP_NAME: str = "Telehealth Smart-Triage System"
    DEBUG: bool = False
    API_V1_PREFIX: str = "/api/v1"

    # MySQL Settings
    MYSQL_HOST: str = Field(
        default="localhost",
        alias="DB_HOST"
    )

    MYSQL_PORT: int = Field(
        default=3306,
        alias="DB_PORT"
    )

    MYSQL_USER: str = Field(
        default="root",
        alias="DB_USER"
    )

    MYSQL_PASSWORD: str = Field(
        default="password",
        alias="DB_PASSWORD"
    )

    MYSQL_DATABASE: str = Field(
        default="triage_db",
        alias="DB_NAME"
    )

    # Redis Settings
    REDIS_HOST: str = Field(
        default="localhost",
        alias="REDIS_HOST"
    )

    REDIS_PORT: int = Field(
        default=6379,
        alias="REDIS_PORT"
    )

    # Queue Aging Configuration
    AGING_INTERVAL_SECONDS: int = 10
    AGING_INCREMENT: int = 1

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    @property
    def database_url(self) -> str:
        """
        Builds the SQLAlchemy database URL.
        """
        return (
            f"mysql+pymysql://"
            f"{self.MYSQL_USER}:"
            f"{self.MYSQL_PASSWORD}@"
            f"{self.MYSQL_HOST}:"
            f"{self.MYSQL_PORT}/"
            f"{self.MYSQL_DATABASE}"
        )


settings = Settings()