# Phase II — Frontend (Next.js + Tailwind)

## Setup

### 1. Install dependencies
```bash
cd phase-2-web/frontend
npm install
```

### 2. Configure API URL
```bash
cp .env.local.example .env.local
# Default: NEXT_PUBLIC_API_URL=http://localhost:8000
```

### 3. Run the frontend
```bash
npm run dev
```

Frontend runs at: http://localhost:3000

> Make sure the backend is running at localhost:8000 first!

## Features
- Add tasks with priority, tags, due date
- Filter by status and priority
- Search tasks in real-time
- Sort by priority, title, due date
- Mark tasks complete with checkbox
- Edit tasks in a modal
- Delete tasks with confirmation
