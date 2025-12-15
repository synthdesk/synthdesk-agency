"""Temporal disagreement records (expressive, non-resolving)."""

from __future__ import annotations

import os
import sys

from ... import ADVISORY_MODE

if ADVISORY_MODE and "PYTEST_CURRENT_TEST" not in os.environ and "pytest" not in sys.modules:
    raise RuntimeError("agency modules are advisory-only and must not be executed")

from dataclasses import dataclass
from typing import Optional, Sequence

from .snapshot import TemporalSnapshot


@dataclass(frozen=True)
class TemporalDisagreement:
    """Represents divergence or instability across time.

    Notes:
    - descriptive only
    - does not imply error or action
    - does not resolve disagreement
    """

    snapshots: Sequence[TemporalSnapshot]
    pattern: Optional[str] = None
    notes: Optional[Sequence[str]] = None
