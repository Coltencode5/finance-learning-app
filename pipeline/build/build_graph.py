#!/usr/bin/env python3
"""Regenerate graph/graph.json from canonical node connects_to and global homes."""
import json
import sys
from pathlib import Path


def load_nodes(root: Path) -> list[dict]:
    nodes = []
    for mdir in sorted((root / "content/modules").iterdir()):
        if not mdir.is_dir():
            continue
        for zfile in sorted((mdir / "zones").glob("z*.json")):
            nodes.extend(json.loads(zfile.read_text(encoding="utf-8")))
    return nodes


def build_edges(nodes: list[dict]) -> list[dict]:
    edges: list[dict] = []
    seen: set[tuple] = set()

    def add(from_id: str, to_id: str, kind: str, note=None):
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

    edges.sort(key=lambda e: (e["from"], e["kind"], e["to"]))
    return edges


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    nodes = load_nodes(root)
    edges = build_edges(nodes)
    out = {
        "generated_by": "pipeline/build/build_graph.py",
        "edge_count": len(edges),
        "edges": edges,
    }
    path = root / "graph/graph.json"
    path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {path}: {len(edges)} edges from {len(nodes)} nodes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
