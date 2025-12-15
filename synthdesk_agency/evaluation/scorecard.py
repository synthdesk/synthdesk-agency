"""Score aggregation container (advisory-only)."""

from __future__ import annotations

import os
import sys

from .. import ADVISORY_MODE

if ADVISORY_MODE and "PYTEST_CURRENT_TEST" not in os.environ and "pytest" not in sys.modules:
    raise RuntimeError("agency modules are advisory-only and must not be executed")

from dataclasses import dataclass
from typing import Mapping, Optional, Sequence

from .scores import Score


@dataclass(frozen=True)
class ScoreCard:
    """Collection of advisory scores."""

    scores: Mapping[str, Score]
    summary: Optional[str] = None
    notes: Optional[Sequence[str]] = None
