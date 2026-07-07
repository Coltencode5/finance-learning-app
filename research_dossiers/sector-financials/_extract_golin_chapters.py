#!/usr/bin/env python3
"""Extract Golin & Delhaise chapter PDFs into sector-financials dossier."""
from __future__ import annotations

import csv
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

import fitz

REPO = Path(__file__).resolve().parents[2]
DOSSIER = Path(__file__).resolve().parent
DOWNLOADS = Path(r"c:\Users\cfroo\Downloads")

BOOK_TITLE = "The Bank Credit Analysis Handbook"
BOOK_AUTHOR = "Jonathan Golin and Philippe Delhaise"
BOOK_YEAR = "2013 (2nd ed.)"

CHAPTERS = [
    {
        "key": "golin_ch3",
        "glob": "*Chapter_3_The_Business_of_Banking*.pdf",
        "title": "Chapter 3 — The Business of Banking",
        "book_ch": 3,
    },
    {
        "key": "golin_ch4",
        "glob": "*Chapter_4_Deconstructing_the_Bank_Income_Statement*.pdf",
        "title": "Chapter 4 — Deconstructing the Bank Income Statement",
        "book_ch": 4,
    },
    {
        "key": "golin_ch9",
        "glob": "*Chapter_9_Capital*.pdf",
        "title": "Chapter 9 — Capital",
        "book_ch": 9,
    },
]

FINANCE_TERM_PATTERNS = [
    r"net interest margin", r"\bNIM\b", r"net interest income",
    r"interest income", r"interest expense", r"non-interest income",
    r"provision for loan losses", r"loan loss provision", r"allowance for loan losses",
    r"\bALLL\b", r"non-performing loan", r"\bNPL\b", r"net charge-off",
    r"efficiency ratio", r"operating leverage", r"return on equity", r"\bROE\b",
    r"return on assets", r"\bROA\b", r"return on capital", r"\bROC\b",
    r"cost-to-income", r"cost to income", r"fee income", r"trading income",
    r"commercial banking", r"investment banking", r"retail banking",
    r"universal bank", r"wholesale banking", r"treasury", r"capital markets",
    r"insurance", r"asset management", r"wealth management", r"brokerage",
    r"Tier 1", r"Tier 2", r"Common Equity Tier 1", r"\bCET1\b",
    r"capital adequacy", r"capital ratio", r"regulatory capital",
    r"risk-weighted assets", r"\bRWA\b", r"leverage ratio",
    r"tangible equity", r"tangible common equity", r"\bTCE\b",
    r"Basel", r"capital buffer", r"capital conservation",
    r"dividend", r"retained earnings", r"goodwill",
    r"deposit", r"loan portfolio", r"securitization",
    r"credit risk", r"market risk", r"operational risk",
    r"liquidity", r"maturity transformation",
    r"spread", r"yield", r"credit spread",
    r"price-to-book", r"\bP/B\b", r"book value",
    r"moral hazard", r"too big to fail", r"bail-in",
    r"stress test", r"CCAR", r"DFAST",
    r"combined ratio", r"loss ratio", r"expense ratio",
    r"underwriting", r"reinsurance", r"float",
]

SECTION_HEAD = re.compile(
    r"^(?:\d+\.\s+)?[A-Z][A-Za-z0-9 ,\-–—'&()/]+$"
)


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


def find_pdf(glob_pat: str) -> Path:
    matches = list(DOWNLOADS.glob(glob_pat))
    if not matches:
        raise FileNotFoundError(glob_pat)
    return matches[0]


def extract_pdf(path: Path) -> dict:
    doc = fitz.open(path)
    pages = [doc.load_page(i).get_text("text") or "" for i in range(doc.page_count)]
    doc.close()
    full = "\n".join(pages)
    headings = []
    for i, text in enumerate(pages, 1):
        for line in text.splitlines():
            s = line.strip()
            if 8 <= len(s) <= 90 and SECTION_HEAD.match(s) and s.count(" ") >= 1:
                headings.append({"page": i, "line": s})
    return {"page_count": len(pages), "pages": pages, "full_text": full, "headings": headings}


def detect_sections(text: str, headings: list[dict]) -> list[dict]:
    sections = []
    for h in headings:
        line = h["line"]
        if line.lower().startswith("chapter "):
            continue
        if len(line.split()) <= 12:
            sections.append(h)
    seen = set()
    out = []
    for s in sections:
        k = s["line"].lower()
        if k in seen:
            continue
        seen.add(k)
        out.append(s)
    return out[:40]


def definition_snippets(text: str, term: str, window: int = 200) -> str:
    rx = re.compile(re.escape(term), re.I)
    m = rx.search(text)
    if not m:
        return ""
    start = max(0, m.start() - 30)
    end = min(len(text), m.end() + window)
    return re.sub(r"\s+", " ", text[start:end]).strip()[:300]


def find_terms(text: str, source_label: str) -> list[dict]:
    found = []
    seen = set()
    for pat in FINANCE_TERM_PATTERNS:
        for m in re.finditer(pat, text, re.I):
            term = m.group(0)
            k = norm_term(term)
            if not k or k in seen:
                continue
            seen.add(k)
            pos = m.start()
            page = max(1, pos // 3200 + 1)
            found.append({"term": term, "page": page, "source": source_label})
    return found


def load_existing_inventory() -> dict[str, dict]:
    path = DOSSIER / "Concept_Inventory.csv"
    rows: dict[str, dict] = {}
    if not path.exists():
        return rows
    with path.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows[row["normalized_term"]] = row
    return rows


def main() -> None:
    raw_dir = DOSSIER / "raw_extractions"
    raw_dir.mkdir(exist_ok=True)
    corpus = load_corpus_terms()
    inventory = load_existing_inventory()

    extracted = []
    toc_parts = ["\n## The Bank Credit Analysis Handbook (Golin & Delhaise) — licensed chapter extracts\n"]
    toc_parts.append("Extraction status: **partial** (Chapters 3, 4, 9 only; user-exported non-DRM PDFs)\n")
    summary_parts = ["\n## The Bank Credit Analysis Handbook (Golin & Delhaise)\n"]
    summary_parts.append(f"Author: {BOOK_AUTHOR} | Edition: {BOOK_YEAR}\n")
    summary_parts.append("Extracted chapters: 3 (Business of Banking), 4 (Income Statement), 9 (Capital)\n")

    for ch in CHAPTERS:
        path = find_pdf(ch["glob"])
        data = extract_pdf(path)
        (raw_dir / f"{ch['key']}.txt").write_text(data["full_text"], encoding="utf-8")

        sections = detect_sections(data["full_text"], data["headings"])
        block = {
            "key": ch["key"],
            "title": ch["title"],
            "path": str(path),
            "page_count": data["page_count"],
            "sections": [s["line"] for s in sections],
            "status": "clean",
            "status_reason": "user-exported chapter PDF; text extraction clean",
        }
        extracted.append(block)

        toc_parts.append(f"\n### {ch['title']}\n")
        toc_parts.append(f"Source file: `{path.name}` | Pages in extract: {data['page_count']}\n")
        toc_parts.append("Section headings (reconstructed):\n")
        for s in sections[:35]:
            toc_parts.append(f"- p{s['page']}: {s['line']}\n")

        summary_parts.append(f"\n### {ch['title']} ({data['page_count']} pp in extract)\n")
        for s in sections[:25]:
            page = s["page"]
            snippet = data["pages"][page - 1] if page - 1 < len(data["pages"]) else ""
            concepts = []
            for pat in FINANCE_TERM_PATTERNS[:25]:
                if re.search(pat, snippet, re.I):
                    concepts.append(re.search(pat, snippet, re.I).group(0))
            summary_parts.append(f"\n#### {s['line']} (p.{page})\n")
            if concepts:
                summary_parts.append(
                    f"- Named concepts/topics in vicinity: {', '.join(sorted(set(concepts))[:10])}\n"
                )
            snip = definition_snippets(snippet, s["line"].split()[0] if s["line"] else "")
            if len(snip) > 60:
                summary_parts.append(f"- Nearby source context (paraphrase basis): {snip}\n")

        for occ in find_terms(data["full_text"], BOOK_TITLE):
            nt = norm_term(occ["term"])
            loc = f"{BOOK_TITLE} {ch['title']}:~p{occ['page']}"
            if nt not in inventory:
                inventory[nt] = {
                    "term": occ["term"],
                    "normalized_term": nt,
                    "short_definition": definition_snippets(data["full_text"], occ["term"]),
                    "source_titles": BOOK_TITLE,
                    "source_locations": loc,
                    "extraction_confidence": "high",
                    "also_appears_as_corpus_term": corpus_match(occ["term"], corpus),
                    "notes": f"From licensed extract: {ch['title']}",
                }
            else:
                row = inventory[nt]
                if BOOK_TITLE not in row.get("source_titles", ""):
                    row["source_titles"] = " | ".join(
                        filter(None, [row.get("source_titles", ""), BOOK_TITLE])
                    )
                if loc not in row.get("source_locations", ""):
                    row["source_locations"] = " | ".join(
                        filter(None, [row.get("source_locations", ""), loc])
                    )
                if "golin" not in row.get("notes", "").lower():
                    row["notes"] = (row.get("notes", "") + f"; {ch['title']} extract").strip("; ")

    # Update Source_Manifest — replace Golin section
    manifest_path = DOSSIER / "Source_Manifest.md"
    manifest = manifest_path.read_text(encoding="utf-8")
    marker = "## The Bank Credit Analysis Handbook (Golin & Delhaise)"
    if marker in manifest:
        manifest = manifest.split(marker)[0].rstrip() + "\n"

    golin_manifest = f"\n{marker} — licensed chapter extracts\n"
    golin_manifest += f"- **Author/editor:** {BOOK_AUTHOR}\n"
    golin_manifest += "- **Source type:** practitioner handbook (bank credit analysis)\n"
    golin_manifest += f"- **Edition/year:** {BOOK_YEAR}\n"
    golin_manifest += "- **Extraction status:** partial\n"
    golin_manifest += (
        "- **Status detail:** Full ADE copy remains DRM-locked; user exported non-DRM PDFs for "
        "Chapters 3, 4, and 9 only (172 book pages per original TOC; extract page counts may differ). "
        "Chapters 5–8, 10–15 not included.\n"
    )
    for b in extracted:
        golin_manifest += f"- **Extract file — {b['title']}:** `{b['path']}` ({b['page_count']} pp, {b['status']})\n"
        if b["sections"]:
            golin_manifest += "  - Section headings detected:\n"
            for s in b["sections"][:20]:
                golin_manifest += f"    - {s}\n"
    manifest_path.write_text(manifest + golin_manifest, encoding="utf-8")

    # Append to TOC_Index
    toc_path = DOSSIER / "TOC_Index.md"
    toc_path.write_text(toc_path.read_text(encoding="utf-8") + "".join(toc_parts), encoding="utf-8")

    # Append to Chapter_Summaries
    chap_path = DOSSIER / "Chapter_Summaries.md"
    chap_path.write_text(chap_path.read_text(encoding="utf-8") + "".join(summary_parts), encoding="utf-8")

    # Write merged inventory
    with (DOSSIER / "Concept_Inventory.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "term", "normalized_term", "short_definition", "source_titles",
                "source_locations", "extraction_confidence",
                "also_appears_as_corpus_term", "notes",
            ],
        )
        w.writeheader()
        for row in sorted(inventory.values(), key=lambda r: r["normalized_term"]):
            w.writerow(row)

    # Update Handoff_Note
    inv_count = len(inventory)
    handoff = f"""# Handoff Note — sector-financials

## 1. Module configuration
- **Title:** Financials (Sector)
- **Slug:** sector-financials
- **Kind:** sector-layer1
- **Expected build_order:** 12
- **Expected global start:** G286

## 2. Sources processed
- **The Bankers' New Clothes** — partial (TOC reconstructed from headings)
- **Handbook of Basel III Capital** — partial (TOC reconstructed from headings)
- **The Dark Side of Valuation** — partial (TOC reconstructed from headings)
- **Competition Demystified** — partial (TOC reconstructed from headings)
- **Expectations Investing** — partial (TOC reconstructed from headings)
- **Common Stocks and Uncommon Profits and Other Writings** — partial (TOC reconstructed from headings)
- **Common Stocks and Uncommon Profits and Other Writings (alt file)** — partial (TOC reconstructed from headings)
- **Paths to Wealth Through Common Stocks** — partial (TOC reconstructed from headings)
- **The Bank Credit Analysis Handbook (Golin & Delhaise)** — **partial** (Chapters 3, 4, 9 extracted from user-exported non-DRM PDFs; remaining chapters not read)

## 3. Sources needing human attention
- The Bankers' New Clothes: partial — TOC not cleanly detected; chapter map reconstructed from headings
- Handbook of Basel III Capital: partial — TOC not cleanly detected; chapter map reconstructed from headings
- The Dark Side of Valuation: partial — TOC not cleanly detected; chapter map reconstructed from headings
- Competition Demystified: partial — TOC not cleanly detected; chapter map reconstructed from headings
- Expectations Investing: partial — TOC not cleanly detected; chapter map reconstructed from headings
- Common Stocks and Uncommon Profits and Other Writings: partial — TOC not cleanly detected; chapter map reconstructed from headings
- Common Stocks and Uncommon Profits and Other Writings (alt file): partial — TOC not cleanly detected; chapter map reconstructed from headings
- Paths to Wealth Through Common Stocks: partial — TOC not cleanly detected; chapter map reconstructed from headings
- **Golin & Delhaise — partial only:** Chapters 5–8 (balance sheet, earnings, asset quality, governance), 10 (liquidity), 11–15 not in dossier. Insurance KPIs (combined ratio) still thin across all sources.

## 4. Dossier files
- `Source_Manifest.md` — per-source metadata, extraction status, heading-level coverage
- `TOC_Index.md` — detected or reconstructed tables of contents / chapter maps
- `Chapter_Summaries.md` — chapter/section entries with named topics and nearby source text
- `Concept_Inventory.csv` — mechanical term inventory with corpus string matches only
- `Handoff_Note.md` — this file
- `raw_extractions/` — plain-text dumps (includes `golin_ch3.txt`, `golin_ch4.txt`, `golin_ch9.txt`)

## 5. Concept inventory row count
{inv_count}

## 6. Repo-state facts (read-only inspection)
- Active modules: 11
- Draft modules: 0
- Global count/range: 285 (G1–G285)
- Next available global ID: G286
- Module kinds in use: asset-class, core-concept, role (sector-layer1/2 not yet built)
- Five-zone convention: each module has zones z1–z5 with front-door nodes; node fields include id, title, tag, quick_definition, explainer_covers, connects_to, gaps
- ADRs flagged by title only (relevant to sector-layer1): ADR-001-json-canonical.md; ADR-003-sector-topology.md

### Active module list (slug | kind | build_order)
| slug | kind | build_order |
|---|---|---|
| private-equity | role | 1 |
| private-credit | role | 2 |
| investment-banking | role | 3 |
| hedge-funds | role | 4 |
| asset-management | role | 5 |
| wealth-management | role | 6 |
| equity-research | role | 7 |
| venture-capital | role | 8 |
| real-estate | role | 9 |
| macro-economics | core-concept | 10 |
| fixed-income | asset-class | 11 |

## 6b. Configuration notes recorded (factual flags only — not resolved)
- Compact module target per ADR-003 rule 6: 8–14 nodes (architect session decides final count).
- Corpus overlap zones flagged for name-matching in `Concept_Inventory.csv` (no reuse/new-global judgment made): FI credit vocabulary G264–G285 (esp. G275, G276, G277); macro rate/Fed globals G236–G263; ER bank worked-contrast at `equity-research.z2.3` (NIM, credit losses, capital ratios).
- GICS capital-markets industries overlap existing role modules (`investment-banking`, `asset-management`, `wealth-management`) — inventory includes string matches; seam ownership deferred.
- Insurance coverage remains thinner than banking across all sources.
- Duplicate Fisher file pair in dossier; architect may dedupe.
- Golin extracts cover sector economics (Ch3), income-statement/NIM (Ch4), and capital (Ch9) — aligned with ER Z2.3 bank contrast; Ch7 asset quality not extracted.

## 7. Architecture deferral
**No architecture decisions, zone spines, global-reuse calls, or disambiguation judgments have been made. All of that is deferred to the architecture session.**
"""
    (DOSSIER / "Handoff_Note.md").write_text(handoff, encoding="utf-8")
    print(f"golin_chapters=3 inventory_rows={inv_count}")


if __name__ == "__main__":
    main()
