#!/usr/bin/env python3
"""Write 04_INHERITANCE_LEDGER.md from _inheritance_raw.json."""
from __future__ import annotations

import json
from pathlib import Path

DOSSIER = Path(__file__).resolve().parents[1]
raw = json.loads((DOSSIER / "raw_extractions" / "_inheritance_raw.json").read_text(encoding="utf-8"))

homed = [r for r in raw if r["verdict"].startswith("Already")]
unhomed = [r for r in raw if r["verdict"].startswith("Mentioned but")]
absent = [r for r in raw if r["verdict"].startswith("Absent")]
verify = [r for r in raw if r not in homed + unhomed + absent]

lines = [
    "# 04 — Inheritance Ledger (PART 0 mechanical pass)",
    "",
    "Corpus searched live: **313 globals** + **615 zone nodes**. "
    "Script: `_scripts/corpus_search.py` (aliases + inflections via regex patterns). "
    "Raw JSON: `raw_extractions/_inheritance_raw.json`.",
    "",
    "## Headline counts (script heuristics — architect verifies meaning)",
    "",
    f"- Already-homed string hits (heuristic; often collisions): **{len(homed)}**",
    f"- Mentioned but unhomed: **{len(unhomed)}**",
    f"- Needs verify (glossary string-hit ± node mentions): **{len(verify)}**",
    f"- Absent / genuine mint candidates: **{len(absent)}**",
    f"- Total candidates searched: **{len(raw)}**",
    "",
    "Note: \"Already homed\" here means a glossary *string* match on the search pattern — "
    "not a confirmed same-meaning home. Cross-check `05_COLLISION_MAP.md` before back-linking.",
    "",
    "## Full table",
    "",
    "| Candidate concept | Already homed? | Where (G-number + home) | Mentioned but unhomed? | Where (every matching node) | Verdict for the architect |",
    "|---|---|---|---|---|---|",
]

for r in raw:
    gbits = []
    for g in r["globals"]:
        gbits.append(f"{g['id']} «{g['term']}» @ {g['home']}")
    nodes = ", ".join(f"`{n}`" for n in r["nodes"])
    already = "yes — verify meaning" if r["globals"] else "no"
    mentioned = "yes" if r["nodes"] else "no"
    lines.append(
        "| {concept} | {already} | {g} | {mentioned} | {nodes} | {verdict} |".format(
            concept=r["concept"].replace("|", "/"),
            already=already,
            g="; ".join(gbits) if gbits else "—",
            mentioned=mentioned,
            nodes=nodes if nodes else "—",
            verdict=r["verdict"].replace("|", "/"),
        )
    )

lines += [
    "",
    "## Script shown",
    "",
    "See `_scripts/corpus_search.py` — loads `content/glossary/globals.json` (term, aliases, quick_definition) "
    "and all module zone `nodes[]` (title, quick_definition, explainer_covers, connects_to notes, connects_to_raw).",
    "",
]

out = DOSSIER / "04_INHERITANCE_LEDGER.md"
out.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("wrote", out, "bytes", out.stat().st_size)
print(
    "counts",
    {
        "homed": len(homed),
        "unhomed": len(unhomed),
        "verify": len(verify),
        "absent": len(absent),
    },
)
