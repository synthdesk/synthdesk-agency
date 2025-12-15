"""Temporal advisory records (regime-sensitive, non-resolving)."""

from __future__ import annotations

import os
import sys

from .. import ADVISORY_MODE

if ADVISORY_MODE and "PYTEST_CURRENT_TEST" not in os.environ and "pytest" not in sys.modules:
    raise RuntimeError("agency modules are advisory-only and must not be executed")

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from .disagreement import Disagreement
from .scorecard import ScoreCard


@dataclass(frozen=True)
class TemporalSnapshot:
    """Snapshot of advisory evaluation at a point in time."""

    timestamp: datetime
    scorecard: Optional[ScoreCard] = None
    disagreement: Optional[Disagreement] = None
