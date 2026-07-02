"""Shared helpers for module visibility and slug validation."""
from __future__ import annotations

import json
import re
from pathlib import Path

SLUG_PATTERN = re.compile(r"^[a-z][a-z0-9-]*$")


def module_visibility(module: dict) -> str:
    return module.get("visibility", "active")


def is_draft(module: dict) -> bool:
    return module_visibility(module) == "draft"


def is_active(module: dict) -> bool:
    return module_visibility(module) == "active"


def validate_slug(slug: str) -> str | None:
    if not SLUG_PATTERN.match(slug):
        return "slug must match ^[a-z][a-z0-9-]*$ (lowercase, hyphens)"
    return None


def load_module_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def iter_module_dirs(root: Path):
    modules_dir = root / "content/modules"
    if not modules_dir.exists():
        return
    for mdir in sorted(modules_dir.iterdir()):
        if mdir.is_dir():
            yield mdir


def load_all_modules(root: Path) -> dict[str, dict]:
    modules: dict[str, dict] = {}
    for mdir in iter_module_dirs(root):
        modules[mdir.name] = load_module_json(mdir / "module.json")
    return modules


def load_active_modules(root: Path) -> dict[str, dict]:
    return {slug: m for slug, m in load_all_modules(root).items() if is_active(m)}


def load_nodes_for_modules(root: Path, module_slugs: set[str] | None = None) -> list[dict]:
    nodes: list[dict] = []
    for mdir in iter_module_dirs(root):
        if module_slugs is not None and mdir.name not in module_slugs:
            continue
        for zfile in sorted((mdir / "zones").glob("z*.json")):
            nodes.extend(json.loads(zfile.read_text(encoding="utf-8")))
    return nodes


def load_active_nodes(root: Path) -> list[dict]:
    active = set(load_active_modules(root))
    return load_nodes_for_modules(root, active)


def next_build_order(root: Path) -> int:
    """Next sequential build_order, excluding draft sentinel band (>= 900)."""
    orders = [
        m.get("build_order", 0)
        for m in load_all_modules(root).values()
        if m.get("build_order", 0) < 900
    ]
    return max(orders, default=0) + 1


def corpus_max_g(globals_: list[dict]) -> int:
    if not globals_:
        return 0
    return max(int(g["id"][1:]) for g in globals_)


def next_global_id(globals_: list[dict]) -> str:
    return f"G{corpus_max_g(globals_) + 1}"
