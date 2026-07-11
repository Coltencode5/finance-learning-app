# Graph Health Report

Generated: 2026-07-10 by `pipeline/build/graph_health.py`

## Summary

| Metric | Value |
|---|---|
| Globals | 313 |
| Module zone nodes | 615 |
| Total edges | 4433 |
| Cross-module reference edges | 2783 |

### Edge kinds

- **disambiguates**: 34
- **home_of**: 344
- **references**: 4055

### Inbound degree distribution (all indexed ids)

- min: 0
- max: 52
- mean: 4.8

### Outbound degree distribution

- min: 0
- max: 28
- mean: 4.8

## Top 10 most-referenced globals

| Rank | ID | Term | Inbound refs |
|---|---|---|---|
| 1 | G29 | Leverage | 52 |
| 2 | G127 | Market cycles & the pendulum | 32 |
| 3 | G1 | IRR (Internal Rate of Return) | 27 |
| 4 | G255 | The credit cycle (Z4.1) | 23 |
| 5 | G9 | "2 and 20" | 23 |
| 6 | G124 | Second-level thinking | 22 |
| 7 | G247 | The federal funds rate (the policy rate) (Z2.5) | 22 |
| 8 | G61 | Recovery rate / Loss Given Default (LGD) | 22 |
| 9 | G248 | The risk-free rate & the term structure of interest rates (Z2.6) | 20 |
| 10 | G33 | Debt stack / Funding instruments | 20 |

## Disambiguation edges (canonical metadata only)

- `G102` → `G53`
- `G132` → `G297`
- `G20` → `G306`
- `G209` → `G305`
- `G216` → `G297`
- `G216` → `G306`
- `G225` → `G306`
- `G265` → `G58`
- `G269` → `G248`
- `G269` → `G257`
- `G276` → `G77`
- `G277` → `G286`
- `G277` → `G307`
- `G277` → `G70`
- `G285` → `G72`
- `G286` → `G277`
- `G286` → `G307`
- `G286` → `G70`
- `G288` → `G69`
- `G294` → `G67`
- `G297` → `G132`
- `G297` → `G216`
- `G305` → `G209`
- `G306` → `G20`
- `G306` → `G216`
- `G306` → `G225`
- `G307` → `G277`
- `G307` → `G286`
- `G307` → `G70`
- `G53` → `G102`
- `G67` → `G294`
- `G69` → `G288`
- `G70` → `G286`
- `G70` → `G307`

## Orphan nodes (zero inbound and zero outbound)

_None._

## Low-reference nodes (≤2 total edges)

Count: 3 (see `graph/orphan_low_reference.json` for full list)

## Low-reference globals (<2 inbound references)

Count: 18
- `G128` Long/short equity (1 refs)
- `G272` The money market (bills, CP, CDs) (Z3.5) (1 refs)
- `G288` Insurance float (Z2.2) (1 refs)
- `G289` The combined ratio (Z2.2) (1 refs)
- `G292` The bank run & deposit insurance (Z5.2) (1 refs)
- `G297` The multi-sided platform (Z3.1) (1 refs)
- `G298` Network effects (Z3.1) (1 refs)
- `G300` ARR (annual recurring revenue) (Z3.2) (1 refs)
- `G302` The Rule of 40 (Z4.1) (1 refs)
- `G303` Stock-based compensation (SBC) (Z4.2) (1 refs)
- `G304` The petroleum value chain (upstream · midstream · downstream) (Z1.1) (1 refs)
- `G306` The master limited partnership (MLP) (Z2.2) (1 refs)
- `G307` The crack spread (the refining margin) (Z2.3) (1 refs)
- `G308` The oil price: benchmarks & how crude is priced (Z3.1) (1 refs)
- `G309` OPEC, spare capacity & the swing producer (Z3.3) (1 refs)
- … and 3 more

## Cross-module dependencies (reference counts)

- **asset-management** → global (192), hedge-funds (31), private-equity (14), investment-banking (3), private-credit (2)
- **equity-research** → global (181), asset-management (24), investment-banking (24), hedge-funds (19), real-estate (3)
- **fixed-income** → global (197), hedge-funds (14), asset-management (7), private-credit (6), macro-economics (4)
- **hedge-funds** → global (181), private-equity (12), investment-banking (9), private-credit (2)
- **investment-banking** → global (120), private-equity (31), private-credit (18)
- **macro-economics** → global (307), private-equity (3), hedge-funds (2)
- **private-credit** → global (181), private-equity (27), sector-energy (1)
- **private-equity** → global (298)
- **real-estate** → global (161), private-equity (17), investment-banking (2), private-credit (1), sector-information-technology (1)
- **sector-energy** → global (42), macro-economics (5), sector-information-technology (4), equity-research (3), hedge-funds (3)
- **sector-financials** → global (37), equity-research (3), fixed-income (2), investment-banking (2), macro-economics (2)
- **sector-information-technology** → global (48), asset-management (4), equity-research (4), sector-financials (4), macro-economics (3)
- **venture-capital** → global (152), private-equity (33), equity-research (5), investment-banking (3), hedge-funds (1)
- **wealth-management** → global (249), asset-management (38), private-equity (9), hedge-funds (4), private-credit (1)

## Human review queue

These items are warnings, not validation errors:

- **Orphan nodes**: 0 — may be front-door nodes or missing connects_to
- **Low-reference globals**: 18 — candidate demotions or missing cross-links
- **Disambiguation pairs**: only globals with `disambiguate_with` in `globals.json` produce edges; other legacy "this vs. that" pairs remain prose-only until metadata is added
- **Prerequisites**: `graph/prerequisites.json` is experimental — do not treat as canonical

## Regeneration

```bash
python pipeline/build/build_graph.py
python pipeline/validate/validate.py
python pipeline/validate/validate.py --strict
```

