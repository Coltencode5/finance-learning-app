"""Shared loaders for graph build pipeline."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lib.module_utils import is_draft


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_globals(root: Path) -> list[dict]:
    return json.loads((root / "content/glossary/globals.json").read_text(encoding="utf-8"))


def load_nodes(root: Path) -> list[dict]:
    nodes: list[dict] = []
    for mdir in sorted((root / "content/modules").iterdir()):
        if not mdir.is_dir():
            continue
        mod = json.loads((mdir / "module.json").read_text(encoding="utf-8"))
        if is_draft(mod):
            continue
        for zfile in sorted((mdir / "zones").glob("z*.json")):
            nodes.extend(json.loads(zfile.read_text(encoding="utf-8")))
    return nodes


def load_modules(root: Path) -> dict[str, dict]:
    modules: dict[str, dict] = {}
    for mdir in sorted((root / "content/modules").iterdir()):
        if not mdir.is_dir():
            continue
        mod = json.loads((mdir / "module.json").read_text(encoding="utf-8"))
        if is_draft(mod):
            continue
        modules[mdir.name] = mod
    return modules


def module_of(ref: str) -> str | None:
    if ref.startswith("G"):
        return None
    if "." in ref:
        return ref.split(".", 1)[0]
    return None


def zone_num(node: dict) -> int:
    z = node["zone"]
    if isinstance(z, int):
        return z
    return int(re.sub(r"\D", "", str(z)) or "0")


def base_order_key(node: dict) -> tuple:
    return (node["module"], zone_num(node), node["ordinal"])
