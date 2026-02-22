# ADR-002: Neon DB for Phase II Database
**Date:** 2026-02-22 | **Status:** Accepted

## Decision
Use Neon DB (serverless PostgreSQL) as the database for Phase II.

## Context
Need a cloud PostgreSQL database that is free-tier, easy to set up, and works with SQLModel.

## Alternatives Considered
1. Local PostgreSQL — requires local install, harder for non-techies
2. Supabase — more complex setup
3. Neon DB — accepted (free tier, instant setup, postgres-compatible)

## Consequences
- Database is cloud-hosted (no local postgres needed)
- Connection via asyncpg works seamlessly
- SSL required (configured in DATABASE_URL)
