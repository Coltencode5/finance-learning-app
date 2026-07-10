# Handoff Note — sector-energy

## 1. Module configuration
- **Title:** Energy (Sector)
- **Slug:** sector-energy
- **Kind:** sector-layer1
- **Expected build_order:** 14
- **Expected global start:** G304

## 2. Sources processed
- **Oil 101** (primary) — poor (first pages mostly empty — likely image-only or broken OCR layer)
- **The New Map: Energy, Climate, and the Clash of Nations** (primary) — partial (chapter map reconstructed from headings; page references approximate)
- **The World for Sale** (primary) — partial (chapter map reconstructed from headings; page references approximate)
- **How the World Really Works** (primary) — partial (chapter map reconstructed from headings; page references approximate)
- **The Economics of Oil and Gas** (secondary) — partial (chapter map reconstructed from headings; page references approximate)
- **Oil: A Beginner's Guide** (secondary) — partial (chapter map reconstructed from headings; page references approximate)
- **Energy: A Beginner's Guide** (secondary) — partial (chapter map reconstructed from headings; page references approximate)
- **Energy (Vaclav Smil)** (secondary) — partial (chapter map reconstructed from headings; page references approximate)
- **Oil Company Crisis: Managing Structure, Profitability and Growth** (primary-adjacent) — partial (OIES monograph (not Valuing Oil and Gas Companies); TOC/structure from headings; Not the full book Valuing Oil and Gas Companies; this is the 2003 OIES monograph by the same authors. Flagged separately from the missing book.)
- **Valuation of International Oil Companies (Osmundsen et al. 2006)** (secondary) — partial (short academic article; section map from headings)
- **Exxon Mobil Corporation Form 10-K (FY2025)** (primary) — clean
- **ConocoPhillips Form 10-K (FY2025)** (primary) — clean
- **SLB N.V. (SLB Limited) Form 10-K (FY2025)** (primary) — clean
- **Enterprise Products Partners L.P. Form 10-K (FY2025)** (primary) — clean
- **Valero Energy Corporation Form 10-K (FY2024)** (primary) — clean
- **Valuing Oil and Gas Companies** (primary) — not provided (Listed in SOURCE_FOLDER_OR_FILES as a primary book; full book not present in Downloads. A related OIES monograph by the same authors (Oil Company Crisis, SP15, 2003) WAS present and was extracted separately. Do not treat the monograph as a substitute for the missing book.)
- **The Prize: The Epic Quest for Oil, Money & Power** (primary) — not provided (Listed in SOURCE_FOLDER_OR_FILES; PDF not present in the provided Downloads set. The New Map (also by Yergin) was present and extracted.)

## 3. Sources needing human attention
- Oil 101: poor — first pages mostly empty — likely image-only or broken OCR layer
- The New Map: Energy, Climate, and the Clash of Nations: partial — chapter map reconstructed from headings; page references approximate
- The World for Sale: partial — chapter map reconstructed from headings; page references approximate
- How the World Really Works: partial — chapter map reconstructed from headings; page references approximate
- The Economics of Oil and Gas: partial — chapter map reconstructed from headings; page references approximate
- Oil: A Beginner's Guide: partial — chapter map reconstructed from headings; page references approximate
- Energy: A Beginner's Guide: partial — chapter map reconstructed from headings; page references approximate
- Energy (Vaclav Smil): partial — chapter map reconstructed from headings; page references approximate
- Oil Company Crisis: Managing Structure, Profitability and Growth: partial — OIES monograph (not Valuing Oil and Gas Companies); TOC/structure from headings; Not the full book Valuing Oil and Gas Companies; this is the 2003 OIES monograph by the same authors. Flagged separately from the missing book.
- Valuation of International Oil Companies (Osmundsen et al. 2006): partial — short academic article; section map from headings
- Valuing Oil and Gas Companies: not provided — Listed in SOURCE_FOLDER_OR_FILES as a primary book; full book not present in Downloads. A related OIES monograph by the same authors (Oil Company Crisis, SP15, 2003) WAS present and was extracted separately. Do not treat the monograph as a substitute for the missing book.
- The Prize: The Epic Quest for Oil, Money & Power: not provided — Listed in SOURCE_FOLDER_OR_FILES; PDF not present in the provided Downloads set. The New Map (also by Yergin) was present and extracted.

**Explicit flag:** *Valuing Oil and Gas Companies* (Nick Antill & Robert Arnott) was **not present**. A related OIES monograph by the same authors (*Oil Company Crisis*, SP15, 2003) was present and extracted separately — not treated as a substitute.
**Explicit flag:** *The Prize* (Daniel Yergin) was listed in the prompt source list but was **not present** in Downloads. *The New Map* (also Yergin) was extracted.

## 4. Dossier files
- `Source_Manifest.md` — per-source metadata, extraction status, heading-level coverage
- `TOC_Index.md` — detected or reconstructed tables of contents / chapter maps
- `Chapter_Summaries.md` — chapter/section entries with named topics and nearby source text
- `Concept_Inventory.csv` — mechanical term inventory with corpus string matches only
- `Handoff_Note.md` — this file
- `raw_extractions/` — plain-text dumps (truncated) for architect reference

## 5. Concept inventory row count
164

## 6. Repo-state facts (read-only inspection)
- Active modules: 13
- Draft modules: 0
- Global count/range: 303 (G1–G303)
- Next available global ID: G304
- Module kinds in use: asset-class, core-concept, role, sector-layer1
- Five-zone convention: each module has zones z1–z5 with front-door nodes; node fields include id, title, tag, quick_definition, explainer_covers, connects_to, gaps
- Gap-metadata: structured `gaps` arrays on nodes (observed in existing sector modules)
- Cross-module reference/back-link conventions: `connects_to` with module.zone.node refs; `appears_in` / `home_of` on globals
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
| sector-information-technology | sector-layer1 | 13 |

## 6b. Configuration notes recorded (factual flags only — not resolved)
- Tier A sector (D2 in docs/SECTOR_LAYER_DESIGN.md): full dossier expected.
- Compact module target per ADR-003 rule 6: 8–14 nodes (architect session decides final count).
- Dense upstream/valuation vocabulary flagged in prompt for capture: reserves (proved/probable), DD&A, successful-efforts vs full-cost, reserve replacement ratio, PV-10, netbacks, F&D cost, EV/boe, EV/production — string-matched into inventory only.
- Segment vocabulary flagged: upstream / midstream / downstream / oilfield services / integrated major; crack spread; MLP; OPEC/OPEC+; WTI/Brent; energy transition / decarbonization / stranded assets.
- Name-match note (mechanical): glossary partnership-family (G20 LPA, G216 venture partnership, G225 sponsor & JV) and cycle entries (G127, G232, G237, G255) — recorded in `also_appears_as_corpus_term` where string-matched; no reuse judgment.
- GICS Energy boundary (fossil-fuel-centric; renewables often elsewhere) — capture only if a source states it; no editorializing.
- Additional Downloads present beyond prompt list (Smil Energy titles, Mu textbook, Osmundsen article, Antill/Arnott OIES monograph) were extracted and labeled as not-in-config-list where applicable.
- Workspace note: Cursor workspace path was `finance-graph` (empty); dossier written to the live app repo at `OneDrive/finance-learning-app` where prior sector dossiers live.

## 7. Architecture deferral
**No architecture decisions, zone spines, global-reuse calls, or disambiguation judgments have been made. All of that is deferred to the architecture session.**
