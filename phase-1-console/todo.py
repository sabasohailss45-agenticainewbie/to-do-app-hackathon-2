"""
TodoManager — In-memory todo list business logic.
Phase I: Console App
"""
from datetime import datetime
from typing import Optional


class TaskNotFoundError(Exception):
    """Raised when a task ID does not exist."""
    pass


class ValidationError(Exception):
    """Raised when input data is invalid."""
    pass


class TodoManager:
    """Manages an in-memory list of todo tasks."""

    VALID_PRIORITIES = {"high", "medium", "low"}
    VALID_STATUSES = {"pending", "completed"}

    def __init__(self) -> None:
        self._tasks: dict[int, dict] = {}
        self._counter: int = 0

    def _next_id(self) -> int:
        self._counter += 1
        return self._counter

    def _validate_priority(self, priority: str) -> str:
        p = priority.lower().strip()
        if p not in self.VALID_PRIORITIES:
            raise ValidationError(f"Priority must be high, medium, or low. Got: '{priority}'")
        return p

    def _validate_due_date(self, due_date: str) -> str:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
            return due_date
        except ValueError:
            raise ValidationError(f"Invalid date format. Use YYYY-MM-DD. Got: '{due_date}'")

    def _get_task_or_raise(self, task_id: int) -> dict:
        if task_id not in self._tasks:
            raise TaskNotFoundError(f"Task #{task_id} not found.")
        return self._tasks[task_id]

    def add_task(
        self,
        title: str,
        priority: str = "medium",
        tags: Optional[list[str]] = None,
        due_date: Optional[str] = None,
    ) -> dict:
        """Create a new task and return it."""
        title = title.strip()
        if not title:
            raise ValidationError("Task title cannot be empty.")

        priority = self._validate_priority(priority)
        if due_date:
            due_date = self._validate_due_date(due_date)

        task_id = self._next_id()
        task = {
            "id": task_id,
            "title": title,
            "status": "pending",
            "priority": priority,
            "tags": tags or [],
            "due_date": due_date,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        }
        self._tasks[task_id] = task
        return task

    def delete_task(self, task_id: int) -> dict:
        """Delete a task by ID and return the deleted task."""
        task = self._get_task_or_raise(task_id)
        del self._tasks[task_id]
        return task

    def update_task(self, task_id: int, **kwargs) -> dict:
        """Update one or more fields of a task."""
        task = self._get_task_or_raise(task_id)

        allowed_fields = {"title", "priority", "due_date", "tags", "status"}
        for key, value in kwargs.items():
            if key not in allowed_fields:
                raise ValidationError(f"Unknown field: '{key}'. Allowed: {', '.join(allowed_fields)}")
            if key == "priority":
                value = self._validate_priority(value)
            if key == "due_date" and value:
                value = self._validate_due_date(value)
            if key == "title":
                value = value.strip()
                if not value:
                    raise ValidationError("Task title cannot be empty.")
            if key == "status" and value not in self.VALID_STATUSES:
                raise ValidationError(f"Status must be pending or completed.")
            task[key] = value

        return task

    def complete_task(self, task_id: int) -> dict:
        """Mark a task as completed."""
        task = self._get_task_or_raise(task_id)
        task["status"] = "completed"
        return task

    def get_task(self, task_id: int) -> dict:
        """Return a single task by ID."""
        return self._get_task_or_raise(task_id)

    def list_tasks(
        self,
        status: Optional[str] = None,
        priority: Optional[str] = None,
        tag: Optional[str] = None,
        sort_by: Optional[str] = None,
    ) -> list[dict]:
        """Return tasks with optional filtering and sorting."""
        tasks = list(self._tasks.values())

        if status:
            tasks = [t for t in tasks if t["status"] == status.lower()]
        if priority:
            tasks = [t for t in tasks if t["priority"] == priority.lower()]
        if tag:
            tasks = [t for t in tasks if tag.lower() in [tg.lower() for tg in t["tags"]]]

        sort_options = {
            "priority": lambda t: {"high": 0, "medium": 1, "low": 2}[t["priority"]],
            "title": lambda t: t["title"].lower(),
            "status": lambda t: t["status"],
            "id": lambda t: t["id"],
        }
        if sort_by and sort_by in sort_options:
            tasks.sort(key=sort_options[sort_by])
        else:
            tasks.sort(key=lambda t: t["id"])

        return tasks

    def search_tasks(self, query: str) -> list[dict]:
        """Search tasks by title (case-insensitive)."""
        q = query.lower().strip()
        return [t for t in self._tasks.values() if q in t["title"].lower()]

    def count(self) -> int:
        """Return total number of tasks."""
        return len(self._tasks)
