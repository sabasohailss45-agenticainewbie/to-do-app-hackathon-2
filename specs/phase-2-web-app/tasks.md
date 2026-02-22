# Tasks — Phase II: Full-Stack Web Todo App
**Phase:** 2 | **Command:** /sp.tasks | **Date:** 2026-02-22

---

## Backend Tasks

| # | Task | File | Depends On |
|---|------|------|-----------|
| B1 | Create requirements.txt (fastapi, sqlmodel, asyncpg, python-dotenv, uvicorn) | `backend/requirements.txt` | None |
| B2 | Create database.py with Neon DB async connection | `backend/database.py` | B1 |
| B3 | Create models.py with Task SQLModel table | `backend/models.py` | B2 |
| B4 | Create schemas.py (TaskCreate, TaskUpdate, TaskResponse) | `backend/schemas.py` | B3 |
| B5 | Create main.py with FastAPI app + all 5 endpoints + CORS | `backend/main.py` | B4 |
| B6 | Create .env.example with DATABASE_URL placeholder | `backend/.env.example` | None |
| B7 | Write pytest tests for all endpoints | `backend/tests/test_api.py` | B5 |
| B8 | Create backend README.md | `backend/README.md` | B5 |

## Frontend Tasks

| # | Task | File | Depends On |
|---|------|------|-----------|
| F1 | Initialize Next.js project with TypeScript + Tailwind | `frontend/` | None |
| F2 | Create Task TypeScript type | `frontend/types/task.ts` | F1 |
| F3 | Create api.ts with all fetch functions | `frontend/lib/api.ts` | F2 |
| F4 | Create PriorityBadge component | `frontend/components/PriorityBadge.tsx` | F1 |
| F5 | Create TaskCard component | `frontend/components/TaskCard.tsx` | F4 |
| F6 | Create AddTaskForm component | `frontend/components/AddTaskForm.tsx` | F2 |
| F7 | Create FilterBar component | `frontend/components/FilterBar.tsx` | F1 |
| F8 | Create TaskList component | `frontend/components/TaskList.tsx` | F5 |
| F9 | Create main page.tsx wiring everything together | `frontend/app/page.tsx` | F3,F6,F7,F8 |
| F10 | Create .env.local.example | `frontend/.env.local.example` | None |
| F11 | Create frontend README.md | `frontend/README.md` | F9 |

---

## Acceptance Checklist
- [ ] Backend starts with `uvicorn main:app --reload`
- [ ] GET /health returns `{"status": "ok"}`
- [ ] POST /tasks creates task in Neon DB
- [ ] GET /tasks returns all tasks
- [ ] PATCH /tasks/{id} updates task
- [ ] DELETE /tasks/{id} deletes task
- [ ] Frontend starts with `npm run dev`
- [ ] Tasks load on page open
- [ ] Add form creates and shows new task
- [ ] Checkbox toggles completion
- [ ] Delete removes task
- [ ] Filter by priority works
- [ ] Search filters by title
