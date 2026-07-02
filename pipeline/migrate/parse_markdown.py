#!/usr/bin/env python3
"""
parse_markdown.py — one-time migration of legacy markdown node maps into canonical JSON.

Reads:  legacy/markdown/*_Node_Map.md
Writes: content/glossary/globals.json
        content/modules/{slug}/module.json
        content/modules/{slug}/zones/z{1..5}.json

Design notes:
- LENIENT reader, STRICT writer. The nine legacy files have known drift
  (Real Estate uses '# ZONE 1 —' headers; ER/VC/RE use consolidated gap
  sections instead of inline GAP: tags; HF has one non-standard tag).
  The parser tolerates all of it; the emitted JSON conforms to /schemas.
- Lossless where judgment is needed: the raw 'Connects to.' line is kept in
  connects_to_raw so nothing is destroyed if reference extraction is imperfect.
- After this migration is signed off (Milestone 2), JSON is the single source
  of truth and legacy/markdown/ becomes a frozen reference.

Usage: python pipeline/migrate/parse_markdown.py [--repo-root PATH]
"""
import argparse
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------- constants

MODULE_FILES = {
    "PE_Module_Node_Map.md":                 ("private-equity",      "Private Equity",      1),
    "Private_Credit_Module_Node_Map.md":     ("private-credit",      "Private Credit",      2),
    "Investment_Banking_Module_Node_Map.md": ("investment-banking",  "Investment Banking",  3),
    "Hedge_Fund_Module_Node_Map.md":         ("hedge-funds",         "Hedge Funds",         4),
    "Asset_Management_Module_Node_Map.md":   ("asset-management",    "Asset Management",    5),
    "Wealth_Management_Module_Node_Map.md":  ("wealth-management",   "Wealth Management",   6),
    "Equity_Research_Module_Node_Map.md":    ("equity-research",     "Equity Research",     7),
    "Venture_Capital_Module_Node_Map.md":    ("venture-capital",     "Venture Capital",     8),
    "Real_Estate_Module_Node_Map.md":        ("real-estate",         "Real Estate",         9),
}

# Cross-module abbreviations used inside 'Connects to.' lines (e.g. "PE Z1.1")
MODULE_ABBREVS = {
    "PE": "private-equity", "PC": "private-credit", "IB": "investment-banking",
    "HF": "hedge-funds", "AM": "asset-management", "WM": "wealth-management",
    "ER": "equity-research", "VC": "venture-capital", "RE": "real-estate",
    # long-form prefixes found in the legacy corpus
    "Credit": "private-credit", "Asset Management": "asset-management",
}

NODE_HEADER = re.compile(
    r"^###\s+Z(?P<zone>[1-5])\.(?P<ord>\d+)\s*[·:]\s*(?P<title>.+?)\s*$", re.M)
TAG_RE = re.compile(r"`\[(core|process|branch)\]`")
GLOBAL_TAG_RE = re.compile(r"`?★\s*GLOBAL\s*\(G(\d+)[^)]*\)`?")
GLOSSARY_ROW = re.compile(
    r"^\|\s*\*{0,2}G(?P<gnum>\d+)\*{0,2}\s*\|(?P<rest>.*)\|\s*$", re.M)
CATEGORY_HEADER = re.compile(r"^###\s+(?:[A-Z]\.\s+)?(?P<cat>[^\n#].*?)\s*$", re.M)
ZONE_TITLE_PATTERNS = [
    re.compile(r"^#\s+PART\s+\d+\s*[·:]\s*Zone\s+(?P<z>[1-5])\s*[—–-]\s*(?P<t>.+?)\s*$", re.M),
    re.compile(r"^#\s+ZONE\s+(?P<z>[1-5])\s*[—–-]\s*(?P<t>.+?)\s*$", re.M),  # Real Estate drift
]

def strip_md(s: str) -> str:
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"\*(.+?)\*", r"\1", s)
    s = re.sub(r"`(.+?)`", r"\1", s)
    return s.strip()

# ---------------------------------------------------------------- glossary

def parse_glossary(text: str, slug: str) -> list[dict]:
    """Parse the Part 1 glossary tables of one module into GlobalConcept dicts."""
    part1_start = text.find("# PART 1")
    part1_end = min(x for x in [
        text.find("# PART 2"), text.find("# ZONE 1"), len(text)
    ] if x > 0)
    section = text[part1_start:part1_end] if part1_start >= 0 else ""

    # track the most recent '### <category>' header above each table row
    globals_out = []
    current_cat = "Uncategorized"
    for line in section.splitlines():
        mcat = re.match(r"^###\s+(?:[A-Z]\.\s+)?(.+)$", line)
        if mcat:
            current_cat = strip_md(mcat.group(1))
            continue
        mrow = GLOSSARY_ROW.match(line)
        if not mrow:
            continue
        cells = [c.strip() for c in mrow.group("rest").split("|")]
        # expected: term | quick_definition | home | appears_in  (some modules vary)
        if len(cells) < 2:
            continue
        term = strip_md(cells[0])
        qdef = strip_md(cells[1]) if len(cells) > 1 else ""
        home = strip_md(cells[2]) if len(cells) > 2 else ""
        appears = strip_md(cells[3]) if len(cells) > 3 else ""
        # normalize home zone: accept 'Z5', 'Z1.5', 'RE Z4.2', 'all zones'
        home_zone = None
        hz = re.search(r"Z([1-5](?:\.\d+)?)", home)
        if hz:
            home_zone = f"Z{hz.group(1)}"
        # aliases: parenthetical expansions in the term
        aliases = []
        par = re.search(r"\((.+?)\)", term)
        if par:
            aliases.append(par.group(1).strip())
        globals_out.append({
            "id": f"G{mrow.group('gnum')}",
            "term": term,
            "aliases": aliases,
            "quick_definition": qdef,
            "home_module": slug,
            "home_zone": home_zone,
            "contributed_by": slug,
            "category": current_cat,
            "appears_in": [a.strip() for a in appears.split(",") if a.strip()] if appears else [],
            "disambiguate_with": [],
            "status": "mapped",
        })
    return globals_out

# ---------------------------------------------------------------- zone nodes

def expand_ranges(raw: str) -> str:
    """Expand 'Z1.10–Z1.17' / 'Z2.4–2.7' range notation into explicit comma lists,
    propagating any module prefix ('PE Z1.10–Z1.17' → 'PE Z1.10, PE Z1.11, …')."""
    abbrev_alt = "|".join(sorted((re.escape(k) for k in MODULE_ABBREVS), key=len, reverse=True))
    pat = re.compile(
        r"(?:\b(" + abbrev_alt + r")\s+)?Z([1-5])\.(\d+)\s*[–—-]\s*(?:Z([1-5])\.)?(\d+)")
    def _expand(m):
        prefix = (m.group(1) + " ") if m.group(1) else ""
        z1, a = int(m.group(2)), int(m.group(3))
        z2 = int(m.group(4)) if m.group(4) else z1
        b = int(m.group(5))
        if z1 != z2 or b < a or b - a > 40:
            return m.group(0)  # malformed/cross-zone range: leave as-is
        return ", ".join(f"{prefix}Z{z1}.{i}" for i in range(a, b + 1))
    return pat.sub(_expand, raw)


def propagate_abbrev_prefix(raw: str) -> str:
    """Expand slash-chained refs: 'PE Z2.21 / Z3.12' → 'PE Z2.21, PE Z3.12'."""
    abbrev_alt = "|".join(sorted((re.escape(k) for k in MODULE_ABBREVS), key=len, reverse=True))
    pat = re.compile(
        r"\b(" + abbrev_alt + r")\s+(Z[1-5]\.\d+)((?:\s*/\s*Z[1-5]\.\d+)+)"
    )

    def _expand(m: re.Match) -> str:
        prefix = m.group(1)
        first = m.group(2)
        rest = re.findall(r"Z([1-5]\.\d+)", m.group(3))
        all_z = [first] + [f"Z{z}" for z in rest]
        return ", ".join(f"{prefix} {z}" for z in all_z)

    return pat.sub(_expand, raw)


def extract_refs(raw: str, slug: str) -> list[dict]:
    """Extract structured refs from a free-text 'Connects to.' line."""
    raw = propagate_abbrev_prefix(expand_ranges(raw))
    refs, seen = [], set()
    # cross-module refs first: 'PE Z1.1', 'PC Z1.1', etc.
    abbrev_alt = "|".join(sorted((re.escape(k) for k in MODULE_ABBREVS), key=len, reverse=True))
    for m in re.finditer(r"\b(" + abbrev_alt + r")\s+Z([1-5])\.(\d+)", raw):
        target = f"{MODULE_ABBREVS[m.group(1)]}.z{m.group(2)}.{m.group(3)}"
        if target not in seen:
            seen.add(target)
            refs.append({"ref": target, "note": None})
    # blank out cross-module spans so local matcher doesn't re-capture them
    blanked = re.sub(r"\b(" + abbrev_alt + r")\s+Z[1-5]\.\d+", " ", raw)
    for m in re.finditer(r"\bZ([1-5])\.(\d+)", blanked):
        target = f"{slug}.z{m.group(1)}.{m.group(2)}"
        if target not in seen:
            seen.add(target)
            refs.append({"ref": target, "note": None})
    for m in re.finditer(r"\bG(\d+)\b", raw):
        target = f"G{m.group(1)}"
        if target not in seen:
            seen.add(target)
            refs.append({"ref": target, "note": None})
    return refs

def parse_nodes(text: str, slug: str) -> list[dict]:
    nodes = []
    headers = list(NODE_HEADER.finditer(text))
    for i, h in enumerate(headers):
        start = h.end()
        end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
        # stop a node's body at the next '# PART'/'# ZONE' heading if one intervenes
        nxt = re.search(r"^#\s+(PART|ZONE)\b", text[start:end], re.M)
        if nxt:
            end = start + nxt.start()
        body = text[start:end]

        raw_title = h.group("title")
        zone, ordinal = int(h.group("zone")), int(h.group("ord"))

        gmatch = GLOBAL_TAG_RE.search(raw_title) or GLOBAL_TAG_RE.search(body[:200])
        tmatch = TAG_RE.search(raw_title)
        tag = "global" if gmatch else (tmatch.group(1) if tmatch else "core")
        global_id = f"G{gmatch.group(1)}" if gmatch else None

        title = strip_md(GLOBAL_TAG_RE.sub("", TAG_RE.sub("", raw_title)))

        qm = re.search(r"\*\*Quick definition[^*]*\*\*\s*(.+?)(?=\n\*\*|\n###|\Z)", body, re.S)
        quick_def = strip_md(re.sub(r"\s+", " ", qm.group(1))) if qm else ""

        em = re.search(r"\*\*Explainer covers[^*]*\*\*\s*(.*?)(?=\n\*\*Connects to|\Z)", body, re.S)
        bullets = []
        if em:
            for line in em.group(1).splitlines():
                line = line.strip()
                if line.startswith("- "):
                    bullets.append(strip_md(line[2:]))

        cm = re.search(r"\*\*Connects to\.?\*\*\s*(.+?)(?=\n###|\n#\s|\n\*Real-world|\Z)", body, re.S)
        connects_raw = re.sub(r"\s+", " ", cm.group(1)).strip() if cm else ""

        rw = re.search(r"\*Real-world layer:\s*(.+?)\*", body)

        # gaps: inline 'GAP:' tags anywhere in the node body
        gaps = []
        for gm in re.finditer(r"GAP\s*/?\s*(recency)?[:\s]\s*([^*\n]+)", body):
            kind = "recency" if (gm.group(1) or "recency" in gm.group(2).lower()) else "source"
            gaps.append({"kind": kind, "note": strip_md(gm.group(2)).rstrip("*. )"), "needed_source": None})

        nodes.append({
            "id": f"{slug}.z{zone}.{ordinal}",
            "local_id": f"Z{zone}.{ordinal}",
            "module": slug,
            "zone": zone,
            "ordinal": ordinal,
            "title": title,
            "tag": tag,
            "global_id": global_id,
            "quick_definition": quick_def,
            "explainer_covers": bullets if bullets else ([quick_def] if quick_def else ["(missing)"]),
            "connects_to": extract_refs(connects_raw, slug),
            "connects_to_raw": connects_raw or None,
            "gaps": gaps,
            "real_world_layer": strip_md(rw.group(1)) if rw else None,
            "source_refs": [],
            "status": "mapped",
        })
    return nodes

def parse_zone_titles(text: str) -> dict[int, str]:
    titles = {}
    for pat in ZONE_TITLE_PATTERNS:
        for m in pat.finditer(text):
            titles.setdefault(int(m.group("z")), strip_md(m.group("t")))
    return titles

# ---------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=str(Path(__file__).resolve().parents[2]))
    args = ap.parse_args()
    root = Path(args.repo_root)
    legacy = root / "legacy" / "markdown"

    all_globals: list[dict] = []
    report = {"modules": {}, "warnings": []}

    for fname, (slug, title, order) in MODULE_FILES.items():
        path = legacy / fname
        if not path.exists():
            report["warnings"].append(f"missing legacy file: {fname}")
            continue
        text = path.read_text(encoding="utf-8")

        globals_ = parse_glossary(text, slug)
        nodes = parse_nodes(text, slug)
        zone_titles = parse_zone_titles(text)
        all_globals.extend(globals_)

        mdir = root / "content" / "modules" / slug
        (mdir / "zones").mkdir(parents=True, exist_ok=True)
        for z in range(1, 6):
            znodes = sorted([n for n in nodes if n["zone"] == z], key=lambda n: n["ordinal"])
            (mdir / "zones" / f"z{z}.json").write_text(
                json.dumps(znodes, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

        gnums = sorted(int(g["id"][1:]) for g in globals_)
        reused = sorted({r["ref"] for n in nodes for r in n["connects_to"]
                         if r["ref"].startswith("G") and int(r["ref"][1:]) not in gnums},
                        key=lambda x: int(x[1:]))
        module_meta = {
            "slug": slug, "title": title, "kind": "role", "build_order": order,
            "zones": [{"zone": z, "title": zone_titles.get(z, f"Zone {z}"),
                       "front_door": f"Z{z}.1"} for z in range(1, 6)],
            "sources": [],
            "derived": {
                "globals_contributed": len(gnums),
                "global_range": f"G{gnums[0]}–G{gnums[-1]}" if gnums else None,
                "zone_node_count": len(nodes),
                "globals_reused": reused,
                "gap_count": sum(len(n["gaps"]) for n in nodes),
            },
            "status": "mapped",
        }
        (mdir / "module.json").write_text(
            json.dumps(module_meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

        report["modules"][slug] = {
            "globals": len(gnums),
            "global_range": module_meta["derived"]["global_range"],
            "zone_nodes": len(nodes),
            "reused_globals": len(reused),
            "gaps": module_meta["derived"]["gap_count"],
        }

    all_globals.sort(key=lambda g: int(g["id"][1:]))
    (root / "content" / "glossary" / "globals.json").write_text(
        json.dumps(all_globals, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(json.dumps(report, indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
