#!/usr/bin/env python3
"""Generate graph index and analysis artifacts from edges."""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

from _load import module_of


def _write(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {path}")


def build_indexes(
    root: Path,
    edges: list[dict],
    nodes: list[dict],
    globals_: list[dict],
) -> None:
    inbound: dict[str, list[dict]] = defaultdict(list)
    outbound: dict[str, list[dict]] = defaultdict(list)
    by_module: dict[str, list[dict]] = defaultdict(list)

    node_ids = {n["id"] for n in nodes}
    global_ids = {g["id"] for g in globals_}
    all_ids = node_ids | global_ids

    for e in edges:
        entry = {"from": e["from"], "to": e["to"], "kind": e["kind"], "note": e.get("note")}
        inbound[e["to"]].append({"from": e["from"], "kind": e["kind"], "note": e.get("note")})
        outbound[e["from"]].append({"to": e["to"], "kind": e["kind"], "note": e.get("note")})

        for endpoint in (e["from"], e["to"]):
            mod = module_of(endpoint)
            if mod:
                by_module[mod].append(entry)

    for ref_id in sorted(all_ids):
        inbound.setdefault(ref_id, [])
        outbound.setdefault(ref_id, [])

    for ref_id in inbound:
        inbound[ref_id].sort(key=lambda x: (x["from"], x["kind"]))
    for ref_id in outbound:
        outbound[ref_id].sort(key=lambda x: (x["to"], x["kind"]))

    _write(
        root / "graph/inbound.json",
        {
            "generated_by": "pipeline/build/build_indexes.py",
            "description": "Reverse lookup: target id → sources that point to it.",
            "index": dict(sorted(inbound.items())),
        },
    )
    _write(
        root / "graph/outbound.json",
        {
            "generated_by": "pipeline/build/build_indexes.py",
            "description": "Forward lookup: source id → targets it points to.",
            "index": dict(sorted(outbound.items())),
        },
    )
    _write(
        root / "graph/by_module.json",
        {
            "generated_by": "pipeline/build/build_indexes.py",
            "description": "Edge subset where at least one endpoint is a node in the module.",
            "modules": {k: v for k, v in sorted(by_module.items())},
        },
    )

    ref_inbound = Counter()
    for e in edges:
        if e["kind"] in ("references", "home_of"):
            ref_inbound[e["to"]] += 1

    global_ref_counts = [
        {
            "id": g["id"],
            "term": g["term"],
            "inbound_references": ref_inbound.get(g["id"], 0),
            "home_of_edges": sum(1 for x in edges if x["to"] == g["id"] and x["kind"] == "home_of"),
            "total_inbound": len(inbound.get(g["id"], [])),
        }
        for g in globals_
    ]
    global_ref_counts.sort(key=lambda x: (-x["inbound_references"], x["id"]))

    _write(
        root / "graph/most_referenced_globals.json",
        {
            "generated_by": "pipeline/build/build_indexes.py",
            "description": "Globals ranked by inbound reference count (references + home_of).",
            "globals": global_ref_counts,
            "top_10": global_ref_counts[:10],
        },
    )

    orphan_nodes = []
    low_reference_nodes = []
    for n in nodes:
        nid = n["id"]
        inc = len(inbound.get(nid, []))
        out = len(outbound.get(nid, []))
        total = inc + out
        row = {
            "id": nid,
            "title": n["title"],
            "module": n["module"],
            "zone": n["zone"],
            "inbound": inc,
            "outbound": out,
        }
        if inc == 0 and out == 0:
            orphan_nodes.append(row)
        elif total <= 2:
            low_reference_nodes.append({**row, "total_edges": total})

    low_reference_globals = [
        {
            "id": g["id"],
            "term": g["term"],
            "inbound_references": ref_inbound.get(g["id"], 0),
        }
        for g in globals_
        if ref_inbound.get(g["id"], 0) < 2
    ]

    _write(
        root / "graph/orphan_low_reference.json",
        {
            "generated_by": "pipeline/build/build_indexes.py",
            "description": "Nodes with zero graph edges, low-edge nodes, and globals referenced fewer than twice.",
            "orphan_nodes": orphan_nodes,
            "low_reference_nodes": sorted(low_reference_nodes, key=lambda x: x["total_edges"]),
            "low_reference_globals": sorted(
                low_reference_globals, key=lambda x: x["inbound_references"]
            ),
        },
    )

    cross_module_edges = []
    for e in edges:
        if e["kind"] != "references":
            continue
        from_mod = module_of(e["from"])
        to_mod = module_of(e["to"])
        if from_mod and to_mod and from_mod != to_mod:
            cross_module_edges.append(e)
        elif from_mod and e["to"].startswith("G"):
            cross_module_edges.append({**e, "to_module": "global"})
        elif e["from"].startswith("G") and to_mod:
            cross_module_edges.append({**e, "from_module": "global"})

    module_deps: dict[str, Counter] = defaultdict(Counter)
    for e in cross_module_edges:
        from_mod = module_of(e["from"]) or "global"
        to_mod = module_of(e["to"]) if not e["to"].startswith("G") else "global"
        if from_mod != to_mod:
            module_deps[from_mod][to_mod] += 1

    dep_matrix = {
        src: dict(sorted(targets.items(), key=lambda kv: (-kv[1], kv[0])))
        for src, targets in sorted(module_deps.items())
    }

    _write(
        root / "graph/cross_module_edges.json",
        {
            "generated_by": "pipeline/build/build_indexes.py",
            "description": "Reference edges whose endpoints span modules (or module ↔ global).",
            "edge_count": len(cross_module_edges),
            "edges": cross_module_edges,
        },
    )
    _write(
        root / "graph/module_dependencies.json",
        {
            "generated_by": "pipeline/build/build_indexes.py",
            "description": "Cross-module reference counts: source module → target module.",
            "dependencies": dep_matrix,
        },
    )
