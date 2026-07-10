#!/usr/bin/env python3
"""One-off local extractor for sector-energy dossier. Not part of pipeline."""
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
        "key": "oil_101",
        "path": DOWNLOADS / "_OceanofPDF.com_Oil_101_-_Morgan_Downey.pdf",
        "title": "Oil 101",
        "author": "Morgan Downey",
        "type": "practitioner guide / industry primer",
        "tier": "primary",
        "in_config_list": True,
    },
    {
        "key": "new_map",
        "path": DOWNLOADS / "_OceanofPDF.com_The_New_Map_-_Daniel_Yergin.pdf",
        "title": "The New Map: Energy, Climate, and the Clash of Nations",
        "author": "Daniel Yergin",
        "type": "narrative / geopolitics of energy",
        "tier": "primary",
        "in_config_list": True,
    },
    {
        "key": "world_for_sale",
        "path": DOWNLOADS / "_OceanofPDF.com_The_World_for_Sale_-_Jack_Farchy.pdf",
        "title": "The World for Sale",
        "author": "Javier Blas and Jack Farchy",
        "type": "narrative / commodity trading history",
        "tier": "primary",
        "in_config_list": True,
    },
    {
        "key": "how_world_works",
        "path": DOWNLOADS / "_OceanofPDF.com_How_the_World_Really_Works_-_Vaclav_Smil.pdf",
        "title": "How the World Really Works",
        "author": "Vaclav Smil",
        "type": "popular science / energy systems",
        "tier": "primary",
        "in_config_list": True,
    },
    {
        "key": "economics_oil_gas",
        "path": DOWNLOADS / "_OceanofPDF.com_The_Economics_of_Oil_and_Gas_-_Xiaoyi_Mu.pdf",
        "title": "The Economics of Oil and Gas",
        "author": "Xiaoyi Mu",
        "type": "textbook",
        "tier": "secondary",
        "in_config_list": False,
    },
    {
        "key": "oil_smil",
        "path": DOWNLOADS / "_OceanofPDF.com_Oil_-_Vaclav_Smil.pdf",
        "title": "Oil: A Beginner's Guide",
        "author": "Vaclav Smil",
        "type": "popular science / energy primer",
        "tier": "secondary",
        "in_config_list": False,
    },
    {
        "key": "energy_beginners",
        "path": DOWNLOADS / "_OceanofPDF.com_Energy_the_beginners_guide_-_Vaclav_smil.pdf",
        "title": "Energy: A Beginner's Guide",
        "author": "Vaclav Smil",
        "type": "popular science / energy primer",
        "tier": "secondary",
        "in_config_list": False,
    },
    {
        "key": "energy_smil",
        "path": DOWNLOADS / "_OceanofPDF.com_Energy_-_Vaclav_Smil.pdf",
        "title": "Energy (Vaclav Smil)",
        "author": "Vaclav Smil",
        "type": "popular science / energy systems",
        "tier": "secondary",
        "in_config_list": False,
    },
    {
        "key": "antill_arnott_crisis",
        "path": DOWNLOADS
        / "SP15-OilCompanyCrisisManagingStructureProfitabilityandgGrowth-NAntillRArnott-2003.pdf",
        "title": "Oil Company Crisis: Managing Structure, Profitability and Growth",
        "author": "Nick Antill and Robert Arnott",
        "type": "academic / practitioner monograph (OIES SP15)",
        "tier": "primary-adjacent",
        "in_config_list": False,
        "notes": (
            "Not the full book Valuing Oil and Gas Companies; this is the 2003 OIES "
            "monograph by the same authors. Flagged separately from the missing book."
        ),
    },
    {
        "key": "osmundsen_2006",
        "path": DOWNLOADS / "OsmundsenAscheMisundMohn2006.pdf",
        "title": "Valuation of International Oil Companies (Osmundsen et al. 2006)",
        "author": "Petter Osmundsen, Frank Asche, Bård Misund, and Klaus Mohn",
        "type": "academic journal article",
        "tier": "secondary",
        "in_config_list": False,
    },
]

FILING_SOURCES = [
    {
        "key": "xom_10k",
        "path": DOWNLOADS / "0000034088-26-000045.pdf",
        "title": "Exxon Mobil Corporation Form 10-K (FY2025)",
        "company": "Exxon Mobil Corporation",
        "filing_year": "2025",
        "type": "regulatory filing (Form 10-K)",
        "tier": "primary",
        "segment_role": "integrated supermajor",
    },
    {
        "key": "cop_10k",
        "path": DOWNLOADS / "2025 10-K Filed with SEC.pdf",
        "title": "ConocoPhillips Form 10-K (FY2025)",
        "company": "ConocoPhillips",
        "filing_year": "2025",
        "type": "regulatory filing (Form 10-K)",
        "tier": "primary",
        "segment_role": "pure-play upstream E&P",
    },
    {
        "key": "slb_10k",
        "path": DOWNLOADS / "0001193125-26-021017.pdf",
        "title": "SLB N.V. (SLB Limited) Form 10-K (FY2025)",
        "company": "SLB N.V. (SLB Limited)",
        "filing_year": "2025",
        "type": "regulatory filing (Form 10-K)",
        "tier": "primary",
        "segment_role": "oilfield services",
    },
    {
        "key": "epd_10k",
        "path": DOWNLOADS / "EPD 10-K 2025 02.27.2026.pdf",
        "title": "Enterprise Products Partners L.P. Form 10-K (FY2025)",
        "company": "Enterprise Products Partners L.P.",
        "filing_year": "2025",
        "type": "regulatory filing (Form 10-K)",
        "tier": "primary",
        "segment_role": "midstream MLP",
    },
    {
        "key": "vlo_10k",
        "path": DOWNLOADS / "NYSE_VLO_2024.pdf",
        "title": "Valero Energy Corporation Form 10-K (FY2024)",
        "company": "Valero Energy Corporation",
        "filing_year": "2024",
        "type": "regulatory filing (Form 10-K)",
        "tier": "primary",
        "segment_role": "downstream / refining",
    },
]

MISSING_SOURCES = [
    {
        "title": "Valuing Oil and Gas Companies",
        "author": "Nick Antill and Robert Arnott",
        "type": "practitioner valuation handbook",
        "tier": "primary",
        "status": "not provided",
        "status_reason": (
            "Listed in SOURCE_FOLDER_OR_FILES as a primary book; full book not present in "
            "Downloads. A related OIES monograph by the same authors "
            "(Oil Company Crisis, SP15, 2003) WAS present and was extracted separately. "
            "Do not treat the monograph as a substitute for the missing book."
        ),
    },
    {
        "title": "The Prize: The Epic Quest for Oil, Money & Power",
        "author": "Daniel Yergin",
        "type": "narrative / industry history",
        "tier": "primary",
        "status": "not provided",
        "status_reason": (
            "Listed in SOURCE_FOLDER_OR_FILES; PDF not present in the provided Downloads set. "
            "The New Map (also by Yergin) was present and extracted."
        ),
    },
]

HEADING_RE = re.compile(
    r"^(?:chapter|part|section|appendix)\s+[\divxlc\d]+[\.\:\s]",
    re.I,
)
ALLCAPS_LINE = re.compile(r"^[A-Z][A-Z0-9 ,\-–—:&'()/]{8,}$")
NUMBERED_HEAD = re.compile(r"^\d+(\.\d+)*\s+[A-Z]")
FILING_ITEM_RE = re.compile(
    r"^Item\s+(\d+[A-Z]?)\.?\s*(.*)$",
    re.I,
)

ENERGY_TERM_PATTERNS = [
    r"proved reserves?",
    r"probable reserves?",
    r"possible reserves?",
    r"\b1P\b",
    r"\b2P\b",
    r"\b3P\b",
    r"reserve replacement ratio",
    r"\bRRR\b",
    r"\bPV-?10\b",
    r"standardized measure",
    r"successful[- ]efforts",
    r"full[- ]cost",
    r"\bDD&A\b",
    r"depletion, depreciation",
    r"finding (?:and|&) development",
    r"\bF&D\b",
    r"finding cost",
    r"development cost",
    r"netback",
    r"\bEV/boe\b",
    r"\bEV/production\b",
    r"barrels? of oil equivalent",
    r"\bboe\b",
    r"\bboed\b",
    r"\bmmboe\b",
    r"upstream",
    r"midstream",
    r"downstream",
    r"oilfield services?",
    r"integrated (?:oil |energy )?(?:major|company|supermajor)",
    r"exploration and production",
    r"\bE&P\b",
    r"crack spread",
    r"refining margin",
    r"master limited partnership",
    r"\bMLP\b",
    r"\bOPEC\+?\b",
    r"\bWTI\b",
    r"West Texas Intermediate",
    r"\bBrent\b",
    r"Henry Hub",
    r"natural gas liquids?",
    r"\bNGL\b",
    r"liquefied natural gas",
    r"\bLNG\b",
    r"energy transition",
    r"decarboni[sz]ation",
    r"stranded assets?",
    r"carbon capture",
    r"\bCCS\b",
    r"scope [123]",
    r"greenhouse gas",
    r"\bGHG\b",
    r"production sharing",
    r"\bPSC\b",
    r"royalt(?:y|ies)",
    r"concession",
    r"working interest",
    r"net revenue interest",
    r"\bNRI\b",
    r"lease operating expense",
    r"\bLOE\b",
    r"lifting cost",
    r"cash operating cost",
    r"all[- ]in sustaining",
    r"decline curve",
    r"decline rate",
    r"type curve",
    r"shale",
    r"tight oil",
    r"unconventional",
    r"hydraulic fracturing",
    r"fracking",
    r"horizontal drilling",
    r"deepwater",
    r"offshore",
    r"onshore",
    r"pipeline",
    r"gathering",
    r"processing",
    r"fractionation",
    r"storage",
    r"throughput",
    r"take[- ]or[- ]pay",
    r"fee[- ]based",
    r"commodity price risk",
    r"hedging",
    r"futures",
    r"spot price",
    r"benchmark",
    r"contango",
    r"backwardation",
    r"refinery",
    r"crude distillation",
    r"\bCDU\b",
    r"catalytic cracking",
    r"\bFCC\b",
    r"hydrocracking",
    r"coking",
    r"utilization rate",
    r"capacity utilization",
    r"throughput margin",
    r"\bRoACE\b",
    r"return on average capital employed",
    r"capital employed",
    r"reserve life",
    r"\bRLI\b",
    r"production growth",
    r"organic replacement",
    r"acreage",
    r"rig count",
    r"drilling",
    r"completion",
    r"wellhead",
    r"API gravity",
    r"sulfur content",
    r"sweet crude",
    r"sour crude",
    r"light crude",
    r"heavy crude",
    r"petroleum",
    r"crude oil",
    r"natural gas",
    r"coal",
    r"fossil fuel",
    r"primary energy",
    r"energy density",
    r"energy intensity",
    r"power density",
    r"commodity trading",
    r"trading house",
    r"physical trading",
    r"paper trading",
    r"arbitrage",
    r"national oil company",
    r"\bNOC\b",
    r"international oil company",
    r"\bIOC\b",
    r"supermajor",
    r"majors",
    r"independents?",
    r"service company",
    r"seismic",
    r"reservoir",
    r"recovery factor",
    r"enhanced oil recovery",
    r"\bEOR\b",
    r"GICS",
    r"energy sector",
    r"renewables?",
    r"wind",
    r"solar",
    r"biofuel",
    r"renewable diesel",
    r"hydrogen",
    r"capex",
    r"capital expenditure",
    r"free cash flow",
    r"enterprise value",
    r"\bEBITDA\b",
    r"operating cash flow",
    r"dividend",
    r"share repurchase",
    r"buyback",
    r"geopolitics",
    r"sanctions",
    r"supply shock",
    r"demand destruction",
    r"peak oil",
    r"energy security",
]

FILING_TERM_PATTERNS = [
    r"upstream",
    r"midstream",
    r"downstream",
    r"exploration and production",
    r"\bE&P\b",
    r"proved reserves?",
    r"\bPV-?10\b",
    r"standardized measure",
    r"oilfield services?",
    r"drilling",
    r"completion",
    r"production",
    r"refining",
    r"crack spread",
    r"refining margin",
    r"master limited partnership",
    r"\bMLP\b",
    r"pipeline",
    r"natural gas liquids?",
    r"\bNGL\b",
    r"liquefied natural gas",
    r"\bLNG\b",
    r"throughput",
    r"fee[- ]based",
    r"take[- ]or[- ]pay",
    r"segment",
    r"commodity price",
    r"crude oil",
    r"natural gas",
    r"energy transition",
    r"decarboni[sz]ation",
    r"carbon capture",
    r"greenhouse gas",
    r"\bGHG\b",
    r"renewable diesel",
    r"biofuel",
    r"capex",
    r"capital expenditure",
    r"free cash flow",
    r"\bEBITDA\b",
    r"working interest",
    r"royalt(?:y|ies)",
    r"lease operating",
    r"\bDD&A\b",
    r"depletion",
    r"impairment",
    r"asset retirement",
    r"\bARO\b",
]

BOOK_QA_REASONS = {
    "oil_101": "chapter map reconstructed from headings; page references approximate",
    "new_map": "chapter map reconstructed from headings; page references approximate",
    "world_for_sale": "chapter map reconstructed from headings; page references approximate",
    "how_world_works": "chapter map reconstructed from headings; page references approximate",
    "economics_oil_gas": "chapter map reconstructed from headings; page references approximate",
    "oil_smil": "chapter map reconstructed from headings; page references approximate",
    "energy_beginners": "chapter map reconstructed from headings; page references approximate",
    "energy_smil": "chapter map reconstructed from headings; page references approximate",
    "antill_arnott_crisis": (
        "OIES monograph (not Valuing Oil and Gas Companies); TOC/structure from headings"
    ),
    "osmundsen_2006": "short academic article; section map from headings",
}


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
    # Explicit partnership / cycle name-match note from prompt
    partnership_ids = []
    cycle_ids = []
    for ck, ids in lookup.items():
        if "partnership" in ck or ck in ("lpa", "venture partnership", "sponsor jv", "sponsor & jv"):
            partnership_ids.extend(ids)
        if "cycle" in ck:
            cycle_ids.extend(ids)
    if "partnership" in nt or nt in ("mlp", "master limited partnership"):
        # only add if term itself mentions partnership/MLP — mechanical flag only
        if "partnership" in nt:
            hits.update(partnership_ids)
    if "cycle" in nt:
        hits.update(cycle_ids)
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


def detect_toc(pages: list[str], max_pages: int = 30) -> list[str]:
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
                sections.append(
                    {"item": item, "label": label or item_labels.get(item, ""), "page": page_no}
                )
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
    reason = BOOK_QA_REASONS.get(
        key, "chapter map reconstructed from headings; page references approximate"
    )
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


def filing_section_summary(data: dict, sections: list[dict]) -> list[str]:
    parts: list[str] = []
    pages = data["pages"]
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
        for pat in FILING_TERM_PATTERNS[:30]:
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
    notes: str = "",
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
            "notes": notes,
        }
    else:
        if notes and notes not in concept_rows[nt]["notes"]:
            concept_rows[nt]["notes"] = (
                (concept_rows[nt]["notes"] + "; " + notes).strip("; ")
                if concept_rows[nt]["notes"]
                else notes
            )
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
    toc_index_parts = ["# TOC Index — sector-energy\n"]
    chapter_parts = ["# Chapter Summaries — sector-energy\n"]
    concept_rows: dict[str, dict] = {}
    source_texts: dict[str, str] = {}

    # --- Book / monograph / article sources ---
    for src in BOOK_SOURCES:
        path: Path = src["path"]
        block = {
            "key": src["key"],
            "title": src["title"],
            "author": src["author"],
            "type": src["type"],
            "tier": src["tier"],
            "in_config_list": src.get("in_config_list", False),
            "path": str(path),
            "status": "failed",
            "status_reason": "",
            "page_count": 0,
            "areas": [],
            "notes": src.get("notes", ""),
        }
        if not path.exists():
            block["status"] = "failed"
            block["status_reason"] = "file not found at configured path"
            manifest_rows.append(block)
            continue
        try:
            print(f"extracting {src['key']}...", flush=True)
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
        if block["notes"]:
            block["status_reason"] = (
                (block["status_reason"] + "; " + block["notes"]).strip("; ")
                if block["status_reason"]
                else block["notes"]
            )
        block["areas"] = [c["line"] for c in chapters[:40]]
        manifest_rows.append(block)

        toc_index_parts.append(f"\n## {src['title']} ({src['author']})\n")
        toc_index_parts.append(
            f"Source tier: **{src['tier']}** | Extraction status: **{block['status']}** — "
            f"{block['status_reason'] or 'n/a'}\n"
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
            f"Author: {src['author']} | Tier: {src['tier']} | Pages: {data['page_count']} | "
            f"Status: {block['status']}\n"
        )
        if not chapters:
            chapter_parts.append("_No reliable chapter headings detected — see raw extraction file._\n")
        for c in chapters[:35]:
            title_line = c["line"]
            page = c["page"]
            snippet_page = data["pages"][page - 1] if page - 1 < len(data["pages"]) else ""
            concepts = []
            for pat in ENERGY_TERM_PATTERNS[:50]:
                m = re.search(pat, snippet_page, re.I)
                if m:
                    concepts.append(m.group(0))
            chapter_parts.append(f"\n### {title_line} (p.{page})\n")
            chapter_parts.append(f"- Pages: ~{page}+\n")
            if concepts:
                chapter_parts.append(
                    f"- Named concepts/topics in vicinity: {', '.join(sorted(set(concepts))[:12])}\n"
                )
            def_snip = definition_snippets(
                snippet_page, title_line.split()[-1] if title_line.split() else title_line
            )
            if def_snip:
                chapter_parts.append(f"- Nearby text (source context): {def_snip}\n")

        confidence = "medium" if block["status"] == "clean" else "low"
        for occ in find_term_occurrences(
            data["full_text"], src["title"], ENERGY_TERM_PATTERNS, data["page_offsets"]
        ):
            add_concept(
                concept_rows, occ, src["title"], data["full_text"], confidence, corpus_lookup
            )

    # --- Filing sources ---
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
            "segment_role": src.get("segment_role", ""),
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
            print(f"extracting {src['key']}...", flush=True)
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
        if block["segment_role"]:
            block["areas"].insert(0, f"Config segment role: {block['segment_role']}")
        manifest_rows.append(block)

        toc_index_parts.append(f"\n## {src['title']}\n")
        toc_index_parts.append(
            f"Company: **{src['company']}** | Filing year: **{src['filing_year']}** | "
            f"Segment role (config): **{src.get('segment_role', 'n/a')}**\n"
        )
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
            f"Segment role (config): {src.get('segment_role', 'n/a')} | "
            f"Pages: {data['page_count']} | Status: {block['status']}\n"
        )
        chapter_parts.extend(filing_section_summary(data, sections))

        confidence = "high" if block["status"] == "clean" else "medium"
        all_patterns = list(dict.fromkeys(ENERGY_TERM_PATTERNS + FILING_TERM_PATTERNS))
        for occ in find_term_occurrences(
            data["full_text"], src["title"], all_patterns, data["page_offsets"]
        ):
            add_concept(
                concept_rows, occ, src["title"], data["full_text"], confidence, corpus_lookup
            )

    # --- Missing sources ---
    for missing in MISSING_SOURCES:
        manifest_rows.append(
            {
                "key": "missing",
                "title": missing["title"],
                "author": missing.get("author", ""),
                "type": missing["type"],
                "tier": missing["tier"],
                "path": "n/a",
                "status": missing["status"],
                "status_reason": missing["status_reason"],
                "page_count": 0,
                "areas": [],
            }
        )

    # --- Write Source_Manifest.md ---
    sm = ["# Source Manifest — sector-energy\n"]
    for b in manifest_rows:
        sm.append(f"\n## {b['title']}\n")
        if b.get("company"):
            sm.append(f"- **Company:** {b['company']}\n")
        if b.get("filing_year"):
            sm.append(f"- **Filing/report year:** {b['filing_year']}\n")
        if b.get("segment_role"):
            sm.append(f"- **Segment role (config list):** {b['segment_role']}\n")
        sm.append(f"- **Author/editor:** {b['author']}\n")
        sm.append(f"- **Source type:** {b['type']}\n")
        sm.append(f"- **Source tier (config list):** {b['tier']}\n")
        if "in_config_list" in b:
            sm.append(
                f"- **Listed in prompt SOURCE_FOLDER_OR_FILES:** "
                f"{'yes' if b['in_config_list'] else 'no (present in Downloads; extracted as additional)'}\n"
            )
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

    # Synonym notes for inventory (mechanical only)
    synonym_notes = {
        "wti": "variant: West Texas Intermediate",
        "west texas intermediate": "variant: WTI",
        "brent": "benchmark crude",
        "mlp": "variant: master limited partnership",
        "master limited partnership": "variant: MLP",
        "lng": "variant: liquefied natural gas",
        "liquefied natural gas": "variant: LNG",
        "ngl": "variant: natural gas liquids",
        "natural gas liquids": "variant: NGL",
        "e&p": "variant: exploration and production",
        "exploration and production": "variant: E&P",
        "dd&a": "variant: depletion, depreciation and amortization",
        "f&d": "variant: finding and development",
        "finding and development": "variant: F&D",
        "rrr": "variant: reserve replacement ratio",
        "reserve replacement ratio": "variant: RRR",
        "pv-10": "variant: PV10 / standardized measure related",
        "pv10": "variant: PV-10",
        "successful efforts": "do not collapse with full-cost",
        "full cost": "do not collapse with successful-efforts",
        "proved reserves": "do not collapse with probable/possible",
        "probable reserves": "do not collapse with proved/possible",
        "possible reserves": "do not collapse with proved/probable",
        "opec": "variant may include OPEC+",
        "opec+": "variant of OPEC grouping",
        "noc": "variant: national oil company",
        "national oil company": "variant: NOC",
        "ioc": "variant: international oil company",
        "international oil company": "variant: IOC",
        "roace": "variant: return on average capital employed",
        "return on average capital employed": "variant: RoACE",
    }
    for nt, note in synonym_notes.items():
        if nt in concept_rows:
            existing = concept_rows[nt]["notes"]
            concept_rows[nt]["notes"] = (existing + "; " + note).strip("; ") if existing else note

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
                    "source_titles": " | ".join(sorted(row["source_titles"]))
                    or "location unavailable from extraction",
                    "source_locations": " | ".join(locs)
                    if locs
                    else "location unavailable from extraction",
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
        b for b in manifest_rows if b["status"] in ("failed", "poor", "partial", "not provided")
    ]

    # ADR list by filename only
    adr_dir = REPO / "docs" / "decisions"
    adr_files = sorted(p.name for p in adr_dir.glob("ADR-*.md")) if adr_dir.exists() else []
    sector_relevant_adrs = [
        a for a in adr_files if any(x in a.lower() for x in ("sector", "json-canonical", "topology"))
    ]

    hn = [
        "# Handoff Note — sector-energy\n",
        "\n## 1. Module configuration\n",
        "- **Title:** Energy (Sector)\n",
        "- **Slug:** sector-energy\n",
        "- **Kind:** sector-layer1\n",
        "- **Expected build_order:** 14\n",
        "- **Expected global start:** G304\n",
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
    hn.append(
        "\n**Explicit flag:** *Valuing Oil and Gas Companies* (Nick Antill & Robert Arnott) "
        "was **not present**. A related OIES monograph by the same authors "
        "(*Oil Company Crisis*, SP15, 2003) was present and extracted separately — "
        "not treated as a substitute.\n"
    )
    hn.append(
        "**Explicit flag:** *The Prize* (Daniel Yergin) was listed in the prompt source list "
        "but was **not present** in Downloads. *The New Map* (also Yergin) was extracted.\n"
    )

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
            "- Five-zone convention: each module has zones z1–z5 with front-door nodes; "
            "node fields include id, title, tag, quick_definition, explainer_covers, connects_to, gaps\n",
            "- Gap-metadata: structured `gaps` arrays on nodes (observed in existing sector modules)\n",
            "- Cross-module reference/back-link conventions: `connects_to` with module.zone.node refs; "
            "`appears_in` / `home_of` on globals\n",
            "- ADRs flagged by title only (relevant to sector-layer1): "
            + (
                "; ".join(sector_relevant_adrs)
                if sector_relevant_adrs
                else "ADR-001-json-canonical.md; ADR-003-sector-topology.md"
            )
            + "\n",
            "\n### Active module list (slug | kind | build_order)\n",
            "| slug | kind | build_order |\n",
            "|---|---|---|\n",
        ]
    )
    for m in active:
        hn.append(f"| {m['slug']} | {m.get('kind', 'role')} | {m.get('build_order', '')} |\n")
    if draft:
        hn.append("\n### Draft modules\n")
        for m in draft:
            hn.append(f"- {m['slug']} ({m.get('kind', '')}, build_order={m.get('build_order', '')})\n")

    hn.append("\n## 6b. Configuration notes recorded (factual flags only — not resolved)\n")
    hn.extend(
        [
            "- Tier A sector (D2 in docs/SECTOR_LAYER_DESIGN.md): full dossier expected.\n",
            "- Compact module target per ADR-003 rule 6: 8–14 nodes "
            "(architect session decides final count).\n",
            "- Dense upstream/valuation vocabulary flagged in prompt for capture: reserves "
            "(proved/probable), DD&A, successful-efforts vs full-cost, reserve replacement ratio, "
            "PV-10, netbacks, F&D cost, EV/boe, EV/production — string-matched into inventory only.\n",
            "- Segment vocabulary flagged: upstream / midstream / downstream / oilfield services / "
            "integrated major; crack spread; MLP; OPEC/OPEC+; WTI/Brent; energy transition / "
            "decarbonization / stranded assets.\n",
            "- Name-match note (mechanical): glossary partnership-family (G20 LPA, G216 venture "
            "partnership, G225 sponsor & JV) and cycle entries (G127, G232, G237, G255) — "
            "recorded in `also_appears_as_corpus_term` where string-matched; no reuse judgment.\n",
            "- GICS Energy boundary (fossil-fuel-centric; renewables often elsewhere) — capture "
            "only if a source states it; no editorializing.\n",
            "- Additional Downloads present beyond prompt list (Smil Energy titles, Mu textbook, "
            "Osmundsen article, Antill/Arnott OIES monograph) were extracted and labeled as "
            "not-in-config-list where applicable.\n",
            "- Workspace note: Cursor workspace path was `finance-graph` (empty); dossier written "
            "to the live app repo at `OneDrive/finance-learning-app` where prior sector dossiers live.\n",
        ]
    )

    hn.append(
        "\n## 7. Architecture deferral\n"
        "**No architecture decisions, zone spines, global-reuse calls, or disambiguation "
        "judgments have been made. All of that is deferred to the architecture session.**\n"
    )
    (DOSSIER / "Handoff_Note.md").write_text("".join(hn), encoding="utf-8")

    print(f"manifest_sources={len(manifest_rows)} concepts={inv_count}")


if __name__ == "__main__":
    main()
