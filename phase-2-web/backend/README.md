# Phase II — Backend (FastAPI + Neon DB)

## Setup

### 1. Install dependencies
```bash
cd phase-2-web/backend
pip install -r requirements.txt
```

### 2. Configure database
```bash
cp .env.example .env
# Edit .env and paste your Neon DB connection string
```

Get your Neon DB connection string from: https://neon.tech
Format: `postgresql+asyncpg://user:password@host/dbname?sslmode=require`

### 3. Run the backend
```bash
uvicorn main:app --reload
```

Backend runs at: http://localhost:8000
API docs at: http://localhost:8000/docs

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | /health | Health check |
| GET | /tasks | List tasks (supports ?status=&priority=&sort=&search=) |
| POST | /tasks | Create task |
| GET | /tasks/{id} | Get single task |
| PATCH | /tasks/{id} | Update task |
| DELETE | /tasks/{id} | Delete task |

## Run Tests
```bash
pytest tests/ -v
```
