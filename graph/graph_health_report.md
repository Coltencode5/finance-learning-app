# Graph Health Report

Generated: 2026-07-02 by `pipeline/build/graph_health.py`

## Summary

| Metric | Value |
|---|---|
| Globals | 263 |
| Module zone nodes | 529 |
| Total edges | 3755 |
| Cross-module reference edges | 2357 |

### Edge kinds

- **disambiguates**: 2
- **home_of**: 294
- **references**: 3459

### Inbound degree distribution (all indexed ids)

- min: 0
- max: 46
- mean: 4.7

### Outbound degree distribution

- min: 0
- max: 28
- mean: 4.7

## Top 10 most-referenced globals

| Rank | ID | Term | Inbound refs |
|---|---|---|---|
| 1 | G29 | Leverage | 46 |
| 2 | G127 | Market cycles & the pendulum | 26 |
| 3 | G1 | IRR (Internal Rate of Return) | 25 |
| 4 | G9 | "2 and 20" | 23 |
| 5 | G124 | Second-level thinking | 22 |
| 6 | G33 | Debt stack / Funding instruments | 20 |
| 7 | G125 | Market efficiency (and its limits) | 19 |
| 8 | G156 | Manager selection (the allocator's manager due diligence) | 19 |
| 9 | G247 | The federal funds rate (the policy rate) (Z2.5) | 19 |
| 10 | G4 | J-curve | 19 |

## Disambiguation edges (canonical metadata only)

- `G102` → `G53`
- `G53` → `G102`

## Orphan nodes (zero inbound and zero outbound)

- `real-estate.z5.6` — The Real Estate Career & Where Real Estate Is Heading (real-estate)

## Low-reference nodes (≤2 total edges)

Count: 2 (see `graph/orphan_low_reference.json` for full list)

## Low-reference globals (<2 inbound references)

Count: 2
- `G63` Non-bank lending / Disintermediation (1 refs)
- `G128` Long/short equity (1 refs)

## Cross-module dependencies (reference counts)

- **asset-management** → global (192), hedge-funds (31), private-equity (14), investment-banking (3), private-credit (2)
- **equity-research** → global (181), asset-management (24), investment-banking (24), hedge-funds (19)
- **hedge-funds** → global (181), private-equity (12), investment-banking (9), private-credit (2)
- **investment-banking** → global (120), private-equity (31), private-credit (18)
- **macro-economics** → global (307), private-equity (3), hedge-funds (2)
- **private-credit** → global (181), private-equity (27)
- **private-equity** → global (298)
- **real-estate** → global (161), private-equity (17), investment-banking (2), private-credit (1)
- **venture-capital** → global (152), private-equity (33), equity-research (5), investment-banking (3), hedge-funds (1)
- **wealth-management** → global (249), asset-management (38), private-equity (9), hedge-funds (4), private-credit (1)

## Human review queue

These items are warnings, not validation errors:

- **Orphan nodes**: 1 — may be front-door nodes or missing connects_to
- **Low-reference globals**: 2 — candidate demotions or missing cross-links
- **Disambiguation pairs**: only globals with `disambiguate_with` in `globals.json` produce edges; other legacy "this vs. that" pairs remain prose-only until metadata is added
- **Prerequisites**: `graph/prerequisites.json` is experimental — do not treat as canonical

## Regeneration

```bash
python pipeline/build/build_graph.py
python pipeline/validate/validate.py
python pipeline/validate/validate.py --strict
```

