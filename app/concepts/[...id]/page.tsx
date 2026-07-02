import Link from "next/link";
import { notFound } from "next/navigation";

import {
  conceptHref,
  getAllConceptIds,
  getConceptOrNode,
  getDisplayTitle,
  getHomeNodeForGlobal,
  getInboundReferences,
  getOutboundReferences,
  moduleHref,
} from "@/lib/graph";
import { ReferenceList } from "@/lib/graph/RefLink";
import { isGlobalConcept, isModuleNode } from "@/lib/graph/types";

export function generateStaticParams() {
  return getAllConceptIds().map((id) => ({
    id: [id],
  }));
}

export default async function ConceptPage({
  params,
}: {
  params: Promise<{ id: string[] }>;
}) {
  const { id: segments } = await params;
  const id = segments.join("/");
  const item = getConceptOrNode(id);

  if (!item) {
    notFound();
  }

  const inbound = getInboundReferences(id);
  const outbound = getOutboundReferences(id);
  const title = getDisplayTitle(item);

  return (
    <>
      <p className="meta">
        <Link href="/">Home</Link>
        {isModuleNode(item) ? (
          <>
            {" "}
            / <Link href={moduleHref(item.module)}>{item.module}</Link>
          </>
        ) : isGlobalConcept(item) ? (
          <>
            {" "}
            / <Link href={moduleHref(item.home_module)}>{item.home_module}</Link>
          </>
        ) : null}
      </p>

      <h1>{title}</h1>
      <p className="meta">
        <span className="badge">{id}</span>
        <span className="badge">
          {isGlobalConcept(item) ? "Global concept" : "Module node"}
        </span>
      </p>

      {isModuleNode(item) ? (
        <p className="meta">
          Module: <Link href={moduleHref(item.module)}>{item.module}</Link> · Zone{" "}
          {item.zone}
          {item.local_id ? ` · ${item.local_id}` : null}
          {item.global_id ? ` · hosts ${item.global_id}` : null}
        </p>
      ) : null}

      {isGlobalConcept(item) ? (
        <>
          <p className="meta">
            Home module:{" "}
            <Link href={moduleHref(item.home_module)}>{item.home_module}</Link>
            {item.home_zone ? ` · ${item.home_zone}` : null}
          </p>
          <p className="meta">
            Category: {item.category} · Contributed by {item.contributed_by}
          </p>
          {(() => {
            const homeNode = getHomeNodeForGlobal(item.id);
            return homeNode ? (
              <p className="meta">
                Deep explainer node:{" "}
                <Link href={conceptHref(homeNode.id)}>{homeNode.title}</Link>
              </p>
            ) : (
              <p className="muted">No hosting zone node mapped for this global.</p>
            );
          })()}
          {item.disambiguate_with && item.disambiguate_with.length > 0 ? (
            <p className="meta">
              Disambiguate with:{" "}
              {item.disambiguate_with.map((g, i) => (
                <span key={g}>
                  {i > 0 ? ", " : null}
                  <Link href={conceptHref(g)}>{g}</Link>
                </span>
              ))}
            </p>
          ) : null}
        </>
      ) : null}

      <section className="section">
        <h2>Quick definition</h2>
        <p>{item.quick_definition}</p>
      </section>

      {"explainer_covers" in item && item.explainer_covers?.length ? (
        <section className="section">
          <h2>Explainer covers</h2>
          <ul className="bullets">
            {item.explainer_covers.map((bullet, i) => (
              <li key={i}>{bullet}</li>
            ))}
          </ul>
        </section>
      ) : null}

      <ReferenceList title="Inbound references" refs={inbound} direction="inbound" />
      <ReferenceList title="Outbound references" refs={outbound} direction="outbound" />
    </>
  );
}
