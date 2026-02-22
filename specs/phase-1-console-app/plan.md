# Plan — Phase I: In-Memory Python Console Todo App
**Phase:** 1 | **Command:** /sp.plan | **Date:** 2026-02-22

---

## Architecture Overview

Single-file Python application with an interactive REPL loop. No frameworks needed.

```
phase-1-console/
├── main.py          # Entry point + CLI loop
├── todo.py          # TodoManager class (business logic)
├── display.py       # Rich table formatting
├── tests/
│   ├── test_todo.py
│   └── test_display.py
├── requirements.txt
└── README.md
```

---

## Component Breakdown

### 1. Data Model (in todo.py)
```python
Task = {
  "id": int,
  "title": str,
  "status": "pending" | "completed",
  "priority": "high" | "medium" | "low",
  "tags": list[str],
  "due_date": str | None,   # YYYY-MM-DD string
  "created_at": str          # ISO timestamp
}
```
Storage: `dict[int, Task]` keyed by task ID. Counter: `int` starting at 1.

### 2. TodoManager class (in todo.py)
Methods:
- `add_task(title, priority, tags, due_date) -> Task`
- `delete_task(task_id) -> None`
- `update_task(task_id, **kwargs) -> Task`
- `complete_task(task_id) -> Task`
- `list_tasks(status, priority, tag, sort_by) -> list[Task]`
- `search_tasks(query) -> list[Task]`
- `get_task(task_id) -> Task`

### 3. CLI Parser (in main.py)
Uses Python's built-in `argparse` module.
Commands parsed: add, delete, update, complete, list, search, help, exit.

### 4. Display Layer (in display.py)
Uses `rich` library for colored tables, panels, and messages.

---

## Implementation Phases

### Phase A: Core Data Layer
- TodoManager class with add, delete, update, complete, get, list
- All in-memory dict storage
- Full type hints

### Phase B: CLI Parser
- argparse setup for all commands
- Input validation (empty title, invalid priority, invalid date, invalid ID)
- Interactive REPL loop in main.py

### Phase C: Display Layer
- Rich table for task list
- Color-coded priorities (red=high, yellow=medium, green=low)
- Color-coded status (green=completed, yellow=pending)
- Success/error message formatting

### Phase D: Tests
- pytest tests for all TodoManager methods
- Edge cases: empty title, invalid ID, invalid priority

---

## Dependencies
```
rich>=13.0.0
pytest>=7.0.0
```

---

## Design Decisions
1. **Single file vs multiple:** Split into 3 files (todo.py, display.py, main.py) for clean separation but still simple
2. **argparse vs manual parsing:** argparse handles edge cases automatically
3. **rich library:** Makes output professional without much code — allowed by constitution
