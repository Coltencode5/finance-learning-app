#!/usr/bin/env python3
"""Generate graph/graph_health_report.md from build artifacts."""
from __future__ import annotations

import json
from collections import Counter
from datetime import date
from pathlib import Path

from _load import load_globals, load_nodes, repo_root


def write_health_report(root: Path | None = None) -> None:
    root = root or repo_root()
    graph = json.loads((root / "graph/graph.json").read_text(encoding="utf-8"))
    inbound = json.loads((root / "graph/inbound.json").read_text(encoding="utf-8"))
    orphan_data = json.loads((root / "graph/orphan_low_reference.json").read_text(encoding="utf-8"))
    top_globals = json.loads((root / "graph/most_referenced_globals.json").read_text(encoding="utf-8"))
    cross_mod = json.loads((root / "graph/cross_module_edges.json").read_text(encoding="utf-8"))
    mod_deps = json.loads((root / "graph/module_dependencies.json").read_text(encoding="utf-8"))

    nodes = load_nodes(root)
    globals_ = load_globals(root)
    edges = graph["edges"]

    inbound_counts = [len(v) for v in inbound["index"].values()]
    outbound_path = root / "graph/outbound.json"
    outbound = json.loads(outbound_path.read_text(encoding="utf-8"))
    outbound_counts = [len(v) for v in outbound["index"].values()]

    kind_counts = Counter(e["kind"] for e in edges)
    disambiguation_edges = [e for e in edges if e["kind"] == "disambiguates"]

    lines = [
        "# Graph Health Report",
        "",
        f"Generated: {date.today().isoformat()} by `pipeline/build/graph_health.py`",
        "",
        "## Summary",
        "",
        f"| Metric | Value |",
        f"|---|---|",
        f"| Globals | {len(globals_)} |",
        f"| Module zone nodes | {len(nodes)} |",
        f"| Total edges | {len(edges)} |",
        f"| Cross-module reference edges | {cross_mod['edge_count']} |",
        "",
        "### Edge kinds",
        "",
    ]
    for kind, count in sorted(kind_counts.items()):
        lines.append(f"- **{kind}**: {count}")

    lines.extend(
        [
            "",
            "### Inbound degree distribution (all indexed ids)",
            "",
            f"- min: {min(inbound_counts)}",
            f"- max: {max(inbound_counts)}",
            f"- mean: {sum(inbound_counts) / len(inbound_counts):.1f}",
            "",
            "### Outbound degree distribution",
            "",
            f"- min: {min(outbound_counts)}",
            f"- max: {max(outbound_counts)}",
            f"- mean: {sum(outbound_counts) / len(outbound_counts):.1f}",
            "",
            "## Top 10 most-referenced globals",
            "",
            "| Rank | ID | Term | Inbound refs |",
            "|---|---|---|---|",
        ]
    )
    for i, g in enumerate(top_globals["top_10"], 1):
        lines.append(f"| {i} | {g['id']} | {g['term']} | {g['inbound_references']} |")

    lines.extend(["", "## Disambiguation edges (canonical metadata only)", ""])
    if disambiguation_edges:
        for e in disambiguation_edges:
            lines.append(f"- `{e['from']}` → `{e['to']}`")
    else:
        lines.append("_None._")

    lines.extend(
        [
            "",
            "## Orphan nodes (zero inbound and zero outbound)",
            "",
        ]
    )
    orphans = orphan_data["orphan_nodes"]
    if orphans:
        for o in orphans:
            lines.append(f"- `{o['id']}` — {o['title']} ({o['module']})")
    else:
        lines.append("_None._")

    lines.extend(["", "## Low-reference nodes (≤2 total edges)", ""])
    low_nodes = orphan_data["low_reference_nodes"]
    lines.append(f"Count: {len(low_nodes)} (see `graph/orphan_low_reference.json` for full list)")

    lines.extend(["", "## Low-reference globals (<2 inbound references)", ""])
    low_globals = orphan_data["low_reference_globals"]
    lines.append(f"Count: {len(low_globals)}")
    for g in low_globals[:15]:
        lines.append(f"- `{g['id']}` {g['term']} ({g['inbound_references']} refs)")
    if len(low_globals) > 15:
        lines.append(f"- … and {len(low_globals) - 15} more")

    lines.extend(["", "## Cross-module dependencies (reference counts)", ""])
    for src, targets in mod_deps["dependencies"].items():
        top = ", ".join(f"{t} ({c})" for t, c in list(targets.items())[:5])
        lines.append(f"- **{src}** → {top}")

    lines.extend(
        [
            "",
            "## Human review queue",
            "",
            "These items are warnings, not validation errors:",
            "",
            f"- **Orphan nodes**: {len(orphans)} — may be front-door nodes or missing connects_to",
            f"- **Low-reference globals**: {len(low_globals)} — candidate demotions or missing cross-links",
            "- **Disambiguation pairs**: only globals with `disambiguate_with` in `globals.json` "
            "produce edges; other legacy \"this vs. that\" pairs remain prose-only until metadata is added",
            "- **Prerequisites**: `graph/prerequisites.json` is experimental — do not treat as canonical",
            "",
            "## Regeneration",
            "",
            "```bash",
            "python pipeline/build/build_graph.py",
            "python pipeline/validate/validate.py",
            "python pipeline/validate/validate.py --strict",
            "```",
            "",
        ]
    )

    path = root / "graph/graph_health_report.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {path}")
