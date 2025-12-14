"""Normalized signal schema (dataclasses only)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class SignalEvent:
    """Normalized listener event record for advisory-only processing."""

    event: str
    pair: str
    price: float
    timestamp: str
    metrics: Optional[dict] = None
    version: Optional[str] = None
    tick_id: Optional[int] = None

