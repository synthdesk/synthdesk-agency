#!/usr/bin/env python3
import json, sys

if len(sys.argv) < 2:
    print("usage: render_table.py <analysis.json>")
    sys.exit(1)

path = sys.argv[1]
data = json.load(open(path))
snap = data.get("temporal_regime_snapshot", {})

print(f"\nregime snapshot — {data.get('pairs')} — {path}\n")
print(f"{'hour':<14} {'quiet':>6} {'transition':>11} {'expansion':>11}")
print("-" * 46)

for hour in sorted(snap):
    q = snap[hour].get("quiet", 0)
    t = snap[hour].get("transition", 0)
    e = snap[hour].get("expansion", 0)
    print(f"{hour:<14} {q:>6} {t:>11} {e:>11}")

