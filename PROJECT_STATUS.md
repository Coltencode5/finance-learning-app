# Project Status

**Last updated:** Milestone 12 complete (2026-07-12)

## Corpus totals (validated)

| Metric | Value |
|---|---|
| Active modules | **15** |
| Shared globals | **322** (G1–G322, contiguous) |
| Zone nodes | **629** |
| Graph edges | **4,568** |
| Validation (`--strict`) | **0 errors, 0 warnings** |

## Milestones

| # | Module | Slug | Kind | build_order | Nodes | Globals | Status |
|---|---|---|---|---|---|---|---|
| 1–9 | Role modules (PE → RE) | various | role | 1–9 | 478 | G1–G235 | complete |
| 6 | Macro & Economics | macro-economics | core-concept | 10 | 51 | G236–G263 | complete |
| 7 | Fixed Income | fixed-income | asset-class | 11 | 51 | G264–G285 | complete |
| 8 | Sector Layer Prep | — | prep | — | — | — | complete |
| 9 | Financials (Sector) | sector-financials | sector-layer1 | 12 | 11 | G286–G292 | complete |
| 10 | Information Technology (Sector) | sector-information-technology | sector-layer1 | 13 | 11 | G293–G303 | complete |
| 11 | Energy (Sector) | sector-energy | sector-layer1 | 14 | 13 | G304–G313 | complete |
| **12** | **Consumer Discretionary (Sector)** | **sector-consumer-discretionary** | **sector-layer1** | **15** | **14** | **G314–G322** | **complete** |

## Milestone 12 — Consumer Discretionary (Sector)

- **Slug:** `sector-consumer-discretionary`
- **Kind:** `sector-layer1` (ADR-003 rule 1)
- **Zones:** Z1 Selling What Nobody Needs (2) · Z2 Four Ways to Sell a Want (4) · Z3 The Scoreboard & the Consumer's Head (4) · Z4 The Analyst's Layer (2) · Z5 The Cycle & the Store's Next Life (2)
- **New globals:** G314–G322 (9 net-new; append-only; each with exactly one `home_of`; no `hosts_globals`)
- **Disambiguation (approved only):** G318 → [G88, G89] hub-and-spoke (append G318 to each spoke; G88↔G89 remain unlinked); G317 ↔ G196 (franchise pair). **G31 left unchanged** — G319 connects via `connects_to` as a retail WC application, not `disambiguate_with`.
- **Attachment edges:** Z1.1 ↔ `equity-research.z2.3` (bidirectional, ER retailer forward-link bullet — wave one's fourth contrast closed); Z4.2 → `fixed-income.z4.8` (credit handshake — lease-adjusted & cycle-adjusted; whole-business securitization & retail ABL named); Z2.1 ↔ `sector-information-technology.z1.1` (Amazon boundary); Z5.2 ↔ `real-estate.z2.2` (storefront boundary); Z4.1 → Financials/IT/Energy Z4.1 (valuation dialect chain, accretive only)
- **Structured GAPs:** 4 (`ota-lodging-kpi-gap` on Z2.3; `auto-economics-source-thin` on Z2.4; `trading-up-era-data` on Z3.3; `retail-transition-recency` on Z5.2)
- **Design ripple:** none — `SECTOR_LAYER_DESIGN.md` unchanged. Moat (§G #16), operating leverage (§G #17), TAM (§G #18) remain OPEN. No generic flywheel/brand diaspora retrofit or resolution claim.
- **Wave one:** **closed.** Next gate: **G1**.

## Milestone 11 — Energy (Sector)


- **Slug:** `sector-energy`
- **Kind:** `sector-layer1` (ADR-003 rule 1)
- **Zones:** Z1 Powering Everything, Pricing Nothing (2) · Z2 Four Businesses Along One Barrel's Journey (4) · Z3 The Price, the Cycle & the Cartel (3) · Z4 Going Deeper: Analyzing One (2) · Z5 The State, the Sunset & the New Map (2)
- **New globals:** G304–G313 (10 net-new; append-only; each with exactly one `home_of`; no `hosts_globals`)
- **Disambiguation:** G305 ↔ G209 (reserves pairwise); G306 ↔ G20/G216/G225 (partnership, first 4-way); G307 ↔ G70/G277/G286 (spread, 4-way; G103 excluded) — first migration to fire N-way retrofit twice
- **Attachment edges:** Z1.1 ↔ `equity-research.z2.3` (bidirectional, ER commodity forward-link bullet); Z4.2 → `fixed-income.z4.8` (credit handshake as weighted back-link — template works on mid-cycle inputs + RBL); Z5.2 ↔ `sector-information-technology.z5.2` (reinvention / AI-power); Z2.2 ↔ `private-credit.z2.13` (midstream ↔ infrastructure debt)
- **Structured GAPs:** 3 (`oil101-extraction-poor` on Z3.1; `reserves-valuation-source-absent` on Z4.2; `transition-recency` on Z5.2)
- **Design ripple:** none — `SECTOR_LAYER_DESIGN.md` unchanged (N-way convention applied twice without modification). Commodities/trading-houses backlog + RBL→PC forward seam added to `docs/MIGRATION_DEFECTS.md`
- **Node count note:** 615 is one above the prior derived band — four genuine segments (upstream/midstream/downstream/services) defended in the node map, not an error

## Milestone 10 — Information Technology (Sector)

- **Slug:** `sector-information-technology`
- **Kind:** `sector-layer1` (ADR-003 rule 1)
- **Zones:** Z1 Code Eats the World (2) · Z2 Three Businesses, One Ticker Prefix (3) · Z3 Networks, Lock-In & the Scoreboard (2) · Z4 Going Deeper: Analyzing One (2) · Z5 Gravity, Regulators & the Next Wave (2)
- **New globals:** G293–G303 (11 net-new; append-only; each with exactly one `home_of`; hosted: G295 on Z2.1, G298/G299 on Z3.1, G301 on Z3.2)
- **Disambiguation:** G297 ↔ G132/G216 (first three-way family); G294 ↔ G67
- **Attachment edges:** Z1.1 ↔ `equity-research.z2.3` (bidirectional, ER forward-link bullet); Z4.2 → `fixed-income.z4.8` (credit handshake as back-link — template works); Z5.2 ↔ `real-estate.z2.3` (AI/data-center seam)
- **Structured GAPs:** 2 (`software-paradox-absent` on Z2.2 — Apple FY2025 10-K now grounds devices; `ai-cycle-recency` on Z5.2)
- **Design ripple:** N-way `disambiguate_with` retrofit sentence added to `docs/SECTOR_LAYER_DESIGN.md` checklist step 4; unhomed-generics backlog (moat / operating leverage / TAM) added to `docs/MIGRATION_DEFECTS.md`

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

- **Wave one closed** (Financials → IT → Energy → Consumer Discretionary).
- Next gate: **G1** (post-pilot, real-user evidence) before wave-two content.

## Known defects (unchanged)

- 26 pre-existing globals (G1–G263) have multiple `home_of` edges — logged; not worsened by M7–M12
- Unhomed cross-module concepts (moat / operating leverage / TAM / commodities-as-asset-class) — see `docs/MIGRATION_DEFECTS.md` §G–§H — **remain OPEN**; M12 did not resolve flywheel/brand diasporas or close moat/TAM/operating leverage
