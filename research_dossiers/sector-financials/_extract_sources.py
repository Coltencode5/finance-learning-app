#!/usr/bin/env python3
"""One-off local extractor for sector-financials dossier. Not part of pipeline."""
from __future__ import annotations

import csv
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

import fitz  # PyMuPDF

REPO = Path(__file__).resolve().parents[2]
DOSSIER = Path(__file__).resolve().parent
DOWNLOADS = Path(r"c:\Users\cfroo\Downloads")

SOURCES = [
    {
        "key": "bankers_new_clothes",
        "path": DOWNLOADS / "_OceanofPDF.com_The_bankers_new_clothes_-_Anat_Admat.pdf",
        "title": "The Bankers' New Clothes",
        "author": "Anat Admati and Martin Hellwig",
        "type": "academic / practitioner critique",
    },
    {
        "key": "basel_iii",
        "path": DOWNLOADS / "_OceanofPDF.com_Handbook_of_Basel_III_Capital_-_Juan_Ramirez.pdf",
        "title": "Handbook of Basel III Capital",
        "author": "Juan Ramirez",
        "type": "regulatory handbook",
    },
    {
        "key": "dark_side_valuation",
        "path": DOWNLOADS / "_OceanofPDF.com_The_Dark_Side_of_Valuation_-_Aswath_Damodaran.pdf",
        "title": "The Dark Side of Valuation",
        "author": "Aswath Damodaran",
        "type": "textbook / practitioner guide",
    },
    {
        "key": "competition_demystified",
        "path": DOWNLOADS / "_OceanofPDF.com_Competition_Demystified_-_Bruce_C_Greenwald.pdf",
        "title": "Competition Demystified",
        "author": "Bruce C. Greenwald and Judd Kahn",
        "type": "textbook",
    },
    {
        "key": "expectations_investing",
        "path": DOWNLOADS / "_OceanofPDF.com_Expectations_Investing__Reading_Stock_Pric_-_Alfred_Rappaport (1).pdf",
        "title": "Expectations Investing",
        "author": "Alfred Rappaport and Michael J. Mauboussin",
        "type": "practitioner guide",
    },
    {
        "key": "fisher_csuop",
        "path": DOWNLOADS / "_OceanofPDF.com_Common_Stocks_and_Uncommon_Profits_and_Oth_-_Philip_A_Fisher (1).pdf",
        "title": "Common Stocks and Uncommon Profits and Other Writings",
        "author": "Philip A. Fisher",
        "type": "practitioner guide",
    },
    {
        "key": "fisher_writings",
        "path": DOWNLOADS / "_OceanofPDF.com_Common_Stocks_and_Uncommon_Profits_and_Other_Writings_-_Philip_Arthur_Fisher.pdf",
        "title": "Common Stocks and Uncommon Profits and Other Writings (alt file)",
        "author": "Philip A. Fisher",
        "type": "practitioner guide",
    },
    {
        "key": "fisher_paths",
        "path": DOWNLOADS / "_OceanofPDF.com_Paths_to_Wealth_Through_Common_Stocks_-_Philip_A_Fisher.pdf",
        "title": "Paths to Wealth Through Common Stocks",
        "author": "Philip A. Fisher",
        "type": "practitioner guide",
    },
    {
        "key": "acsm_drm",
        "path": DOWNLOADS / "1157398.acsm",
        "title": "1157398.acsm (Adobe DRM)",
        "author": "unknown — DRM file",
        "type": "encrypted purchase file",
    },
]

HEADING_RE = re.compile(
    r"^(?:chapter|part|section|appendix)\s+[\divxlc\d]+[\.\:\s]",
    re.I,
)
ALLCAPS_LINE = re.compile(r"^[A-Z][A-Z0-9 ,\-–—:&'()/]{8,}$")
NUMBERED_HEAD = re.compile(r"^\d+(\.\d+)*\s+[A-Z]")

FINANCE_TERM_PATTERNS = [
    r"net interest margin",
    r"\bNIM\b",
    r"combined ratio",
    r"loss ratio",
    r"expense ratio",
    r"book value per share",
    r"tangible book",
    r"return on equity",
    r"\bROE\b",
    r"return on assets",
    r"\bROA\b",
    r"cost of equity",
    r"cost of capital",
    r"capital ratio",
    r"Tier 1",
    r"Tier 2",
    r"Common Equity Tier 1",
    r"\bCET1\b",
    r"leverage ratio",
    r"risk-weighted assets",
    r"\bRWA\b",
    r"Basel III",
    r"Basel II",
    r"liquidity coverage ratio",
    r"\bLCR\b",
    r"net stable funding ratio",
    r"\bNSFR\b",
    r"credit risk",
    r"market risk",
    r"operational risk",
    r"loan loss provision",
    r"allowance for loan losses",
    r"\bALLL\b",
    r"non-performing loan",
    r"\bNPL\b",
    r"net charge-off",
    r"deposit beta",
    r"efficiency ratio",
    r"price-to-book",
    r"\bP/B\b",
    r"price-to-earnings",
    r"\bP/E\b",
    r"dividend discount model",
    r"\bDDM\b",
    r"residual income",
    r"excess return",
    r"economic profit",
    r"free cash flow",
    r"enterprise value",
    r"terminal value",
    r"WACC",
    r"beta",
    r"systemic risk",
    r"moral hazard",
    r"too big to fail",
    r"bail-in",
    r"deposit insurance",
    r"shadow banking",
    r"securitization",
    r"credit default swap",
    r"\bCDS\b",
    r"investment banking",
    r"asset management",
    r"wealth management",
    r"brokerage",
    r"insurance",
    r"underwriting",
    r"reinsurance",
    r"float",
    r"policyholder",
    r"claims reserve",
    r"solvency",
    r"regulatory capital",
    r"stress test",
    r"CCAR",
    r"DFAST",
    r"yield curve",
    r"credit spread",
    r"investment grade",
    r"high yield",
    r"covenant",
    r"leverage",
    r"capital structure",
    r"share repurchase",
    r"buyback",
    r"expectations investing",
    r"expectations gap",
    r"competitive advantage",
    r"moat",
    r"barriers to entry",
    r"switching costs",
    r"network effects",
    r"economies of scale",
    r"franchise value",
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
    # dedupe adjacent identical
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
    lower = text.lower()
    for pat in FINANCE_TERM_PATTERNS:
        rx = re.compile(pat, re.I)
        for m in rx.finditer(text):
            term = m.group(0)
            # approximate page from char offset
            pos = m.start()
            page = text[:pos].count("\f") + 1 if "\f" in text else max(1, pos // 3000 + 1)
            found.append({"term": term, "pattern": pat, "approx_page": page})
    # dedupe by normalized term
    seen = set()
    uniq = []
    for f in found:
        k = norm_term(f["term"])
        if k in seen:
            continue
        seen.add(k)
        uniq.append({**f, "source": title})
    return uniq


def definition_snippets(text: str, term: str, window: int = 220) -> str:
    rx = re.compile(re.escape(term), re.I)
    m = rx.search(text)
    if not m:
        return ""
    start = max(0, m.start() - 40)
    end = min(len(text), m.end() + window)
    snippet = re.sub(r"\s+", " ", text[start:end]).strip()
    return snippet[:280]


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
    toc_index_parts = ["# TOC Index\n"]
    chapter_parts = ["# Chapter Summaries\n"]
    concept_rows: dict[str, dict] = {}

    for src in SOURCES:
        path: Path = src["path"]
        block = {
            "key": src["key"],
            "title": src["title"],
            "author": src["author"],
            "type": src["type"],
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
        if path.suffix.lower() == ".acsm":
            block["status"] = "failed"
            block["status_reason"] = (
                "Adobe ACSM DRM purchase file — not a readable PDF; requires Adobe Digital Editions activation"
            )
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
        toc_index_parts.append(f"Extraction status: **{block['status']}** — {block['status_reason'] or 'n/a'}\n")
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
        chapter_parts.append(f"Author: {src['author']} | Pages: {data['page_count']} | Status: {block['status']}\n")
        if not chapters:
            chapter_parts.append("_No reliable chapter headings detected — see raw extraction file._\n")
        for c in chapters[:35]:
            title = c["line"]
            page = c["page"]
            snippet_page = data["pages"][page - 1] if page - 1 < len(data["pages"]) else ""
            concepts = []
            for pat in FINANCE_TERM_PATTERNS[:30]:
                if re.search(pat, snippet_page, re.I):
                    concepts.append(re.search(pat, snippet_page, re.I).group(0))
            chapter_parts.append(f"\n### {title} (p.{page})\n")
            chapter_parts.append(f"- Pages: ~{page}+\n")
            if concepts:
                chapter_parts.append(f"- Named concepts/topics in vicinity: {', '.join(sorted(set(concepts))[:12])}\n")
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
            concept_rows[nt]["source_locations"].append(
                f"{src['title']}:~p{occ['approx_page']}"
            )

    # Write Source_Manifest.md
    sm = ["# Source Manifest — sector-financials\n"]
    for b in manifest_rows:
        sm.append(f"\n## {b['title']}\n")
        sm.append(f"- **Author/editor:** {b['author']}\n")
        sm.append(f"- **Source type:** {b['type']}\n")
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
    needs_attention = [
        b for b in manifest_rows if b["status"] in ("failed", "poor", "partial")
    ]

    hn = [
        "# Handoff Note — sector-financials\n",
        "\n## 1. Module configuration\n",
        "- **Title:** Financials (Sector)\n",
        "- **Slug:** sector-financials\n",
        "- **Kind:** sector-layer1\n",
        "- **Expected build_order:** 12\n",
        "- **Expected global start:** G286\n",
        "\n## 2. Sources processed\n",
    ]
    for b in manifest_rows:
        hn.append(f"- **{b['title']}** — {b['status']}" + (f" ({b['status_reason']})" if b['status_reason'] else "") + "\n")
    hn.append("\n## 3. Sources needing human attention\n")
    if needs_attention:
        for b in needs_attention:
            hn.append(f"- {b['title']}: {b['status']} — {b['status_reason'] or 'see manifest'}\n")
    else:
        hn.append("- None\n")
    hn.extend(
        [
            "\n## 4. Dossier files\n",
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
            "\n## 7. Architecture deferral\n",
            "**No architecture decisions, zone spines, global-reuse calls, or disambiguation judgments have been made. All of that is deferred to the architecture session.**\n",
        ]
    )
    (DOSSIER / "Handoff_Note.md").write_text("".join(hn), encoding="utf-8")

    print(f"manifest_sources={len(manifest_rows)} concepts={inv_count}")


if __name__ == "__main__":
    main()
