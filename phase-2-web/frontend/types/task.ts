export type Priority = "high" | "medium" | "low";
export type Status = "pending" | "completed";

export interface Task {
  id: number;
  title: string;
  status: Status;
  priority: Priority;
  tags: string[];
  due_date: string | null;
  created_at: string;
  updated_at: string;
}

export interface TaskCreate {
  title: string;
  priority: Priority;
  tags: string[];
  due_date: string | null;
}

export interface TaskUpdate {
  title?: string;
  status?: Status;
  priority?: Priority;
  tags?: string[];
  due_date?: string | null;
}
