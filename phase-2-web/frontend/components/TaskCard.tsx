"use client";
import { Task } from "@/types/task";
import PriorityBadge from "./PriorityBadge";

interface Props {
  task: Task;
  onComplete: (id: number) => void;
  onDelete: (id: number) => void;
  onEdit: (task: Task) => void;
}

export default function TaskCard({ task, onComplete, onDelete, onEdit }: Props) {
  const isCompleted = task.status === "completed";

  return (
    <div className={`flex items-start gap-3 p-4 rounded-lg border transition-all ${
      isCompleted ? "bg-gray-900 border-gray-800 opacity-60" : "bg-gray-800 border-gray-700"
    }`}>
      {/* Checkbox */}
      <input
        type="checkbox"
        checked={isCompleted}
        onChange={() => onComplete(task.id)}
        className="mt-1 w-4 h-4 accent-green-500 cursor-pointer flex-shrink-0"
      />

      {/* Content */}
      <div className="flex-1 min-w-0">
        <p className={`font-medium text-sm ${isCompleted ? "line-through text-gray-500" : "text-gray-100"}`}>
          {task.title}
        </p>
        <div className="flex flex-wrap gap-2 mt-2 items-center">
          <PriorityBadge priority={task.priority} />
          {task.due_date && (
            <span className="text-xs text-gray-400">📅 {task.due_date}</span>
          )}
          {task.tags.map((tag) => (
            <span key={tag} className="text-xs bg-gray-700 text-gray-300 px-2 py-0.5 rounded-full">
              #{tag}
            </span>
          ))}
        </div>
      </div>

      {/* Actions */}
      <div className="flex gap-1 flex-shrink-0">
        <button
          onClick={() => onEdit(task)}
          className="text-gray-400 hover:text-blue-400 transition-colors p-1 text-sm"
          title="Edit"
        >
          ✏️
        </button>
        <button
          onClick={() => {
            if (confirm(`Delete "${task.title}"?`)) onDelete(task.id);
          }}
          className="text-gray-400 hover:text-red-400 transition-colors p-1 text-sm"
          title="Delete"
        >
          🗑️
        </button>
      </div>
    </div>
  );
}
