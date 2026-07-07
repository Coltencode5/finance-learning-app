# Project Status

**Last updated:** Milestone 9 complete (2026-07-07)

## Corpus totals (validated)

| Metric | Value |
|---|---|
| Active modules | **12** |
| Shared globals | **292** (G1–G292, contiguous) |
| Zone nodes | **591** |
| Graph edges | **4,185** |
| Validation (`--strict`) | **0 errors, 0 warnings** |

## Milestones

| # | Module | Slug | Kind | build_order | Nodes | Globals | Status |
|---|---|---|---|---|---|---|---|
| 1–9 | Role modules (PE → RE) | various | role | 1–9 | 478 | G1–G235 | complete |
| 6 | Macro & Economics | macro-economics | core-concept | 10 | 51 | G236–G263 | complete |
| 7 | Fixed Income | fixed-income | asset-class | 11 | 51 | G264–G285 | complete |
| 8 | Sector Layer Prep | — | prep | — | — | — | complete |
| **9** | **Financials (Sector)** | **sector-financials** | **sector-layer1** | **12** | **11** | **G286–G292** | **complete** |

## Milestone 9 — Financials (Sector)

- **Slug:** `sector-financials`
- **Kind:** `sector-layer1` (ADR-003 rule 1)
- **Zones:** Z1 The Spread Business (2) · Z2 Three Businesses, One Sector (3) · Z3 What Drives the Firms (2) · Z4 Going Deeper: Analyzing One (2) · Z5 The Rules & the Fragility (2)
- **New globals:** G286–G292 (7 net-new; append-only; each with exactly one `home_of`)
- **Back-links:** 28 existing globals referenced; G69/G70/G277 disambiguate_with updated for G286/G288 pairs
- **Attachment edges:** Z1.1 ↔ `equity-research.z2.3` (bidirectional); Z4.2 → `fixed-income.z4.8` (FI deferral handshake completed)
- **Structured GAPs:** 2 (`insurance-source-depth` on Z2.2; `golin-ch7-not-extracted` on Z3.2)
- **Design ripple:** D7 (sector-module voice rule) added to `docs/SECTOR_LAYER_DESIGN.md`

## Milestone 8 — Sector Layer Prep

Prep milestone (no new module content authored):

- Removed `corporate-finance` draft placeholder (regenerable via factory; not in standing build sequence)
- ADR-003 pipeline consequences: sector spine placeholders in `scaffold_module.py`; extended placeholder-mismatch and sector compactness checks in `new_module_checks.py`
- ER Z2.3 → Real Estate back-links (GICS real-estate exclusion per sector design D1)
- Ratified standing reference: `docs/SECTOR_LAYER_DESIGN.md`

## Milestone 7 — Fixed Income

- **Slug:** `fixed-income`
- **Kind:** `asset-class` (ADR-003 ruling 3 — concept-progression spine)
- **Zones:** Z1 The Bond & Its Market (9) · Z2 Bond Math & the Curve (11) · Z3 The Instrument Universe (12) · Z4 Credit & Spread (9) · Z5 Trading, Financing & the Portfolio (10)
- **New globals:** G264–G285 (22 net-new; append-only; each with exactly one `home_of`)
- **Back-links:** 43 existing globals referenced; no G1–G263 entries modified
- **Disambiguation pairs (one-way on FI globals):** G265↔G58, G277↔G70, G276↔G77, G285↔G72, G269↔G248/G257
- **Seam:** FI Z1.8 ↔ Private Credit Z1.7

## Next gate

- Next module: **sector-information-technology** (M10, `kind: sector-layer1`, `build_order: 13`, globals from **G293**)
- M10 source dossier prepared at `research_dossiers/sector-information-technology/` (architecture session pending; not yet in `content/`)
- Wave one build order: IT → Energy → Consumer Discretionary

## Known defects (unchanged)

- 26 pre-existing globals (G1–G263) have multiple `home_of` edges — logged; not worsened by M7/M8/M9
