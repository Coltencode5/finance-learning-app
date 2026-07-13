#!/usr/bin/env python3
"""Extract disclosed KPI snippets from FY2025 10-K text dumps."""
from __future__ import annotations

import re
from pathlib import Path

RAW = Path(__file__).resolve().parents[1] / "raw_extractions"


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def contexts(text: str, patterns: list[str], window: int = 350, limit: int = 8) -> list[str]:
    out = []
    for pat in patterns:
        for m in re.finditer(pat, text, re.I):
            start = max(0, m.start() - window)
            end = min(len(text), m.end() + window)
            snip = norm(text[start:end])
            if snip not in out:
                out.append(snip)
            if len(out) >= limit:
                return out
    return out


def main():
    specs = {
        "amazon": [
            r"Online stores",
            r"Third-party seller services",
            r"Advertising services",
            r"Subscription services",
            r"AWS",
            r"fulfillment",
            r"operating income",
            r"Net sales",
            r"North America",
            r"segment",
        ],
        "nike": [
            r"NIKE Direct",
            r"Wholesale",
            r"Gross margin",
            r"Inventories",
            r"inventory days",
            r"Revenues",
            r"Converse",
            r"Direct to Consumer",
        ],
        "starbucks": [
            r"comparable store sales",
            r"Company-operated",
            r"Licensed stores",
            r"systemwide",
            r"operating margin",
            r"Net revenues",
            r"transaction",
            r"ticket",
            r"America",
        ],
        "marriott": [
            r"RevPAR",
            r"Average Daily Rate",
            r"ADR",
            r"Occupancy",
            r"franchise fees",
            r"management fees",
            r"incentive management",
            r"owned",
            r"fee revenue",
            r"gross fee revenues",
        ],
    }
    for key, pats in specs.items():
        text = (RAW / f"{key}_10k.txt").read_text(encoding="utf-8", errors="replace")
        # collapse whitespace for searchability but keep large
        flat = norm(text)
        hits = contexts(flat, pats, window=280, limit=40)
        out = RAW / f"_{key}_kpi_contexts.txt"
        out.write_text("\n\n----\n\n".join(hits), encoding="utf-8")
        print(key, "contexts", len(hits), "chars", len(flat))

        # pull likely numeric disclosure sentences
        nums = []
        for m in re.finditer(
            r".{0,80}(?:\$\s*[\d,\.]+|\d+\.\d+\s*%|\d{1,3}(?:\,\d{3})+).{0,120}",
            flat,
        ):
            s = norm(m.group(0))
            if re.search(
                r"sales|revenue|margin|inventory|RevPAR|occupancy|comparable|AWS|Wholesale|Direct|fee|fulfillment|stores",
                s,
                re.I,
            ):
                nums.append(s)
            if len(nums) >= 150:
                break
        (RAW / f"_{key}_numeric_windows.txt").write_text("\n".join(nums), encoding="utf-8")
        print(" ", "numeric windows", len(nums))


if __name__ == "__main__":
    main()
