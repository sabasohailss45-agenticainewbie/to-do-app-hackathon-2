# ADR-003: OpenAI Agents SDK for Phase III
**Date:** 2026-02-22 | **Status:** Accepted

## Decision
Use OpenAI Agents SDK with gpt-4o-mini for the Phase III AI chatbot.

## Context
Constitution requires OpenAI Agents SDK + MCP SDK. Need cost-effective model.

## Alternatives Considered
1. Raw OpenAI function calling — rejected (Agents SDK is the spec requirement)
2. gpt-4o — rejected (more expensive than needed for this demo)
3. gpt-4o-mini — accepted (fast, cheap, capable for todo management)

## Consequences
- Lower cost per conversation
- MCP tools provide clean separation between AI and API logic
- Agent maintains conversation history across turns
