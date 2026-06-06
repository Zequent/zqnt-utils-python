"""
Logging formatters and root-logger setup for ZQNT services.

Two formatters are provided:

* :class:`JsonFormatter` – single-line JSON, suited for log aggregators
  (ELK, Loki, Cloud Logging). Any ``extra={...}`` fields passed to the
  logger are merged into the JSON object.
* :class:`TextFormatter` – human-readable, optional ANSI colour, intended
  for local development.

:func:`setup_logging` configures the root logger and is safe to call
multiple times — existing handlers are replaced rather than duplicated.
"""

import json
import logging
import os
import sys
from datetime import datetime, timezone


class JsonFormatter(logging.Formatter):
    """Single-line JSON formatter suited for log aggregators."""

    def format(self, record: logging.LogRecord) -> str:
        entry: dict = {
            "timestamp": datetime.fromtimestamp(
                record.created, tz=timezone.utc
            ).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        if record.exc_info:
            entry["exception"] = self.formatException(record.exc_info)
        skip = logging.LogRecord.__dict__.keys() | {
            "message",
            "asctime",
            "args",
            "msg",
            "exc_text",
            "stack_info",
        }
        for key, value in record.__dict__.items():
            if key not in skip:
                entry[key] = value
        return json.dumps(entry, default=str)


class TextFormatter(logging.Formatter):
    """Human-readable formatter for local development. ANSI colour when stderr is a TTY."""

    _LEVEL_COLORS = {
        "DEBUG": "\033[36m",
        "INFO": "\033[32m",
        "WARNING": "\033[33m",
        "ERROR": "\033[31m",
        "CRITICAL": "\033[35m",
    }
    _RESET = "\033[0m"

    def __init__(self, *, colorize: bool = True) -> None:
        super().__init__()
        self._colorize = colorize and sys.stderr.isatty()

    def format(self, record: logging.LogRecord) -> str:
        ts = (
            datetime.fromtimestamp(record.created, tz=timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%S.%f"
            )[:-3]
            + "Z"
        )
        level = record.levelname
        if self._colorize:
            color = self._LEVEL_COLORS.get(level, "")
            level = f"{color}{level}{self._RESET}"
        line = f"{ts} [{level}] {record.name}: {record.getMessage()}"
        if record.exc_info:
            line += "\n" + self.formatException(record.exc_info)
        return line


def setup_logging(level: str | None = None, fmt: str | None = None) -> None:
    """
    Configure the root logger once at application startup.

    Args:
        level: Override the ``LOG_LEVEL`` env var (``DEBUG``/``INFO``/``WARNING``/``ERROR``).
        fmt:   Override the ``LOG_FORMAT`` env var (``json``/``text``).
    """
    level = (level or os.getenv("LOG_LEVEL", "INFO")).upper()
    fmt = (fmt or os.getenv("LOG_FORMAT", "json")).lower()

    numeric_level = getattr(logging, level, logging.INFO)
    formatter: logging.Formatter = TextFormatter() if fmt == "text" else JsonFormatter()

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    root = logging.getLogger()
    root.setLevel(numeric_level)
    root.handlers = [handler]
