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

BOOK_SOURCES = [
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

FILING_SOURCES = [
    {
        "key": "accenture_10k",
        "path": DOWNLOADS / "Accenture-2025-10-K.pdf",
        "title": "Accenture plc Form 10-K (FY2025)",
        "company": "Accenture plc",
        "filing_year": "FY2025 (fiscal year ended August 31, 2025)",
        "type": "Form 10-K / annual report",
        "tier": "add-on",
    },
    {
        "key": "palo_alto_10k",
        "path": DOWNLOADS / "0001327567-25-000027.pdf",
        "title": "Palo Alto Networks Form 10-K (FY2025)",
        "company": "Palo Alto Networks, Inc.",
        "filing_year": "FY2025 (fiscal year ended July 31, 2025)",
        "type": "Form 10-K / annual report",
        "tier": "add-on",
    },
    {
        "key": "servicenow_10k",
        "path": DOWNLOADS / "0505eb02-5a4e-449e-a662-edef3bc70e7b.pdf",
        "title": "ServiceNow Form 10-K (FY2025)",
        "company": "ServiceNow, Inc.",
        "filing_year": "FY2025 (fiscal year ended December 31, 2025)",
        "type": "Form 10-K / annual report",
        "tier": "add-on",
    },
    {
        "key": "crowdstrike_10k",
        "path": DOWNLOADS / "0001535527-25-000009.pdf",
        "title": "CrowdStrike Holdings Form 10-K (FY2025)",
        "company": "CrowdStrike Holdings, Inc.",
        "filing_year": "FY2025 (fiscal year ended January 31, 2025)",
        "type": "Form 10-K / annual report",
        "tier": "add-on",
    },
]

MISSING_SOURCES = [
    {
        "title": "The Software Paradox",
        "author": "Stephen O'Grady",
        "type": "practitioner guide",
        "tier": "secondary",
        "status": "not provided",
        "status_reason": "file not in user-supplied folder",
    },
    {
        "title": "Apple Inc. Form 10-K",
        "author": "Apple Inc.",
        "company": "Apple Inc.",
        "type": "Form 10-K / annual report",
        "tier": "add-on",
        "status": "not provided",
        "status_reason": "file not in user-supplied folder",
    },
]

# Source-specific partial-extraction reasons (observed per file, not generic).
BOOK_QA_REASONS: dict[str, str] = {
    "business_of_platforms": (
        "OceanofPDF copy: Contents page detected but dot-leader page numbers absent; "
        "chapter headings reconstructed from inline text; figure/table caption lines "
        "mixed into heading map; page references approximate."
    ),
    "subscribed": (
        "OceanofPDF copy: no dot-leader TOC; chapter titles split across lines "
        "(e.g. 'CHAPTER 1' / 'THE END OF AN ERA'); front-matter headings duplicated; "
        "page references approximate."
    ),
    "chip_war": (
        "OceanofPDF copy: chapter numbers extracted without chapter titles on same line; "
        "promotional 'CLICK HERE TO SIGN UP' debris in heading map; no reliable dot-leader TOC; "
        "page references approximate."
    ),
    "investment_valuation": (
        "OceanofPDF copy: Contents label detected but chapter list uses inline headings "
        "without dot leaders; very large page count increases offset-based page-reference "
        "uncertainty for concept locations."
    ),
    "platform_revolution": (
        "OceanofPDF copy: cover/title-page text captured as headings; chapter takeaways "
        "and section labels duplicated; no dot-leader TOC; page references approximate."
    ),
    "lean_analytics": (
        "OceanofPDF copy: spaced-letter chapter labels (e.g. 'C H A P T E R 1'); "
        "duplicate part/chapter headings from layout reflow; ISBN lines in heading map; "
        "no dot-leader TOC; page references approximate."
    ),
}

HEADING_RE = re.compile(
    r"^(?:chapter|part|section|appendix)\s+[\divxlc\d]+[\.\:\s]",
    re.I,
)
ALLCAPS_LINE = re.compile(r"^[A-Z][A-Z0-9 ,\-–—:&'()/]{8,}$")
NUMBERED_HEAD = re.compile(r"^\d+(\.\d+)*\s+[A-Z]")
FILING_ITEM_RE = re.compile(r"^Item\s+(\d+[A-Z]?)\.?\s*(.*)$", re.I)

IT_TERM_PATTERNS = [
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
    r"semiconductor",
    r"fabless",
    r"foundry",
    r"semiconductor equipment",
    r"chip design",
    r"fabrication",
    r"\bwafer\b",
    r"\bTSMC\b",
    r"\bEUV\b",
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
    r"artificial intelligence",
    r"\bAI\b",
    r"data center",
    r"GPU",
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

FILING_TERM_PATTERNS = [
    r"IT services",
    r"consulting",
    r"systems integrat",
    r"managed services",
    r"outsourcing",
    r"cybersecurity",
    r"firewall",
    r"\bSASE\b",
    r"cloud security",
    r"\bXDR\b",
    r"endpoint security",
    r"security operations",
    r"enterprise software",
    r"workflow automation",
    r"IT service management",
    r"platform expansion",
    r"subscription revenue",
    r"professional services revenue",
    r"hardware",
    r"services revenue",
    r"installed base",
    r"platform ecosystem",
    r"product revenue",
    r"services revenue",
    r"remaining performance obligations",
    r"\bRPO\b",
    r"annual recurring revenue",
    r"\bARR\b",
    r"net retention",
    r"dollar-based net retention",
    r"gross margin",
    r"operating margin",
    r"segment",
    r"cloud platform",
    r"cloud-delivered",
    r"next-generation firewall",
    r"\bNGFW\b",
    r"prisma",
    r"cortex",
    r"reinvention services",
    r"technology services",
]

COVERAGE_BUCKETS: list[tuple[str, list[str], list[str]]] = [
    (
        "IT services",
        ["IT services", r"\bconsulting\b", r"professional services"],
        ["Accenture plc Form 10-K (FY2025)"],
    ),
    (
        "systems integration",
        [r"systems integrat", r"technology services", r"integration services"],
        ["Accenture plc Form 10-K (FY2025)"],
    ),
    (
        "managed services / outsourcing",
        [r"managed services", r"outsourcing", r"managed service"],
        ["Accenture plc Form 10-K (FY2025)"],
    ),
    (
        "cybersecurity",
        [r"cybersecurity", r"endpoint security", r"cloud security", r"\bXDR\b", r"\bSASE\b", r"firewall"],
        [
            "Palo Alto Networks Form 10-K (FY2025)",
            "CrowdStrike Holdings Form 10-K (FY2025)",
        ],
    ),
    (
        "enterprise software",
        [r"enterprise software", r"workflow automation", r"IT service management", r"cloud platform"],
        ["ServiceNow Form 10-K (FY2025)"],
    ),
    (
        "hardware/devices",
        [r"\bhardware\b", r"devices", r"iPhone", r"installed base"],
        [],
    ),
    (
        "cloud infrastructure",
        [r"cloud infrastructure", r"hyperscaler", r"data center", r"cloud platform"],
        [
            "Palo Alto Networks Form 10-K (FY2025)",
            "ServiceNow Form 10-K (FY2025)",
            "CrowdStrike Holdings Form 10-K (FY2025)",
        ],
    ),
    (
        "semiconductors",
        [r"semiconductor", r"fabless", r"foundry", r"chip design", r"\bwafer\b", r"\bTSMC\b"],
        ["Chip War"],
    ),
    (
        "SaaS/subscription",
        [r"\bSaaS\b", r"subscription revenue", r"recurring revenue", r"\bARR\b", r"annual recurring revenue"],
        [
            "Subscribed",
            "Lean Analytics",
            "ServiceNow Form 10-K (FY2025)",
            "CrowdStrike Holdings Form 10-K (FY2025)",
            "Palo Alto Networks Form 10-K (FY2025)",
        ],
    ),
    (
        "platform/ecosystem economics",
        [r"platform ecosystem", r"network effects?", r"two-sided market", r"platform business"],
        [
            "The Business of Platforms",
            "Platform Revolution",
            "Subscribed",
        ],
    ),
    (
        "AI infrastructure",
        [r"artificial intelligence", r"\bAI\b", r"GPU", r"data center"],
        [
            "Chip War",
            "ServiceNow Form 10-K (FY2025)",
            "Accenture plc Form 10-K (FY2025)",
            "Palo Alto Networks Form 10-K (FY2025)",
        ],
    ),
]

BOOK_ONLY_KEYS = {s["key"] for s in BOOK_SOURCES}


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
    pages: list[str] = []
    headings: list[dict] = []
    page_offsets: list[int] = []
    offset = 0
    for i in range(doc.page_count):
        text = doc.load_page(i).get_text("text") or ""
        pages.append(text)
        page_offsets.append(offset)
        offset += len(text) + 1
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
        "page_offsets": page_offsets,
    }


def char_to_page(pos: int, page_offsets: list[int]) -> int:
    page = 1
    for i, off in enumerate(page_offsets):
        if off <= pos:
            page = i + 1
        else:
            break
    return page


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


def detect_filing_toc(pages: list[str], max_pages: int = 15) -> list[str]:
    toc_lines: list[str] = []
    for i in range(min(max_pages, len(pages))):
        for line in pages[i].splitlines():
            s = line.strip()
            if not s:
                continue
            if re.match(r"^Item\s+\d", s, re.I):
                toc_lines.append(f"p{i+1}: {s}")
            elif re.match(r"^Part\s+[IVXLC]+", s, re.I):
                toc_lines.append(f"p{i+1}: {s}")
            elif re.search(r"Item\s+\d+[A-Z]?\.\s+", s, re.I) and len(s) < 120:
                toc_lines.append(f"p{i+1}: {s}")
    return toc_lines


def filing_sections(pages: list[str]) -> list[dict]:
    """Detect major Form 10-K Item sections with PDF page numbers."""
    sections: list[dict] = []
    seen: set[str] = set()
    item_labels = {
        "1": "Business",
        "1A": "Risk Factors",
        "1C": "Cybersecurity",
        "7": "Management's Discussion and Analysis",
        "8": "Financial Statements",
    }
    for i, page in enumerate(pages):
        page_no = i + 1
        for line in page.splitlines():
            s = line.strip()
            m = FILING_ITEM_RE.match(s)
            if not m:
                continue
            item = m.group(1).upper()
            label = m.group(2).strip() or item_labels.get(item, "")
            key = f"Item {item}"
            if key in seen:
                continue
            if item in item_labels or label:
                seen.add(key)
                sections.append({"item": item, "label": label or item_labels.get(item, ""), "page": page_no})
    return sections


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


def assess_book_status(key: str, data: dict, toc: list[str]) -> tuple[str, str]:
    text_quality = sum(1 for p in data["pages"][:10] if len(p.strip()) > 80)
    if text_quality < 3:
        return "poor", "first pages mostly empty — likely image-only or broken OCR layer"
    if len(data["full_text"].strip()) < 5000:
        return "partial", "very little extractable text"
    reason = BOOK_QA_REASONS.get(key, "chapter map reconstructed from headings; page references approximate")
    if len(toc) >= 5:
        return "partial", reason
    return "partial", reason


def assess_filing_status(data: dict, toc: list[str]) -> tuple[str, str]:
    text_quality = sum(1 for p in data["pages"][:10] if len(p.strip()) > 80)
    if text_quality < 3:
        return "poor", "first pages mostly empty — likely image-only or broken extraction layer"
    if len(data["full_text"].strip()) < 5000:
        return "partial", "very little extractable text"
    if len(toc) >= 4:
        return "clean", ""
    sections = filing_sections(data["pages"])
    if len(sections) >= 3:
        return "partial", (
            "SEC filing structure reconstructed from Item headings; "
            "printed page numbers in filing may differ from PDF page index"
        )
    return "partial", "Item headings sparsely detected; filing section map incomplete"


def find_term_occurrences(
    text: str,
    title: str,
    patterns: list[str],
    page_offsets: list[int],
    is_filing: bool = False,
) -> list[dict]:
    found = []
    for pat in patterns:
        rx = re.compile(pat, re.I)
        for m in rx.finditer(text):
            term = m.group(0)
            page = char_to_page(m.start(), page_offsets)
            found.append({"term": term, "pattern": pat, "approx_page": page})
    seen = set()
    uniq = []
    for f in found:
        k = norm_term(f["term"])
        if not k or len(k) < 3:
            continue
        if k in seen:
            continue
        seen.add(k)
        uniq.append({**f, "source": title})
    return uniq


def count_hits(text: str, patterns: list[str]) -> int:
    total = 0
    for pat in patterns:
        total += len(re.compile(pat, re.I).findall(text))
    return total


def count_hits_by_source(
    source_texts: dict[str, str],
    patterns: list[str],
) -> dict[str, int]:
    return {title: count_hits(text, patterns) for title, text in source_texts.items()}


def coverage_limits_report(source_texts: dict[str, str]) -> list[str]:
    book_text = "\n".join(t for title, t in source_texts.items() if "Form 10-K" not in title)
    bullets: list[str] = []
    for label, patterns, expected_filings in COVERAGE_BUCKETS:
        all_hits = count_hits("\n".join(source_texts.values()), patterns)
        book_hits = count_hits(book_text, patterns)
        filing_hits: dict[str, int] = {}
        for title, text in source_texts.items():
            if "Form 10-K" in title:
                h = count_hits(text, patterns)
                if h:
                    filing_hits[title] = h
        if label == "hardware/devices":
            apple_title = "Apple Inc. Form 10-K"
            if apple_title in source_texts:
                h = count_hits(source_texts[apple_title], patterns)
                bullets.append(
                    f"**{label}:** covered by {apple_title} ({h} hits); prior book-source mechanical hits: {book_hits}."
                )
            else:
                incidental = {t: h for t, h in filing_hits.items() if t != apple_title}
                if incidental:
                    parts = [f"{t} ({h} incidental hits)" for t, h in incidental.items()]
                    bullets.append(
                        f"**{label}:** Apple 10-K not in folder; incidental mentions in {', '.join(parts)}; "
                        f"prior book-source mechanical hits: {book_hits}."
                    )
                else:
                    bullets.append(
                        f"**{label}:** no add-on filing provided (Apple 10-K not in folder); "
                        f"prior book-source mechanical hits: {book_hits}."
                    )
            continue
        if filing_hits:
            parts = [f"{t} ({h} hits)" for t, h in filing_hits.items()]
            if book_hits == 0:
                bullets.append(
                    f"**{label}:** covered by {', '.join(parts)}; prior book-source coverage had 0 direct hits."
                )
            else:
                bullets.append(
                    f"**{label}:** covered by {', '.join(parts)}; prior book-source mechanical hits: {book_hits}."
                )
        elif all_hits >= 5:
            bullets.append(f"**{label}:** book-source mechanical hits: {book_hits} (total across dossier: {all_hits}).")
        else:
            bullets.append(
                f"**{label}:** thin across dossier — total mechanical hits: {all_hits}; "
                f"book hits: {book_hits}; expected filing add-ons not matched: {', '.join(expected_filings) or 'n/a'}."
            )
    return bullets


def filing_section_summary(data: dict, title: str, sections: list[dict]) -> list[str]:
    parts: list[str] = []
    pages = data["pages"]
    full = data["full_text"]
    section_map = {s["item"]: s for s in sections}

    def section_text(item: str) -> str:
        if item not in section_map:
            return ""
        start_page = section_map[item]["page"] - 1
        end_page = min(start_page + 8, len(pages) - 1)
        return "\n".join(pages[start_page : end_page + 1])

    summaries = [
        ("1", "Business overview"),
        ("7", "MD&A operating drivers"),
        ("1A", "Risk factors (sector-relevant)"),
        ("8", "Segment / financial statement references"),
    ]
    for item, heading in summaries:
        if item not in section_map:
            continue
        sec = section_map[item]
        snippet = section_text(item)
        concepts = []
        for pat in FILING_TERM_PATTERNS[:25]:
            m = re.search(pat, snippet, re.I)
            if m:
                concepts.append(m.group(0))
        parts.append(f"\n### {heading} — Item {item} (PDF p.{sec['page']})\n")
        if concepts:
            parts.append(f"- Named terms in vicinity: {', '.join(sorted(set(concepts))[:12])}\n")
        def_snip = definition_snippets(snippet[:8000], sec["label"] or heading)
        if def_snip:
            parts.append(f"- Nearby text: {def_snip}\n")
    return parts


def add_concept(
    concept_rows: dict[str, dict],
    occ: dict,
    src_title: str,
    full_text: str,
    confidence: str,
    corpus_lookup: dict[str, list[str]],
) -> None:
    nt = norm_term(occ["term"])
    if not nt or len(nt) < 3:
        return
    if nt not in concept_rows:
        concept_rows[nt] = {
            "term": occ["term"],
            "normalized_term": nt,
            "short_definition": definition_snippets(full_text, occ["term"]),
            "source_titles": set(),
            "source_locations": [],
            "extraction_confidence": confidence,
            "also_appears_as_corpus_term": corpus_match(occ["term"], corpus_lookup),
            "notes": "",
        }
    concept_rows[nt]["source_titles"].add(src_title)
    concept_rows[nt]["source_locations"].append(f"{src_title}:p{occ['approx_page']}")


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

    manifest_rows: list[dict] = []
    toc_index_parts = ["# TOC Index — sector-information-technology\n"]
    chapter_parts = ["# Chapter Summaries — sector-information-technology\n"]
    concept_rows: dict[str, dict] = {}
    source_texts: dict[str, str] = {}

    # --- Book sources ---
    for src in BOOK_SOURCES:
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
        source_texts[src["title"]] = data["full_text"]
        toc = detect_toc(data["pages"])
        chapters = chapter_blocks(data["headings"])
        block["status"], block["status_reason"] = assess_book_status(src["key"], data, toc)
        block["areas"] = [c["line"] for c in chapters[:40]]
        manifest_rows.append(block)

        toc_index_parts.append(f"\n## {src['title']} ({src['author']})\n")
        toc_index_parts.append(
            f"Source tier: **{src['tier']}** | Extraction status: **{block['status']}** — {block['status_reason'] or 'n/a'}\n"
        )
        toc_index_parts.append(f"Page count: {data['page_count']}\n")
        if toc:
            toc_index_parts.append("### Detected TOC lines\n")
            for line in toc[:80]:
                toc_index_parts.append(f"- {line}\n")
        else:
            toc_index_parts.append("### Reconstructed from detected headings\n")
            for c in chapters[:60]:
                toc_index_parts.append(f"- p{c['page']}: {c['line']}\n")

        chapter_parts.append(f"\n## {src['title']}\n")
        chapter_parts.append(
            f"Author: {src['author']} | Tier: {src['tier']} | Pages: {data['page_count']} | Status: {block['status']}\n"
        )
        if not chapters:
            chapter_parts.append("_No reliable chapter headings detected — see raw extraction file._\n")
        for c in chapters[:35]:
            title_line = c["line"]
            page = c["page"]
            snippet_page = data["pages"][page - 1] if page - 1 < len(data["pages"]) else ""
            concepts = []
            for pat in IT_TERM_PATTERNS[:40]:
                m = re.search(pat, snippet_page, re.I)
                if m:
                    concepts.append(m.group(0))
            chapter_parts.append(f"\n### {title_line} (p.{page})\n")
            chapter_parts.append(f"- Pages: ~{page}+\n")
            if concepts:
                chapter_parts.append(
                    f"- Named concepts/topics in vicinity: {', '.join(sorted(set(concepts))[:12])}\n"
                )
            def_snip = definition_snippets(snippet_page, title_line.split()[-1] if title_line.split() else title_line)
            if def_snip:
                chapter_parts.append(f"- Nearby text (source context): {def_snip}\n")

        confidence = "medium" if block["status"] == "clean" else "low"
        for occ in find_term_occurrences(
            data["full_text"], src["title"], IT_TERM_PATTERNS, data["page_offsets"]
        ):
            add_concept(concept_rows, occ, src["title"], data["full_text"], confidence, corpus_lookup)

    # --- Filing add-ons ---
    for src in FILING_SOURCES:
        path = src["path"]
        block = {
            "key": src["key"],
            "title": src["title"],
            "author": src["company"],
            "company": src["company"],
            "filing_year": src["filing_year"],
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
        source_texts[src["title"]] = data["full_text"]
        toc = detect_filing_toc(data["pages"])
        sections = filing_sections(data["pages"])
        block["status"], block["status_reason"] = assess_filing_status(data, toc)
        block["areas"] = [f"Item {s['item']}: {s['label']}" for s in sections[:25]]
        manifest_rows.append(block)

        toc_index_parts.append(f"\n## {src['title']}\n")
        toc_index_parts.append(f"Company: **{src['company']}** | Filing year: **{src['filing_year']}**\n")
        toc_index_parts.append(
            f"Extraction status: **{block['status']}** — {block['status_reason'] or 'n/a'}\n"
        )
        toc_index_parts.append(f"Page count: {data['page_count']}\n")
        if toc:
            toc_index_parts.append("### Detected filing TOC / Item lines\n")
            for line in toc[:80]:
                toc_index_parts.append(f"- {line}\n")
        else:
            toc_index_parts.append("### Reconstructed from detected headings\n")
            for s in sections[:30]:
                toc_index_parts.append(f"- p{s['page']}: Item {s['item']} — {s['label']}\n")

        chapter_parts.append(f"\n## {src['title']}\n")
        chapter_parts.append(
            f"Company: {src['company']} | Filing year: {src['filing_year']} | "
            f"Pages: {data['page_count']} | Status: {block['status']}\n"
        )
        chapter_parts.extend(filing_section_summary(data, src["title"], sections))

        confidence = "high" if block["status"] == "clean" else "medium"
        all_patterns = list(dict.fromkeys(IT_TERM_PATTERNS + FILING_TERM_PATTERNS))
        for occ in find_term_occurrences(
            data["full_text"], src["title"], all_patterns, data["page_offsets"], is_filing=True
        ):
            add_concept(concept_rows, occ, src["title"], data["full_text"], confidence, corpus_lookup)

    # --- Missing sources ---
    for missing in MISSING_SOURCES:
        manifest_rows.append(
            {
                "key": "missing",
                "title": missing["title"],
                "author": missing.get("author", missing.get("company", "")),
                "company": missing.get("company", ""),
                "filing_year": missing.get("filing_year", ""),
                "type": missing["type"],
                "tier": missing["tier"],
                "path": "n/a",
                "status": missing["status"],
                "status_reason": missing["status_reason"],
                "page_count": 0,
                "areas": [],
            }
        )

    coverage_bullets = coverage_limits_report(source_texts)

    # --- Write Source_Manifest.md ---
    sm = ["# Source Manifest — sector-information-technology\n"]
    for b in manifest_rows:
        sm.append(f"\n## {b['title']}\n")
        if b.get("company"):
            sm.append(f"- **Company:** {b['company']}\n")
        if b.get("filing_year"):
            sm.append(f"- **Filing/report year:** {b['filing_year']}\n")
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
            locs = row["source_locations"][:8]
            w.writerow(
                {
                    "term": row["term"],
                    "normalized_term": row["normalized_term"],
                    "short_definition": row["short_definition"][:300],
                    "source_titles": " | ".join(sorted(row["source_titles"])) or "location unavailable from extraction",
                    "source_locations": " | ".join(locs) if locs else "location unavailable from extraction",
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
        tier = b.get("tier", "")
        hn.append(
            f"- **{b['title']}** ({tier}) — {b['status']}"
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
            "- **Apple Inc. Form 10-K** was in the expected add-on list but was **not provided** in the user folder.\n",
        ]
    )

    hn.append("\n## 6c. Coverage_Limits\n")
    hn.append("Mechanical hit/source coverage observations (not architecture judgments):\n\n")
    for bullet in coverage_bullets:
        hn.append(f"- {bullet}\n")

    hn.append(
        "\n## 7. Architecture deferral\n"
        "No architecture decisions, zone spines, global-reuse calls, or disambiguation judgments have been made. All of that is deferred to the architecture session.\n"
    )
    (DOSSIER / "Handoff_Note.md").write_text("".join(hn), encoding="utf-8")

    probe = DOSSIER / "_pdf_probe.txt"
    if probe.exists():
        probe.unlink()

    print(f"manifest_sources={len(manifest_rows)} concepts={inv_count} coverage={len(coverage_bullets)}")


if __name__ == "__main__":
    main()
