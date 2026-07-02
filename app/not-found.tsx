import Link from "next/link";

export default function NotFound() {
  return (
    <div className="not-found">
      <h1>Not found</h1>
      <p>The requested module, concept, or node does not exist in the canonical graph.</p>
      <p>
        <Link href="/">Return to module list</Link>
      </p>
    </div>
  );
}
