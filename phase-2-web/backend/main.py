"""
main.py — FastAPI application with all Todo CRUD endpoints.
Phase II: Full-Stack Web App

Run with: uvicorn main:app --reload
"""
from contextlib import asynccontextmanager
from datetime import datetime
from typing import Optional, List
import os, sys

from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

from database import create_tables, get_session
from models import Task
from schemas import TaskCreate, TaskUpdate, TaskResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(
    title="Todo Evolution API",
    description="Phase II: Full-Stack Web App — Spec-Kit Plus Hackathon 2026",
    version="2.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ─── Chat Schema ───────────────────────────────────────────────────────────────

class ChatMessage(BaseModel):
    message: str
    history: List[dict] = []


# ─── Chat Endpoint ─────────────────────────────────────────────────────────────

@app.post("/chat")
async def chat(payload: ChatMessage):
    """AI chatbot endpoint — takes a user message, returns AI response."""
    try:
        from openai import OpenAI
        import httpx as _httpx

        api_base = os.getenv("API_BASE_URL", "http://localhost:8000")

        def _get_tasks(status=None, priority=None, search=None):
            params = {}
            if status: params["status"] = status
            if priority: params["priority"] = priority
            if search: params["search"] = search
            r = _httpx.get(f"{api_base}/tasks", params=params, timeout=10)
            return r.json()

        def _create_task(title, priority="medium", tags=None, due_date=None):
            body = {"title": title, "priority": priority, "tags": tags or []}
            if due_date: body["due_date"] = due_date
            r = _httpx.post(f"{api_base}/tasks", json=body, timeout=10)
            return r.json()

        def _update_task(task_id, **kwargs):
            r = _httpx.patch(f"{api_base}/tasks/{task_id}", json=kwargs, timeout=10)
            return r.json()

        def _delete_task(task_id):
            _httpx.delete(f"{api_base}/tasks/{task_id}", timeout=10)
            return {"deleted": task_id}

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        tools = [
            {"type": "function", "function": {"name": "get_tasks", "description": "Get todo tasks. Filter by status (pending/completed), priority (high/medium/low), or search keyword.", "parameters": {"type": "object", "properties": {"status": {"type": "string"}, "priority": {"type": "string"}, "search": {"type": "string"}}, "required": []}}},
            {"type": "function", "function": {"name": "create_task", "description": "Create a new todo task.", "parameters": {"type": "object", "properties": {"title": {"type": "string"}, "priority": {"type": "string", "enum": ["high", "medium", "low"]}, "tags": {"type": "array", "items": {"type": "string"}}, "due_date": {"type": "string"}}, "required": ["title"]}}},
            {"type": "function", "function": {"name": "update_task", "description": "Update a task by ID. Can change title, priority, due_date, status, tags.", "parameters": {"type": "object", "properties": {"task_id": {"type": "integer"}, "title": {"type": "string"}, "priority": {"type": "string"}, "status": {"type": "string"}, "due_date": {"type": "string"}}, "required": ["task_id"]}}},
            {"type": "function", "function": {"name": "delete_task", "description": "Delete a task by ID.", "parameters": {"type": "object", "properties": {"task_id": {"type": "integer"}}, "required": ["task_id"]}}},
        ]

        system_prompt = """You are a friendly todo list assistant built into a todo web app.
You help users manage their tasks through natural language.
Use your tools to get, create, update, and delete tasks.
Always search for tasks first before completing or deleting by name.
Be concise and friendly. When listing tasks, format them nicely."""

        messages = [{"role": "system", "content": system_prompt}]
        for h in payload.history[-10:]:
            messages.append(h)
        messages.append({"role": "user", "content": payload.message})

        import json
        response = client.chat.completions.create(model="gpt-4o-mini", messages=messages, tools=tools, tool_choice="auto")
        msg = response.choices[0].message

        while msg.tool_calls:
            messages.append({"role": "assistant", "content": msg.content, "tool_calls": [{"id": tc.id, "type": "function", "function": {"name": tc.function.name, "arguments": tc.function.arguments}} for tc in msg.tool_calls]})
            for tc in msg.tool_calls:
                name = tc.function.name
                args = json.loads(tc.function.arguments)
                if name == "get_tasks":
                    result = _get_tasks(**args)
                elif name == "create_task":
                    result = _create_task(**args)
                elif name == "update_task":
                    tid = args.pop("task_id")
                    result = _update_task(tid, **args)
                elif name == "delete_task":
                    result = _delete_task(args["task_id"])
                else:
                    result = {"error": "unknown tool"}
                messages.append({"role": "tool", "tool_call_id": tc.id, "content": json.dumps(result, default=str)})
            response = client.chat.completions.create(model="gpt-4o-mini", messages=messages, tools=tools, tool_choice="auto")
            msg = response.choices[0].message

        return {"reply": msg.content, "history": messages[1:]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ─── Health Check ──────────────────────────────────────────────────────────────

@app.get("/health")
async def health_check():
    return {"status": "ok", "phase": "II"}


# ─── Get All Tasks ─────────────────────────────────────────────────────────────

@app.get("/tasks", response_model=List[TaskResponse])
async def get_tasks(
    status: Optional[str] = Query(None, description="Filter by status: pending | completed"),
    priority: Optional[str] = Query(None, description="Filter by priority: high | medium | low"),
    sort: Optional[str] = Query(None, description="Sort by: priority | title | due_date | created_at"),
    search: Optional[str] = Query(None, description="Search in task title"),
    session: AsyncSession = Depends(get_session),
):
    stmt = select(Task)

    if status:
        stmt = stmt.where(Task.status == status)
    if priority:
        stmt = stmt.where(Task.priority == priority)
    if search:
        stmt = stmt.where(Task.title.ilike(f"%{search}%"))

    result = await session.execute(stmt)
    tasks = result.scalars().all()

    # Python-side sort
    sort_map = {
        "priority": lambda t: {"high": 0, "medium": 1, "low": 2}.get(t.priority, 1),
        "title": lambda t: t.title.lower(),
        "due_date": lambda t: (t.due_date is None, t.due_date),
        "created_at": lambda t: t.created_at,
    }
    if sort and sort in sort_map:
        tasks = sorted(tasks, key=sort_map[sort])

    return [_task_response(t) for t in tasks]


# ─── Create Task ───────────────────────────────────────────────────────────────

@app.post("/tasks", response_model=TaskResponse, status_code=201)
async def create_task(
    payload: TaskCreate,
    session: AsyncSession = Depends(get_session),
):
    task = Task(
        title=payload.title,
        priority=payload.priority,
        tags=payload.tags or [],
        due_date=payload.due_date,
    )
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return _task_response(task)


# ─── Get Single Task ───────────────────────────────────────────────────────────

@app.get("/tasks/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int, session: AsyncSession = Depends(get_session)):
    task = await session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task #{task_id} not found")
    return _task_response(task)


# ─── Update Task ───────────────────────────────────────────────────────────────

@app.patch("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: int,
    payload: TaskUpdate,
    session: AsyncSession = Depends(get_session),
):
    task = await session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task #{task_id} not found")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(task, field, value)

    task.updated_at = datetime.utcnow()
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return _task_response(task)


# ─── Delete Task ───────────────────────────────────────────────────────────────

@app.delete("/tasks/{task_id}", status_code=204)
async def delete_task(task_id: int, session: AsyncSession = Depends(get_session)):
    task = await session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task #{task_id} not found")
    await session.delete(task)
    await session.commit()


# ─── Helper ────────────────────────────────────────────────────────────────────

def _task_response(task: Task) -> TaskResponse:
    return TaskResponse(
        id=task.id,
        title=task.title,
        status=task.status,
        priority=task.priority,
        tags=task.tags or [],
        due_date=task.due_date,
        created_at=task.created_at,
        updated_at=task.updated_at,
    )
