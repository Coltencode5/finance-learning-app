# ADR-003 — Sector topology

**Status:** Accepted · **Date:** 2026-07-02

## Decision

Sector content ships as **modules** of the M1-anticipated kinds
`sector-layer1` (broad sectors, GICS-grain: financials, energy, software,
healthcare, …) and `sector-layer2` (industries within a layer-1 sector:
banks, insurance, E&P, …). They are **compact by content policy** (8–14
nodes, 1–3 per zone) and **attached by graph edges, not containment** —
`equity-research.z2.3` is the canonical narrative hub, not the container.

The original dichotomy — "full five-zone peers vs. depth-layer clusters
hanging off ER Z2.3" — is resolved as a synthesis: sector modules keep the
**peer option's machinery** (manifest, factory, validator, graph, home-page
category) and the **cluster option's grain** (compactness, Z2.3 anchoring).
No new structural primitive is introduced.

## Ruled by this ADR

1. **Sectors are modules.** `kind: sector-layer1 | sector-layer2`, ratifying
   the enum present in `schemas/module.schema.json` since M1
   (`18f4edb`). Standard manifest, `build_order`, `visibility`, factory
   scaffold flow.
2. **All six ADR-002 structural invariants apply unchanged**: exactly five
   zone files; `{slug}.z{zone}.{ordinal}` IDs; four required node fields;
   structured `gaps[]`; contiguous globals from `corpus_max + 1` (G264 for
   the next active module); back-link-don't-re-home.
3. **Semantic release extended.** ADR-002's concept-progression allowance is
   extended from `core-concept` to **all non-`role` kinds** (`asset-class`,
   `sector-layer1`, `sector-layer2`), closing this question class. Role
   modules alone remain bound to the role spine.
4. **The canonical sector spine** (all sector modules use it; per template
   rule 6, decide once, apply uniformly):

   | Zone | Sector-grain meaning | Example (banks) |
   |---|---|---|
   | Z1 | How the sector makes money — the economics | NIM, the balance-sheet business |
   | Z2 | The segments / sub-verticals | money-center, regional, custody, … |
   | Z3 | The drivers & KPI framework (the critical factors) | NIM, credit losses, capital ratios |
   | Z4 | The valuation treatment — why generic tools bend here | DDM / P-B; banks break the EV frame |
   | Z5 | Regulation, the cycle, and where the sector is heading | Basel, credit cycle position |

   This is Valentine's sector-framework principle (already taught at ER
   Z2.3 / ★G191) given structural form.
5. **Attachment is topology.** Each `sector-layer1` module's `Z1.1`
   back-links to `equity-research.z2.3` and Z2.3 forward-links to each
   sector front door (`connects_to` edges; existing `references` edge kind —
   no edge-schema change). Each `sector-layer2` module's `Z1.1` links to the
   layer-1 node naming its segment (e.g. banks → `sector-financials.z2.x`).
   Other consumers (`investment-banking.z1.4` coverage groups,
   `real-estate.z2.1–2.3` property sectors, `venture-capital.z2.8`,
   `hedge-funds.z3.2`) attach via ordinary `connects_to` edges as their
   content is touched — no retrofitting sweep required.
6. **Compactness is a content rule, not a schema exception.** Target 8–14
   nodes per sector module, minimum 1 per zone, soft cap 4 per zone. A
   sector that appears to need 20+ nodes is an escalation (it may be a
   layer-1 sector hiding layer-2 industries), mirroring the template's
   sixth-zone escalation rule. Small node and global counts are the
   expected sign of inheritance health, not under-building.
7. **Globals policy unchanged.** Sector-economics primitives that recur
   across role modules (NIM, combined ratio, same-store sales, NRR, …) are
   minted as globals from G264 onward and homed in their sector module.
   One home per global (template rule 2). Sector-idiosyncratic detail stays
   in node prose.
8. **Slug convention.** `sector-` prefix for both layers
   (`sector-financials`, `sector-banks`). The layer-1↔layer-2 parent
   relationship is expressed by the Z1.1 attachment edge — the graph is the
   source of truth; no `parent` manifest field is added (schema is
   `additionalProperties: false`; revisit only if UI grouping demands it).

## Why

- **Precedent symmetry with ADR-002.** The schema anticipated the kinds at
  M1; the exception was never documented. ADR-002 resolved core-concept by
  scoping a *semantic* release to a kind while holding *structural*
  invariants for all kinds. ADR-003 extends the same move rather than
  inventing a second mechanism.
- **A non-module cluster primitive is the bespoke-tooling path ADR-002
  rejected.** The node-ID pattern (`^[a-z0-9-]+\.z[1-5]\.[0-9]+$`) is locked
  in `node.schema.json` and `new_module_checks.py`; graph builders, indexes,
  the data-access layer, and the home-page category system all speak
  "module." A new primitive would touch every layer of the pipeline to save
  five small JSON files.
- **Containment inside equity-research would trap shared infrastructure in
  one role module.** The corpus already treats sectors as a lens *every*
  consuming module reaches for (IB coverage groups, RE property sectors, VC
  sector theses, HF fundamental research) — the same reasoning that
  sequenced Macro before sectors (globalize shared primitives once) applies
  to where sector content lives. ER Z2.3 currently has only two inbound
  edges; it is the right *front door*, not the right *container*.
- **Compactness was the legitimate core of the "cluster" option** — and it
  is fully satisfiable as content policy inside the five-zone frame. The
  sector spine above is a genuine concept progression at 1–3 nodes per
  zone; nothing is padded to fit.

## Explicitly out of scope

- **Which sectors ship first, and how many** — content prioritization for
  the sector-stage execution prompt, not architecture.
- **Fixed Income / Credit Markets module design** — FI is `kind:
  asset-class`; this ADR unblocks its spine semantics via ruling 3 but its
  content plan is its own migration prompt. FI does not depend on sector
  topology and may proceed first, per the standing sequence.
- **Activity generation** — separate backlog item; unaffected.
- **Validator enforcement of the compactness policy** (a warning-level
  node-count check for sector kinds) — optional, deferred to the sector
  execution prompt; this ADR sets policy only.
- **ER Z2.3 prose updates** acknowledging its hub role — execution detail
  for the first sector migration.

## Consequences

- `scaffold_module.py` gains sector-spine placeholder titles selected by
  kind (parallel to the ADR-002 core-concept placeholders);
  `new_module_checks.py` extends its placeholder-mismatch check to the
  sector kinds.
- The first `sector-layer1` module starts its globals at **G264** (the
  parameterized `corpus_max + 1` gate; no code change needed).
- Home-page categories: `sector-layer1` surfaces as a sector category;
  `sector-layer2` modules surface within their parent's context via the
  attachment edge (UI treatment deferred to app work).
- Build sequence confirmed: Fixed Income (asset-class) → sector-layer1 set →
  sector-layer2 on demand → Derivatives, per the standing plan.
