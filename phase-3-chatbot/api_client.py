"""
api_client.py — HTTP client for the Phase II FastAPI backend.
Phase III: AI-Powered Todo Chatbot
"""
import os
import httpx
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")


def _client() -> httpx.Client:
    return httpx.Client(base_url=API_BASE_URL, timeout=10.0)


def get_tasks(
    status: Optional[str] = None,
    priority: Optional[str] = None,
    search: Optional[str] = None,
) -> list[dict]:
    """Fetch tasks from the backend with optional filters."""
    params: dict = {}
    if status:
        params["status"] = status
    if priority:
        params["priority"] = priority
    if search:
        params["search"] = search

    with _client() as client:
        response = client.get("/tasks", params=params)
        response.raise_for_status()
        return response.json()


def create_task(
    title: str,
    priority: str = "medium",
    tags: Optional[list[str]] = None,
    due_date: Optional[str] = None,
) -> dict:
    """Create a new task."""
    payload: dict = {"title": title, "priority": priority, "tags": tags or []}
    if due_date:
        payload["due_date"] = due_date

    with _client() as client:
        response = client.post("/tasks", json=payload)
        response.raise_for_status()
        return response.json()


def update_task(task_id: int, **kwargs) -> dict:
    """Update a task by ID."""
    payload = {k: v for k, v in kwargs.items() if v is not None}
    with _client() as client:
        response = client.patch(f"/tasks/{task_id}", json=payload)
        response.raise_for_status()
        return response.json()


def delete_task(task_id: int) -> bool:
    """Delete a task by ID. Returns True on success."""
    with _client() as client:
        response = client.delete(f"/tasks/{task_id}")
        response.raise_for_status()
        return True


def complete_task(task_id: int) -> dict:
    """Mark a task as completed."""
    return update_task(task_id, status="completed")
