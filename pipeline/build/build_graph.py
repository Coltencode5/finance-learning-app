#!/usr/bin/env python3
"""Regenerate graph/graph.json and derived index artifacts from canonical content."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _load import load_globals, load_nodes, repo_root


def build_edges(nodes: list[dict], globals_: list[dict]) -> list[dict]:
    edges: list[dict] = []
    seen: set[tuple] = set()

    def add(from_id: str, to_id: str, kind: str, note: str | None = None) -> None:
        key = (from_id, to_id, kind)
        if key in seen:
            return
        seen.add(key)
        edges.append({"from": from_id, "to": to_id, "kind": kind, "note": note})

    for n in nodes:
        nid = n["id"]
        for c in n.get("connects_to", []):
            add(nid, c["ref"], "references", c.get("note"))
        if n.get("global_id"):
            add(nid, n["global_id"], "home_of", None)
        for gid in n.get("hosts_globals", []):
            add(nid, gid, "home_of", None)

    for g in globals_:
        for other in g.get("disambiguate_with", []):
            add(g["id"], other, "disambiguates", None)

    edges.sort(key=lambda e: (e["from"], e["kind"], e["to"]))
    return edges


def main() -> int:
    root = repo_root()
    nodes = load_nodes(root)
    globals_ = load_globals(root)
    edges = build_edges(nodes, globals_)

    graph_path = root / "graph/graph.json"
    graph_path.write_text(
        json.dumps(
            {
                "generated_by": "pipeline/build/build_graph.py",
                "edge_count": len(edges),
                "edges": edges,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"wrote {graph_path}: {len(edges)} edges from {len(nodes)} nodes")

    from build_indexes import build_indexes
    from derive_prerequisites import derive_prerequisites
    from graph_health import write_health_report

    build_indexes(root, edges, nodes, globals_)
    derive_prerequisites(root, nodes, edges)
    write_health_report(root)

    return 0


if __name__ == "__main__":
    sys.exit(main())
