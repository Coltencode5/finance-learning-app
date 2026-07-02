import Link from "next/link";

import { getAllModules, moduleHref } from "@/lib/graph";

export default function HomePage() {
  const modules = getAllModules();

  return (
    <>
      <h1>Finance Learning Graph</h1>
      <p className="muted">
        Nine modules, 235 globals, 478 zone nodes — loaded from canonical JSON at
        build time.
      </p>

      <h2>Modules</h2>
      <ul className="card-list">
        {modules.map((mod) => (
          <li key={mod.slug} className="card">
            <h3>
              <Link href={moduleHref(mod.slug)}>{mod.title}</Link>
            </h3>
            <p className="meta">
              <strong>Slug:</strong> {mod.slug}
              {mod.derived?.global_range ? (
                <>
                  {" "}
                  · <strong>Globals:</strong> {mod.derived.global_range}
                </>
              ) : null}
              {mod.derived?.zone_node_count != null ? (
                <>
                  {" "}
                  · <strong>Nodes:</strong> {mod.derived.zone_node_count}
                </>
              ) : null}
            </p>
            <p className="meta">
              <strong>Kind:</strong> {mod.kind} · <strong>Build order:</strong>{" "}
              {mod.build_order}
            </p>
          </li>
        ))}
      </ul>
    </>
  );
}
