"""Rank options (stub; advisory-only)."""

from __future__ import annotations

import os
import sys

from .. import ADVISORY_MODE

if ADVISORY_MODE and "PYTEST_CURRENT_TEST" not in os.environ and "pytest" not in sys.modules:
    raise RuntimeError("agency modules are advisory-only and must not be executed")

from dataclasses import dataclass
from typing import Optional, Sequence


@dataclass(frozen=True)
class Ranker:
    """Stub ranker for advisory options."""

    def rank(self, options: Sequence[dict]) -> Optional[Sequence[dict]]:
        pass
