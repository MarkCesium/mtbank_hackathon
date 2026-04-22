import logging
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field, PostgresDsn
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent.parent


class LoggingConfig(BaseModel):
    level: Literal[
        "debug",
        "info",
        "warning",
        "error",
        "critical",
    ] = Field(default="info")
    format: str = Field(
        default="[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"
    )
    date_format: str = Field(default="%Y-%m-%d %H:%M:%S")

    @property
    def level_value(self) -> int:
        return logging.getLevelNamesMapping()[self.level.upper()]


class PostgresConfig(BaseModel):
    url: PostgresDsn = Field(...)
    echo: bool = Field(default=False)
    echo_pool: bool = Field(default=False)
    pool_size: int = Field(default=10)
    max_overflow: int = Field(default=5)
    pool_pre_ping: bool = Field(default=True)
    pool_timeout: int = Field(default=30)


class JWTConfig(BaseModel):
    secret: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 30


class AppConfig(BaseModel):
    debug: bool = Field(default=True)
    generate_openapi_file: bool = Field(default=True)
    openapi_file_path: str = Field(default="var/app/openapi.json")
    allowed_origins: list[str] = Field(default=["*"])


class Settings(BaseSettings):
    app: AppConfig = Field(default_factory=AppConfig)
    logging: LoggingConfig = Field(default_factory=LoggingConfig)
    database: PostgresConfig = Field(...)
    jwt: JWTConfig = Field(...)

    class Config:
        env_file = BASE_DIR / ".env"
        env_file_encoding = "utf-8"
        env_nested_delimiter = "__"


settings = Settings()  # type: ignore[call-arg]
