# Spec — Phase III: AI-Powered Todo Chatbot
**Phase:** 3 | **Command:** /sp.specify | **Date:** 2026-02-22

---

## Overview
An AI chatbot that lets users manage their todo list through natural language conversation. The chatbot uses OpenAI Agents SDK with MCP (Model Context Protocol) tools that call the Phase II FastAPI backend.

---

## User Stories

### US-1: Natural Language Task Creation
**As a** user
**I want to** type "Add buy groceries with high priority"
**So that** the AI creates the task for me

**Acceptance Criteria:**
- AI understands and calls the create_task MCP tool
- Confirms: "Done! I've added 'Buy groceries' with high priority"
- Task appears in Phase II web app

---

### US-2: Natural Language Task Listing
**As a** user
**I want to** type "Show me my pending tasks"
**So that** the AI lists all pending tasks

**Acceptance Criteria:**
- AI calls get_tasks tool with status=pending filter
- Displays tasks in readable format in chat
- "You have 3 pending tasks: ..."

---

### US-3: Smart Task Completion
**As a** user
**I want to** type "Mark the groceries task as done"
**So that** the AI finds and completes it

**Acceptance Criteria:**
- AI searches tasks, finds best match, calls complete_task
- Confirms: "Done! 'Buy groceries' is now marked complete"
- If ambiguous, asks: "Did you mean task #3 'Buy groceries'?"

---

### US-4: Natural Language Delete
**As a** user
**I want to** type "Delete all completed tasks"
**So that** the AI removes them all

**Acceptance Criteria:**
- AI lists what it will delete, asks confirmation
- User types "yes" → AI deletes them all
- Confirms how many deleted

---

### US-5: Rescheduling Tasks
**As a** user
**I want to** type "Move my morning meeting to next Monday"
**So that** the due date is updated

**Acceptance Criteria:**
- AI parses relative dates ("next Monday" → actual date)
- Calls update_task with new due_date
- Confirms: "Updated! 'Morning meeting' moved to 2026-02-25"

---

### US-6: Task Summary
**As a** user
**I want to** type "What's on my plate today?"
**So that** the AI summarizes my tasks

**Acceptance Criteria:**
- AI fetches all tasks, summarizes by priority and count
- Highlights overdue tasks

---

## MCP Tools Required

| Tool Name | Description | Calls API |
|-----------|-------------|-----------|
| `get_tasks` | List tasks with optional filters | GET /tasks |
| `create_task` | Create a new task | POST /tasks |
| `update_task` | Update task fields | PATCH /tasks/{id} |
| `complete_task` | Mark task as complete | PATCH /tasks/{id} |
| `delete_task` | Delete a task | DELETE /tasks/{id} |
| `search_tasks` | Search tasks by keyword | GET /tasks?search= |

---

## Architecture
- OpenAI Agents SDK: manages the AI agent and tool calls
- MCP SDK: exposes tools to the agent in standard protocol
- Phase II FastAPI: actual data storage (must be running)
- Chat interface: simple terminal input/output loop
- Model: gpt-4o-mini

---

## Constraints
- Phase II backend MUST be running before Phase III
- API base URL configurable via .env: `API_BASE_URL=http://localhost:8000`
- OpenAI API key from .env: `OPENAI_API_KEY=...`
- Run with: `python chatbot.py`
