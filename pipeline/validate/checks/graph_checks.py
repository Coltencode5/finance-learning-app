"""Graph integrity checks over generated graph/graph.json."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


def check_graph(root: Path, nodes: list[dict], globals_: list[dict], warnings: list[str]) -> None:
    graph_path = root / "graph/graph.json"
    if not graph_path.exists():
        warnings.append("[graph] graph/graph.json missing — run build_graph.py")
        return

    graph = json.loads(graph_path.read_text(encoding="utf-8"))
    edges = graph.get("edges", [])
    node_ids = {n["id"] for n in nodes}
    global_ids = {g["id"] for g in globals_}

    for e in edges:
        if e["from"] == e["to"]:
            warnings.append(f"[graph] self-edge: {e['from']} ({e['kind']})")

    inbound: Counter = Counter()
    outbound: Counter = Counter()
    global_refs: Counter = Counter()

    for e in edges:
        outbound[e["from"]] += 1
        inbound[e["to"]] += 1
        if e["kind"] in ("references", "home_of") and e["to"].startswith("G"):
            global_refs[e["to"]] += 1

    for nid in sorted(node_ids):
        if inbound[nid] == 0 and outbound[nid] == 0:
            warnings.append(f"[graph] orphan node (zero inbound and outbound): {nid}")

    for g in globals_:
        gid = g["id"]
        if global_refs[gid] < 2:
            warnings.append(
                f"[graph] global {gid} '{g['term']}' referenced fewer than 2 times "
                f"({global_refs[gid]} refs — candidate demotion review)"
            )
