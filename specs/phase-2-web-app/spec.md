# Spec — Phase II: Full-Stack Web Todo App
**Phase:** 2 | **Command:** /sp.specify | **Date:** 2026-02-22

---

## Overview
A full-stack web application where users manage todos through a browser. FastAPI backend stores data in Neon DB (cloud PostgreSQL). Next.js frontend provides the UI. Includes all Phase I features PLUS persistence.

---

## User Stories

### US-1: View Todo List in Browser
**As a** user
**I want to** open `http://localhost:3000`
**So that** I see all my tasks in a clean web UI

**Acceptance Criteria:**
- Tasks displayed as cards or rows
- Shows title, priority, status, due date, tags
- Color-coded by priority
- Real-time updates after any action

---

### US-2: Add Task via Web Form
**As a** user
**I want to** fill in a form with title, priority, tags, due date
**So that** a new task is saved to the database

**Acceptance Criteria:**
- Form has: text input (title), dropdown (priority), tag input, date picker (due date)
- Submit button saves to backend via POST /tasks
- New task appears in list immediately
- Empty title shows validation error

---

### US-3: Mark Complete via Checkbox
**As a** user
**I want to** click a checkbox next to a task
**So that** it is marked complete/incomplete instantly

**Acceptance Criteria:**
- Single click toggles status
- Visual strikethrough on completed tasks
- PATCH /tasks/{id} called immediately

---

### US-4: Delete Task
**As a** user
**I want to** click a trash icon on a task
**So that** it is deleted permanently

**Acceptance Criteria:**
- Confirmation prompt before delete
- DELETE /tasks/{id} called on confirm
- Task disappears from list

---

### US-5: Edit Task
**As a** user
**I want to** click an edit icon on a task
**So that** an edit form opens with current values pre-filled

**Acceptance Criteria:**
- Inline edit or modal
- Can change title, priority, due_date, tags
- PATCH /tasks/{id} saves changes

---

### US-6: Filter and Search
**As a** user
**I want to** use filter dropdowns and a search box
**So that** I only see relevant tasks

**Acceptance Criteria:**
- Filter by: status (all/pending/completed), priority (all/high/medium/low)
- Search box filters by title in real-time (client-side)
- Filters combinable

---

### US-7: Sort Tasks
**As a** user
**I want to** click column headers or a sort dropdown
**So that** tasks reorder

**Acceptance Criteria:**
- Sort by: priority, title, due date, created date
- Toggle ascending/descending

---

### US-8: Priority & Tags Display
**As a** user
**I want to** see priority badges and tag chips on each task
**So that** I can scan my list quickly

**Acceptance Criteria:**
- Priority badge colors: red=high, yellow=medium, green=low
- Tags shown as small colored chips

---

## API Endpoints (Backend Contract)

| Method | Path | Description |
|--------|------|-------------|
| GET | /tasks | List all tasks (supports ?status=&priority=&sort=) |
| POST | /tasks | Create new task |
| GET | /tasks/{id} | Get single task |
| PATCH | /tasks/{id} | Update task fields |
| DELETE | /tasks/{id} | Delete task |
| GET | /health | Health check |

---

## Data Model (Database)

```sql
CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  title VARCHAR(500) NOT NULL,
  status VARCHAR(20) DEFAULT 'pending',
  priority VARCHAR(10) DEFAULT 'medium',
  tags TEXT[] DEFAULT '{}',
  due_date DATE,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);
```

---

## Constraints
- Backend runs on port 8000
- Frontend runs on port 3000
- Frontend communicates with backend via HTTP (CORS enabled)
- Database: Neon DB (connection string in .env)
- No authentication required (single user app)
