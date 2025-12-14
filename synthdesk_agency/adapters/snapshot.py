"""Read-only adapter for assembling an AgencySnapshot from pre-loaded artifacts."""

from __future__ import annotations

from typing import Optional, Sequence

from ..core.agency_snapshot import AgencySnapshot
from ..core.context import AgencyContext
from ..core.decision import Decision
from ..core.regime_churn import RegimeChurn
from ..evaluation.aggregates import AggregateView
from ..evaluation.disagreement import Disagreement
from ..evaluation.scorecard import ScoreCard


def build_snapshot(
    context: Optional[AgencyContext],
    decisions: Optional[Sequence[Decision]] = None,
    scorecards: Optional[Sequence[ScoreCard]] = None,
    disagreement: Optional[Disagreement] = None,
    aggregate_view: Optional[AggregateView] = None,
    temporal_view: Optional[object] = None,
    regime_churn: Optional[RegimeChurn] = None,
    notes: Optional[Sequence[str]] = None,
) -> AgencySnapshot:
    return AgencySnapshot(
        context=context,
        decisions=decisions,
        scorecards=scorecards,
        disagreement=disagreement,
        aggregate_view=aggregate_view,
        temporal_view=temporal_view,
        regime_churn=regime_churn,
        notes=notes,
    )

