from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # App Settings
    APP_NAME: str = "LifeOps Auth Service"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    PORT: int = 8001

    # MongoDB Settings
    MONGODB_URL: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "lifeops_auth"

    # Redis Settings
    REDIS_URL: str = "redis://localhost:6379/0"

    # Security Settings
    SECRET_KEY: str = "secret-key-for-development-only"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30

    # JWT RSA Keys (Blueprint mentions RS256)
    JWT_PRIVATE_KEY_PATH: Optional[str] = None
    JWT_PUBLIC_KEY_PATH: Optional[str] = None

    # Logging
    LOG_LEVEL: str = "INFO"
    JSON_LOGS: bool = False

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=True, extra="ignore"
    )


settings = Settings()
