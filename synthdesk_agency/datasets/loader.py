"""Load historical listener output (stub; no I/O implementation)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .schema import Dataset


@dataclass(frozen=True)
class DatasetLoader:
    """Stub loader for offline artifacts produced by an external listener."""

    def load(self, path: str) -> Optional[Dataset]:
        pass

