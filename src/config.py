from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass
class LoggingConfig:
    level: str = "INFO"
    format: str = "%(levelname)s: %(message)s"


@dataclass
class AppConfig:
    name: str = "App"
    version: str = "0.1.0"


@dataclass
class Config:
    app: AppConfig
    logging: LoggingConfig


def load_config(config_path: Path | None = None) -> Config:
    if config_path is None:
        config_path = Path(__file__).parent.parent / "data" / "config" / "config.cue"

    config_data: dict[str, dict[str, str]] = {}

    try:
        result = subprocess.run(
            ["cue", "export", str(config_path)],
            capture_output=True,
            text=True,
            check=True,
        )
        config_data = json.loads(result.stdout)
    except (subprocess.CalledProcessError, FileNotFoundError, json.JSONDecodeError):
        pass

    app_data: dict[str, str] = config_data.get("app", {})
    logging_data: dict[str, str] = config_data.get("logging", {})

    return Config(
        app=AppConfig(
            name=app_data.get("name", "App"),
            version=app_data.get("version", "0.1.0"),
        ),
        logging=LoggingConfig(
            level=logging_data.get("level", "INFO"),
            format=logging_data.get("format", "%(levelname)s: %(message)s"),
        ),
    )
