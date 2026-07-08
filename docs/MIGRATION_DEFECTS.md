# Migration Defect Register

Generated during Milestone 1 migration (legacy markdown → canonical JSON).
These are defects **in the legacy content itself**, verified against the source
files — not parser artifacts. They are deliberately NOT auto-fixed: each needs a
human (or Opus architecture-pass) decision, because the right fix is a judgment
call about what the reference *meant*.

**Status legend:** OPEN → DECIDED → FIXED (fix lands in canonical JSON, never in legacy/).

---

## A. Broken graph references (validation errors — block `--strict` CI)

| # | Where | Reference | Problem | Likely intent | Status |
|---|---|---|---|---|---|
| 1 | asset-management.z2.3 | AM Z5.7 | AM Zone 5 ends at Z5.6 | Z5.6 "Where AM Is Heading" (source text says "Z5.7 (where AM is heading)") | FIXED — `connects_to` → `asset-management.z5.6` |
| 2 | asset-management.z4.4 | AM Z5.7 | same | Z5.6 (context: "the giants' stewardship power" — confirm) | FIXED — `connects_to` → `asset-management.z5.6` |
| 3 | asset-management.z5.2 | AM Z5.7 | same | Z5.6 | FIXED — `connects_to` → `asset-management.z5.6` |
| 4 | asset-management.z5.4 | AM Z5.7 | same | PE Z5.7 (context is the PE allocator seat — may be a dropped "PE" prefix) | FIXED — `connects_to` → `private-equity.z5.7` |
| 5 | asset-management.z5.4 | AM Z5.8 | same | PE Z5.8 (same pattern as #4) | FIXED — `connects_to` → `private-equity.z5.8` |
| 6 | investment-banking.z3.13 | PE Z3.20 | PE Zone 3 ends at Z3.19 | PE Z3.17 (SPA) or Z3.19 (equity documentation) — "transaction documentation" | FIXED — `connects_to` → `private-equity.z3.16` (PE Transaction Documentation) |
| 7 | investment-banking.z3.14 | PE Z3.20 | same | same as #6 | FIXED — `connects_to` → `private-equity.z3.16` |
| 8 | venture-capital.z5.6 | VC Z5.7 | VC Zone 5 ends at Z5.6 | self-reference intent unclear — inspect source line | FIXED — `connects_to_raw` cites ER Z5.6/Z5.7; → `equity-research.z5.7` |
| 9 | wealth-management.z2.8 | WM Z5.7 | WM Zone 5 ends at Z5.5 | inspect source line | FIXED — `connects_to_raw` cites PE Z5.6/Z5.7; → `private-equity.z5.7` |
| 10 | wealth-management.z5.4 | WM Z5.7 | same | possibly PE Z5.7 (dropped prefix, same as AM pattern) | FIXED — `connects_to` → `private-equity.z5.7` |
| 11 | wealth-management.z5.4 | WM Z5.8 | same | possibly PE Z5.8 | FIXED — `connects_to` → `private-equity.z5.8` |

**Pattern note:** defects 1–5 and 9–11 cluster in AM and WM Zone-5 references,
suggesting a renumbering pass during authoring that didn't update inbound refs —
the exact failure mode a validator prevents going forward.

## B. Known-intentional term collision (warning — needs confirmation)

| Term | IDs | Note |
|---|---|---|
| IPO | G53, G102 | G53 = IPO **as exit** (PE lens); G102 = IPO **process** (IB lens). VC module Part 7 explicitly treats these as an intentional dual-lens pair. **FIXED:** mutual `disambiguate_with`; validator suppresses the dupe warning. |

## C. Globals without a hosting zone node (45 warnings)

45 of 235 globals had no zone node carrying their `global_id` (e.g. G6 GP,
G7 LP, G24 EBITDA). In the legacy maps these globals' deep explainers live
*inside* a broader zone node (G6/G7 inside PE Z1.3 "Fund Structure & Key
Players") without a `★ GLOBAL` tag on that node.

**Decision (Milestone 2 — applied):** `hosts_globals` array on `node.schema.json`;
each orphan global assigned to the zone node whose legacy prose contains its deep
explainer. Validator accepts `global_id` or `hosts_globals` as hosting.

**Human review — ambiguous host assignments (approved for v0; refine later if needed):**

| Global | Assigned host | Ambiguity |
|---|---|---|
| G73 PIK | `private-credit.z2.5` Mezzanine Debt | `home_zone` is Z3 but no Z3 node owns PIK; mezzanine (Z2) is the upside explainer; `private-credit.z4.11` deepens stress-signal nuance |
| G113 IC / skill | `hedge-funds.z3.4` Position Sizing | IC also introduced in `hedge-funds.z2.9` Quant; Z3.4 hosts the Fundamental Law cluster (G113–G115) |

## D. Legacy schema drift (informational — absorbed by the parser, normalize on render)

- Real Estate uses `# ZONE 1 —` headers; all others use `# PART n · Zone n —`.
- PC Z1.1 uses `**Quick definition (basic → technical).**` variant.
- HF Z2.8 uses non-standard tag `★ GLOBAL (G127-adjacent)` — parsed as a plain
  node (correctly: it is not G127's home). Confirm.
- GAP flags exist in two formats (inline `GAP:` tags vs. consolidated Part 9
  sections). Canonical JSON uses the structured `gaps` field only; consolidated
  Part 9 gaps in ER/VC/RE were NOT parsed node-level (they aren't attached to
  nodes in the source) — they need a one-time manual attachment pass in
  Milestone 2 (~12 gap items total across the three modules).
- Hedge Funds' own prose says "29 new global nodes (G106–G136)"; the actual
  table (and now `derived.globals_contributed`) is 31. Derived counts are the
  fix: module summaries are now generated, never hand-written.

**GAP normalization (Milestone 2):** Consolidated Part 9 summaries from ER, VC,
and RE attached to primary anchor nodes (see `pipeline/build/apply_m2.py`
`CONSOLIDATED_GAPS`). Node-level inline gaps preserved. **Deferred:** ER Part 9
item #4 (sector-specific valuation depth — breadth item, not a true gap); RE
Part 9 item #7 (source-quality/file-access note — module-level, not node-level).

## E. Macro & Economics migration (Milestone 6)

| # | Where | Issue | Decision | Status |
|---|---|---|---|---|
| 12 | Macro map Part 1 source list | **Z5.10** cited as the historical-episode layer alongside Z5.9, but no `### Z5.10` node header exists in the legacy map | Z5.9 "The Historical Episodes (the Crisis Canon)" subsumes the canon; 51 nodes emitted (not 52). No phantom node created. | DECIDED |
| 13 | `validate.py` + draft modules | G236–G263 are in `globals.json` while `macro-economics` is draft; validator loads all globals but skips draft module nodes | **FIXED:** `check_required` skips hosting warnings for globals whose `contributed_by` module is draft. Re-run strict validation after promotion. | FIXED |
| 14 | macro-economics.z1.6 connects_to | Legacy prose `PE Z2.21 / Z3.12 / Z5.21` — bare `Z3.12`/`Z5.21` were parsed as in-module refs | **FIXED** in `parse_markdown.py` via `propagate_abbrev_prefix()`; re-parsed to `private-equity.z3.12` / `.z5.21`. | FIXED |

## F. Scaffold conventions (Milestone 8)

| # | Where | Issue | Decision | Status |
|---|---|---|---|---|
| 15 | `scaffold_module.py` `zone_titles_for_kind()` | Unmapped kinds (e.g. `asset-class`) silently fall back to `ROLE_ZONE_TITLES` instead of erroring or requiring an explicit mapping | Logged for deliberate decision — fallback vs. explicit mapping should not be fixed drive-by; Fixed Income is complete so nothing is broken today | OPEN |

## G. Backlog — unhomed cross-module concepts (Milestone 10)

Surfaced by the IT sector inheritance pass: concepts in wide textual use across modules with **no global home**. Deliberately not minted in a sector module (would wrong-home a corpus-wide concept). Reuse OPEN lifecycle.

| # | Concept | Where used (sample) | Recommended future home | Status |
|---|---|---|---|---|
| 16 | Moat / durable competitive advantage | VC z1.8, ER z2.7, AM z2.7/z3.3, WM z5.1, sector-financials z2.1/z2.3 (7 nodes, 5 modules) | AM Z2.7 (quality) or ER competitive-analysis territory | OPEN |
| 17 | Operating leverage | AM z5.1, WM z5.1, RE z2.3; taught concretely inside sector-IT ★G293 | Unresolved — resurfaces the D5 corporate-finance question | OPEN |
| 18 | TAM / addressable market | VC z3.3/z3.4, PE z2.5, macro | VC Z3.4 | OPEN |

**Related M10 seam (no PC edit):** ARR-based lending (underwriting pre-EBITDA software on recurring revenue) has no home in the Private Credit map. When PC's authoring-depth layer covers it, back-link ★G300/★G294 rather than re-defining them.
