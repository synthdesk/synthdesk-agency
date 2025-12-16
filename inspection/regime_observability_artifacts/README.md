regime observability artifacts

status: frozen (phase d)
scope: synthdesk-agency (advisory-only)

purpose

this package provides read-only observability artifacts for inspecting descriptive market regime analysis outputs produced by synthdesk-agency.

it renders already-computed regime labels and temporal summaries for human inspection only.

this package does not generate signals, alerts, decisions, or recommendations.

inputs
- json analysis artifacts produced by scripts/analyze_run.py
- required fields: temporal_regime_snapshot
- optional: metric_summary

no live data is consumed.

outputs
- terminal tables (hourly regime counts)
- optional ascii visual summaries
- optional markdown snapshots for documentation

all outputs are static and non-interactive.

guarantees (invariants)

this package is:
- advisory-only
- deterministic
- read-only
- offline
- non-operational

this package cannot:
- trigger alerts
- emit signals
- route actions
- execute trades
- influence upstream logic
- perform prediction or optimization

non-goals

this package intentionally does not provide:
- dashboards
- live updating views
- rankings or scores
- thresholding
- regime strength metrics
- outcome-linked metrics
- forward inference

usage (manual)

examples:
python3 render_table.py analysis/btc_usd_2025-12-15.json
python3 render_ascii.py analysis/eth_usd_2025-12-15.json

outputs are printed to stdout only.

governance note

this package exists to preserve inspectability without agency.
it is an artifact surface, not a system component.
any extension beyond rendering requires explicit phase escalation.

