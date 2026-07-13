#!/usr/bin/env python3
"""Pull key FY2025 KPI disclosures from flat 10-K text."""
from __future__ import annotations

import re
from pathlib import Path

RAW = Path(__file__).resolve().parents[1] / "raw_extractions"
OUT = Path(__file__).resolve().parents[1] / "_kpi_pulls.md"


def flat(path: Path) -> str:
    return re.sub(r"\s+", " ", path.read_text(encoding="utf-8", errors="replace"))


def around(text: str, pat: str, n: int = 400) -> list[str]:
    out = []
    for m in re.finditer(pat, text, re.I):
        s = text[max(0, m.start() - 80) : min(len(text), m.end() + n)]
        out.append(s.strip())
        if len(out) >= 5:
            break
    return out


def main():
    sections = []
    amz = flat(RAW / "amazon_10k.txt")
    sections.append("## Amazon")
    for label, pat in [
        ("net sales / segments", r"Net Sales:\s*North America.{0,400}"),
        ("operating income segments", r"Operating Income\s*North America.{0,350}"),
        ("fulfillment", r"Fulfillment\s+[\d,\.]+\s+[\d,\.]+.{0,200}"),
        ("shipping costs", r"Shipping costs were.{0,200}"),
        ("product/service sales", r"Net product sales\s*\$?.{0,250}"),
        ("online stores / 3P / ads", r"Online stores.{0,500}"),
        ("subscription", r"Subscription services.{0,300}"),
        ("advertising", r"Advertising services.{0,300}"),
        ("third-party", r"Third-party seller services.{0,300}"),
    ]:
        hits = around(amz, pat, 500)
        sections.append(f"### {label}")
        sections.extend(hits or ["NO HIT"])

    nke = flat(RAW / "nike_10k.txt")
    sections.append("\n## Nike")
    for label, pat in [
        ("highlights", r"FISCAL 2025 FINANCIAL HIGHLIGHTS.{0,900}"),
        ("wholesale/direct", r"NIKE Direct revenues.{0,500}"),
        ("gross margin", r"Gross margin decreased.{0,300}"),
        ("inventories BS", r"Inventories\s*\$?.{0,200}"),
        ("revenues line", r"Revenues\s*\$\s*46,309.{0,200}"),
        ("channel mix", r"Wholesale.{0,400}"),
    ]:
        hits = around(nke, pat, 600)
        sections.append(f"### {label}")
        sections.extend(hits or ["NO HIT"])

    sbux = flat(RAW / "starbucks_10k.txt")
    sections.append("\n## Starbucks")
    for label, pat in [
        ("comparable", r"comparable store sales.{0,500}"),
        ("company-operated", r"Company-operated stores.{0,400}"),
        ("licensed", r"Licensed stores.{0,300}"),
        ("net revenues", r"Total net revenues.{0,300}"),
        ("America comps", r"decline in comparable store sales.{0,400}"),
        ("transactions/ticket", r"comparable transactions.{0,300}"),
        ("operating margin", r"Operating margin.{0,300}"),
        ("store counts", r"company-operated store.{0,300}"),
    ]:
        hits = around(sbux, pat, 500)
        sections.append(f"### {label}")
        sections.extend(hits or ["NO HIT"])

    mar = flat(RAW / "marriott_10k.txt")
    sections.append("\n## Marriott")
    for label, pat in [
        ("RevPAR table", r"worldwide RevPAR.{0,200}"),
        ("comparable company-operated", r"Comparable Company-Operated Properties.{0,600}"),
        ("fee revenues", r"Franchise fees\s*\$\s*3,325.{0,500}"),
        ("gross fee", r"Gross fee revenues.{0,300}"),
        ("owned leased", r"Owned, leased, and other revenue.{0,300}"),
        ("occupancy ADR", r"U\.S\. \& Canada\s*\$\s*185\.78.{0,400}"),
        ("systemwide", r"Comparable Systemwide Properties.{0,500}"),
    ]:
        hits = around(mar, pat, 600)
        sections.append(f"### {label}")
        sections.extend(hits or ["NO HIT"])

    OUT.write_text("\n\n".join(sections), encoding="utf-8")
    print("wrote", OUT, "chars", OUT.stat().st_size)


if __name__ == "__main__":
    main()
