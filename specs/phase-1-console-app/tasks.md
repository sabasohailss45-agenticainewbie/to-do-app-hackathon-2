# Tasks — Phase I: In-Memory Python Console Todo App
**Phase:** 1 | **Command:** /sp.tasks | **Date:** 2026-02-22

---

## Task List

| # | Task | File | Depends On |
|---|------|------|-----------|
| 1 | Create `requirements.txt` with rich and pytest | `phase-1-console/requirements.txt` | None |
| 2 | Create `TodoManager` class with Task data model | `phase-1-console/todo.py` | 1 |
| 3 | Implement `add_task()` method | `phase-1-console/todo.py` | 2 |
| 4 | Implement `delete_task()` method | `phase-1-console/todo.py` | 2 |
| 5 | Implement `update_task()` method | `phase-1-console/todo.py` | 2 |
| 6 | Implement `complete_task()` method | `phase-1-console/todo.py` | 2 |
| 7 | Implement `list_tasks()` with filter + sort | `phase-1-console/todo.py` | 2 |
| 8 | Implement `search_tasks()` method | `phase-1-console/todo.py` | 2 |
| 9 | Write tests for all TodoManager methods | `phase-1-console/tests/test_todo.py` | 3,4,5,6,7,8 |
| 10 | Create `display.py` with rich table formatting | `phase-1-console/display.py` | 2 |
| 11 | Create `main.py` with argparse CLI loop | `phase-1-console/main.py` | 10 |
| 12 | Create `README.md` with run instructions | `phase-1-console/README.md` | 11 |

---

## Acceptance Checklist
- [ ] `python main.py` starts an interactive loop
- [ ] `add "Test task"` creates task with ID 1
- [ ] `list` shows a formatted table
- [ ] `complete 1` marks task as done
- [ ] `delete 1` removes task
- [ ] `update 1 title "New title"` changes the title
- [ ] `list --priority high` filters correctly
- [ ] `search groceries` finds matching tasks
- [ ] `help` shows all commands
- [ ] `exit` closes the app
- [ ] pytest passes all tests
