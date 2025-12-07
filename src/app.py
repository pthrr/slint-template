from __future__ import annotations

import logging
import os
from pathlib import Path

from slint import slint as native

from .config import Config
from .model import AppModel

logger = logging.getLogger(__name__)


def main(config: Config) -> int:
    ui_file: Path = Path(__file__).parent / "ui.slint"

    try:
        compiler = native.Compiler()
        result = compiler.build_from_path(str(ui_file))
        window = result.component("AppWindow").create()
    except Exception as e:
        logger.error(f"Failed to load UI: {e}")
        return 1

    model = AppModel()

    def on_increment() -> None:
        model.increment()
        logger.debug(f"counter: {model.counter}")
        window.set_property("counter", model.counter)

    def on_reset() -> None:
        model.reset()
        logger.debug(f"counter: {model.counter}")
        window.set_property("counter", model.counter)

    window.set_property("counter", model.counter)
    window.set_callback("increment-clicked", on_increment)
    window.set_callback("reset-clicked", on_reset)

    app_name: str = os.getenv("APP_NAME", config.app.name)
    app_version: str = os.getenv("APP_VERSION", config.app.version)
    logger.info(f"Starting {app_name} v{app_version}")

    window.run()
    return 0
