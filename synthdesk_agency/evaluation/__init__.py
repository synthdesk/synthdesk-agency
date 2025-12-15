import os
import sys

from .. import ADVISORY_MODE

if ADVISORY_MODE and "PYTEST_CURRENT_TEST" not in os.environ and "pytest" not in sys.modules:
    raise RuntimeError("agency modules are advisory-only and must not be executed")

from .simulation import SimulationReport, SimulationResult
from .simulator import Simulator
from .scores import Score
from .scorecard import ScoreCard
from .scoring import Scorer
from .disagreement import Disagreement
from .aggregates import AggregateView
from .aggregation import Aggregator
from .temporal import TemporalSnapshot
from .timeseries import TemporalSeries
from .temporal_analysis import TemporalAnalyzer
from .temporal_disagreement import TemporalDisagreementSeries, TemporalDisagreementSnapshot
from .temporal_disagreement_analysis import TemporalDisagreementAnalyzer
from .temporal.snapshot import TemporalSnapshot
from .temporal.disagreement import TemporalDisagreement
from .temporal.patterns import TEMPORAL_PATTERNS
from .temporal.analyzer import TemporalAnalyzer
from .temporal.regime_churn import RegimeChurn, RegimeChurnAnalyzer, TemporalRegimeSeries, TemporalRegimeSnapshot

__all__ = [
    "SimulationReport",
    "SimulationResult",
    "Simulator",
]

__all__ += [
    "Score",
    "ScoreCard",
    "Scorer",
]

__all__ += [
    "Disagreement",
    "AggregateView",
    "Aggregator",
]

__all__ += [
    "TemporalSnapshot",
    "TemporalSeries",
    "TemporalAnalyzer",
]

__all__ += [
    "TemporalDisagreementSnapshot",
    "TemporalDisagreementSeries",
    "TemporalDisagreementAnalyzer",
]

__all__ += [
    "TemporalSnapshot",
    "TemporalDisagreement",
    "TEMPORAL_PATTERNS",
    "TemporalAnalyzer",
]

__all__ += [
    "TemporalRegimeSnapshot",
    "TemporalRegimeSeries",
    "RegimeChurn",
    "RegimeChurnAnalyzer",
]
