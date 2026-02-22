# Tasks — Phase III: AI-Powered Todo Chatbot
**Phase:** 3 | **Command:** /sp.tasks | **Date:** 2026-02-22

---

## Task List

| # | Task | File | Depends On |
|---|------|------|-----------|
| 1 | Create requirements.txt (openai, httpx, python-dotenv, mcp) | `phase-3-chatbot/requirements.txt` | None |
| 2 | Create api_client.py with httpx calls to Phase II backend | `phase-3-chatbot/api_client.py` | 1 |
| 3 | Create mcp_tools.py with all 6 MCP tool definitions | `phase-3-chatbot/mcp_tools.py` | 2 |
| 4 | Create agent.py with OpenAI Agents SDK setup | `phase-3-chatbot/agent.py` | 3 |
| 5 | Create chatbot.py with interactive chat loop | `phase-3-chatbot/chatbot.py` | 4 |
| 6 | Create .env.example | `phase-3-chatbot/.env.example` | None |
| 7 | Create README.md with setup and run instructions | `phase-3-chatbot/README.md` | 5 |

---

## Acceptance Checklist
- [ ] `python chatbot.py` starts a chat session
- [ ] "Show my tasks" lists tasks from Phase II backend
- [ ] "Add buy milk with high priority" creates a task
- [ ] "Mark the milk task as done" completes it
- [ ] "Delete all completed tasks" asks confirmation then deletes
- [ ] "Reschedule meeting to tomorrow" updates due date
- [ ] Type `exit` to quit
