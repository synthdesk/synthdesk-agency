#!/usr/bin/env python3
import json, sys

if len(sys.argv) < 2:
    print("usage: render_ascii.py <analysis.json>")
    sys.exit(1)

path = sys.argv[1]
data = json.load(open(path))
snap = data.get("temporal_regime_snapshot", {})

def bar(n):
    return "█" * n

print("\nquiet ░  transition ▒  expansion █\n")

for hour in sorted(snap):
    q = snap[hour].get("quiet", 0)
    t = snap[hour].get("transition", 0)
    e = snap[hour].get("expansion", 0)
    print(f"{hour}  ░{bar(q)} ▒{bar(t)} █{bar(e)}")

