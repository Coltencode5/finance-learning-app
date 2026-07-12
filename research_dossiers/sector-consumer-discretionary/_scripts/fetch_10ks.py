#!/usr/bin/env python3
"""Fetch FY2025 Form 10-K filings from SEC EDGAR for CD dossier companies."""
from __future__ import annotations

import json
import re
import time
import urllib.request
from pathlib import Path

DOSSIER = Path(__file__).resolve().parents[1]
RAW = DOSSIER / "raw_extractions"
FILINGS = DOSSIER / "_source_filings"
RAW.mkdir(exist_ok=True)
FILINGS.mkdir(exist_ok=True)

UA = "FinanceLearningApp/1.0 (research dossier; contact: research@example.com)"
HEADERS = {"User-Agent": UA, "Accept": "application/json,text/html,*/*"}

# Prefer these tickers; alternates noted in prompt
TARGETS = [
    {"key": "amazon", "ticker": "AMZN", "cik": "0001018724", "name": "Amazon.com, Inc."},
    {"key": "nike", "ticker": "NKE", "cik": "0000320187", "name": "NIKE, Inc."},
    {"key": "starbucks", "ticker": "SBUX", "cik": "0000829224", "name": "Starbucks Corporation",
     "alt": {"key": "mcdonalds", "ticker": "MCD", "cik": "0000063908", "name": "McDonald's Corporation"}},
    {"key": "marriott", "ticker": "MAR", "cik": "0001048286", "name": "Marriott International, Inc.",
     "alt": {"key": "booking", "ticker": "BKNG", "cik": "0001075531", "name": "Booking Holdings Inc."}},
]


def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=90) as resp:
        data = resp.read()
        # urllib may auto-decompress gzip
        return data


def submissions(cik: str) -> dict:
    url = f"https://data.sec.gov/submissions/CIK{cik}.json"
    return json.loads(get(url).decode("utf-8"))


def pick_fy2025_10k(sub: dict) -> dict | None:
    recent = sub.get("filings", {}).get("recent", {})
    forms = recent.get("form", [])
    dates = recent.get("filingDate", [])
    reports = recent.get("reportDate", [])
    accessions = recent.get("accessionNumber", [])
    primaries = recent.get("primaryDocument", [])
    best = None
    for i, form in enumerate(forms):
        if form not in ("10-K", "10-K/A"):
            continue
        filing_date = dates[i]
        report_date = reports[i] if i < len(reports) else ""
        # FY2025: report date in 2025, or fiscal year ending in 2025 / early 2026 for Dec YE
        year = int(report_date[:4]) if report_date else int(filing_date[:4])
        if year not in (2025, 2026):
            continue
        # Prefer report dates in calendar 2025, or early 2026 filings for YE2025
        score = 0
        if report_date.startswith("2025"):
            score += 10
        if filing_date.startswith("2026") or filing_date.startswith("2025"):
            score += 3
        if form == "10-K":
            score += 2
        # Nike FY ends May — FY2025 is YE 2025-05-31
        # Starbucks FY ends ~Sept — FY2025 is YE 2025-09
        cand = {
            "form": form,
            "filingDate": filing_date,
            "reportDate": report_date,
            "accessionNumber": accessions[i],
            "primaryDocument": primaries[i],
            "score": score,
        }
        if best is None or cand["score"] > best["score"] or (
            cand["score"] == best["score"] and cand["reportDate"] > best["reportDate"]
        ):
            best = cand
    return best


def download_primary(cik: str, acc: str, primary: str, dest: Path) -> Path:
    acc_nodash = acc.replace("-", "")
    cik_int = str(int(cik))
    url = f"https://www.sec.gov/Archives/edgar/data/{cik_int}/{acc_nodash}/{primary}"
    data = get(url)
    dest.write_bytes(data)
    return dest


def html_to_text(html: bytes) -> str:
    try:
        text = html.decode("utf-8")
    except UnicodeDecodeError:
        text = html.decode("latin-1", errors="replace")
    # crude strip
    text = re.sub(r"(?is)<script[^>]*>.*?</script>", " ", text)
    text = re.sub(r"(?is)<style[^>]*>.*?</style>", " ", text)
    text = re.sub(r"(?is)<[^>]+>", " ", text)
    text = re.sub(r"&nbsp;", " ", text)
    text = re.sub(r"&amp;", "&", text)
    text = re.sub(r"&#\d+;", " ", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def process_target(t: dict) -> dict:
    result = {"requested": t, "status": "pending"}
    try:
        sub = submissions(t["cik"])
        time.sleep(0.25)
        pick = pick_fy2025_10k(sub)
        if not pick and t.get("alt"):
            alt = t["alt"]
            sub = submissions(alt["cik"])
            time.sleep(0.25)
            pick = pick_fy2025_10k(sub)
            if pick:
                t = {**alt, "chosen_as_alt_for": result["requested"]["ticker"]}
        if not pick:
            result["status"] = "missing"
            result["error"] = "No FY2025 10-K found in recent filings"
            return result
        dest_name = f"{t['key']}_10k_{pick['reportDate']}_{pick['accessionNumber']}"
        primary = pick["primaryDocument"]
        suffix = Path(primary).suffix or ".htm"
        bin_path = FILINGS / f"{dest_name}{suffix}"
        download_primary(t["cik"], pick["accessionNumber"], primary, bin_path)
        time.sleep(0.25)
        text = html_to_text(bin_path.read_bytes())
        txt_path = RAW / f"{t['key']}_10k.txt"
        # keep manageable size
        txt_path.write_text(text[:2_500_000], encoding="utf-8")
        result.update(
            {
                "status": "ok",
                "company": t.get("name"),
                "ticker": t.get("ticker"),
                "cik": t.get("cik"),
                "form": pick["form"],
                "filingDate": pick["filingDate"],
                "reportDate": pick["reportDate"],
                "accessionNumber": pick["accessionNumber"],
                "primaryDocument": primary,
                "local_binary": str(bin_path.relative_to(DOSSIER)),
                "local_text": str(txt_path.relative_to(DOSSIER)),
                "text_chars": len(text),
                "source_url": (
                    f"https://www.sec.gov/Archives/edgar/data/{int(t['cik'])}/"
                    f"{pick['accessionNumber'].replace('-', '')}/{primary}"
                ),
                "chosen_as_alt_for": t.get("chosen_as_alt_for"),
            }
        )
    except Exception as e:
        result["status"] = "error"
        result["error"] = repr(e)
    return result


def main() -> None:
    results = []
    for t in TARGETS:
        print("fetching", t["ticker"], "...")
        r = process_target(t)
        results.append(r)
        print(" ", r["status"], r.get("reportDate"), r.get("accessionNumber"), r.get("error", ""))
    out = FILINGS / "_filing_manifest.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print("wrote", out)


if __name__ == "__main__":
    main()
