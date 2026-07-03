# Project Status

**Last updated:** Milestone 8 complete (2026-07-03)

## Corpus totals (validated)

| Metric | Value |
|---|---|
| Active modules | **11** |
| Shared globals | **285** (G1–G285, contiguous) |
| Zone nodes | **580** |
| Graph edges | **4,091** |
| Validation (`--strict`) | **0 errors, 0 warnings** |

## Milestones

| # | Module | Slug | Kind | build_order | Nodes | Globals | Status |
|---|---|---|---|---|---|---|---|
| 1–9 | Role modules (PE → RE) | various | role | 1–9 | 478 | G1–G235 | complete |
| 6 | Macro & Economics | macro-economics | core-concept | 10 | 51 | G236–G263 | complete |
| **7** | **Fixed Income** | **fixed-income** | **asset-class** | **11** | **51** | **G264–G285** | **complete** |

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

- Next module: **sector-financials** (M9, `kind: sector-layer1`, `build_order: 12`, globals from **G286**)
- Blocked on Tier A source acquisition (see `docs/SECTOR_LAYER_DESIGN.md` D2–D3)
- Wave one build order: Financials → IT → Energy → Consumer Discretionary

## Known defects (unchanged)

- 26 pre-existing globals (G1–G263) have multiple `home_of` edges — logged; not worsened by M7/M8
