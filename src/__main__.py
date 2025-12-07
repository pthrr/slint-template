from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from .app import main
from .config import load_config

if __name__ == "__main__":
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("--config", type=Path)

    args: argparse.Namespace = parser.parse_args()
    config = load_config(args.config)

    logging.basicConfig(
        level=logging.DEBUG if args.debug else getattr(logging, config.logging.level),
        format=config.logging.format,
    )

    sys.exit(main(config))
