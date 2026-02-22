"use client";
import { useState } from "react";
import { Task, Priority, TaskUpdate } from "@/types/task";

interface Props {
  task: Task;
  onSave: (id: number, data: TaskUpdate) => Promise<void>;
  onClose: () => void;
}

export default function EditTaskModal({ task, onSave, onClose }: Props) {
  const [title, setTitle] = useState(task.title);
  const [priority, setPriority] = useState<Priority>(task.priority);
  const [tags, setTags] = useState(task.tags.join(", "));
  const [dueDate, setDueDate] = useState(task.due_date || "");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSave = async () => {
    if (!title.trim()) { setError("Title is required"); return; }
    setLoading(true);
    try {
      await onSave(task.id, {
        title: title.trim(),
        priority,
        tags: tags ? tags.split(",").map((t) => t.trim()).filter(Boolean) : [],
        due_date: dueDate || null,
      });
      onClose();
    } catch (err: unknown) {
      setError(err instanceof Error ? err.message : "Failed to save");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-black/60 flex items-center justify-center z-50 p-4">
      <div className="bg-gray-800 border border-gray-700 rounded-xl p-6 w-full max-w-md space-y-4">
        <h2 className="font-semibold text-gray-200">Edit Task</h2>
        {error && <p className="text-red-400 text-xs">{error}</p>}

        <input
          type="text" value={title} onChange={(e) => setTitle(e.target.value)}
          className="w-full bg-gray-900 border border-gray-600 rounded-lg px-3 py-2 text-sm text-gray-100 focus:outline-none focus:border-blue-500"
        />
        <select
          value={priority} onChange={(e) => setPriority(e.target.value as Priority)}
          className="w-full bg-gray-900 border border-gray-600 rounded-lg px-3 py-2 text-sm text-gray-100 focus:outline-none focus:border-blue-500"
        >
          <option value="high">🔴 High</option>
          <option value="medium">🟡 Medium</option>
          <option value="low">🟢 Low</option>
        </select>
        <input
          type="text" placeholder="Tags (comma-separated)" value={tags}
          onChange={(e) => setTags(e.target.value)}
          className="w-full bg-gray-900 border border-gray-600 rounded-lg px-3 py-2 text-sm text-gray-100 focus:outline-none focus:border-blue-500"
        />
        <input
          type="date" value={dueDate} onChange={(e) => setDueDate(e.target.value)}
          className="w-full bg-gray-900 border border-gray-600 rounded-lg px-3 py-2 text-sm text-gray-100 focus:outline-none focus:border-blue-500"
        />

        <div className="flex gap-3">
          <button onClick={onClose} className="flex-1 bg-gray-700 hover:bg-gray-600 text-gray-200 rounded-lg py-2 text-sm transition-colors">
            Cancel
          </button>
          <button onClick={handleSave} disabled={loading} className="flex-1 bg-blue-600 hover:bg-blue-500 disabled:opacity-50 text-white rounded-lg py-2 text-sm font-semibold transition-colors">
            {loading ? "Saving..." : "Save"}
          </button>
        </div>
      </div>
    </div>
  );
}
