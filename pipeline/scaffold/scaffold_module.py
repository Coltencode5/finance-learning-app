#!/usr/bin/env python3
"""Scaffold a new module from templates/module/."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lib.module_utils import next_build_order, next_global_id, validate_slug

ROOT = Path(__file__).resolve().parents[2]
TEMPLATES = ROOT / "templates/module"

ROLE_ZONE_TITLES = {
    1: "PLACEHOLDER — Ecosystem",
    2: "PLACEHOLDER — Types",
    3: "PLACEHOLDER — Process",
    4: "PLACEHOLDER — Managing",
    5: "PLACEHOLDER — Meta",
}

CORE_CONCEPT_ZONE_TITLES = {
    1: "PLACEHOLDER — Concept zone 1",
    2: "PLACEHOLDER — Concept zone 2",
    3: "PLACEHOLDER — Concept zone 3",
    4: "PLACEHOLDER — Concept zone 4",
    5: "PLACEHOLDER — Concept zone 5",
}

ZONE_TITLES_BY_KIND = {
    "role": ROLE_ZONE_TITLES,
    "core-concept": CORE_CONCEPT_ZONE_TITLES,
}


def zone_titles_for_kind(kind: str) -> dict[int, str]:
    return ZONE_TITLES_BY_KIND.get(kind, ROLE_ZONE_TITLES)


def _substitute(text: str, mapping: dict[str, str]) -> str:
    for key, value in mapping.items():
        text = text.replace(f"{{{{{key}}}}}", value)
    return text


def _zone_node_title(zone_num: int) -> str:
    return f"PLACEHOLDER — Zone {zone_num} front door"


def plan_scaffold(
    slug: str,
    title: str,
    root: Path = ROOT,
    kind: str = "role",
    build_order: int | None = None,
) -> dict:
    err = validate_slug(slug)
    if err:
        raise ValueError(err)
    target = root / "content/modules" / slug
    if target.exists():
        raise ValueError(f"module already exists: {slug}")

    if kind not in ZONE_TITLES_BY_KIND:
        raise ValueError(f"unsupported kind for scaffold: {kind}")

    zone_titles = zone_titles_for_kind(kind)
    order = build_order if build_order is not None else next_build_order(root)
    build_order_str = str(order)
    zone_title_tokens = {f"ZONE_{n}_TITLE": zone_titles[n] for n in range(1, 6)}
    base = {
        "MODULE_SLUG": slug,
        "MODULE_TITLE": title,
        "MODULE_KIND": kind,
        "BUILD_ORDER": build_order_str,
        **zone_title_tokens,
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

    globals_path = root / "content/glossary/globals.json"
    next_g = "G?"
    if globals_path.exists():
        globals_ = json.loads(globals_path.read_text(encoding="utf-8"))
        next_g = next_global_id(globals_)

    return {
        "slug": slug,
        "title": title,
        "kind": kind,
        "build_order": order,
        "visibility": "draft",
        "next_global_id": next_g,
        "zone_titles": zone_titles,
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
    print(f"  kind:        {plan['kind']}")
    print(f"  build_order: {plan['build_order']}")
    print(f"  visibility:  {plan['visibility']} (excluded from validation/graph/app)")
    print("  zones:")
    for n in range(1, 6):
        print(f"    Z{n}: {plan['zone_titles'][n]} → front door Z{n}.1")
    print("  files:")
    for entry in plan["files"]:
        rel = entry["path"].relative_to(ROOT)
        print(f"    {rel}")
    print()
    print("  warnings:")
    print("    - All content is PLACEHOLDER — replace before setting visibility: active")
    print(f"    - New globals must start at {plan['next_global_id']} and be contiguous")
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
    ap.add_argument(
        "--kind",
        default="role",
        choices=sorted(ZONE_TITLES_BY_KIND),
        help="Module kind (selects zone title placeholders per ADR-002)",
    )
    ap.add_argument(
        "--build-order",
        type=int,
        default=None,
        help="Override build_order (default: next sequential slot, excluding draft band >= 900)",
    )
    ap.add_argument("--dry-run", action="store_true", help="Show plan without writing files")
    ap.add_argument("--repo-root", default=str(ROOT))
    args = ap.parse_args()
    root = Path(args.repo_root)

    try:
        plan = plan_scaffold(
            args.slug, args.title, root, kind=args.kind, build_order=args.build_order
        )
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
