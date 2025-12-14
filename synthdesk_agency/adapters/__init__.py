"""Adapters for interfacing with external systems (interfaces only)."""

from .snapshot import build_snapshot

try:
    __all__
except NameError:
    __all__ = []

__all__ += ["build_snapshot"]
