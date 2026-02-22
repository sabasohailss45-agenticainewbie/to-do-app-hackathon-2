"use client";
import { useState, useEffect, useCallback, useRef } from "react";
import { Task, TaskCreate, TaskUpdate } from "@/types/task";
import { api } from "@/lib/api";
import AddTaskForm from "@/components/AddTaskForm";
import FilterBar from "@/components/FilterBar";
import TaskList from "@/components/TaskList";
import EditTaskModal from "@/components/EditTaskModal";
import ChatBot from "@/components/ChatBot";

function useTaskNotifications(tasks: Task[]) {
  const notifiedIds = useRef<Set<number>>(new Set());

  useEffect(() => {
    if (!("Notification" in window)) return;
    if (Notification.permission === "default") {
      Notification.requestPermission();
    }
    if (Notification.permission !== "granted") return;

    const now = new Date();
    tasks.forEach((task) => {
      if (task.status === "completed" || !task.due_date) return;
      if (notifiedIds.current.has(task.id)) return;

      const due = new Date(task.due_date);
      const diffMs = due.getTime() - now.getTime();
      const diffHours = diffMs / (1000 * 60 * 60);

      if (diffHours <= 24 && diffHours >= 0) {
        notifiedIds.current.add(task.id);
        const label = diffHours <= 1 ? "within the hour" : "today";
        new Notification("Todo Reminder", {
          body: `"${task.title}" is due ${label}!`,
          icon: "/favicon.ico",
        });
      } else if (diffMs < 0) {
        notifiedIds.current.add(task.id);
        new Notification("Overdue Task", {
          body: `"${task.title}" is overdue!`,
          icon: "/favicon.ico",
        });
      }
    });
  }, [tasks]);
}

interface Filters {
  search: string;
  status: string;
  priority: string;
  sort: string;
}

export default function HomePage() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [filters, setFilters] = useState<Filters>({ search: "", status: "", priority: "", sort: "" });
  const [editingTask, setEditingTask] = useState<Task | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const fetchTasks = useCallback(async () => {
    try {
      const data = await api.getTasks({
        status: filters.status || undefined,
        priority: filters.priority || undefined,
        sort: filters.sort || undefined,
      });
      setTasks(data);
      setError("");
    } catch (err: unknown) {
      setError(err instanceof Error ? err.message : "Failed to load tasks");
    } finally {
      setLoading(false);
    }
  }, [filters.status, filters.priority, filters.sort]);

  useEffect(() => {
    fetchTasks();
  }, [fetchTasks]);

  const handleAdd = async (data: TaskCreate) => {
    const newTask = await api.createTask(data);
    setTasks((prev) => [newTask, ...prev]);
  };

  const handleComplete = async (id: number) => {
    const task = tasks.find((t) => t.id === id);
    if (!task) return;
    const newStatus = task.status === "completed" ? "pending" : "completed";
    const updated = await api.updateTask(id, { status: newStatus });
    setTasks((prev) => prev.map((t) => (t.id === id ? updated : t)));
  };

  const handleDelete = async (id: number) => {
    await api.deleteTask(id);
    setTasks((prev) => prev.filter((t) => t.id !== id));
  };

  const handleEdit = async (id: number, data: TaskUpdate) => {
    const updated = await api.updateTask(id, data);
    setTasks((prev) => prev.map((t) => (t.id === id ? updated : t)));
  };

  useTaskNotifications(tasks);

  const pending = tasks.filter((t) => t.status === "pending").length;
  const completed = tasks.filter((t) => t.status === "completed").length;

  return (
    <main className="max-w-2xl mx-auto px-4 py-8 space-y-6">
      {/* Header */}
      <div className="text-center">
        <h1 className="text-3xl font-bold text-white">Todo Evolution</h1>
        <p className="text-gray-400 text-sm mt-1">Phase II — Full-Stack Web App</p>
        <div className="flex justify-center gap-6 mt-3 text-sm">
          <span className="text-yellow-400">{pending} pending</span>
          <span className="text-green-400">{completed} completed</span>
        </div>
      </div>

      {/* Error */}
      {error && (
        <div className="bg-red-900/50 border border-red-700 text-red-300 rounded-lg p-3 text-sm">
          {error} — Is the backend running at localhost:8000?
        </div>
      )}

      {/* Add form */}
      <AddTaskForm onAdd={handleAdd} />

      {/* Filters */}
      <FilterBar filters={filters} onChange={setFilters} />

      {/* Task list */}
      {loading ? (
        <div className="text-center py-12 text-gray-500">Loading tasks...</div>
      ) : (
        <TaskList
          tasks={tasks}
          searchQuery={filters.search}
          onComplete={handleComplete}
          onDelete={handleDelete}
          onEdit={setEditingTask}
        />
      )}

      {/* Edit modal */}
      {editingTask && (
        <EditTaskModal
          task={editingTask}
          onSave={handleEdit}
          onClose={() => setEditingTask(null)}
        />
      )}

      {/* AI Chatbot — floating button bottom right */}
      <ChatBot onTasksChanged={fetchTasks} />
    </main>
  );
}
