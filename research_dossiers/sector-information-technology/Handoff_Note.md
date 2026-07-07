# Handoff Note — sector-information-technology

## 1. Module configuration
- **Title:** Information Technology (Sector)
- **Slug:** sector-information-technology
- **Kind:** sector-layer1
- **Expected build_order:** 13
- **Expected global start:** G293

## 2. Sources processed
- **The Business of Platforms** (primary) — partial (TOC not cleanly detected; chapter map reconstructed from headings)
- **Subscribed** (primary) — partial (TOC not cleanly detected; chapter map reconstructed from headings)
- **Chip War** (primary) — partial (TOC not cleanly detected; chapter map reconstructed from headings)
- **Investment Valuation (University Edition)** (primary) — partial (TOC not cleanly detected; chapter map reconstructed from headings)
- **Platform Revolution** (secondary) — partial (TOC not cleanly detected; chapter map reconstructed from headings)
- **Lean Analytics** (secondary) — partial (TOC not cleanly detected; chapter map reconstructed from headings)
- **The Software Paradox** (secondary) — not provided (file not in user-supplied folder)

## 3. Sources needing human attention
- The Business of Platforms: partial — TOC not cleanly detected; chapter map reconstructed from headings
- Subscribed: partial — TOC not cleanly detected; chapter map reconstructed from headings
- Chip War: partial — TOC not cleanly detected; chapter map reconstructed from headings
- Investment Valuation (University Edition): partial — TOC not cleanly detected; chapter map reconstructed from headings
- Platform Revolution: partial — TOC not cleanly detected; chapter map reconstructed from headings
- Lean Analytics: partial — TOC not cleanly detected; chapter map reconstructed from headings
- The Software Paradox: not provided — file not in user-supplied folder

## 4. Dossier files
- `Source_Manifest.md` — per-source metadata, extraction status, heading-level coverage
- `TOC_Index.md` — detected or reconstructed tables of contents / chapter maps
- `Chapter_Summaries.md` — chapter/section entries with named topics and nearby source text
- `Concept_Inventory.csv` — mechanical term inventory with corpus string matches only
- `Handoff_Note.md` — this file
- `raw_extractions/` — plain-text dumps (truncated) for architect reference

## 5. Concept inventory row count
68

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
- Thin coverage signals (mechanical occurrence counts across all readable sources):
  - IT services: 0 occurrences across all readable sources
  - systems integrat: 1 occurrences across all readable sources

## 7. Architecture deferral
**No architecture decisions, zone spines, global-reuse calls, or disambiguation judgments have been made. All of that is deferred to the architecture session.**
