"""Centralized logging configuration.

This module configures the root logger to output to a rotating file and the
console. Modules throughout the project can simply import ``logging`` and
retrieve a module-specific logger via ``logging.getLogger(__name__)`` once this
configuration has been applied.
"""

from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional


def configure_logging(log_file: str = "logs/app.log", level: int = logging.DEBUG) -> None:
    """Configure the root logger.

    The configuration includes creating the directory for ``log_file`` if it
    does not already exist, attaching a ``RotatingFileHandler`` to keep log
    files at a manageable size, and adding a ``StreamHandler`` so logs also
    appear in stdout.

    Args:
        log_file (str): Path to the log file. If relative, it is resolved from
            the current working directory.
        level (int): Logging level for the root logger. Defaults to
            ``logging.DEBUG``.
    """
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s [%(name)s] %(message)s"
    )

    file_handler = RotatingFileHandler(
        filename=str(log_path),
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    if not root_logger.handlers:
        # Only add handlers once to avoid duplicate logs during testing.
        root_logger.addHandler(file_handler)
        root_logger.addHandler(stream_handler)
    root_logger.setLevel(level)


__all__ = ["configure_logging"]
