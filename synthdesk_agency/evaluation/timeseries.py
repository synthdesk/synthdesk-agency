"""Temporal sequences for advisory evaluation (no interpretation)."""

from __future__ import annotations

import os
import sys

from .. import ADVISORY_MODE

if ADVISORY_MODE and "PYTEST_CURRENT_TEST" not in os.environ and "pytest" not in sys.modules:
    raise RuntimeError("agency modules are advisory-only and must not be executed")

from dataclasses import dataclass
from typing import Optional, Sequence

from .temporal import TemporalSnapshot


@dataclass(frozen=True)
class TemporalSeries:
    """Sequence of temporal advisory snapshots (structure only).

    Notes:
    - no assumptions about ordering enforcement
    - no trend detection
    - no statistics
    - just structure
    """

    snapshots: Sequence[TemporalSnapshot]
    notes: Optional[str] = None
