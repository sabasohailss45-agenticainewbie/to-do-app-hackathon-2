"use client";
import { Task } from "@/types/task";
import TaskCard from "./TaskCard";

interface Props {
  tasks: Task[];
  searchQuery: string;
  onComplete: (id: number) => void;
  onDelete: (id: number) => void;
  onEdit: (task: Task) => void;
}

export default function TaskList({ tasks, searchQuery, onComplete, onDelete, onEdit }: Props) {
  const filtered = searchQuery
    ? tasks.filter((t) => t.title.toLowerCase().includes(searchQuery.toLowerCase()))
    : tasks;

  if (filtered.length === 0) {
    return (
      <div className="text-center py-16 text-gray-500">
        <p className="text-4xl mb-3">📭</p>
        <p className="text-sm">
          {searchQuery ? `No tasks matching "${searchQuery}"` : "No tasks yet. Add one above!"}
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-2">
      {filtered.map((task) => (
        <TaskCard
          key={task.id}
          task={task}
          onComplete={onComplete}
          onDelete={onDelete}
          onEdit={onEdit}
        />
      ))}
      <p className="text-xs text-gray-600 text-right pt-1">{filtered.length} task{filtered.length !== 1 ? "s" : ""}</p>
    </div>
  );
}
