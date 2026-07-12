#!/usr/bin/env python3
"""Build chapter maps and keyword windows for CD book extracts."""
from __future__ import annotations

import json
import re
from pathlib import Path

DOSSIER = Path(__file__).resolve().parents[1]
RAW = DOSSIER / "raw_extractions"


def pages_from_dump(path: Path) -> list[tuple[int, str]]:
    text = path.read_text(encoding="utf-8", errors="replace")
    pages = []
    for m in re.finditer(r"===== PAGE (\d+) / (\d+) =====\n(.*?)(?=\n===== PAGE |\Z)", text, re.S):
        pages.append((int(m.group(1)), m.group(3)))
    return pages


def find_lines(pages, pattern, flags=re.I):
    rx = re.compile(pattern, flags)
    hits = []
    for pno, body in pages:
        for line in body.splitlines():
            s = line.strip()
            if rx.search(s) and 3 < len(s) < 140:
                hits.append((pno, s))
    return hits


def window(pages, start, end):
    chunks = []
    for pno, body in pages:
        if start <= pno <= end:
            chunks.append(f"[p{pno}]\n{body}")
    return "\n".join(chunks)


def keyword_hits(pages, terms, max_per=8):
    out = {}
    for term in terms:
        rx = re.compile(re.escape(term), re.I)
        found = []
        for pno, body in pages:
            if rx.search(body):
                # grab a short context line
                for line in body.splitlines():
                    if rx.search(line):
                        found.append({"page": pno, "line": line.strip()[:160]})
                        break
            if len(found) >= max_per:
                break
        out[term] = found
    return out


def main():
    books = {
        "everything_store": RAW / "everything_store.txt",
        "resurrecting_retail": RAW / "resurrecting_retail.txt",
        "trading_up": RAW / "trading_up.txt",
        "different": RAW / "different.txt",
    }
    report = {}
    for key, path in books.items():
        pages = pages_from_dump(path)
        ch = find_lines(pages, r"^(CHAPTER|Chapter)\s+[0-9IVXLC]+")
        part = find_lines(pages, r"^(PART|Part)\s+[0-9IVXLC]+")
        # Also catch Contents-style entries
        contentsish = []
        for pno, body in pages[:30]:
            if re.search(r"contents|table of contents", body, re.I):
                contentsish.append({"page": pno, "preview": body[:1500]})
        report[key] = {
            "n_pages": len(pages),
            "chapters": ch[:60],
            "parts": part[:30],
            "contents_pages": contentsish,
        }
        # dump first 25 pages for TOC reading
        (RAW / f"_{key}_frontmatter.txt").write_text(window(pages, 1, 30), encoding="utf-8")

    # Everything Store known structure - also catch titled chapters after CHAPTER N
    es = pages_from_dump(books["everything_store"])
    titled = []
    for pno, body in es:
        lines = [ln.strip() for ln in body.splitlines() if ln.strip()]
        for i, ln in enumerate(lines):
            if re.match(r"^CHAPTER\s+\d+", ln, re.I):
                title = lines[i + 1] if i + 1 < len(lines) else ""
                titled.append({"page": pno, "chapter": ln, "title": title})
    report["everything_store"]["titled_chapters"] = titled

    # Trading Up / Different / Stephens - look for numbered chapter titles in contents
    for key in ["trading_up", "different", "resurrecting_retail"]:
        pages = pages_from_dump(books[key])
        # lines that look like chapter titles with page numbers
        toc_lines = []
        for pno, body in pages[:25]:
            for line in body.splitlines():
                s = line.strip()
                if re.search(r".+\s+\d{1,3}$", s) and len(s) < 100:
                    if not re.match(r"^\d+$", s):
                        toc_lines.append((pno, s))
        report[key]["toc_candidate_lines"] = toc_lines[:80]

    (RAW / "_chapter_map.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("wrote chapter map")

    # KPI keyword scans on filings
    filing_terms = {
        "amazon": [
            "Online stores", "Third-party seller services", "Advertising services",
            "Subscription services", "AWS", "Amazon Web Services", "fulfillment",
            "operating income", "North America", "International", "net sales",
        ],
        "nike": [
            "Wholesale", "NIKE Direct", "gross margin", "Inventories", "inventory",
            "comparable", "Direct to Consumer", "DTC", "Converse",
        ],
        "starbucks": [
            "comparable store", "company-operated", "licensed", "systemwide",
            "restaurant-level", "operating margin", "America", "International",
            "same-store", "transactions", "ticket",
        ],
        "marriott": [
            "RevPAR", "ADR", "occupancy", "gross fee", "franchise", "management fee",
            "owned", "leased", "incentive", "rooms", "constant currency",
        ],
    }
    kpi = {}
    for key, terms in filing_terms.items():
        path = RAW / f"{key}_10k.txt"
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        # split roughly into pages by form feed or just search whole
        hits = {}
        for term in terms:
            rx = re.compile(re.escape(term), re.I)
            found = []
            for m in rx.finditer(text):
                start = max(0, m.start() - 120)
                end = min(len(text), m.end() + 220)
                snippet = re.sub(r"\s+", " ", text[start:end]).strip()
                found.append(snippet)
                if len(found) >= 6:
                    break
            hits[term] = found
        kpi[key] = hits
        # also extract tables-ish lines with $ and %
        money_lines = []
        for line in text.splitlines():
            if re.search(r"\$\s*[\d,]+|[\d\.]+\s*%", line) and re.search(
                r"sales|revenue|margin|inventory|RevPAR|ADR|occupancy|comparable|AWS|Wholesale|Direct",
                line,
                re.I,
            ):
                s = re.sub(r"\s+", " ", line).strip()
                if 20 < len(s) < 240:
                    money_lines.append(s)
                if len(money_lines) >= 120:
                    break
        (RAW / f"_{key}_money_lines.txt").write_text("\n".join(money_lines), encoding="utf-8")
    (RAW / "_kpi_keyword_hits.json").write_text(json.dumps(kpi, indent=2), encoding="utf-8")
    print("wrote kpi hits")


if __name__ == "__main__":
    main()
