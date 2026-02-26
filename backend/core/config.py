"""Application configuration helpers."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Runtime configuration loaded from environment variables."""

    app_name: str = "AI Call Attender"
    app_version: str = "1.0.0"
    environment: str = "development"
    cors_allow_origins: tuple[str, ...] = ("*",)



def _parse_cors_origins(raw_origins: str) -> tuple[str, ...]:
    origins = tuple(origin.strip() for origin in raw_origins.split(",") if origin.strip())
    return origins or ("*",)



def get_settings() -> Settings:
    """Build a settings instance from environment variables."""

    return Settings(
        app_name=os.getenv("APP_NAME", "AI Call Attender"),
        app_version=os.getenv("APP_VERSION", "1.0.0"),
        environment=os.getenv("APP_ENV", "development"),
        cors_allow_origins=_parse_cors_origins(os.getenv("CORS_ALLOW_ORIGINS", "*")),
    )
