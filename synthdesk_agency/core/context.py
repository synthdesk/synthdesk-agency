"""Immutable snapshot of inputs provided to the advisory-only agency engine."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Sequence

from ..signals.models import SignalEvent


@dataclass(frozen=True)
class AgencyContext:
    """Input snapshot assembled from listener logs and tick/event records."""

    ticks: Optional[Sequence[dict]] = None
    events: Optional[Sequence[SignalEvent]] = None
    metadata: Optional[dict] = None

