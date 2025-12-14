"""Static regime semantics records (advisory-only; descriptive)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Optional, Sequence


@dataclass(frozen=True)
class RegimeDescriptor:
    """Descriptive record for a named regime (vocabulary only)."""

    name: str
    description: Optional[str] = None
    indicators: Optional[Sequence[str]] = None
    notes: Optional[Sequence[str]] = None
    metadata: Optional[dict] = None


@dataclass(frozen=True)
class RegimeVocabulary:
    """Vocabulary surface for regimes (static; no inference)."""

    names: Sequence[str]
    descriptors: Optional[Mapping[str, RegimeDescriptor]] = None
    notes: Optional[Sequence[str]] = None
    metadata: Optional[dict] = None

