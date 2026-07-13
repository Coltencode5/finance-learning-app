#!/usr/bin/env python3
"""Probe text layers and dump chapter-oriented raw text for CD dossier books."""
from __future__ import annotations

import json
import re
from pathlib import Path

import fitz

DOSSIER = Path(__file__).resolve().parents[1]
PDF_DIR = DOSSIER / "_source_pdfs"
RAW = DOSSIER / "raw_extractions"
RAW.mkdir(exist_ok=True)

BOOKS = [
    ("everything_store", "The_Everything_Store_Brad_Stone.pdf"),
    ("resurrecting_retail", "Resurrecting_Retail_Doug_Stephens.pdf"),
    ("trading_up", "Trading_Up_Silverstein_Fiske.pdf"),
    ("different", "Different_Youngme_Moon.pdf"),
    ("investment_valuation", "Investment_Valuation_Damodaran.pdf"),
]


def probe(path: Path) -> dict:
    doc = fitz.open(path)
    n = doc.page_count
    samples = []
    nonempty = 0
    for i in [0, 1, min(5, n - 1), min(20, n - 1), min(50, n - 1), n // 2, n - 1]:
        if i < 0 or i >= n:
            continue
        t = doc[i].get_text("text") or ""
        samples.append({"page_index": i, "chars": len(t), "preview": t[:200].replace("\n", " ")})
        if len(t.strip()) > 40:
            nonempty += 1
    # full-book char count sample every 10th page for speed on Damodaran
    total_chars = 0
    pages_with_text = 0
    step = 1 if n < 400 else 5
    for i in range(0, n, step):
        t = doc[i].get_text("text") or ""
        total_chars += len(t)
        if len(t.strip()) > 40:
            pages_with_text += 1
    est_chars = int(total_chars * (step if step > 1 else 1))
    has_text = pages_with_text > max(3, n // (20 * step))
    # TOC-ish headings
    headings = []
    for i in range(min(40, n)):
        t = doc[i].get_text("text") or ""
        for line in t.splitlines():
            s = line.strip()
            if re.match(r"^(CHAPTER|Chapter|PART|Part)\b", s) and len(s) < 120:
                headings.append({"page_index": i, "line": s})
            elif re.match(r"^CHAPTER\s+\d+", s, re.I):
                headings.append({"page_index": i, "line": s})
    doc.close()
    return {
        "file": path.name,
        "pages": n,
        "has_text_layer": has_text,
        "pages_with_text_sampled": pages_with_text,
        "est_chars": est_chars,
        "samples": samples,
        "early_headings": headings[:80],
    }


def dump_book(key: str, path: Path, max_pages: int | None = None) -> Path:
    doc = fitz.open(path)
    out = RAW / f"{key}.txt"
    n = doc.page_count
    limit = n if max_pages is None else min(n, max_pages)
    parts = []
    for i in range(limit):
        t = doc[i].get_text("text") or ""
        parts.append(f"\n\n===== PAGE {i+1} / {n} =====\n{t}")
    out.write_text("".join(parts), encoding="utf-8")
    doc.close()
    return out


def main() -> None:
    report = []
    for key, name in BOOKS:
        path = PDF_DIR / name
        info = probe(path)
        report.append(info)
        # Damodaran is huge — dump first 120 pages + TOC region already covered; reuse IT raw for rest
        if key == "investment_valuation":
            dump_book(key, path, max_pages=80)
            # also dump chapters likely useful for retail: revenue multiples etc via page search later
        else:
            dump_book(key, path)
        print(f"{name}: pages={info['pages']} text_layer={info['has_text_layer']} est_chars~{info['est_chars']}")
    (RAW / "_probe_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("wrote", RAW / "_probe_report.json")


if __name__ == "__main__":
    main()
