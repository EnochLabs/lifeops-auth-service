from typing import List, Optional, Union

from pydantic import AnyHttpUrl, TypeAdapter, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # App Settings
    APP_NAME: str = "LifeOps Auth Service"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    PORT: int = 8001
    SERVICE_HOST: str = "0.0.0.0"  # nosec B104

    # MongoDB Settings
    MONGODB_URL: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "lifeops_auth"

    # Redis Settings
    REDIS_URL: str = "redis://localhost:6379/0"

    # Security Settings
    SECRET_KEY: str = "secret-key-for-development-only"
    ALGORITHM: str = "RS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30
    INTERNAL_API_KEY: str = "change-this-to-a-long-random-string"

    # JWT RSA Keys
    JWT_PRIVATE_KEY_PATH: Optional[str] = None
    JWT_PUBLIC_KEY_PATH: Optional[str] = None

    # Cookie Settings
    COOKIE_SECURE: bool = False
    COOKIE_SAMESITE: str = "lax"

    # CORS Settings
    CORS_ALLOWED_ORIGINS: Union[str, List[AnyHttpUrl]] = [
        TypeAdapter(AnyHttpUrl).validate_python("http://localhost:3000")
    ]

    @field_validator("CORS_ALLOWED_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # Subscription Settings
    TRIAL_DURATION_DAYS: int = 7
    TRIAL_PLAN: str = "PRO"
    SUBSCRIPTION_GRACE_PERIOD_DAYS: int = 3

    # Logging
    LOG_LEVEL: str = "INFO"
    JSON_LOGS: bool = False

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=True, extra="ignore"
    )


settings = Settings()
