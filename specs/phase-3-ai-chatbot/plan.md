# Plan — Phase III: AI-Powered Todo Chatbot
**Phase:** 3 | **Command:** /sp.plan | **Date:** 2026-02-22

---

## Architecture Overview

```
phase-3-chatbot/
├── chatbot.py          # Entry point — chat loop
├── agent.py            # OpenAI Agents SDK agent setup
├── mcp_tools.py        # MCP tool definitions + API calls
├── api_client.py       # HTTP client for Phase II backend
├── .env                # OPENAI_API_KEY, API_BASE_URL
├── requirements.txt
└── README.md
```

---

## Component Breakdown

### 1. API Client (api_client.py)
- `httpx` async HTTP client
- Functions matching each API endpoint
- Error handling for network failures

### 2. MCP Tools (mcp_tools.py)
- Each tool defined with name, description, input schema
- Tool handler calls the corresponding api_client function
- Tools registered with MCP server

### 3. Agent Setup (agent.py)
- OpenAI Agents SDK `Agent` configured with:
  - System prompt describing the todo assistant role
  - MCP tools attached
  - Model: gpt-4o-mini

### 4. Chat Loop (chatbot.py)
- Simple `input()` loop
- Sends user message to agent
- Prints agent response
- Type `exit` to quit

---

## Agent System Prompt
```
You are a helpful todo list assistant. You help users manage their tasks
through natural language. You have tools to create, read, update, delete,
and complete tasks. Always confirm actions before deleting multiple tasks.
When a user mentions a task by description (not ID), search for it first.
Be concise and friendly.
```

---

## Key Design Decisions
1. **Terminal chat over web UI:** Simpler, meets hackathon requirements
2. **gpt-4o-mini:** Cost effective for demo
3. **MCP over function calling directly:** Required by spec (Official MCP SDK)
4. **httpx over requests:** Async support, cleaner API
