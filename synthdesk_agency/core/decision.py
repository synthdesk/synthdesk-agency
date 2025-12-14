"""Decision objects (dataclasses only; advisory-only, inert by default)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Sequence


@dataclass(frozen=True)
class Decision:
    """Advisory decision record; does not imply execution or action."""

    kind: str
    confidence: Optional[float] = None
    rationale: Optional[Sequence[str]] = None
    payload: Optional[dict] = None
