"""Score weighting records (advisory-only; inert)."""

from __future__ import annotations

import os
import sys

from .. import ADVISORY_MODE

if ADVISORY_MODE and "PYTEST_CURRENT_TEST" not in os.environ and "pytest" not in sys.modules:
    raise RuntimeError("agency modules are advisory-only and must not be executed")

from dataclasses import dataclass
from typing import Optional, Sequence


@dataclass(frozen=True)
class Weight:
    """Named weight record used for scoring/aggregation (record only)."""

    name: str
    weight: Optional[float] = None
    enabled: Optional[bool] = None
    notes: Optional[Sequence[str]] = None
    metadata: Optional[dict] = None


@dataclass(frozen=True)
class WeightSet:
    """Collection of named weights."""

    weights: Sequence[Weight]
    notes: Optional[Sequence[str]] = None
    metadata: Optional[dict] = None
