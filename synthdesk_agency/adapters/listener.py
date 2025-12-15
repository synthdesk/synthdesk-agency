"""Listener adapter interface (no imports from external listener repos)."""

from __future__ import annotations

import os
import sys

from .. import ADVISORY_MODE

if ADVISORY_MODE and "PYTEST_CURRENT_TEST" not in os.environ and "pytest" not in sys.modules:
    raise RuntimeError("agency modules are advisory-only and must not be executed")

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
