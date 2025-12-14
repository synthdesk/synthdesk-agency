# synthdesk-agency

Advisory-only interpretation layer for SynthDesk.

This repository provides a **purely descriptive, inert agency layer** that interprets
artifacts emitted by `synthdesk-listener` into human-readable advisory views.

## Scope
- advisory-only
- no execution
- no trading
- no automation
- no network calls
- no side effects

## Relationship to synthdesk-listener
`synthdesk-listener` produces signals, logs, and state.
`synthdesk-agency` **interprets** those artifacts into decisions, scores, disagreements,
and snapshots for human inspection.

This repo is intentionally non-operational.
