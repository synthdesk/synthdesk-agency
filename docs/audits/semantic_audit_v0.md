STATUS: REFERENCE (descriptive, non-authoritative)

# semantic audit — v0 (router permanent veto)

scope:
- synthdesk_agency/views/text_report.py

findings:

1. terminology drift
   - the phrase "advisory-only" appears in the renderer header.
   - advisory semantics are explicitly forbidden by the router constitution.
   - recommendation: replace with "epistemic-only" or "non-actionable".

2. authority compression risk
   - section labels "aggregate view" and "temporal view" may imply resolution.
   - although negated in body text, labels alone carry authority weight.
   - recommendation: weaken labels to "aggregate snapshot" and "temporal snapshot".

3. veto visibility gap
   - router veto status is not surfaced in this renderer.
   - this is expected given current separation of concerns.
   - note: justifies a future null snapshot renderer.

status:
- no code changes applied
- findings recorded for later remediation
