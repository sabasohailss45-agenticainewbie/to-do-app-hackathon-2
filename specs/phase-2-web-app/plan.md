# Plan — Phase II: Full-Stack Web Todo App
**Phase:** 2 | **Command:** /sp.plan | **Date:** 2026-02-22

---

## Architecture Overview

```
phase-2-web/
├── backend/                    # FastAPI app
│   ├── main.py                 # FastAPI app + routes
│   ├── models.py               # SQLModel database models
│   ├── database.py             # Neon DB connection
│   ├── schemas.py              # Pydantic request/response schemas
│   ├── .env                    # DATABASE_URL (not committed)
│   ├── requirements.txt
│   └── README.md
└── frontend/                   # Next.js app
    ├── app/
    │   ├── page.tsx            # Main todo page
    │   ├── layout.tsx          # Root layout
    │   └── globals.css         # Tailwind base styles
    ├── components/
    │   ├── TaskList.tsx        # Renders list of tasks
    │   ├── TaskCard.tsx        # Single task row/card
    │   ├── AddTaskForm.tsx     # Form to add new task
    │   ├── EditTaskModal.tsx   # Modal to edit task
    │   ├── FilterBar.tsx       # Filter + search bar
    │   └── PriorityBadge.tsx   # Colored priority badge
    ├── lib/
    │   └── api.ts              # API call functions
    ├── types/
    │   └── task.ts             # TypeScript Task type
    ├── .env.local              # NEXT_PUBLIC_API_URL
    ├── package.json
    └── README.md
```

---

## Backend Implementation Plan

### Step 1: Database Connection (database.py)
- Use `asyncpg` + `SQLModel` for async Neon DB connection
- Connection string from `DATABASE_URL` env var
- Create engine with connection pooling

### Step 2: Data Model (models.py)
- `Task` SQLModel table with all fields
- Use `Optional` for nullable fields
- Auto timestamps with `default_factory`

### Step 3: Schemas (schemas.py)
- `TaskCreate` — fields required to create
- `TaskUpdate` — all fields optional for PATCH
- `TaskResponse` — what API returns

### Step 4: API Routes (main.py)
- CORS middleware for localhost:3000
- All 5 CRUD endpoints
- Query params for filtering/sorting

---

## Frontend Implementation Plan

### Step 1: Types (types/task.ts)
- TypeScript interface for Task

### Step 2: API Layer (lib/api.ts)
- Typed fetch functions for each endpoint
- Error handling built in

### Step 3: Core Components
- `TaskCard` — displays one task with checkbox, edit, delete
- `AddTaskForm` — controlled form with validation
- `FilterBar` — dropdowns + search input
- `TaskList` — maps over tasks, handles empty state

### Step 4: Main Page (app/page.tsx)
- State management with `useState` + `useEffect`
- Fetch tasks on load
- Optimistic updates for checkbox toggle

---

## Key Design Decisions
1. **SQLModel over raw SQLAlchemy:** Cleaner syntax, built-in Pydantic validation
2. **Client-side search:** Faster UX, no extra API calls for search
3. **No Redux:** useState is enough for single-page todo app
4. **Tailwind CSS:** Fast styling without writing custom CSS
