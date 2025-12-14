"""Time utilities (stubs; no environment dependencies)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class TimeRange:
    """Inclusive time range record."""

    start: Optional[datetime] = None
    end: Optional[datetime] = None


def parse_iso8601(value: str) -> Optional[datetime]:
    return None

