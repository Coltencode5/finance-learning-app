#!/usr/bin/env python3
"""Scaffold a new module from templates/module/."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lib.module_utils import next_build_order, validate_slug

ROOT = Path(__file__).resolve().parents[2]
TEMPLATES = ROOT / "templates/module"

DEFAULT_ZONE_TITLES = {
    1: "PLACEHOLDER — Ecosystem",
    2: "PLACEHOLDER — Types",
    3: "PLACEHOLDER — Process",
    4: "PLACEHOLDER — Managing",
    5: "PLACEHOLDER — Meta",
}


def _substitute(text: str, mapping: dict[str, str]) -> str:
    for key, value in mapping.items():
        text = text.replace(f"{{{{{key}}}}}", value)
    return text


def _zone_node_title(zone_num: int) -> str:
    return f"PLACEHOLDER — Zone {zone_num} front door"


def plan_scaffold(slug: str, title: str, root: Path = ROOT) -> dict:
    err = validate_slug(slug)
    if err:
        raise ValueError(err)
    target = root / "content/modules" / slug
    if target.exists():
        raise ValueError(f"module already exists: {slug}")

    build_order = str(next_build_order(root))
    zone_titles = {f"ZONE_{n}_TITLE": DEFAULT_ZONE_TITLES[n] for n in range(1, 6)}
    base = {
        "MODULE_SLUG": slug,
        "MODULE_TITLE": title,
        "BUILD_ORDER": build_order,
        **zone_titles,
    }

    files: list[dict] = []
    module_path = target / "module.json"
    module_body = _substitute(
        (TEMPLATES / "module.template.json").read_text(encoding="utf-8"), base
    )
    files.append({"path": module_path, "content": module_body})

    zone_tpl = (TEMPLATES / "zone.template.json").read_text(encoding="utf-8")
    for zone_num in range(1, 6):
        mapping = {
            **base,
            "ZONE_NUM": str(zone_num),
            "NODE_TITLE": _zone_node_title(zone_num),
        }
        zone_path = target / "zones" / f"z{zone_num}.json"
        files.append(
            {
                "path": zone_path,
                "content": _substitute(zone_tpl, mapping),
            }
        )

    return {
        "slug": slug,
        "title": title,
        "build_order": int(build_order),
        "visibility": "draft",
        "files": files,
    }


def write_scaffold(plan: dict) -> None:
    for entry in plan["files"]:
        path: Path = entry["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(entry["content"], encoding="utf-8")
        json.loads(entry["content"])  # validate JSON


def print_plan(plan: dict, dry_run: bool) -> None:
    mode = "DRY RUN" if dry_run else "SCAFFOLD"
    print(f"{mode}: module '{plan['slug']}' — {plan['title']}")
    print(f"  build_order: {plan['build_order']}")
    print(f"  visibility:  {plan['visibility']} (excluded from validation/graph/app)")
    print("  zones:")
    for n in range(1, 6):
        print(f"    Z{n}: {DEFAULT_ZONE_TITLES[n]} → front door Z{n}.1")
    print("  files:")
    for entry in plan["files"]:
        rel = entry["path"].relative_to(ROOT)
        print(f"    {rel}")
    print()
    print("  warnings:")
    print("    - All content is PLACEHOLDER — replace before setting visibility: active")
    print("    - New globals must start at G236 and be contiguous")
    print("    - Run: python pipeline/validate/validate.py --strict")
    print("    - Run: python pipeline/build/build_graph.py")
    if not dry_run:
        print()
        print("  next steps:")
        print(f"    1. Edit content/modules/{plan['slug']}/")
        print("    2. Add real zone titles, nodes, and connects_to")
        print("    3. Promote: set visibility to active in module.json when ready")


def main() -> int:
    ap = argparse.ArgumentParser(description="Scaffold a new draft module")
    ap.add_argument("--slug", required=True, help="Module slug, e.g. corporate-finance")
    ap.add_argument("--title", required=True, help='Module title, e.g. "Corporate Finance"')
    ap.add_argument("--dry-run", action="store_true", help="Show plan without writing files")
    ap.add_argument("--repo-root", default=str(ROOT))
    args = ap.parse_args()
    root = Path(args.repo_root)

    try:
        plan = plan_scaffold(args.slug, args.title, root)
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

    print_plan(plan, args.dry_run)
    if not args.dry_run:
        write_scaffold(plan)
        print(f"created content/modules/{args.slug}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
