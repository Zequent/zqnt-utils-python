"""
ZQNT Utils – Python
===================

Shared utilities for ZQNT services and adapters.

    from zqnt_utils.caching import CacheKeys, CachingService
    from zqnt_utils.core import EdgeEndpointDTO
"""

from importlib.metadata import PackageNotFoundError, version as _pkg_version

from .caching import CacheKeys, CachingService
from .core import EdgeEndpointDTO

try:
    __version__ = _pkg_version("zqnt-utils")
except PackageNotFoundError:
    __version__ = "1.0.0"

__all__ = ["__version__", "CacheKeys", "CachingService", "EdgeEndpointDTO"]
