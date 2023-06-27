from typing import Any

from pydantic import BaseSettings, RedisDsn, root_validator

from src.constants import Environment


class Config(BaseSettings):
    # DATABASE_URL: str
    
    # DATABASE_USERNAME: str
    # DATABASE_PASSWORD: str
    # DATABASE_HOST: str
    # DATABASE_PORT: str
    # DATABASE_NAME: str

    REDIS_URL: RedisDsn

    SITE_DOMAIN: str = "myapp.com"

    ENVIRONMENT: Environment = Environment.PRODUCTION

    SENTRY_DSN: str | None

    CORS_ORIGINS: list[str]
    CORS_ORIGINS_REGEX: str | None
    CORS_HEADERS: list[str]

    APP_VERSION: str = "1"
    
    # Fireblock configuration
    # FIREBLOCK_API_KEY: str
    # FIREBLOCK_API_URL: str
    
    # Withdrawal Pool
    # WITHDRAWAL_POOL_ACCOUNT_ID: int
    

    class Config:
        env_file = ".env"

    @root_validator(skip_on_failure=True)
    def validate_sentry_non_local(cls, data: dict[str, Any]) -> dict[str, Any]:
        if data["ENVIRONMENT"].is_deployed and not data["SENTRY_DSN"]:
            raise ValueError("Sentry is not set")

        return data


settings = Config()

app_configs: dict[str, Any] = {"title": "App API"}
if settings.ENVIRONMENT.is_deployed:
    app_configs["root_path"] = f"/v{settings.APP_VERSION}"

if not settings.ENVIRONMENT.is_debug:
    app_configs["openapi_url"] = None  # hide docs
