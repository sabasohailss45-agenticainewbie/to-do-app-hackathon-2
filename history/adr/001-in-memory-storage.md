# ADR-001: In-Memory Storage for Phase I
**Date:** 2026-02-22 | **Status:** Accepted

## Decision
Use a Python `dict[int, dict]` for task storage in Phase I — no database, no files.

## Context
Phase I is an MVP console app. Constitution Article II specifies in-memory only.

## Alternatives Considered
1. SQLite file — rejected (adds complexity, not in-memory)
2. JSON file — rejected (file I/O not needed for demo)
3. Python dict — accepted (simple, fast, constitution-compliant)

## Consequences
- Data is lost when the app exits (by design)
- No persistence needed until Phase II
- Zero setup friction for the user
