# Spec — Phase I: In-Memory Python Console Todo App
**Phase:** 1 | **Command:** /sp.specify | **Date:** 2026-02-22

---

## Overview
A Python command-line application that manages a todo list entirely in memory. No database, no files. When the program exits, data is gone. This is the MVP foundation.

## User Stories

### US-1: Add a Task
**As a** user
**I want to** type `add "Buy groceries"` in the terminal
**So that** a new task appears in my list with a unique ID

**Acceptance Criteria:**
- Task is given an auto-incrementing integer ID starting at 1
- Task has a title (required), priority (default: medium), status (default: pending)
- Confirmation message shown: `Task #1 added: Buy groceries`
- Empty title is rejected with error: `Error: Task title cannot be empty`

---

### US-2: View All Tasks
**As a** user
**I want to** type `list` in the terminal
**So that** I see all my tasks in a formatted table

**Acceptance Criteria:**
- Shows ID, title, priority, status, due date (if set), tags (if any)
- Empty list shows: `No tasks yet. Add one with: add "task title"`
- Tasks sorted by ID by default

---

### US-3: Mark Task Complete
**As a** user
**I want to** type `complete 1`
**So that** task #1 is marked as done

**Acceptance Criteria:**
- Status changes from `pending` to `completed`
- Confirmation: `Task #1 marked as completed`
- Invalid ID shows: `Error: Task #99 not found`

---

### US-4: Update a Task
**As a** user
**I want to** type `update 1 title "New title"`
**So that** task #1's title is changed

**Acceptance Criteria:**
- Supports updating: title, priority, due_date, tags
- Confirmation: `Task #1 updated`
- Invalid field name shows appropriate error

---

### US-5: Delete a Task
**As a** user
**I want to** type `delete 1`
**So that** task #1 is permanently removed

**Acceptance Criteria:**
- Task removed from list
- Confirmation: `Task #1 deleted`
- Invalid ID shows: `Error: Task #99 not found`

---

### US-6: Set Priority
**As a** user
**I want to** type `add "Urgent thing" --priority high`
**So that** the task is flagged as high priority

**Acceptance Criteria:**
- Priority values: `high`, `medium`, `low` (case-insensitive)
- Invalid priority shows: `Error: Priority must be high, medium, or low`
- Default is `medium` if not specified

---

### US-7: Add Tags/Categories
**As a** user
**I want to** type `add "Report" --tags work`
**So that** I can categorize tasks

**Acceptance Criteria:**
- Multiple tags supported: `--tags work,home`
- Tags stored as a list of strings

---

### US-8: Filter Tasks
**As a** user
**I want to** type `list --status completed` or `list --priority high`
**So that** I only see tasks matching my filter

**Acceptance Criteria:**
- Supports filtering by: status, priority, tag
- Combined filters work: `list --status pending --priority high`

---

### US-9: Search Tasks
**As a** user
**I want to** type `search groceries`
**So that** I see all tasks containing that word

**Acceptance Criteria:**
- Case-insensitive search on task title
- Shows matching tasks in same table format
- No results shows: `No tasks found matching "groceries"`

---

### US-10: Sort Tasks
**As a** user
**I want to** type `list --sort priority`
**So that** tasks are reordered

**Acceptance Criteria:**
- Sort options: `priority`, `title`, `status`
- Default sort: by ID

---

### US-11: Set Due Date
**As a** user
**I want to** type `add "Pay rent" --due 2026-03-01`
**So that** I can track deadlines

**Acceptance Criteria:**
- Due date format: YYYY-MM-DD
- Invalid date shows: `Error: Invalid date format. Use YYYY-MM-DD`

---

### US-12: Help Command
**As a** user
**I want to** type `help`
**So that** I see all available commands

**Acceptance Criteria:**
- Shows all commands with usage examples

---

## Constraints
- No database — all data in Python dict/list in memory
- No external libraries except `rich` (for pretty terminal output)
- Single file entry point: `main.py`
- Must run with: `python main.py`
- Interactive loop — app stays open until user types `exit`

---

## Out of Scope for Phase I
- Persistent storage
- Web interface
- AI features
- Recurring tasks
