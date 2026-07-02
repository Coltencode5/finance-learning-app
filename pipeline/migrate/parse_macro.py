#!/usr/bin/env python3
"""
parse_macro.py — one-off migration of Macro_Economics_Module_Node_Map.md into canonical JSON.

Reads:  legacy/markdown/Macro_Economics_Module_Node_Map.md
Writes: content/modules/macro-economics/  (populates scaffold)
        appends G236–G263 to content/glossary/globals.json

Imports node/global parsing from parse_markdown.py (ADR-001 frozen regression
fixtures). Handles Macro-specific deltas: Part 2 glossary, ZONE N · titles,
kind core-concept.

Usage:
  python pipeline/scaffold/scaffold_module.py --slug macro-economics \\
      --title "Macro & Economics" --kind core-concept --build-order 10
  python pipeline/migrate/parse_macro.py [--repo-root PATH]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from migrate.parse_markdown import (  # noqa: E402
    GLOSSARY_ROW,
    NODE_HEADER,
    extract_refs,
    parse_nodes,
    strip_md,
)

SLUG = "macro-economics"
TITLE = "Macro & Economics"
BUILD_ORDER = 10
MACRO_FILE = "Macro_Economics_Module_Node_Map.md"
EXPECTED_NODES = 51
EXPECTED_GLOBALS = 28
EXPECTED_GLOBAL_RANGE = (236, 263)
EXPECTED_ZONE_COUNTS = {1: 12, 2: 12, 3: 8, 4: 10, 5: 9}

MACRO_ZONE_TITLE = re.compile(
    r"^#\s+ZONE\s+(?P<z>[1-5])\s*·\s*(?P<t>.+?)\s*$", re.M
)


def parse_macro_glossary(text: str, slug: str) -> list[dict]:
    """Parse Part 2 glossary table (G236–G263)."""
    part2_start = text.find("# PART 2")
    if part2_start < 0:
        return []
    part2_end = min(
        x for x in (text.find("# ZONE 1", part2_start), text.find("# PART 3", part2_start), len(text))
        if x > part2_start
    )
    section = text[part2_start:part2_end]

    globals_out = []
    for line in section.splitlines():
        mrow = GLOSSARY_ROW.match(line)
        if not mrow:
            continue
        gnum = int(mrow.group("gnum"))
        if gnum < EXPECTED_GLOBAL_RANGE[0]:
            continue
        cells = [c.strip() for c in mrow.group("rest").split("|")]
        if len(cells) < 2:
            continue
        term = strip_md(cells[0])
        qdef = strip_md(cells[1]) if len(cells) > 1 else ""
        appears = strip_md(cells[2]) if len(cells) > 2 else ""

        home_zone = None
        hz = re.search(r"\(Z([1-5](?:\.\d+)?)\)", term)
        if hz:
            home_zone = f"Z{hz.group(1)}"

        aliases = []
        par = re.search(r"\((.+?)\)", term)
        if par and not par.group(1).startswith("Z"):
            aliases.append(par.group(1).strip())

        globals_out.append({
            "id": f"G{gnum}",
            "term": term,
            "aliases": aliases,
            "quick_definition": qdef,
            "home_module": slug,
            "home_zone": home_zone,
            "contributed_by": slug,
            "category": "Core Concepts — Macro & Economics",
            "appears_in": [a.strip() for a in appears.split(",") if a.strip()] if appears else [],
            "disambiguate_with": [],
            "status": "mapped",
        })
    return globals_out


def parse_macro_zone_titles(text: str) -> dict[int, str]:
    titles: dict[int, str] = {}
    for m in MACRO_ZONE_TITLE.finditer(text):
        titles.setdefault(int(m.group("z")), strip_md(m.group("t")))
    return titles


def verify_migration(
    nodes: list[dict],
    new_globals: list[dict],
    zone_titles: dict[int, str],
    report: dict,
) -> list[str]:
    """Return hard-stop discrepancies (empty list = pass)."""
    issues: list[str] = []

    if len(nodes) != EXPECTED_NODES:
        issues.append(f"node count {len(nodes)} != expected {EXPECTED_NODES}")

    for z, expected in EXPECTED_ZONE_COUNTS.items():
        actual = len([n for n in nodes if n["zone"] == z])
        if actual != expected:
            issues.append(f"zone {z} node count {actual} != expected {expected}")

    if len(new_globals) != EXPECTED_GLOBALS:
        issues.append(f"global count {len(new_globals)} != expected {EXPECTED_GLOBALS}")

    gnums = sorted(int(g["id"][1:]) for g in new_globals)
    lo, hi = EXPECTED_GLOBAL_RANGE
    if gnums != list(range(lo, hi + 1)):
        issues.append(f"global IDs not contiguous G{lo}–G{hi}: got {[f'G{n}' for n in gnums]}")

    if len(zone_titles) != 5:
        issues.append(f"zone title count {len(zone_titles)} != 5")

    report["verification"] = {
        "nodes": len(nodes),
        "globals": len(new_globals),
        "global_range": f"G{gnums[0]}–G{gnums[-1]}" if gnums else None,
        "zone_counts": {z: len([n for n in nodes if n["zone"] == z]) for z in range(1, 6)},
        "zone_titles": zone_titles,
        "issues": issues,
    }
    return issues


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=str(Path(__file__).resolve().parents[2]))
    ap.add_argument(
        "--force",
        action="store_true",
        help="overwrite existing macro-economics content (re-run migration)",
    )
    args = ap.parse_args()
    root = Path(args.repo_root)
    legacy_path = root / "legacy" / "markdown" / MACRO_FILE
    mod_dir = root / "content" / "modules" / SLUG

    if not legacy_path.exists():
        print(f"error: missing required source file: {legacy_path}", file=sys.stderr)
        return 1
    if not mod_dir.is_dir():
        print(
            f"error: module scaffold missing at {mod_dir}\n"
            f"  run: python pipeline/scaffold/scaffold_module.py "
            f"--slug {SLUG} --title \"{TITLE}\" --kind core-concept --build-order {BUILD_ORDER}",
            file=sys.stderr,
        )
        return 1

    text = legacy_path.read_text(encoding="utf-8")
    new_globals = parse_macro_glossary(text, SLUG)
    nodes = parse_nodes(text, SLUG)
    zone_titles = parse_macro_zone_titles(text)

    report: dict = {"warnings": []}
    issues = verify_migration(nodes, new_globals, zone_titles, report)
    if issues:
        print("VERIFICATION FAILED:", file=sys.stderr)
        for issue in issues:
            print(f"  - {issue}", file=sys.stderr)
        print(json.dumps(report, indent=2))
        return 1

    globals_path = root / "content" / "glossary" / "globals.json"
    existing_globals = json.loads(globals_path.read_text(encoding="utf-8"))
    existing_ids = {g["id"] for g in existing_globals}
    overlap = existing_ids & {g["id"] for g in new_globals}
    if overlap and not args.force:
        print(f"error: globals already present: {sorted(overlap)}", file=sys.stderr)
        print("  use --force to replace macro-economics globals and zone nodes", file=sys.stderr)
        return 1

    if args.force:
        existing_globals = [g for g in existing_globals if g.get("contributed_by") != SLUG]

    all_globals = existing_globals + new_globals
    all_globals.sort(key=lambda g: int(g["id"][1:]))
    globals_path.write_text(
        json.dumps(all_globals, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    (mod_dir / "zones").mkdir(parents=True, exist_ok=True)
    for z in range(1, 6):
        znodes = sorted([n for n in nodes if n["zone"] == z], key=lambda n: n["ordinal"])
        (mod_dir / "zones" / f"z{z}.json").write_text(
            json.dumps(znodes, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )

    gnums = sorted(int(g["id"][1:]) for g in new_globals)
    reused = sorted(
        {r["ref"] for n in nodes for r in n["connects_to"]
         if r["ref"].startswith("G") and r["ref"] not in {g["id"] for g in new_globals}},
        key=lambda x: int(x[1:]),
    )

    module_meta = {
        "slug": SLUG,
        "title": TITLE,
        "kind": "core-concept",
        "build_order": BUILD_ORDER,
        "visibility": "draft",
        "status": "in-progress",
        "zones": [
            {"zone": z, "title": zone_titles.get(z, f"Zone {z}"), "front_door": f"Z{z}.1"}
            for z in range(1, 6)
        ],
        "sources": [],
        "derived": {
            "globals_contributed": len(gnums),
            "global_range": f"G{gnums[0]}–G{gnums[-1]}" if gnums else None,
            "zone_node_count": len(nodes),
            "globals_reused": reused,
            "gap_count": sum(len(n["gaps"]) for n in nodes),
        },
    }
    (mod_dir / "module.json").write_text(
        json.dumps(module_meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    report["module"] = {
        "slug": SLUG,
        "globals": len(gnums),
        "nodes": len(nodes),
        "reused_globals": len(reused),
        "gaps": module_meta["derived"]["gap_count"],
        "visibility": "draft",
    }
    print(json.dumps(report, indent=2))
    print(
        f"\nMacro migration complete ({len(nodes)} nodes, {len(gnums)} globals). "
        "Module remains draft — promote to active after strict validation passes."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
