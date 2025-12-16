### phase d freeze — descriptive regime analysis

- status: frozen
- scope: synthdesk-agency (advisory-only)
- validation date: 2025-12-15 (btc + eth)

### purpose

Phase D defines a descriptive regime layer for labeling market minutes as observational categories; it names market minutes and does not act on them.

### primitives (locked)

- inputs
  - listener candle records (JSONL) containing: symbol, interval_start, open, high, low, close, volume, resolution, exchange, listener_version
- derived metrics
  - return_pct: (close - open) / open; null if open is falsy
  - range_abs: high - low
  - body_abs: abs(close - open)
  - body_ratio: body_abs / range_abs; defined only when range_abs > 0
- regime labels
  - quiet
  - expansion
  - transition
- transition definition
  - temporal flip: base regime differs from immediately previous candle
  - OR median straddle: range_abs within ±10% of median(range_abs) AND body_ratio within ±10% of median(body_ratio)
  - transition overrides base regime label
- outputs
  - per-candle metrics dict includes derived metrics and regime label
  - metric_summary reports min/max/mean for derived metrics
  - temporal_regime_snapshot reports per-hour counts of regime labels

### invariants (must not change)

- advisory-only
- deterministic
- no thresholds tied to price levels
- no alerts, signals, routing, or execution
- no prediction or optimization
- analyzer may label, never decide

### validated observations (non-binding)

- late-day ignition clustering
- eth higher regime noise than btc
- cross-asset synchrony
- transition as minority boundary class
- these are observations, not rules

### explicit exclusions

- alerting
- signals
- execution
- strength scoring
- forward inference
- tuning
- multi-day aggregation logic

### allowed future work (gated)

- visualization
- multi-day repetition of identical analysis
- cross-asset summaries
- offline reporting
- all require a new phase charter

### freeze declaration

Phase D descriptive regime semantics are locked; any change requires a new phase designation.

