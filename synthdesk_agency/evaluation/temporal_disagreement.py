"""Temporal disagreement records (advisory-only; structure only)."""

from __future__ import annotations

import os
import sys

from .. import ADVISORY_MODE

if ADVISORY_MODE and "PYTEST_CURRENT_TEST" not in os.environ and "pytest" not in sys.modules:
    raise RuntimeError("agency modules are advisory-only and must not be executed")

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Sequence

from .disagreement import Disagreement


@dataclass(frozen=True)
class TemporalDisagreementSnapshot:
    """Snapshot of disagreement at a point in time.

    Notes:
    - no assumptions about ordering enforcement
    - no trends, deltas, or statistics
    - no resolution, thresholds, or alerts
    - just structure
    """

    timestamp: datetime
    disagreement: Disagreement
    notes: Optional[Sequence[str]] = None


@dataclass(frozen=True)
class TemporalDisagreementSeries:
    """Sequence of temporal disagreement snapshots (structure only).

    Notes:
    - no assumptions about ordering enforcement
    - no trends, deltas, or statistics
    - no resolution, thresholds, or alerts
    - just structure
    """

    snapshots: Sequence[TemporalDisagreementSnapshot]
    notes: Optional[Sequence[str]] = None
