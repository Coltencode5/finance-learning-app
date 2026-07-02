import Link from "next/link";
import { notFound } from "next/navigation";

import {
  conceptHref,
  getAllModules,
  getModule,
  getModuleDependencies,
  getNodesByModule,
  moduleHref,
} from "@/lib/graph";

export function generateStaticParams() {
  return getAllModules().map((m) => ({ moduleSlug: m.slug }));
}

export default async function ModulePage({
  params,
}: {
  params: Promise<{ moduleSlug: string }>;
}) {
  const { moduleSlug } = await params;
  const mod = getModule(moduleSlug);
  if (!mod) {
    notFound();
  }

  const nodes = getNodesByModule(moduleSlug);
  const deps = getModuleDependencies(moduleSlug);

  const byZone = mod.zones.map((z) => ({
    ...z,
    nodes: nodes.filter((n) => n.zone === z.zone),
  }));

  return (
    <>
      <p className="meta">
        <Link href="/">Home</Link> / {mod.title}
      </p>
      <h1>{mod.title}</h1>
      <p className="meta">
        <span className="badge">{mod.slug}</span>
        <span className="badge">{mod.kind}</span>
        {mod.derived?.global_range ? (
          <span className="badge">Globals {mod.derived.global_range}</span>
        ) : null}
        {mod.derived?.zone_node_count != null ? (
          <span className="badge">{mod.derived.zone_node_count} nodes</span>
        ) : null}
      </p>

      {deps && Object.keys(deps).length > 0 ? (
        <section className="section">
          <h2>Cross-module dependencies</h2>
          <p className="muted">Reference counts to other modules (from graph index).</p>
          <table className="dep-table">
            <tbody>
              {Object.entries(deps)
                .sort((a, b) => b[1] - a[1])
                .map(([target, count]) => (
                  <tr key={target}>
                    <td>
                      {target === "global" ? (
                        "Shared globals"
                      ) : (
                        <Link href={moduleHref(target)}>{target}</Link>
                      )}
                    </td>
                    <td>{count} refs</td>
                  </tr>
                ))}
            </tbody>
          </table>
        </section>
      ) : null}

      <h2>Zones</h2>
      {byZone.map((zone) => (
        <section key={zone.zone} className="zone-block">
          <h3>
            Zone {zone.zone}: {zone.title}
            {zone.front_door ? (
              <span className="muted"> (front door {zone.front_door})</span>
            ) : null}
          </h3>
          {zone.nodes.length === 0 ? (
            <p className="muted">No nodes in this zone.</p>
          ) : (
            zone.nodes.map((node) => (
              <article key={node.id} className="node-item">
                <p>
                  <span className="tag">{node.tag}</span>
                  <Link href={conceptHref(node.id)}>
                    <strong>{node.title}</strong>
                  </Link>
                </p>
                <p className="meta">
                  {node.local_id ?? node.id} · {node.id}
                  {node.global_id ? ` · home of ${node.global_id}` : null}
                </p>
                <p>{node.quick_definition}</p>
              </article>
            ))
          )}
        </section>
      ))}
    </>
  );
}
