# Phase III — AI-Powered Todo Chatbot

## Prerequisites
- Phase II backend must be running at `http://localhost:8000`
- OpenAI API key

## Setup

### 1. Install dependencies
```bash
cd phase-3-chatbot
pip install -r requirements.txt
```

### 2. Configure environment
```bash
cp .env.example .env
# Edit .env:
# OPENAI_API_KEY=your-key-here
# API_BASE_URL=http://localhost:8000
```

### 3. Start Phase II backend first
```bash
cd ../phase-2-web/backend
uvicorn main:app --reload
```

### 4. Run the chatbot
```bash
cd ../../phase-3-chatbot
python chatbot.py
```

## Example Conversations

```
You: Show me my pending tasks
Assistant: You have 3 pending tasks: ...

You: Add buy milk with high priority
Assistant: Done! I've added 'Buy milk' with high priority (Task #4)

You: Mark the milk task as done
Assistant: Task #4 'Buy milk' is now marked as completed!

You: Reschedule my meeting to 2026-03-10
Assistant: Updated! 'Morning meeting' is now due on 2026-03-10

You: Delete all completed tasks
Assistant: I found 2 completed tasks. Shall I delete them? (yes/no)
```

## Tech Stack
- OpenAI Agents SDK — AI agent orchestration
- MCP (Model Context Protocol) — tool definitions
- gpt-4o-mini — language model
- httpx — HTTP calls to Phase II backend
