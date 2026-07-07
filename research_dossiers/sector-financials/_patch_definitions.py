#!/usr/bin/env python3
"""Re-patch short_definition column in Concept_Inventory.csv using improved heuristics."""
from __future__ import annotations

import csv
import sys
from pathlib import Path

DOSSIER = Path(__file__).resolve().parent
sys.path.insert(0, str(DOSSIER))
from _dossier_utils import definition_snippets  # noqa: E402

RAW = DOSSIER / "raw_extractions"

# Map source_titles substrings to raw extraction files
SOURCE_FILES: dict[str, str] = {
    "The Bankers' New Clothes": "bankers_new_clothes.txt",
    "Handbook of Basel III Capital": "basel_iii.txt",
    "The Dark Side of Valuation": "dark_side_valuation.txt",
    "Competition Demystified": "competition_demystified.txt",
    "Expectations Investing": "expectations_investing.txt",
    "Common Stocks and Uncommon Profits and Other Writings (alt file)": "fisher_writings.txt",
    "Common Stocks and Uncommon Profits and Other Writings": "fisher_csuop.txt",
    "Paths to Wealth Through Common Stocks": "fisher_paths.txt",
    "The Bank Credit Analysis Handbook": "golin_ch3.txt",  # default; all golin merged below
}

TEXT_CACHE: dict[str, str] = {}


def load_texts() -> None:
    for path in RAW.glob("*.txt"):
        TEXT_CACHE[path.stem] = path.read_text(encoding="utf-8")
    # Combined Golin text for handbook title lookups
    golin = ""
    for key in ("golin_ch3", "golin_ch4", "golin_ch9"):
        golin += TEXT_CACHE.get(key, "") + "\n"
    TEXT_CACHE["golin_combined"] = golin


def texts_for_source_titles(source_titles: str) -> str:
    blob = ""
    for title in [t.strip() for t in source_titles.split("|")]:
        if not title:
            continue
        if "Bank Credit Analysis Handbook" in title:
            blob += TEXT_CACHE.get("golin_combined", "")
            continue
        for key, fname in SOURCE_FILES.items():
            if key in title:
                stem = Path(fname).stem
                blob += TEXT_CACHE.get(stem, "")
                break
    return blob


def main() -> None:
    load_texts()
    inv_path = DOSSIER / "Concept_Inventory.csv"
    rows = list(csv.DictReader(inv_path.open(encoding="utf-8")))
    changed = 0
    for row in rows:
        blob = texts_for_source_titles(row.get("source_titles", ""))
        if not blob:
            continue
        new_def = definition_snippets(blob, row["term"])
        if new_def and new_def != row.get("short_definition", ""):
            row["short_definition"] = new_def
            changed += 1
    with inv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)
    print(f"patched={changed} total={len(rows)}")


if __name__ == "__main__":
    main()
