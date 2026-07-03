# Sector Layer — Standing Design Reference

**Status:** Ratified by product owner, 2026-07-03. Governs all sector-layer1/sector-layer2 builds.
**Parent decision:** ADR-003 (sector topology). This document records the content-plan decisions ADR-003 explicitly left out of scope.

## Resolved decisions

### D1 — Real Estate exclusion
GICS "Real Estate" is **not** built as a sector module. The `real-estate` role module already homes the full sector syllabus (segments z2.1–z2.3, ★G219, FFO/AFFO z5.2, NAV z5.3). ER Z2.3 forward-links there instead (edges landed in M8). The active GICS candidate list is therefore **10 sectors**. If an analyst-lens gap ever surfaces, the fix is a node added to the RE module — never a `sector-real-estate` module.

### D2 — Source-grounding tiers
Two tiers, assigned per sector. Criterion: **(cost of being confidently wrong) × (distance from generalist knowledge).**

| Tier | Process | Sectors |
|---|---|---|
| **A** — full dossier | Cursor source-extraction prompt against acquired texts | Financials, Energy; Health Care when scheduled |
| **B** — light | Architect drafts from existing knowledge + targeted verification searches | IT, Consumer Discretionary, Consumer Staples, Industrials, Materials, Communication Services; Utilities (B with mandatory ratemaking searches) |

### D3 — Wave one
**Financials → Information Technology → Energy → Consumer Discretionary**, in that build order. Grounding: these are ER Z2.3's own four worked contrasts (bank / software / commodity-cyclical / retailer) and ADR-003 rule 7's example globals (NIM, combined ratio, NRR, same-store sales). ~45 nodes total ≈ one FI-scale milestone. Wave-two leaders: Health Care, Industrials.

### D4 — Format confirmations post-FI
- Node budget is **8–14 per module, min 1/zone, soft cap 4/zone** (ADR-003 rule 6; supersedes "8–12" in earlier notes).
- Inheritance rule restated: sectors inherit from the **full prior corpus**, with FI's G264–G285 as the primary **credit interface** (★G275 IG/HY, ★G276 ratings, ★G277 spreads, plus ★G74 coverage, ★G34 covenants). Sector credit content mints none of these.
- **FI Z4.8 handshake:** every sector with a credit leg back-links to `fixed-income.z4.8` from its credit node, completing Z4.8's named deferral.
- **Named rule — the Z4 duplication guard:** sector Z4 (valuation treatment) back-links to ER Z3.7–3.8 / Damodaran special-case content and adds only the sector-specific method. It never re-teaches DCF/multiples. This is the highest duplication risk in the layer; treat it with the same force as back-link-don't-re-home.

### D5 — Corporate-finance draft
Removed in M8. Any future corporate-finance module requires fresh scoping (much of its syllabus is already homed elsewhere).

### D6 — Build mechanics (per ADR-003 rules 1, 6, 8)
Each sector is a standard module: own directory `content/modules/sector-{slug}/`, own `build_order`, factory scaffold, five zone files, canonical sector spine (rule 4). Wave-one build orders: sector-financials **12**, sector-information-technology **13**, sector-energy **14**, sector-consumer-discretionary **15**. Globals contiguous from **G286**, append-only, exactly one `home_of` each. Expected ~6–10 net-new globals per sector — a low count is the health signal.

## Per-sector build checklist (reuse for every sector)

1. Scaffold via `scaffold_module.py --kind sector-layer1` (sector spine placeholders land automatically post-M8).
2. Inheritance pass over all prior globals **before** authoring — list inherited vs. candidate-new.
3. Tier A sectors: run the source-extraction prompt first; Tier B: architect drafts with targeted searches.
4. Author per the standing node standards: four required fields, structured `gaps[]`, back-link-don't-re-home, disambiguation callouts at every seam (esp. vs. parent asset-class/macro globals; vs. the RE module where relevant per D1).
5. Attachment edges: Z1.1 → `equity-research.z2.3`; ER Z2.3 → sector front door; credit node → `fixed-income.z4.8` (D4).
6. Z4 duplication guard review (D4) as an explicit QA step.
7. `validate.py --strict` at 0/0 (compactness warnings included) before delivery.

## Milestone numbering
M8 = this prep. M9 = sector-financials (Tier A — blocked on source acquisition). M10–M12 = remaining wave one.
