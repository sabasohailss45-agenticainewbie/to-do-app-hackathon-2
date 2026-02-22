"use client";

interface Filters {
  search: string;
  status: string;
  priority: string;
  sort: string;
}

interface Props {
  filters: Filters;
  onChange: (f: Filters) => void;
}

export default function FilterBar({ filters, onChange }: Props) {
  const set = (key: keyof Filters, value: string) =>
    onChange({ ...filters, [key]: value });

  return (
    <div className="flex flex-wrap gap-3 items-center bg-gray-800 border border-gray-700 rounded-xl p-3">
      <input
        type="text"
        placeholder="🔍 Search tasks..."
        value={filters.search}
        onChange={(e) => set("search", e.target.value)}
        className="flex-1 min-w-[160px] bg-gray-900 border border-gray-600 rounded-lg px-3 py-1.5 text-sm text-gray-100 placeholder-gray-500 focus:outline-none focus:border-blue-500"
      />

      <select
        value={filters.status}
        onChange={(e) => set("status", e.target.value)}
        className="bg-gray-900 border border-gray-600 rounded-lg px-3 py-1.5 text-sm text-gray-100 focus:outline-none focus:border-blue-500"
      >
        <option value="">All Status</option>
        <option value="pending">Pending</option>
        <option value="completed">Completed</option>
      </select>

      <select
        value={filters.priority}
        onChange={(e) => set("priority", e.target.value)}
        className="bg-gray-900 border border-gray-600 rounded-lg px-3 py-1.5 text-sm text-gray-100 focus:outline-none focus:border-blue-500"
      >
        <option value="">All Priority</option>
        <option value="high">🔴 High</option>
        <option value="medium">🟡 Medium</option>
        <option value="low">🟢 Low</option>
      </select>

      <select
        value={filters.sort}
        onChange={(e) => set("sort", e.target.value)}
        className="bg-gray-900 border border-gray-600 rounded-lg px-3 py-1.5 text-sm text-gray-100 focus:outline-none focus:border-blue-500"
      >
        <option value="">Sort: Default</option>
        <option value="priority">Sort: Priority</option>
        <option value="title">Sort: Title</option>
        <option value="due_date">Sort: Due Date</option>
      </select>
    </div>
  );
}
