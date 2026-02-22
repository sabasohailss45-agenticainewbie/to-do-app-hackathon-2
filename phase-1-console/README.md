# Phase I — In-Memory Python Console Todo App

**Spec-Kit Plus | Panaversity Hackathon 2026**

---

## How to Run

### 1. Install dependencies
```bash
cd phase-1-console
pip install -r requirements.txt
```

### 2. Start the app
```bash
python main.py
```

---

## Commands

| Command | Example | Description |
|---------|---------|-------------|
| `add` | `add "Buy groceries" --priority high --tags home --due 2026-03-01` | Add a task |
| `list` | `list --status pending --priority high --sort priority` | View tasks |
| `complete` | `complete 1` | Mark task #1 done |
| `delete` | `delete 1` | Delete task #1 |
| `update` | `update 1 title "New title"` | Update a field |
| `search` | `search groceries` | Search by keyword |
| `help` | `help` | Show all commands |
| `exit` | `exit` | Quit |

---

## Run Tests
```bash
pytest tests/ -v
```

---

## Tech Stack
- Python 3.11+
- `rich` — beautiful terminal output
- `pytest` — testing
- In-memory storage (no database)
