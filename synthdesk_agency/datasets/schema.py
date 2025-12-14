"""Dataset contracts (dataclasses only)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Sequence


@dataclass(frozen=True)
class Dataset:
    """In-memory dataset representation (schema-only)."""

    rows: Optional[Sequence[dict]] = None
    metadata: Optional[dict] = None

