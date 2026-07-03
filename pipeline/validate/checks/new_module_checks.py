"""Validation gates for module structure and new-module global rules."""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

from lib.module_utils import is_draft

NODE_ID_PATTERN = re.compile(r"^[a-z0-9-]+\.z[1-5]\.\d+$")
GLOBAL_ID_PATTERN = re.compile(r"^G[1-9][0-9]*$")
REQUIRED_ZONE_FILES = [f"z{n}.json" for n in range(1, 6)]

ROLE_SPINE_PLACEHOLDERS = {
    "PLACEHOLDER — Ecosystem",
    "PLACEHOLDER — Types",
    "PLACEHOLDER — Process",
    "PLACEHOLDER — Managing",
    "PLACEHOLDER — Meta",
}

CORE_CONCEPT_SPINE_PLACEHOLDERS = {
    "PLACEHOLDER — Concept zone 1",
    "PLACEHOLDER — Concept zone 2",
    "PLACEHOLDER — Concept zone 3",
    "PLACEHOLDER — Concept zone 4",
    "PLACEHOLDER — Concept zone 5",
}

SECTOR_SPINE_PLACEHOLDERS = {
    "PLACEHOLDER — Sector economics",
    "PLACEHOLDER — Segments",
    "PLACEHOLDER — Drivers & KPIs",
    "PLACEHOLDER — Valuation treatment",
    "PLACEHOLDER — Regulation & cycle",
}

SECTOR_KINDS = frozenset({"sector-layer1", "sector-layer2"})


def _norm_term(t: str) -> str:
    t = unicodedata.normalize("NFKD", t.lower())
    t = re.sub(r"\(.*?\)", " ", t)
    t = re.sub(r"[^a-z0-9 ]", " ", t)
    t = re.sub(r"\b(the|a|an|of|and)\b", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def check_zone_titles_by_kind(
    modules: dict,
    errors: list[str],
    warnings: list[str],
) -> None:
    """Active modules must use zone title placeholders appropriate to their kind."""
    for slug, mod in sorted(modules.items()):
        if is_draft(mod):
            continue
        kind = mod.get("kind", "role")
        titles = {z["zone"]: z["title"] for z in mod.get("zones", [])}
        for zone_num, title in titles.items():
            if kind == "core-concept" and title in ROLE_SPINE_PLACEHOLDERS:
                errors.append(
                    f"[module] {slug} zone {zone_num} uses role spine placeholder "
                    f"'{title}' but kind is core-concept (ADR-002)"
                )
            elif kind == "role" and title in CORE_CONCEPT_SPINE_PLACEHOLDERS:
                errors.append(
                    f"[module] {slug} zone {zone_num} uses core-concept placeholder "
                    f"'{title}' but kind is role (ADR-002)"
                )
            elif kind in SECTOR_KINDS and title in ROLE_SPINE_PLACEHOLDERS:
                errors.append(
                    f"[module] {slug} zone {zone_num} uses role spine placeholder "
                    f"'{title}' but kind is {kind} (ADR-003)"
                )
            elif kind in SECTOR_KINDS and title in CORE_CONCEPT_SPINE_PLACEHOLDERS:
                errors.append(
                    f"[module] {slug} zone {zone_num} uses core-concept placeholder "
                    f"'{title}' but kind is {kind} (ADR-003)"
                )
            elif kind not in SECTOR_KINDS and title in SECTOR_SPINE_PLACEHOLDERS:
                errors.append(
                    f"[module] {slug} zone {zone_num} uses sector spine placeholder "
                    f"'{title}' but kind is {kind} (ADR-003)"
                )


def check_sector_compactness(
    modules: dict,
    nodes: list[dict],
    errors: list[str],
    warnings: list[str],
) -> None:
    """Warn when active sector modules fall outside ADR-003 compactness bounds."""
    nodes_by_module: dict[str, list] = {}
    for n in nodes:
        nodes_by_module.setdefault(n["module"], []).append(n)

    for slug, mod in sorted(modules.items()):
        if is_draft(mod):
            continue
        kind = mod.get("kind", "role")
        if kind not in SECTOR_KINDS:
            continue

        module_nodes = nodes_by_module.get(slug, [])
        total = len(module_nodes)
        if total < 8 or total > 14:
            warnings.append(
                f"[module] {slug} has {total} nodes — sector modules should have "
                f"8–14 nodes (ADR-003 rule 6)"
            )

        by_zone: dict[int, int] = {}
        for n in module_nodes:
            by_zone[n["zone"]] = by_zone.get(n["zone"], 0) + 1
        for zone_num, count in sorted(by_zone.items()):
            if count > 4:
                warnings.append(
                    f"[module] {slug} zone {zone_num} has {count} nodes — "
                    f"soft cap is 4 per zone (ADR-003 rule 6)"
                )


def check_module_structure(modules: dict, nodes: list[dict], errors: list[str], warnings: list[str]) -> None:
    """Active modules must have complete five-zone structure."""
    nodes_by_module: dict[str, list] = {}
    for n in nodes:
        nodes_by_module.setdefault(n["module"], []).append(n)

    for slug, mod in sorted(modules.items()):
        if is_draft(mod):
            warnings.append(f"[module] {slug} is draft — excluded from canonical validation")
            continue

        mod_dir = Path("content/modules") / slug
        zones_dir = mod_dir / "zones"
        if not zones_dir.is_dir():
            errors.append(f"[module] {slug} missing zones/ directory")
            continue

        present = sorted(p.name for p in zones_dir.glob("z*.json"))
        for required in REQUIRED_ZONE_FILES:
            if required not in present:
                errors.append(f"[module] {slug} missing required zone file zones/{required}")

        if len(mod.get("zones", [])) != 5:
            errors.append(f"[module] {slug} must define exactly 5 zones in module.json")

        for n in nodes_by_module.get(slug, []):
            if not NODE_ID_PATTERN.match(n["id"]):
                errors.append(f"[module] {n['id']} malformed node ID")
            if n["id"].split(".", 1)[0] != slug:
                errors.append(f"[module] {n['id']} module field does not match slug {slug}")
            if n.get("global_id") and not GLOBAL_ID_PATTERN.match(n["global_id"]):
                errors.append(f"[module] {n['id']} malformed global_id {n.get('global_id')}")

        zone_defs = {z["zone"] for z in mod.get("zones", [])}
        node_zones = {n["zone"] for n in nodes_by_module.get(slug, [])}
        for z in zone_defs - node_zones:
            warnings.append(f"[module] {slug} zone {z} defined in module.json but has no nodes")


def check_new_module_globals(
    globals_: list[dict],
    modules: dict,
    errors: list[str],
    warnings: list[str],
) -> None:
    """New globals from active modules must start at corpus_max+1 and not collide."""
    existing_norm: dict[str, str] = {}
    for g in globals_:
        existing_norm[_norm_term(g["term"])] = g["id"]
        for a in g.get("aliases", []):
            key = _norm_term(a)
            if key:
                existing_norm[key] = g["id"]

    for slug, mod in modules.items():
        if is_draft(mod):
            continue

        module_globals = sorted(
            (g for g in globals_ if g.get("contributed_by") == slug),
            key=lambda g: int(g["id"][1:]),
        )
        if not module_globals:
            continue

        other_max = max(
            (int(g["id"][1:]) for g in globals_ if g.get("contributed_by") != slug),
            default=0,
        )
        new_globals = [g for g in module_globals if int(g["id"][1:]) > other_max]
        if not new_globals:
            continue

        nums = sorted(int(g["id"][1:]) for g in new_globals)
        next_expected = other_max + 1
        expected = list(range(next_expected, next_expected + len(new_globals)))
        if nums != expected:
            errors.append(
                f"[module] {slug} new globals must be contiguous from G{next_expected}: "
                f"got {[f'G{n}' for n in nums]}"
            )
        for g in new_globals:
            keys = [_norm_term(g["term"])] + [_norm_term(a) for a in g.get("aliases", [])]
            for key in keys:
                if not key:
                    continue
                prior = existing_norm.get(key)
                if prior and prior != g["id"]:
                    errors.append(
                        f"[module] {slug} global {g['id']} redefines existing term "
                        f"(collision with {prior}, normalized '{key}')"
                    )


def check_module_graph_presence(
    root: Path,
    modules: dict,
    errors: list[str],
    warnings: list[str],
) -> None:
    """Active modules should appear in by_module.json after graph build."""
    by_mod_path = root / "graph/by_module.json"
    if not by_mod_path.exists():
        warnings.append("[module] graph/by_module.json missing — run build_graph.py")
        return

    by_mod = json.loads(by_mod_path.read_text(encoding="utf-8")).get("modules", {})
    for slug, mod in modules.items():
        if is_draft(mod):
            continue
        if slug not in by_mod:
            errors.append(f"[module] {slug} missing from graph/by_module.json")


def check_new_modules(
    root: Path,
    globals_: list[dict],
    modules: dict,
    nodes: list[dict],
    errors: list[str],
    warnings: list[str],
) -> None:
    check_module_structure(modules, nodes, errors, warnings)
    check_zone_titles_by_kind(modules, errors, warnings)
    check_sector_compactness(modules, nodes, errors, warnings)
    check_new_module_globals(globals_, modules, errors, warnings)
    check_module_graph_presence(root, modules, errors, warnings)
