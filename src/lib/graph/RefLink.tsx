import Link from "next/link";

import { conceptHref, refExists, resolveRefLabel } from "@/lib/graph";
import type { InboundRef, OutboundRef } from "@/lib/graph/types";

export function RefLink({ id }: { id: string }) {
  const label = resolveRefLabel(id);
  const exists = refExists(id);

  if (!exists) {
    return (
      <span className="missing-ref" title="Reference target not found in content">
        {label} ({id}) — unavailable
      </span>
    );
  }

  return <Link href={conceptHref(id)}>{label}</Link>;
}

export function ReferenceList({
  title,
  refs,
  direction,
}: {
  title: string;
  refs: InboundRef[] | OutboundRef[];
  direction: "inbound" | "outbound";
}) {
  if (refs.length === 0) {
    return (
      <section className="section">
        <h2>{title}</h2>
        <p className="muted">None recorded in the graph index.</p>
      </section>
    );
  }

  return (
    <section className="section">
      <h2>{title}</h2>
      <ul className="ref-list">
        {refs.map((ref, i) => {
          const id = direction === "inbound" ? (ref as InboundRef).from : (ref as OutboundRef).to;
          return (
            <li key={`${id}-${ref.kind}-${i}`}>
              <RefLink id={id} />
              <span className="kind-tag">{ref.kind}</span>
              {ref.note ? <span className="note"> — {ref.note}</span> : null}
            </li>
          );
        })}
      </ul>
    </section>
  );
}
