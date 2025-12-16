# Candle Builders

## candle_builder_v1 (v1.0.0)

Status: **FROZEN / IMMUTABLE**

This builder consumes `tick_observation.jsonl` and deterministically emits
60-second OHLC candles.

Guarantees:
- deterministic output
- replayable from raw ticks
- no gap filling
- no lookahead
- idempotent when re-run
- standard library only

This builder MUST NOT be modified.
Any changes require a new versioned builder (e.g. `candle_builder_v2.py`).
