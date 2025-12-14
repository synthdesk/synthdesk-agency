"""Human-facing agency snapshot record (advisory-only; inert)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Sequence

from .context import AgencyContext
from .decision import Decision
from .regime_churn import RegimeChurn
from ..evaluation.aggregates import AggregateView
from ..evaluation.disagreement import Disagreement
from ..evaluation.scorecard import ScoreCard


@dataclass(frozen=True)
class AgencySnapshot:
    """
    Human-facing snapshot of the agency’s current observational state.

    Notes:
    - descriptive only
    - no decisions are implied
    - disagreement is preserved, not resolved
    """

    context: Optional[AgencyContext]
    decisions: Optional[Sequence[Decision]]
    scorecards: Optional[Sequence[ScoreCard]]
    disagreement: Optional[Disagreement]
    aggregate_view: Optional[AggregateView]
    temporal_view: Optional[object]
    regime_churn: Optional[RegimeChurn]
    notes: Optional[Sequence[str]]
