"""
Tests for TodoManager — Phase I
Run with: pytest tests/
"""
import pytest
from todo import TodoManager, TaskNotFoundError, ValidationError


@pytest.fixture
def manager():
    return TodoManager()


# ─── Add Task ──────────────────────────────────────────────────────────────────

def test_add_task_basic(manager):
    task = manager.add_task("Buy groceries")
    assert task["id"] == 1
    assert task["title"] == "Buy groceries"
    assert task["status"] == "pending"
    assert task["priority"] == "medium"
    assert task["tags"] == []
    assert task["due_date"] is None


def test_add_task_with_all_fields(manager):
    task = manager.add_task("Meeting", priority="high", tags=["work"], due_date="2026-03-01")
    assert task["priority"] == "high"
    assert task["tags"] == ["work"]
    assert task["due_date"] == "2026-03-01"


def test_add_task_ids_increment(manager):
    t1 = manager.add_task("Task 1")
    t2 = manager.add_task("Task 2")
    t3 = manager.add_task("Task 3")
    assert t1["id"] == 1
    assert t2["id"] == 2
    assert t3["id"] == 3


def test_add_task_empty_title_raises(manager):
    with pytest.raises(ValidationError):
        manager.add_task("")


def test_add_task_whitespace_title_raises(manager):
    with pytest.raises(ValidationError):
        manager.add_task("   ")


def test_add_task_invalid_priority_raises(manager):
    with pytest.raises(ValidationError):
        manager.add_task("Task", priority="urgent")


def test_add_task_invalid_date_raises(manager):
    with pytest.raises(ValidationError):
        manager.add_task("Task", due_date="01-03-2026")


def test_add_task_case_insensitive_priority(manager):
    task = manager.add_task("Task", priority="HIGH")
    assert task["priority"] == "high"


# ─── Delete Task ───────────────────────────────────────────────────────────────

def test_delete_task(manager):
    manager.add_task("Task 1")
    deleted = manager.delete_task(1)
    assert deleted["id"] == 1
    assert manager.count() == 0


def test_delete_nonexistent_task_raises(manager):
    with pytest.raises(TaskNotFoundError):
        manager.delete_task(99)


# ─── Complete Task ─────────────────────────────────────────────────────────────

def test_complete_task(manager):
    manager.add_task("Task 1")
    task = manager.complete_task(1)
    assert task["status"] == "completed"


def test_complete_nonexistent_task_raises(manager):
    with pytest.raises(TaskNotFoundError):
        manager.complete_task(99)


# ─── Update Task ───────────────────────────────────────────────────────────────

def test_update_title(manager):
    manager.add_task("Old title")
    task = manager.update_task(1, title="New title")
    assert task["title"] == "New title"


def test_update_priority(manager):
    manager.add_task("Task")
    task = manager.update_task(1, priority="low")
    assert task["priority"] == "low"


def test_update_tags(manager):
    manager.add_task("Task")
    task = manager.update_task(1, tags=["work", "urgent"])
    assert task["tags"] == ["work", "urgent"]


def test_update_invalid_field_raises(manager):
    manager.add_task("Task")
    with pytest.raises(ValidationError):
        manager.update_task(1, nonexistent_field="value")


def test_update_empty_title_raises(manager):
    manager.add_task("Task")
    with pytest.raises(ValidationError):
        manager.update_task(1, title="")


def test_update_nonexistent_task_raises(manager):
    with pytest.raises(TaskNotFoundError):
        manager.update_task(99, title="New")


# ─── List Tasks ────────────────────────────────────────────────────────────────

def test_list_all(manager):
    manager.add_task("Task 1")
    manager.add_task("Task 2")
    tasks = manager.list_tasks()
    assert len(tasks) == 2


def test_list_filter_by_status(manager):
    manager.add_task("Task 1")
    manager.add_task("Task 2")
    manager.complete_task(1)
    completed = manager.list_tasks(status="completed")
    assert len(completed) == 1
    assert completed[0]["id"] == 1


def test_list_filter_by_priority(manager):
    manager.add_task("High task", priority="high")
    manager.add_task("Low task", priority="low")
    high = manager.list_tasks(priority="high")
    assert len(high) == 1
    assert high[0]["priority"] == "high"


def test_list_filter_by_tag(manager):
    manager.add_task("Work task", tags=["work"])
    manager.add_task("Home task", tags=["home"])
    work_tasks = manager.list_tasks(tag="work")
    assert len(work_tasks) == 1
    assert "work" in work_tasks[0]["tags"]


def test_list_sort_by_priority(manager):
    manager.add_task("Low task", priority="low")
    manager.add_task("High task", priority="high")
    manager.add_task("Medium task", priority="medium")
    tasks = manager.list_tasks(sort_by="priority")
    assert tasks[0]["priority"] == "high"
    assert tasks[1]["priority"] == "medium"
    assert tasks[2]["priority"] == "low"


def test_list_sort_by_title(manager):
    manager.add_task("Zebra")
    manager.add_task("Apple")
    tasks = manager.list_tasks(sort_by="title")
    assert tasks[0]["title"] == "Apple"
    assert tasks[1]["title"] == "Zebra"


# ─── Search Tasks ──────────────────────────────────────────────────────────────

def test_search_finds_match(manager):
    manager.add_task("Buy groceries")
    manager.add_task("Go to gym")
    results = manager.search_tasks("groceries")
    assert len(results) == 1
    assert results[0]["title"] == "Buy groceries"


def test_search_case_insensitive(manager):
    manager.add_task("Buy GROCERIES")
    results = manager.search_tasks("groceries")
    assert len(results) == 1


def test_search_no_results(manager):
    manager.add_task("Buy groceries")
    results = manager.search_tasks("dentist")
    assert results == []


def test_search_empty_list(manager):
    results = manager.search_tasks("anything")
    assert results == []
