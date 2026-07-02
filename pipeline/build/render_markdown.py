#!/usr/bin/env python3
"""Render canonical module JSON back to markdown in build/ for human review."""
import json
import sys
from pathlib import Path

TAG_LABELS = {
    "core": "core",
    "process": "process",
    "branch": "branch",
    "global": "global",
}


def zone_heading(module: dict, zone_num: int) -> str:
    zones = module.get("zones", [])
    title = zones[zone_num - 1]["title"] if zone_num <= len(zones) else f"Zone {zone_num}"
    return f"# PART {zone_num} · Zone {zone_num} — {title}"


def render_node(n: dict) -> str:
    tag = n.get("tag", "core")
    gid = n.get("global_id")
    tag_suffix = ""
    if tag == "global" and gid:
        tag_suffix = f" ★ GLOBAL ({gid} — home)"
    elif gid:
        tag_suffix = f" ★ GLOBAL — deep home of {gid}"
    hosts = n.get("hosts_globals") or []
    if hosts and not gid:
        tag_suffix += f" *(hosts {', '.join(hosts)})*"

    lines = [
        f"### {n['local_id']} · {n['title']} `[{TAG_LABELS.get(tag, tag)}]`{tag_suffix}",
        f"**Quick definition.** {n['quick_definition']}",
        "**Explainer covers.**",
    ]
    for bullet in n.get("explainer_covers", []):
        lines.append(f"- {bullet}")

    refs = []
    for c in n.get("connects_to", []):
        ref = c["ref"]
        if c.get("note"):
            refs.append(f"`{ref}` ({c['note']})")
        else:
            refs.append(f"`{ref}`")
    if refs:
        lines.append(f"**Connects to.** {', '.join(refs)}.")

    if n.get("real_world_layer"):
        lines.append(f"*Real-world layer: {n['real_world_layer']}*")

    for gap in n.get("gaps", []):
        kind = gap.get("kind", "source")
        note = gap.get("note", "")
        src = gap.get("needed_source")
        suffix = f" — needed: {src}" if src else ""
        lines.append(f"**GAP / {kind} flag.** {note}{suffix}")

    lines.append("")
    return "\n".join(lines)


def render_module(root: Path, slug: str) -> str:
    mdir = root / "content/modules" / slug
    module = json.loads((mdir / "module.json").read_text(encoding="utf-8"))
    parts = [
        f"# {module.get('title', slug)}",
        "",
        f"*Module slug: `{slug}` · {module.get('kind', '')} · build order {module.get('build_order', '?')}*",
        "",
    ]
    for z in range(1, 6):
        zfile = mdir / "zones" / f"z{z}.json"
        if not zfile.exists():
            continue
        nodes = json.loads(zfile.read_text(encoding="utf-8"))
        parts.append(zone_heading(module, z))
        parts.append("")
        for n in sorted(nodes, key=lambda x: x["ordinal"]):
            parts.append(render_node(n))
    return "\n".join(parts)


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    out_dir = root / "build" / "markdown"
    out_dir.mkdir(parents=True, exist_ok=True)

    for mdir in sorted((root / "content/modules").iterdir()):
        if not mdir.is_dir():
            continue
        slug = mdir.name
        md = render_module(root, slug)
        path = out_dir / f"{slug}.md"
        path.write_text(md, encoding="utf-8")
        print(f"wrote {path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
