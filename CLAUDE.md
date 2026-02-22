# CLAUDE.md — Todo Evolution Hackathon Project

## Project Identity
- **Name:** Todo Evolution — 3-Phase Hackathon Project
- **Methodology:** Spec-Kit Plus (Spec-Driven Development)
- **AI Agent:** Claude Code
- **Constitution:** `.specify/memory/constitution.md`

## Your Role
You are the AI coding agent for this project. You MUST:
1. Read `.specify/memory/constitution.md` before every implementation
2. Read the relevant `specs/<phase>/spec.md`, `plan.md`, and `tasks.md` before writing any code
3. Never write code that contradicts the constitution
4. Follow the checkpoint pattern: complete one task, report back, wait for approval

## Spec-Kit Plus Commands Available
- `/sp.constitution` — Review/update constitution
- `/sp.specify` — Write or refine a feature spec
- `/sp.plan` — Generate implementation plan
- `/sp.tasks` — Break plan into atomic tasks
- `/sp.implement` — Implement tasks one by one

## Project Phases
- **Phase I:** `phase-1-console/` — Python in-memory console app
- **Phase II:** `phase-2-web/` — FastAPI backend + Next.js frontend + Neon DB
- **Phase III:** `phase-3-chatbot/` — OpenAI Agents SDK + MCP chatbot

## Non-Negotiable Rules
1. Always follow the constitution
2. Always write tests alongside implementation
3. Never skip error handling
4. Keep each phase self-contained and runnable independently
