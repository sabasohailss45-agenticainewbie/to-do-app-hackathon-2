import { Task, TaskCreate, TaskUpdate } from "@/types/task";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "https://to-do-app-hackathon-2-production.up.railway.app";

async function request<T>(path: string, options?: RequestInit): Promise<T> {
  const res = await fetch(`${API_URL}${path}`, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: res.statusText }));
    throw new Error(err.detail || "API error");
  }
  if (res.status === 204) return undefined as T;
  return res.json();
}

export const api = {
  getTasks: (params?: { status?: string; priority?: string; sort?: string; search?: string }) => {
    const qs = new URLSearchParams();
    if (params?.status) qs.set("status", params.status);
    if (params?.priority) qs.set("priority", params.priority);
    if (params?.sort) qs.set("sort", params.sort);
    if (params?.search) qs.set("search", params.search);
    const query = qs.toString() ? `?${qs.toString()}` : "";
    return request<Task[]>(`/tasks${query}`);
  },
  createTask: (data: TaskCreate) =>
    request<Task>("/tasks", { method: "POST", body: JSON.stringify(data) }),
  updateTask: (id: number, data: TaskUpdate) =>
    request<Task>(`/tasks/${id}`, { method: "PATCH", body: JSON.stringify(data) }),
  deleteTask: (id: number) =>
    request<void>(`/tasks/${id}`, { method: "DELETE" }),
  completeTask: (id: number) =>
    request<Task>(`/tasks/${id}`, { method: "PATCH", body: JSON.stringify({ status: "completed" }) }),
};
