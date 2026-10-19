# OR Regula

Version-aware mapping of financial-crime requirements to controls and time-bounded evidence.

## Why it matters

Policies and controls become difficult to defend when source versions, ownership, approvals, and evidence freshness are unclear. This project assesses a user-supplied catalog and surfaces coverage gaps without pretending to determine legal compliance.

## Current capabilities

- Requirement version, jurisdiction, and HTTPS source validation.
- Control ownership, approval status, review dates, and version mapping.
- Evidence approval and validity windows.
- Rejection of unknown references and expired or stale coverage.
- Reproducible assessment date and explicit catalog-only conclusion.
- Owner-level schedules for overdue and upcoming control reviews.
- CLI, optional authenticated API, Docker image, and CI.

## Run

```sh
python -m pip install -e '.[dev,api]'
python -m or_regula --demo
pytest -q && ruff check src tests
```

API: set `OR_API_KEY` to at least 16 characters, run `uvicorn or_regula.api:create_app --factory`, then POST `examples/request.json` to `/v1/analyze`.

## Limitations and roadmap

Set `action` to `schedule` to build a deterministic review queue for a chosen horizon. The software does not provide legal advice, interpret regulations, or certify compliance. Catalog content requires official sources and qualified review. Next steps are signed catalog releases, approval workflows, control testing frequency, evidence provenance, multi-jurisdiction change alerts, and historical snapshots.
