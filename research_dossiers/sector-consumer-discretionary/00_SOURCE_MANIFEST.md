# 00 — Source Manifest — sector-consumer-discretionary

**Tier-B honesty convention (mirrors IT dossier):** This is a **business-history / practitioner-framework / filings** source set, not a technical treatise on retail operations research or auto engineering. Depth is strong on narrative mechanisms and disclosed KPIs; weak on formal industrial-organization models and on sub-industries without a dedicated source.

**Corpus state at extraction (live `validate.py --strict`):** 313 globals (G1–G313 contiguous) · 14 modules · 615 zone nodes · **0 errors / 0 warnings**.

---

## Books

### The Everything Store — Brad Stone
- **Expected title match:** yes
- **Author:** Brad Stone
- **Original uploaded filename:** `_OceanofPDF.com_The_Everything_Store__Jeff_Bezos_and_the_A_-_Brad_Stone.pdf`
- **Repo path:** `research_dossiers/sector-consumer-discretionary/_source_pdfs/The_Everything_Store_Brad_Stone.pdf`
- **Format:** PDF (OceanofPDF) · **351 pages**
- **Text layer:** **YES** (~719k chars)
- **Extracted:** Prologue + Chapters 1–11 → `01_EXTRACTS/everything_store.md`
- **Failed:** No standalone epilogue in dump (photos/notes/index only)
- **Load-bearing for:** E-commerce/broadline retail economics, marketplace, fulfillment, Prime, flywheel, Amazon platform/retail hybrid

### Trading Up — Michael J. Silverstein & Neil Fiske
- **Expected title match:** yes (co-author Fiske present in book; filename credits Silverstein)
- **Original uploaded filename:** `_OceanofPDF.com_Trading_Up_-_Michael_J_Silverstein.pdf`
- **Repo path:** `_source_pdfs/Trading_Up_Silverstein_Fiske.pdf`
- **Format:** PDF · **318 pages** · **Text layer YES** (~618k chars)
- **Extracted:** Preface through Ch. 13 + sources → `01_EXTRACTS/trading_up.md`
- **Failed:** Some figure pages thin/OCR empty; Ch. 5 TOC title truncated
- **Load-bearing for:** Premiumization, trade-up/trade-down, New Luxury, death-in-the-middle

### Different — Youngme Moon
- **Expected title match:** yes (*Different: Escaping the Competitive Herd*)
- **Original uploaded filename:** `_OceanofPDF.com_Different_-_Youngme_Moon.pdf`
- **Repo path:** `_source_pdfs/Different_Youngme_Moon.pdf`
- **Format:** PDF · **213 pages** · **Text layer YES** (~374k chars)
- **Extracted:** Full discursive sections → `01_EXTRACTS/different.md`
- **Failed:** Automated chapter map empty; boundaries reconstructed from TOC (flagged in extract)
- **Load-bearing for:** Brand differentiation, reverse/breakaway/hostile brands, category blur

### Resurrecting Retail — Doug Stephens
- **TITLE MISMATCH (flag loudly):** Prompt expected **“Reengineering Retail”**; uploaded file and book title are **Resurrecting Retail** (Doug Stephens, foreword Nov 2020).
- **Original uploaded filename:** `_OceanofPDF.com_Resurrecting_Retail_-_Doug_Stephens.pdf`
- **Repo path:** `_source_pdfs/Resurrecting_Retail_Doug_Stephens.pdf`
- **Format:** PDF · **302 pages** · **Text layer YES** (~478k chars)
- **Extracted:** Foreword through closing essay → `01_EXTRACTS/resurrecting_retail.md`
- **Failed:** Exact end-pages approximate where next chapter starts; Notes/Index not analyzed as content
- **Load-bearing for:** Omnichannel/post-digital retail transition, apex predators, store-as-media, mall reincarnation, retail archetypes

### Investment Valuation (University Edition) — Aswath Damodaran
- **Expected title match:** yes
- **Original uploaded filename:** `_OceanofPDF.com_Investment_Valuation_University_Edition_-_Aswath_Damodaran.pdf`
- **Repo path:** `_source_pdfs/Investment_Valuation_Damodaran.pdf`
- **Format:** PDF · **1331 pages** · **Text layer YES**
- **Extraction approach:** **REUSED from M10 IT dossier** (not re-extracted chapter-by-chapter). Pointer file: `01_EXTRACTS/investment_valuation.md`
- **Load-bearing for:** Multiples / relative valuation toolkit supporting CD analysis (not operating KPIs)

### Ludicrous — Edward Niedermeyer *(follow-up add)*
- **Expected in original upload list:** **no** — added in follow-up to cover Automobiles
- **Original uploaded filename:** `_OceanofPDF.com_Ludicrous_-_Edward_Niedermeyer.pdf`
- **Repo path:** `_source_pdfs/Ludicrous_Edward_Niedermeyer.pdf`
- **Format:** PDF · **265 pages** · **Text layer YES** (~573k chars)
- **Extracted:** Intro + Chapters 1–17 → `01_EXTRACTS/ludicrous.md`
- **Failed / thin:** Systematic ICE OEM economics; full dealer-franchise P&L; captive finance; post-2019 facts
- **Load-bearing for:** EV/Tesla economics, manufacturing difficulty, vertical integration/Gigafactory, Autopilot/Supercharger/swap adjuncts, capital & hype loops; **partial** direct-sales vs dealer conflict

---

## Filings (SEC EDGAR — fetched, not user-uploaded)

| Company | Role | Form | Report date | Filing date | Accession | Local | Source URL |
|---|---|---|---|---|---|---|---|
| Amazon.com, Inc. (AMZN) | Broadline / e-commerce | 10-K | 2025-12-31 | 2026-02-06 | 0001018724-26-000004 | `_source_filings/amazon_10k_…htm` + `raw_extractions/amazon_10k.txt` | https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm |
| NIKE, Inc. (NKE) | Apparel & durables | 10-K | 2025-05-31 | 2025-07-17 | 0000320187-25-000047 | `_source_filings/nike_10k_…htm` + `nike_10k.txt` | https://www.sec.gov/Archives/edgar/data/320187/000032018725000047/nke-20250531.htm |
| Starbucks Corporation (SBUX) | Restaurants / consumer services | 10-K | 2025-09-28 | 2025-11-14 | 0000829224-25-000114 | `_source_filings/starbucks_10k_…htm` + `starbucks_10k.txt` | https://www.sec.gov/Archives/edgar/data/829224/000082922425000114/sbux-20250928.htm |
| Marriott International, Inc. (MAR) | Hotels / travel | 10-K | 2025-12-31 | 2026-02-10 | 0001048286-26-000007 | `_source_filings/marriott_10k_…htm` + `marriott_10k.txt` | https://www.sec.gov/Archives/edgar/data/1048286/000104828626000007/mar-20251231.htm |

**Alternates not used:** McDonald’s (restaurants) — Starbucks obtained; Booking Holdings (travel) — Marriott obtained.

**Missing expected uploads:** none from the five-book original list (Stephens title string differs as flagged). Ludicrous was a later add, not an original omission.

**Manifest of filing fetch:** `_source_filings/_filing_manifest.json`
