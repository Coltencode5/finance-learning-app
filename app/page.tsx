import Link from "next/link";

import { getActiveModules, getDraftModules, moduleHref } from "@/lib/graph";

export default function HomePage() {
  const modules = getActiveModules();
  const drafts = getDraftModules();
  const showDrafts = process.env.SHOW_DRAFT_MODULES === "1";

  return (
    <>
      <h1>Finance Learning Graph</h1>
      <p className="muted">
        {modules.length} active modules, 235 globals, 478 zone nodes — loaded from
        canonical JSON at build time.
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

      {showDrafts && drafts.length > 0 ? (
        <>
          <h2>Draft modules</h2>
          <p className="muted">
            Scaffold-only modules (excluded from validation and graph). Set{" "}
            <code>SHOW_DRAFT_MODULES=1</code> to reveal.
          </p>
          <ul className="card-list">
            {drafts.map((mod) => (
              <li key={mod.slug} className="card">
                <h3>
                  <Link href={moduleHref(mod.slug)}>{mod.title}</Link>
                  <span className="tag">draft</span>
                </h3>
                <p className="meta">
                  <strong>Slug:</strong> {mod.slug}
                </p>
              </li>
            ))}
          </ul>
        </>
      ) : null}
    </>
  );
}
