#!/usr/bin/env bash

# Manual examples for multi-asset temporal regime snapshots.
# `temporal_regime_snapshot` is asset-agnostic: run the same analysis per asset and compare outputs.

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONPATH="$ROOT_DIR"

DATE_UTC="$(date -u +%F)"
OUT_DIR="$ROOT_DIR/analysis"
mkdir -p "$OUT_DIR"

# Example: BTC-USD candles (listener JSONL)
python3 "$ROOT_DIR/scripts/analyze_run.py" "/path/to/btc_usd_candles.jsonl" \
  --output "$OUT_DIR/btc_usd_${DATE_UTC}.json"

# Example: ETH-USD candles (listener JSONL)
python3 "$ROOT_DIR/scripts/analyze_run.py" "/path/to/eth_usd_candles.jsonl" \
  --output "$OUT_DIR/eth_usd_${DATE_UTC}.json"

