"""
mcp_tools.py — MCP tool definitions for the Todo AI Agent.
Phase III: AI-Powered Todo Chatbot

Each function is registered as an OpenAI Agents SDK tool.
The agent calls these tools to manage todos via the Phase II API.
"""
import json
from typing import Optional
import api_client


def get_tasks(
    status: Optional[str] = None,
    priority: Optional[str] = None,
    search: Optional[str] = None,
) -> str:
    """
    Get todo tasks from the list.

    Args:
        status: Filter by status — 'pending' or 'completed'. Leave empty for all.
        priority: Filter by priority — 'high', 'medium', or 'low'. Leave empty for all.
        search: Search keyword to filter tasks by title.

    Returns:
        JSON string with list of matching tasks.
    """
    try:
        tasks = api_client.get_tasks(status=status, priority=priority, search=search)
        if not tasks:
            return "No tasks found matching the criteria."
        return json.dumps(tasks, indent=2, default=str)
    except Exception as e:
        return f"Error fetching tasks: {e}"


def create_task(
    title: str,
    priority: str = "medium",
    tags: Optional[str] = None,
    due_date: Optional[str] = None,
) -> str:
    """
    Create a new todo task.

    Args:
        title: The task title (required).
        priority: Task priority — 'high', 'medium', or 'low'. Default: 'medium'.
        tags: Comma-separated tags, e.g. 'work,urgent'. Optional.
        due_date: Due date in YYYY-MM-DD format. Optional.

    Returns:
        Confirmation message with the created task details.
    """
    try:
        tag_list = [t.strip() for t in tags.split(",")] if tags else []
        task = api_client.create_task(
            title=title,
            priority=priority,
            tags=tag_list,
            due_date=due_date,
        )
        return f"Task created successfully! ID: {task['id']}, Title: '{task['title']}', Priority: {task['priority']}"
    except Exception as e:
        return f"Error creating task: {e}"


def update_task(
    task_id: int,
    title: Optional[str] = None,
    priority: Optional[str] = None,
    due_date: Optional[str] = None,
    tags: Optional[str] = None,
) -> str:
    """
    Update an existing todo task.

    Args:
        task_id: The numeric ID of the task to update.
        title: New title. Optional.
        priority: New priority — 'high', 'medium', or 'low'. Optional.
        due_date: New due date in YYYY-MM-DD format. Optional.
        tags: New comma-separated tags. Optional.

    Returns:
        Confirmation message.
    """
    try:
        kwargs: dict = {}
        if title:
            kwargs["title"] = title
        if priority:
            kwargs["priority"] = priority
        if due_date:
            kwargs["due_date"] = due_date
        if tags is not None:
            kwargs["tags"] = [t.strip() for t in tags.split(",")]

        task = api_client.update_task(task_id, **kwargs)
        return f"Task #{task_id} updated successfully! Title: '{task['title']}'"
    except Exception as e:
        return f"Error updating task #{task_id}: {e}"


def complete_task(task_id: int) -> str:
    """
    Mark a todo task as completed.

    Args:
        task_id: The numeric ID of the task to complete.

    Returns:
        Confirmation message.
    """
    try:
        task = api_client.complete_task(task_id)
        return f"Task #{task_id} '{task['title']}' marked as completed!"
    except Exception as e:
        return f"Error completing task #{task_id}: {e}"


def delete_task(task_id: int) -> str:
    """
    Delete a todo task permanently.

    Args:
        task_id: The numeric ID of the task to delete.

    Returns:
        Confirmation message.
    """
    try:
        api_client.delete_task(task_id)
        return f"Task #{task_id} has been deleted."
    except Exception as e:
        return f"Error deleting task #{task_id}: {e}"


def search_tasks(query: str) -> str:
    """
    Search todo tasks by keyword in the title.

    Args:
        query: The search keyword.

    Returns:
        JSON string with matching tasks.
    """
    try:
        tasks = api_client.get_tasks(search=query)
        if not tasks:
            return f"No tasks found matching '{query}'."
        return json.dumps(tasks, indent=2, default=str)
    except Exception as e:
        return f"Error searching tasks: {e}"


# List of all tools to register with the agent
ALL_TOOLS = [
    get_tasks,
    create_task,
    update_task,
    complete_task,
    delete_task,
    search_tasks,
]
