### phase d freeze — descriptive regime analysis

status: frozen  
scope: synthdesk-agency (advisory-only)  
validation date: 2025-12-15 (btc + eth)

### purpose
phase d defines a descriptive regime analysis that names market minutes without acting on them. this phase observes structure and emits labels only.

### primitives (locked)
- inputs: candle observations
- derived metrics: range_abs, body_abs, return_pct, body_ratio
- regime labels: quiet, expansion, transition
- transition definition: temporal flip OR median-relative metric straddle
- outputs: metric_summary, temporal_regime_snapshot

### invariants (must not change)
- advisory-only
- deterministic
- no price-level thresholds
- no alerts, signals, routing, or execution
- no prediction or optimization
- analyzer may label, never decide

### validated observations (non-binding)
- late-day regime ignition clustering
- eth exhibits higher regime boundary noise than btc
- cross-asset temporal synchrony
- transition appears as a minority boundary class
(these are observations, not rules)

### explicit exclusions
- alerting
- signaling
- execution
- strength scoring
- forward inference
- tuning
- multi-day aggregation logic

### allowed future work (gated)
- read-only visualization
- multi-day repetition of identical analysis
- cross-asset summaries
(all require a new phase charter)

### freeze declaration
phase d descriptive regime semantics are locked. any semantic change requires a new phase designation.
