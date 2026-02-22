# Constitution — Todo Evolution Project
**Version:** 1.0 | **Created:** 2026-02-22 | **Command:** /sp.constitution

---

## Article I — Project Mission
Build a 3-phase Todo application that evolves from a simple Python console app to a full-stack web app to an AI-powered chatbot, demonstrating spec-driven development using Spec-Kit Plus and Claude Code.

---

## Article II — Technology Stack (Non-Negotiable)

### Phase I — Console App
- Language: Python 3.11+
- Storage: In-memory only (no database, no files)
- Interface: Command-line (terminal)
- Testing: pytest

### Phase II — Web App
- Backend: FastAPI (Python)
- Database: Neon DB (PostgreSQL via asyncpg + SQLModel)
- Frontend: Next.js 14 (App Router, TypeScript)
- Styling: Tailwind CSS
- Testing: pytest (backend), Jest (frontend)

### Phase III — AI Chatbot
- AI Framework: OpenAI Agents SDK
- Chat UI: OpenAI ChatKit (or simple terminal chat)
- Tool Protocol: Official MCP SDK
- Model: gpt-4o-mini (cost-effective)
- Testing: pytest

---

## Article III — Code Quality Standards
1. Python: Type hints on every function, docstrings on every class
2. TypeScript: Strict mode enabled, no `any` types
3. All functions must have at least one test
4. Error handling required at every user-facing operation
5. No hardcoded secrets — use environment variables via .env files

---

## Article IV — Feature Requirements (All Phases Must Have)

### Basic (Phase I minimum)
- Add task
- Delete task
- Update task
- View all tasks
- Mark as complete/incomplete

### Intermediate (Phase II adds)
- Priorities: high / medium / low
- Tags/Categories: work, home, personal
- Search by keyword
- Filter by status, priority
- Sort by due date, priority, alphabetical

### Advanced (Phase II + III)
- Due dates with date picker
- Recurring tasks
- AI natural language management (Phase III)

---

## Article V — Architecture Principles
1. Each phase is self-contained — Phase II does not require Phase I to run
2. Phase II backend exposes a REST API that Phase III chatbot also uses
3. All API responses use JSON
4. Frontend calls backend via HTTP — never directly touches the database
5. The AI chatbot uses MCP tools to call the Phase II API

---

## Article VI — File Naming & Structure
- Python files: snake_case.py
- TypeScript files: PascalCase for components, camelCase for utils
- Environment files: .env (never committed to git)
- Specs: specs/<phase-name>/spec.md, plan.md, tasks.md

---

## Article VII — Delivery Constraints
- Phase I must run with: `python main.py`
- Phase II backend must run with: `uvicorn main:app --reload`
- Phase II frontend must run with: `npm run dev`
- Phase III must run with: `python chatbot.py`
- Each phase must have a README.md with exact run instructions

---

## Article VIII — What Claude Code Must NOT Do
- Do not use external databases in Phase I (in-memory only)
- Do not use class inheritance when simple functions suffice
- Do not over-engineer — minimum viable implementation first
- Do not create files outside the designated phase folders
- Do not use deprecated libraries
