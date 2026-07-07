#!/usr/bin/env python3
"""One-off local extractor for sector-information-technology dossier. Not part of pipeline."""
from __future__ import annotations

import csv
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

import fitz  # PyMuPDF

from _dossier_utils import definition_snippets

REPO = Path(__file__).resolve().parents[2]
DOSSIER = Path(__file__).resolve().parent
DOWNLOADS = Path(r"c:\Users\cfroo\Downloads")

SOURCES = [
    {
        "key": "business_of_platforms",
        "path": DOWNLOADS
        / "_OceanofPDF.com_The_Business_of_Platforms_-_Michael_A_Cusumano.pdf",
        "title": "The Business of Platforms",
        "author": "Michael A. Cusumano, Annabelle Gawer, and David B. Yoffie",
        "type": "textbook / practitioner guide",
        "tier": "primary",
    },
    {
        "key": "subscribed",
        "path": DOWNLOADS / "_OceanofPDF.com_Subscribed_-_Tien_Tzuo.pdf",
        "title": "Subscribed",
        "author": "Tien Tzuo and Gabe Weisert",
        "type": "practitioner guide",
        "tier": "primary",
    },
    {
        "key": "chip_war",
        "path": DOWNLOADS / "_OceanofPDF.com_Chip_War_-_Chris_Miller.pdf",
        "title": "Chip War",
        "author": "Chris Miller",
        "type": "narrative / industry history",
        "tier": "primary",
    },
    {
        "key": "investment_valuation",
        "path": DOWNLOADS
        / "_OceanofPDF.com_Investment_Valuation_University_Edition_-_Aswath_Damodaran.pdf",
        "title": "Investment Valuation (University Edition)",
        "author": "Aswath Damodaran",
        "type": "textbook",
        "tier": "primary",
    },
    {
        "key": "platform_revolution",
        "path": DOWNLOADS
        / "_OceanofPDF.com_Platform_Revolution_How_Networked_Markets_Are_Transforming_the_Economy--And_How_to_Make_Them_Work_for_You_-_Sangeet_Paul_Choudary.pdf",
        "title": "Platform Revolution",
        "author": "Geoffrey G. Parker, Marshall W. Van Alstyne, and Sangeet Paul Choudary",
        "type": "textbook / practitioner guide",
        "tier": "secondary",
    },
    {
        "key": "lean_analytics",
        "path": DOWNLOADS
        / "_OceanofPDF.com_Lean_Analytics_-_Alistair_Croll_Benjamin_Yoskovitz.pdf",
        "title": "Lean Analytics",
        "author": "Alistair Croll and Benjamin Yoskovitz",
        "type": "practitioner guide",
        "tier": "secondary",
    },
]

MISSING_SOURCES = [
    {
        "title": "The Software Paradox",
        "author": "Stephen O'Grady",
        "tier": "secondary",
        "status": "not provided",
        "status_reason": "file not in user-supplied folder",
    },
]

HEADING_RE = re.compile(
    r"^(?:chapter|part|section|appendix)\s+[\divxlc\d]+[\.\:\s]",
    re.I,
)
ALLCAPS_LINE = re.compile(r"^[A-Z][A-Z0-9 ,\-–—:&'()/]{8,}$")
NUMBERED_HEAD = re.compile(r"^\d+(\.\d+)*\s+[A-Z]")

IT_TERM_PATTERNS = [
    # Subscription / SaaS economics
    r"software as a service",
    r"\bSaaS\b",
    r"software licensing",
    r"subscription",
    r"\bARR\b",
    r"annual recurring revenue",
    r"recurring revenue",
    r"gross retention",
    r"net revenue retention",
    r"\bNRR\b",
    r"\bchurn\b",
    r"CAC payback",
    r"customer acquisition cost",
    r"\bCAC\b",
    r"sales efficiency",
    r"Rule of 40",
    r"usage-based pricing",
    r"seat-based pricing",
    r"freemium",
    r"product-market fit",
    # Platforms / cloud
    r"platform ecosystem",
    r"platform business",
    r"two-sided market",
    r"network effects?",
    r"cloud infrastructure",
    r"hyperscaler",
    r"infrastructure as a service",
    r"\bIaaS\b",
    r"platform as a service",
    r"\bPaaS\b",
    # Semiconductors
    r"semiconductor",
    r"fabless",
    r"foundry",
    r"semiconductor equipment",
    r"chip design",
    r"fabrication",
    r"\bwafer\b",
    r"\bTSMC\b",
    r"\bEUV\b",
    # Hardware / services / margins
    r"hardware",
    r"IT services",
    r"systems integrat",
    r"outsourcing",
    r"gross margin",
    r"contribution margin",
    r"R&D intensity",
    r"research and development",
    r"capex",
    r"capital expenditure",
    r"operating leverage",
    # AI (source-grounded only via pattern match)
    r"artificial intelligence",
    r"\bAI\b",
    r"data center",
    r"GPU",
    # Valuation / finance overlap
    r"valuation multiple",
    r"price-to-sales",
    r"\bP/S\b",
    r"price-to-earnings",
    r"\bP/E\b",
    r"enterprise value",
    r"free cash flow",
    r"intrinsic value",
    r"relative valuation",
    r"discounted cash flow",
    r"\bDCF\b",
    r"terminal value",
    r"WACC",
    r"beta",
    r"revenue growth",
    r"operating margin",
    r"burn rate",
    r"leverage",
    r"capital structure",
    r"credit spread",
    r"credit rating",
    r"M&A",
    r"mergers and acquisitions",
    r"initial public offering",
    r"\bIPO\b",
    r"venture capital",
    r"private equity",
    r"competitive advantage",
    r"moat",
    r"barriers to entry",
    r"switching costs",
    r"economies of scale",
]

THIN_COVERAGE_TERMS = [
    "IT services",
    "hardware",
    "cybersecurity",
    "enterprise software",
    "systems integrat",
    "outsourcing",
]


def norm_term(t: str) -> str:
    t = unicodedata.normalize("NFKD", t.lower())
    t = re.sub(r"\(.*?\)", " ", t)
    t = re.sub(r"[^a-z0-9 ]", " ", t)
    t = re.sub(r"\b(the|a|an|of|and)\b", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def load_corpus_terms() -> dict[str, list[str]]:
    globals_ = json.loads((REPO / "content/glossary/globals.json").read_text(encoding="utf-8"))
    lookup: dict[str, list[str]] = defaultdict(list)
    for g in globals_:
        keys = {norm_term(g["term"])}
        for a in g.get("aliases", []):
            keys.add(norm_term(a))
        for k in keys:
            if k:
                lookup[k].append(g["id"])
    return lookup


def corpus_match(term: str, lookup: dict[str, list[str]]) -> str:
    nt = norm_term(term)
    if not nt:
        return ""
    hits: set[str] = set()
    if nt in lookup:
        hits.update(lookup[nt])
    for ck, ids in lookup.items():
        if len(nt) >= 4 and (nt in ck or ck in nt):
            hits.update(ids)
    return ";".join(sorted(hits, key=lambda x: int(x[1:])))


def extract_pdf(path: Path) -> dict:
    doc = fitz.open(path)
    meta = doc.metadata or {}
    pages = []
    headings: list[dict] = []
    for i in range(doc.page_count):
        text = doc.load_page(i).get_text("text") or ""
        pages.append(text)
        page_no = i + 1
        for line in text.splitlines():
            s = line.strip()
            if not s or len(s) > 140:
                continue
            if HEADING_RE.match(s) or ALLCAPS_LINE.match(s) or NUMBERED_HEAD.match(s):
                headings.append({"page": page_no, "line": s})
    full = "\n".join(pages)
    doc.close()
    return {
        "page_count": len(pages),
        "metadata": meta,
        "pages": pages,
        "full_text": full,
        "headings": headings,
    }


def detect_toc(pages: list[str], max_pages: int = 25) -> list[str]:
    toc_lines: list[str] = []
    for i in range(min(max_pages, len(pages))):
        for line in pages[i].splitlines():
            s = line.strip()
            if not s:
                continue
            if re.search(r"\.{2,}\s*\d+\s*$", s):
                toc_lines.append(f"p{i+1}: {s}")
            elif re.match(r"^(contents|table of contents)$", s, re.I):
                toc_lines.append(f"p{i+1}: {s}")
    return toc_lines


def chapter_blocks(headings: list[dict]) -> list[dict]:
    chapters = []
    for h in headings:
        line = h["line"]
        if re.search(r"chapter|part|appendix", line, re.I) or (
            ALLCAPS_LINE.match(line) and len(line.split()) <= 12
        ):
            chapters.append(h)
    out = []
    prev = None
    for c in chapters:
        if prev and prev["line"] == c["line"] and abs(prev["page"] - c["page"]) <= 2:
            continue
        out.append(c)
        prev = c
    return out[:200]


def find_term_occurrences(text: str, title: str) -> list[dict]:
    found = []
    for pat in IT_TERM_PATTERNS:
        rx = re.compile(pat, re.I)
        for m in rx.finditer(text):
            term = m.group(0)
            pos = m.start()
            page = text[:pos].count("\f") + 1 if "\f" in text else max(1, pos // 3000 + 1)
            found.append({"term": term, "pattern": pat, "approx_page": page})
    seen = set()
    uniq = []
    for f in found:
        k = norm_term(f["term"])
        if k in seen:
            continue
        seen.add(k)
        uniq.append({**f, "source": title})
    return uniq


def thin_coverage_report(all_text: str) -> list[str]:
    flags = []
    lower = all_text.lower()
    for pat in THIN_COVERAGE_TERMS:
        rx = re.compile(pat, re.I)
        hits = len(rx.findall(lower))
        if hits < 5:
            flags.append(f"{pat}: {hits} occurrences across all readable sources")
    return flags


def repo_facts() -> dict:
    mods = []
    for mdir in sorted((REPO / "content/modules").iterdir()):
        if not mdir.is_dir():
            continue
        mod = json.loads((mdir / "module.json").read_text(encoding="utf-8"))
        mods.append(mod)
    mods.sort(key=lambda m: m.get("build_order", 999))
    globals_ = json.loads((REPO / "content/glossary/globals.json").read_text(encoding="utf-8"))
    return {
        "modules": mods,
        "global_count": len(globals_),
        "global_range": f"{globals_[0]['id']}–{globals_[-1]['id']}",
        "next_global": f"G{int(globals_[-1]['id'][1:]) + 1}",
    }


def main() -> None:
    DOSSIER.mkdir(parents=True, exist_ok=True)
    raw_dir = DOSSIER / "raw_extractions"
    raw_dir.mkdir(exist_ok=True)
    corpus_lookup = load_corpus_terms()
    facts = repo_facts()

    manifest_rows = []
    toc_index_parts = ["# TOC Index — sector-information-technology\n"]
    chapter_parts = ["# Chapter Summaries — sector-information-technology\n"]
    concept_rows: dict[str, dict] = {}
    combined_text = ""

    for src in SOURCES:
        path: Path = src["path"]
        block = {
            "key": src["key"],
            "title": src["title"],
            "author": src["author"],
            "type": src["type"],
            "tier": src["tier"],
            "path": str(path),
            "status": "failed",
            "status_reason": "",
            "page_count": 0,
            "areas": [],
        }
        if not path.exists():
            block["status"] = "failed"
            block["status_reason"] = "file not found at configured path"
            manifest_rows.append(block)
            continue
        try:
            data = extract_pdf(path)
        except Exception as e:
            block["status"] = "failed"
            block["status_reason"] = str(e)
            manifest_rows.append(block)
            continue

        block["page_count"] = data["page_count"]
        (raw_dir / f"{src['key']}.txt").write_text(data["full_text"][:500000], encoding="utf-8")
        combined_text += data["full_text"]
        toc = detect_toc(data["pages"])
        chapters = chapter_blocks(data["headings"])
        text_quality = sum(1 for p in data["pages"][:10] if len(p.strip()) > 80)
        if text_quality < 3:
            block["status"] = "poor"
            block["status_reason"] = "first pages mostly empty — likely image-only or broken OCR layer"
        elif len(data["full_text"].strip()) < 5000:
            block["status"] = "partial"
            block["status_reason"] = "very little extractable text"
        else:
            block["status"] = "clean" if len(toc) >= 5 else "partial"
            if block["status"] == "partial":
                block["status_reason"] = "TOC not cleanly detected; chapter map reconstructed from headings"

        block["areas"] = [c["line"] for c in chapters[:40]]
        manifest_rows.append(block)

        toc_index_parts.append(f"\n## {src['title']} ({src['author']})\n")
        toc_index_parts.append(f"Source tier: **{src['tier']}** | Extraction status: **{block['status']}** — {block['status_reason'] or 'n/a'}\n")
        toc_index_parts.append(f"Page count: {data['page_count']}\n")
        if toc:
            toc_index_parts.append("### Detected TOC lines\n")
            for line in toc[:80]:
                toc_index_parts.append(f"- {line}\n")
        else:
            toc_index_parts.append("### Reconstructed chapter/heading map\n")
            for c in chapters[:60]:
                toc_index_parts.append(f"- p{c['page']}: {c['line']}\n")

        chapter_parts.append(f"\n## {src['title']}\n")
        chapter_parts.append(
            f"Author: {src['author']} | Tier: {src['tier']} | Pages: {data['page_count']} | Status: {block['status']}\n"
        )
        if not chapters:
            chapter_parts.append("_No reliable chapter headings detected — see raw extraction file._\n")
        for c in chapters[:35]:
            title = c["line"]
            page = c["page"]
            snippet_page = data["pages"][page - 1] if page - 1 < len(data["pages"]) else ""
            concepts = []
            for pat in IT_TERM_PATTERNS[:40]:
                m = re.search(pat, snippet_page, re.I)
                if m:
                    concepts.append(m.group(0))
            chapter_parts.append(f"\n### {title} (p.{page})\n")
            chapter_parts.append(f"- Pages: ~{page}+\n")
            if concepts:
                chapter_parts.append(
                    f"- Named concepts/topics in vicinity: {', '.join(sorted(set(concepts))[:12])}\n"
                )
            def_snip = definition_snippets(snippet_page, title.split()[-1] if title.split() else title)
            if def_snip:
                chapter_parts.append(f"- Nearby text (paraphrase source context): {def_snip}\n")

        occurrences = find_term_occurrences(data["full_text"], src["title"])
        for occ in occurrences:
            nt = norm_term(occ["term"])
            if not nt or len(nt) < 3:
                continue
            if nt not in concept_rows:
                concept_rows[nt] = {
                    "term": occ["term"],
                    "normalized_term": nt,
                    "short_definition": definition_snippets(data["full_text"], occ["term"]),
                    "source_titles": set(),
                    "source_locations": [],
                    "extraction_confidence": "medium" if block["status"] == "clean" else "low",
                    "also_appears_as_corpus_term": corpus_match(occ["term"], corpus_lookup),
                    "notes": "",
                }
            concept_rows[nt]["source_titles"].add(src["title"])
            concept_rows[nt]["source_locations"].append(f"{src['title']}:~p{occ['approx_page']}")

    for missing in MISSING_SOURCES:
        manifest_rows.append(
            {
                "key": "missing",
                "title": missing["title"],
                "author": missing["author"],
                "type": "practitioner guide",
                "tier": missing["tier"],
                "path": "n/a",
                "status": missing["status"],
                "status_reason": missing["status_reason"],
                "page_count": 0,
                "areas": [],
            }
        )

    thin_flags = thin_coverage_report(combined_text)

    sm = ["# Source Manifest — sector-information-technology\n"]
    for b in manifest_rows:
        sm.append(f"\n## {b['title']}\n")
        sm.append(f"- **Author/editor:** {b['author']}\n")
        sm.append(f"- **Source type:** {b['type']}\n")
        sm.append(f"- **Source tier (config list):** {b['tier']}\n")
        if b["path"] != "n/a":
            sm.append(f"- **Path:** `{b['path']}`\n")
        sm.append(f"- **Page count:** {b['page_count'] or 'n/a'}\n")
        sm.append(f"- **Extraction status:** {b['status']}\n")
        if b["status_reason"]:
            sm.append(f"- **Status detail:** {b['status_reason']}\n")
        if b["areas"]:
            sm.append("- **Main areas covered (heading-level, factual):**\n")
            for a in b["areas"][:25]:
                sm.append(f"  - {a}\n")
    (DOSSIER / "Source_Manifest.md").write_text("".join(sm), encoding="utf-8")
    (DOSSIER / "TOC_Index.md").write_text("".join(toc_index_parts), encoding="utf-8")
    (DOSSIER / "Chapter_Summaries.md").write_text("".join(chapter_parts), encoding="utf-8")

    with (DOSSIER / "Concept_Inventory.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "term",
                "normalized_term",
                "short_definition",
                "source_titles",
                "source_locations",
                "extraction_confidence",
                "also_appears_as_corpus_term",
                "notes",
            ],
        )
        w.writeheader()
        for row in sorted(concept_rows.values(), key=lambda r: r["normalized_term"]):
            w.writerow(
                {
                    "term": row["term"],
                    "normalized_term": row["normalized_term"],
                    "short_definition": row["short_definition"][:300],
                    "source_titles": " | ".join(sorted(row["source_titles"])),
                    "source_locations": " | ".join(row["source_locations"][:8]),
                    "extraction_confidence": row["extraction_confidence"],
                    "also_appears_as_corpus_term": row["also_appears_as_corpus_term"],
                    "notes": row["notes"],
                }
            )

    active = [m for m in facts["modules"] if m.get("visibility", "active") != "draft"]
    draft = [m for m in facts["modules"] if m.get("visibility", "active") == "draft"]
    kinds = sorted({m.get("kind", "role") for m in facts["modules"]})
    inv_count = len(concept_rows)
    needs_attention = [b for b in manifest_rows if b["status"] in ("failed", "poor", "partial", "not provided")]

    hn = [
        "# Handoff Note — sector-information-technology\n",
        "\n## 1. Module configuration\n",
        "- **Title:** Information Technology (Sector)\n",
        "- **Slug:** sector-information-technology\n",
        "- **Kind:** sector-layer1\n",
        "- **Expected build_order:** 13\n",
        "- **Expected global start:** G293\n",
        "\n## 2. Sources processed\n",
    ]
    for b in manifest_rows:
        hn.append(
            f"- **{b['title']}** ({b['tier']}) — {b['status']}"
            + (f" ({b['status_reason']})" if b["status_reason"] else "")
            + "\n"
        )
    hn.append("\n## 3. Sources needing human attention\n")
    if needs_attention:
        for b in needs_attention:
            hn.append(f"- {b['title']}: {b['status']} — {b['status_reason'] or 'see manifest'}\n")
    else:
        hn.append("- None\n")

    hn.append("\n## 4. Dossier files\n")
    hn.extend(
        [
            "- `Source_Manifest.md` — per-source metadata, extraction status, heading-level coverage\n",
            "- `TOC_Index.md` — detected or reconstructed tables of contents / chapter maps\n",
            "- `Chapter_Summaries.md` — chapter/section entries with named topics and nearby source text\n",
            "- `Concept_Inventory.csv` — mechanical term inventory with corpus string matches only\n",
            "- `Handoff_Note.md` — this file\n",
            "- `raw_extractions/` — plain-text dumps (truncated) for architect reference\n",
            f"\n## 5. Concept inventory row count\n{inv_count}\n",
            "\n## 6. Repo-state facts (read-only inspection)\n",
            f"- Active modules: {len(active)}\n",
            f"- Draft modules: {len(draft)}\n",
            f"- Global count/range: {facts['global_count']} ({facts['global_range']})\n",
            f"- Next available global ID: {facts['next_global']}\n",
            f"- Module kinds in use: {', '.join(kinds)}\n",
            "- Five-zone convention: each module has zones z1–z5 with front-door nodes; node fields include id, title, tag, quick_definition, explainer_covers, connects_to, gaps\n",
            "- ADRs flagged by title only (relevant to sector-layer1): ADR-001-json-canonical.md; ADR-003-sector-topology.md\n",
            "\n### Active module list (slug | kind | build_order)\n",
            "| slug | kind | build_order |\n",
            "|---|---|---|\n",
        ]
    )
    for m in active:
        hn.append(f"| {m['slug']} | {m.get('kind', 'role')} | {m.get('build_order', '')} |\n")

    hn.append("\n## 6b. Configuration notes recorded (factual flags only — not resolved)\n")
    hn.extend(
        [
            "- Tier B / light source-grounding sector per extraction config — dossier supports architecture session, not a comprehensive tech industry textbook.\n",
            "- Compact module target per ADR-003 rule 6: 8–14 nodes (architect session decides final count).\n",
            "- Corpus overlap zones flagged for name-matching in `Concept_Inventory.csv` (no reuse/new-global judgment made): equity-research (sector analysis, valuation, multiples); fixed-income (credit spreads, capital structure); macro-economics (rates, inflation, business cycles, AI capex if source-grounded); venture-capital (burn, PMF, scaling); private-equity (buyouts, recurring revenue, leverage); asset-management (benchmark/exposure lens); investment-banking (M&A, issuance, capital markets).\n",
            "- Known disambiguation/name-match risks flagged in config, not resolved: platform vs SaaS; software vs IT services; software vs semiconductors; semiconductors vs hardware/devices; ARR vs revenue; gross retention vs NRR; churn variants; gross margin vs contribution margin; usage-based vs seat-based pricing; capex-light software vs capex-heavy fabs; valuation multiple vs intrinsic value; AI hype vs durable economics.\n",
            "- **The Software Paradox** (Stephen O'Grady) was in the secondary source list but was **not provided** in the user folder.\n",
        ]
    )
    if thin_flags:
        hn.append("- Thin coverage signals (mechanical occurrence counts across all readable sources):\n")
        for flag in thin_flags:
            hn.append(f"  - {flag}\n")

    hn.append(
        "\n## 7. Architecture deferral\n"
        "**No architecture decisions, zone spines, global-reuse calls, or disambiguation judgments have been made. All of that is deferred to the architecture session.**\n"
    )
    (DOSSIER / "Handoff_Note.md").write_text("".join(hn), encoding="utf-8")

    print(f"manifest_sources={len(manifest_rows)} concepts={inv_count} thin_flags={len(thin_flags)}")


if __name__ == "__main__":
    main()
