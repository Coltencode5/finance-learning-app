# Handoff Note — sector-information-technology

## 1. Module configuration
- **Title:** Information Technology (Sector)
- **Slug:** sector-information-technology
- **Kind:** sector-layer1
- **Expected build_order:** 13
- **Expected global start:** G293

## 2. Sources processed
- **The Business of Platforms** (primary) — partial (OceanofPDF copy: Contents page detected but dot-leader page numbers absent; chapter headings reconstructed from inline text; figure/table caption lines mixed into heading map; page references approximate.)
- **Subscribed** (primary) — partial (OceanofPDF copy: no dot-leader TOC; chapter titles split across lines (e.g. 'CHAPTER 1' / 'THE END OF AN ERA'); front-matter headings duplicated; page references approximate.)
- **Chip War** (primary) — partial (OceanofPDF copy: chapter numbers extracted without chapter titles on same line; promotional 'CLICK HERE TO SIGN UP' debris in heading map; no reliable dot-leader TOC; page references approximate.)
- **Investment Valuation (University Edition)** (primary) — partial (OceanofPDF copy: Contents label detected but chapter list uses inline headings without dot leaders; very large page count increases offset-based page-reference uncertainty for concept locations.)
- **Platform Revolution** (secondary) — partial (OceanofPDF copy: cover/title-page text captured as headings; chapter takeaways and section labels duplicated; no dot-leader TOC; page references approximate.)
- **Lean Analytics** (secondary) — partial (OceanofPDF copy: spaced-letter chapter labels (e.g. 'C H A P T E R 1'); duplicate part/chapter headings from layout reflow; ISBN lines in heading map; no dot-leader TOC; page references approximate.)
- **Accenture plc Form 10-K (FY2025)** (add-on) — clean
- **Palo Alto Networks Form 10-K (FY2025)** (add-on) — clean
- **ServiceNow Form 10-K (FY2025)** (add-on) — clean
- **CrowdStrike Holdings Form 10-K (FY2025)** (add-on) — clean
- **The Software Paradox** (secondary) — not provided (file not in user-supplied folder)
- **Apple Inc. Form 10-K** (add-on) — not provided (file not in user-supplied folder)

## 3. Sources needing human attention
- The Business of Platforms: partial — OceanofPDF copy: Contents page detected but dot-leader page numbers absent; chapter headings reconstructed from inline text; figure/table caption lines mixed into heading map; page references approximate.
- Subscribed: partial — OceanofPDF copy: no dot-leader TOC; chapter titles split across lines (e.g. 'CHAPTER 1' / 'THE END OF AN ERA'); front-matter headings duplicated; page references approximate.
- Chip War: partial — OceanofPDF copy: chapter numbers extracted without chapter titles on same line; promotional 'CLICK HERE TO SIGN UP' debris in heading map; no reliable dot-leader TOC; page references approximate.
- Investment Valuation (University Edition): partial — OceanofPDF copy: Contents label detected but chapter list uses inline headings without dot leaders; very large page count increases offset-based page-reference uncertainty for concept locations.
- Platform Revolution: partial — OceanofPDF copy: cover/title-page text captured as headings; chapter takeaways and section labels duplicated; no dot-leader TOC; page references approximate.
- Lean Analytics: partial — OceanofPDF copy: spaced-letter chapter labels (e.g. 'C H A P T E R 1'); duplicate part/chapter headings from layout reflow; ISBN lines in heading map; no dot-leader TOC; page references approximate.
- The Software Paradox: not provided — file not in user-supplied folder
- Apple Inc. Form 10-K: not provided — file not in user-supplied folder

## 4. Dossier files
- `Source_Manifest.md` — per-source metadata, extraction status, heading-level coverage
- `TOC_Index.md` — detected or reconstructed tables of contents / chapter maps
- `Chapter_Summaries.md` — chapter/section entries with named topics and nearby source text
- `Concept_Inventory.csv` — mechanical term inventory with corpus string matches only
- `Handoff_Note.md` — this file
- `raw_extractions/` — plain-text dumps (truncated) for architect reference

## 5. Concept inventory row count
72

## 6. Repo-state facts (read-only inspection)
- Active modules: 12
- Draft modules: 0
- Global count/range: 292 (G1–G292)
- Next available global ID: G293
- Module kinds in use: asset-class, core-concept, role, sector-layer1
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
| sector-financials | sector-layer1 | 12 |

## 6b. Configuration notes recorded (factual flags only — not resolved)
- Tier B / light source-grounding sector per extraction config — dossier supports architecture session, not a comprehensive tech industry textbook.
- Compact module target per ADR-003 rule 6: 8–14 nodes (architect session decides final count).
- Corpus overlap zones flagged for name-matching in `Concept_Inventory.csv` (no reuse/new-global judgment made): equity-research (sector analysis, valuation, multiples); fixed-income (credit spreads, capital structure); macro-economics (rates, inflation, business cycles, AI capex if source-grounded); venture-capital (burn, PMF, scaling); private-equity (buyouts, recurring revenue, leverage); asset-management (benchmark/exposure lens); investment-banking (M&A, issuance, capital markets).
- Known disambiguation/name-match risks flagged in config, not resolved: platform vs SaaS; software vs IT services; software vs semiconductors; semiconductors vs hardware/devices; ARR vs revenue; gross retention vs NRR; churn variants; gross margin vs contribution margin; usage-based vs seat-based pricing; capex-light software vs capex-heavy fabs; valuation multiple vs intrinsic value; AI hype vs durable economics.
- **The Software Paradox** (Stephen O'Grady) was in the secondary source list but was **not provided** in the user folder.
- **Apple Inc. Form 10-K** was in the expected add-on list but was **not provided** in the user folder.

## 6c. Coverage_Limits
Mechanical hit/source coverage observations (not architecture judgments):

- **IT services:** covered by Accenture plc Form 10-K (FY2025) (49 hits), Palo Alto Networks Form 10-K (FY2025) (13 hits), ServiceNow Form 10-K (FY2025) (41 hits), CrowdStrike Holdings Form 10-K (FY2025) (66 hits); prior book-source mechanical hits: 64.
- **systems integration:** covered by Accenture plc Form 10-K (FY2025) (3 hits), Palo Alto Networks Form 10-K (FY2025) (1 hits), ServiceNow Form 10-K (FY2025) (5 hits), CrowdStrike Holdings Form 10-K (FY2025) (1 hits); prior book-source mechanical hits: 3.
- **managed services / outsourcing:** covered by Accenture plc Form 10-K (FY2025) (46 hits), ServiceNow Form 10-K (FY2025) (4 hits), CrowdStrike Holdings Form 10-K (FY2025) (3 hits); prior book-source mechanical hits: 21.
- **cybersecurity:** covered by Accenture plc Form 10-K (FY2025) (30 hits), Palo Alto Networks Form 10-K (FY2025) (129 hits), ServiceNow Form 10-K (FY2025) (39 hits), CrowdStrike Holdings Form 10-K (FY2025) (141 hits); prior book-source mechanical hits: 11.
- **enterprise software:** covered by Palo Alto Networks Form 10-K (FY2025) (2 hits), ServiceNow Form 10-K (FY2025) (8 hits), CrowdStrike Holdings Form 10-K (FY2025) (13 hits); prior book-source mechanical hits: 17.
- **hardware/devices:** Apple 10-K not in folder; incidental mentions in Accenture plc Form 10-K (FY2025) (9 incidental hits), Palo Alto Networks Form 10-K (FY2025) (61 incidental hits), ServiceNow Form 10-K (FY2025) (8 incidental hits), CrowdStrike Holdings Form 10-K (FY2025) (8 incidental hits); prior book-source mechanical hits: 377.
- **cloud infrastructure:** covered by Palo Alto Networks Form 10-K (FY2025) (14 hits), ServiceNow Form 10-K (FY2025) (24 hits), CrowdStrike Holdings Form 10-K (FY2025) (52 hits); prior book-source mechanical hits: 66.
- **semiconductors:** covered by Accenture plc Form 10-K (FY2025) (1 hits), CrowdStrike Holdings Form 10-K (FY2025) (2 hits); prior book-source mechanical hits: 1135.
- **SaaS/subscription:** covered by Palo Alto Networks Form 10-K (FY2025) (29 hits), ServiceNow Form 10-K (FY2025) (32 hits), CrowdStrike Holdings Form 10-K (FY2025) (59 hits); prior book-source mechanical hits: 250.
- **platform/ecosystem economics:** covered by CrowdStrike Holdings Form 10-K (FY2025) (3 hits); prior book-source mechanical hits: 616.
- **AI infrastructure:** covered by Accenture plc Form 10-K (FY2025) (81 hits), Palo Alto Networks Form 10-K (FY2025) (119 hits), ServiceNow Form 10-K (FY2025) (162 hits), CrowdStrike Holdings Form 10-K (FY2025) (131 hits); prior book-source mechanical hits: 210.

## 6d. Cleanup pass (2026-07-07)
- Concept inventory audited: removed index/OCR false positives and snippet fragments; rewrote definitions as short paraphrases.
- Chapter_Summaries.md compacted; long copyrighted excerpts removed.
- Local Windows file paths replaced with neutral filenames in committed dossier files.
- `raw_extractions/` remains gitignored and uncommitted.

## 7. Architecture deferral
No architecture decisions, zone spines, global-reuse calls, or disambiguation judgments have been made. All of that is deferred to the architecture session.
