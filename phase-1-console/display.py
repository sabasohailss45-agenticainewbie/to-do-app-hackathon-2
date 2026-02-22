"""
Display layer — Rich terminal output for the Todo app.
Phase I: Console App
"""
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

console = Console()

PRIORITY_COLORS = {
    "high": "bold red",
    "medium": "bold yellow",
    "low": "bold green",
}

STATUS_COLORS = {
    "pending": "yellow",
    "completed": "green",
}


def print_success(message: str) -> None:
    console.print(f"[bold green]✓[/bold green] {message}")


def print_error(message: str) -> None:
    console.print(f"[bold red]✗ Error:[/bold red] {message}")


def print_info(message: str) -> None:
    console.print(f"[bold cyan]ℹ[/bold cyan] {message}")


def print_task_table(tasks: list[dict], title: str = "Your Tasks") -> None:
    """Render a list of tasks as a Rich table."""
    if not tasks:
        console.print(Panel(
            '[dim]No tasks found. Add one with: [bold]add "task title"[/bold][/dim]',
            title=title,
            border_style="dim",
        ))
        return

    table = Table(
        title=title,
        box=box.ROUNDED,
        show_header=True,
        header_style="bold magenta",
        border_style="bright_blue",
    )

    table.add_column("ID", style="dim", width=4, justify="right")
    table.add_column("Title", min_width=20)
    table.add_column("Priority", width=8, justify="center")
    table.add_column("Status", width=10, justify="center")
    table.add_column("Due Date", width=12, justify="center")
    table.add_column("Tags", min_width=10)

    for task in tasks:
        priority_style = PRIORITY_COLORS.get(task["priority"], "white")
        status_style = STATUS_COLORS.get(task["status"], "white")

        title_display = task["title"]
        if task["status"] == "completed":
            title_display = f"[strike dim]{title_display}[/strike dim]"

        tags_display = ", ".join(task["tags"]) if task["tags"] else "[dim]—[/dim]"
        due_display = task["due_date"] if task["due_date"] else "[dim]—[/dim]"

        table.add_row(
            str(task["id"]),
            title_display,
            f"[{priority_style}]{task['priority'].upper()}[/{priority_style}]",
            f"[{status_style}]{task['status']}[/{status_style}]",
            due_display,
            tags_display,
        )

    console.print(table)


def print_help() -> None:
    """Display all available commands."""
    help_text = """
[bold cyan]Available Commands:[/bold cyan]

  [bold green]add[/bold green] "Task title" [dim][--priority high|medium|low] [--tags tag1,tag2] [--due YYYY-MM-DD][/dim]
      Add a new task

  [bold green]list[/bold green] [dim][--status pending|completed] [--priority high|medium|low] [--tag tagname] [--sort priority|title|status][/dim]
      Show all tasks with optional filters

  [bold green]complete[/bold green] <id>
      Mark task as completed

  [bold green]delete[/bold green] <id>
      Delete a task permanently

  [bold green]update[/bold green] <id> <field> <value>
      Update a task field (title, priority, due_date, tags)

  [bold green]search[/bold green] <keyword>
      Search tasks by keyword

  [bold green]help[/bold green]
      Show this help message

  [bold green]exit[/bold green]
      Quit the application

[dim]Examples:
  add "Buy groceries" --priority high --tags home --due 2026-03-01
  list --priority high --status pending
  update 1 title "Buy organic groceries"
  complete 1
  delete 1
  search groceries[/dim]
"""
    console.print(Panel(help_text, title="[bold]Todo App Help[/bold]", border_style="cyan"))


def print_welcome() -> None:
    """Display the welcome banner."""
    console.print(Panel(
        "[bold cyan]Todo Evolution — Phase I Console App[/bold cyan]\n"
        "[dim]Spec-Driven Development | Panaversity Hackathon 2026[/dim]\n\n"
        "Type [bold green]help[/bold green] to see all commands. Type [bold red]exit[/bold red] to quit.",
        border_style="bright_blue",
        padding=(1, 2),
    ))
