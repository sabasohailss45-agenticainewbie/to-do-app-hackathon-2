import { Priority } from "@/types/task";

const styles: Record<Priority, string> = {
  high: "bg-red-900 text-red-200 border border-red-700",
  medium: "bg-yellow-900 text-yellow-200 border border-yellow-700",
  low: "bg-green-900 text-green-200 border border-green-700",
};

export default function PriorityBadge({ priority }: { priority: Priority }) {
  return (
    <span className={`px-2 py-0.5 rounded text-xs font-semibold uppercase ${styles[priority]}`}>
      {priority}
    </span>
  );
}
