"""
main.py — Entry point for the Todo Evolution Phase I Console App.
Run with: python main.py
"""
import sys
import shlex
from typing import Optional

from rich.console import Console

from todo import TodoManager, TaskNotFoundError, ValidationError
from display import (
    console,
    print_success,
    print_error,
    print_info,
    print_task_table,
    print_help,
    print_welcome,
)

manager = TodoManager()


def parse_flags(tokens: list[str]) -> tuple[list[str], dict[str, str]]:
    """Split tokens into positional args and --flag value pairs."""
    positional = []
    flags: dict[str, str] = {}
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        if tok.startswith("--"):
            key = tok[2:]
            if i + 1 < len(tokens) and not tokens[i + 1].startswith("--"):
                flags[key] = tokens[i + 1]
                i += 2
            else:
                flags[key] = "true"
                i += 1
        else:
            positional.append(tok)
            i += 1
    return positional, flags


def cmd_add(tokens: list[str]) -> None:
    positional, flags = parse_flags(tokens)
    if not positional:
        print_error('Usage: add "Task title" [--priority high|medium|low] [--tags work,home] [--due YYYY-MM-DD]')
        return

    title = " ".join(positional)
    priority = flags.get("priority", "medium")
    due_date = flags.get("due", None)
    tags_raw = flags.get("tags", "")
    tags = [t.strip() for t in tags_raw.split(",") if t.strip()] if tags_raw else []

    try:
        task = manager.add_task(title, priority=priority, tags=tags, due_date=due_date)
        print_success(f"Task #{task['id']} added: {task['title']}")
    except ValidationError as e:
        print_error(str(e))


def cmd_list(tokens: list[str]) -> None:
    _, flags = parse_flags(tokens)
    status = flags.get("status")
    priority = flags.get("priority")
    tag = flags.get("tag")
    sort_by = flags.get("sort")

    tasks = manager.list_tasks(status=status, priority=priority, tag=tag, sort_by=sort_by)

    title_parts = ["Tasks"]
    if status:
        title_parts.append(f"status={status}")
    if priority:
        title_parts.append(f"priority={priority}")
    if tag:
        title_parts.append(f"tag={tag}")

    print_task_table(tasks, title=" | ".join(title_parts))


def cmd_complete(tokens: list[str]) -> None:
    if not tokens:
        print_error("Usage: complete <id>")
        return
    try:
        task_id = int(tokens[0])
        task = manager.complete_task(task_id)
        print_success(f"Task #{task['id']} marked as completed: {task['title']}")
    except ValueError:
        print_error(f"ID must be a number. Got: '{tokens[0]}'")
    except TaskNotFoundError as e:
        print_error(str(e))


def cmd_delete(tokens: list[str]) -> None:
    if not tokens:
        print_error("Usage: delete <id>")
        return
    try:
        task_id = int(tokens[0])
        task = manager.delete_task(task_id)
        print_success(f"Task #{task['id']} deleted: {task['title']}")
    except ValueError:
        print_error(f"ID must be a number. Got: '{tokens[0]}'")
    except TaskNotFoundError as e:
        print_error(str(e))


def cmd_update(tokens: list[str]) -> None:
    if len(tokens) < 3:
        print_error('Usage: update <id> <field> <value>  (fields: title, priority, due_date, tags, status)')
        return
    try:
        task_id = int(tokens[0])
        field = tokens[1]
        value = " ".join(tokens[2:])

        if field == "tags":
            parsed_value = [t.strip() for t in value.split(",") if t.strip()]
            manager.update_task(task_id, **{field: parsed_value})
        else:
            manager.update_task(task_id, **{field: value})

        task = manager.get_task(task_id)
        print_success(f"Task #{task_id} updated — {field} set to: {value}")
    except ValueError:
        print_error(f"ID must be a number. Got: '{tokens[0]}'")
    except (TaskNotFoundError, ValidationError) as e:
        print_error(str(e))


def cmd_search(tokens: list[str]) -> None:
    if not tokens:
        print_error("Usage: search <keyword>")
        return
    query = " ".join(tokens)
    tasks = manager.search_tasks(query)
    if not tasks:
        print_info(f'No tasks found matching "{query}"')
    else:
        print_task_table(tasks, title=f'Search: "{query}"')


def run() -> None:
    print_welcome()

    while True:
        try:
            raw = console.input("\n[bold blue]todo>[/bold blue] ").strip()
        except (KeyboardInterrupt, EOFError):
            print_info("Goodbye!")
            break

        if not raw:
            continue

        try:
            tokens = shlex.split(raw)
        except ValueError as e:
            print_error(f"Could not parse input: {e}")
            continue

        if not tokens:
            continue

        command = tokens[0].lower()
        args = tokens[1:]

        if command in ("exit", "quit", "q"):
            print_info("Goodbye!")
            break
        elif command == "help":
            print_help()
        elif command == "add":
            cmd_add(args)
        elif command == "list":
            cmd_list(args)
        elif command == "complete":
            cmd_complete(args)
        elif command == "delete":
            cmd_delete(args)
        elif command == "update":
            cmd_update(args)
        elif command == "search":
            cmd_search(args)
        else:
            print_error(f"Unknown command: '{command}'. Type 'help' to see available commands.")


if __name__ == "__main__":
    run()
