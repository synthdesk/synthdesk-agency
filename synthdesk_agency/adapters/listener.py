"""Listener adapter interface (no imports from external listener repos)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Protocol, Sequence

from ..signals.models import SignalEvent


@dataclass(frozen=True)
class ListenerSnapshot:
    """Snapshot of listener-emitted observational records (schema-only)."""

    ticks: Optional[Sequence[dict]] = None
    events: Optional[Sequence[SignalEvent]] = None


class ListenerAdapter(Protocol):
    """Interface for adapting external listener artifacts into normalized records."""

    def snapshot(self, source: str) -> ListenerSnapshot:
        pass
