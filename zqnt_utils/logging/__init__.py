"""
Structured logging for ZQNT Python services.

Standard formatters (JSON for log aggregators, coloured text for local dev)
plus a single ``setup_logging`` call to configure the root logger.

Usage::

    from zqnt_utils.logging import setup_logging
    setup_logging()
    logger = logging.getLogger(__name__)

Environment variables (read by :func:`setup_logging` when no arguments are
passed explicitly):

* ``LOG_LEVEL``  – ``DEBUG`` | ``INFO`` | ``WARNING`` | ``ERROR`` (default ``INFO``)
* ``LOG_FORMAT`` – ``json`` | ``text`` (default ``json``)
"""

from .config import JsonFormatter, TextFormatter, setup_logging

__all__ = ["JsonFormatter", "TextFormatter", "setup_logging"]
