#!/usr/bin/env python3
"""Experimental prerequisite suggestions from zone order and connects_to hints."""
from __future__ import annotations

import json
from pathlib import Path

from _load import base_order_key, load_nodes


def derive_prerequisites(root: Path, nodes: list[dict], edges: list[dict]) -> None:
    by_module: dict[str, list[dict]] = {}
    for n in nodes:
        by_module.setdefault(n["module"], []).append(n)

    order_index: dict[str, int] = {}
    module_sequences: dict[str, list[str]] = {}

    for mod, mod_nodes in sorted(by_module.items()):
        ordered = sorted(mod_nodes, key=base_order_key)
        module_sequences[mod] = [n["id"] for n in ordered]
        for i, n in enumerate(ordered):
            order_index[n["id"]] = i

    connects_to_map: dict[str, set[str]] = {}
    for n in nodes:
        refs = {
            c["ref"]
            for c in n.get("connects_to", [])
            if not c["ref"].startswith("G") and c["ref"].split(".", 1)[0] == n["module"]
        }
        connects_to_map[n["id"]] = refs

    suggestions: dict[str, list[dict]] = {}
    for mod, sequence in module_sequences.items():
        mod_suggestions: list[dict] = []
        for i, nid in enumerate(sequence):
            candidates: list[dict] = []
            if i > 0:
                prev = sequence[i - 1]
                candidates.append(
                    {
                        "prerequisite": prev,
                        "reason": "zone_order",
                        "confidence": "base_sequence",
                    }
                )
            for ref in sorted(connects_to_map.get(nid, [])):
                if ref in order_index and order_index[ref] < order_index[nid]:
                    candidates.append(
                        {
                            "prerequisite": ref,
                            "reason": "connects_to_hint",
                            "confidence": "experimental",
                        }
                    )
            if candidates:
                seen = set()
                deduped = []
                for c in candidates:
                    if c["prerequisite"] not in seen:
                        seen.add(c["prerequisite"])
                        deduped.append(c)
                mod_suggestions.append({"node": nid, "suggested_prerequisites": deduped})
        suggestions[mod] = mod_suggestions

    out = {
        "status": "experimental",
        "generated_by": "pipeline/build/derive_prerequisites.py",
        "warning": (
            "NOT canonical. Suggestions only — for future learning-path design. "
            "Do not enforce as course order or write back to content/."
        ),
        "method": (
            "Per module: (1) immediate predecessor in zone+ordinal order; "
            "(2) same-module connects_to targets that appear earlier in that order."
        ),
        "modules": suggestions,
    }
    path = root / "graph/prerequisites.json"
    path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {path} (experimental)")
