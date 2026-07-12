# ADR-004: Presentation-Layer Separation (Lessons, Paths, Assessments)

**Status:** Accepted
**Accepted:** 2026-07-11
**Date:** 2026-07-11 (revised, correction pass 1)
**Deciders:** Product owner (ratifier); Claude/Fable (design); informed by the P0 read-only repo audit.
**Repo state at revision:** `main` @ `34c6a07` · 14 modules · G1–G313 contiguous · 615 zone nodes · 4,433 edges · strict validation 0/0 · `fixed-income` (asset-class, build order 11).
**Relates to:** extends ADR-001 (JSON canonical); operates under the two-track operating roadmap (architecture `M##`, product `P#`).

## Context

The learner-facing product needs lessons, paths, and assessments. The canonical graph is the project's core asset; the named failure modes are (a) duplicating canonical prose into lessons, creating drift-capable competing definitions, and (b) back-pressure — mutating graph nodes to suit UI. The audit confirms no lesson/path/assessment content, loader, or route exists today; a dormant `activity.schema.json` (`A{n}` IDs, quiz enum) is defined but unwired to validation, build, or UI.

## Decision

1. **A second content family** is created: `content/lessons/`, `content/paths/`, `content/assessments/` — authored JSON, schema-validated, versioned. It is **canonical for pedagogy**; `content/glossary/` + `content/modules/` remain **canonical for financial truth**. Neither overrides the other inside its own domain (the two-canons model).

2. **Reference-by-ID only.** Layer-2 files cite graph entities by ID using one shared grammar — a **canonical graph reference** is either a global `G{n}` or a zone node `{slug}.z{zone}.{ordinal}`. Layer-2 never mints graph IDs, never re-homes a concept, never copies a canonical definition as its own authority, and never writes to `content/glossary/**` or `content/modules/**`. Missing or wrong graph facts route to `MIGRATION_DEFECTS.md` as defects/gaps — never lesson-local fixes.

3. **The four reference fields have distinct, non-overlapping meanings** (revised — supersedes the globals-only `teaches` of the first draft):
   - **`teaches[]`** — the canonical concept(s) the lesson advances. Accepts **any resolving graph reference** (global *or* node), because pedagogically load-bearing concepts are not all homed as globals (e.g. Total Return lives at `fixed-income.z2.6` with no global of its own). ≥1 entry required. This is the drift-review anchor and the primary mastery key.
   - **`draws_on[]`** — the zone nodes consulted while authoring: the fact-check trail and the node-change review hook. Node IDs only.
   - **`connects[]`** — the graph relationships surfaced on the generated completion screen. Globals only (they are what a learner can navigate to as a concept). Governed by the one-hop rule below.
   - **`concept_ids[]`** (assessment items) — what the item tests. Same grammar as `teaches[]`; the forward-compatibility hinge for a future mastery model.

4. **The one-hop edge-reality rule.** Every `connects[]` entry must be reachable in **one hop** in the canonical graph from one of the lesson's `teaches[]` or `draws_on[]` entities, along a real edge kind: `references` (a node's `connects_to`), `home_of` (a node's `global_id` / `hosts_globals`), or `disambiguates` (a global's `disambiguate_with`). Decorative connections are a schema-level lie and are forbidden. Mechanically checkable by validator V-13 **directly from canonical content** — node `connects_to[].ref`, `global_id`, `hosts_globals[]`, global `disambiguate_with[]`, and resolved home nodes — with **no dependency on generated `graph/*` freshness** (see D4 / `LESSON_LAYER_DESIGN.md` §4); editorially reviewed for *pedagogical* relevance, which is not mechanizable.

5. **The drift test** governs authored copy: if the referenced node changed, the lesson text must not silently become wrong. Lessons **may** paraphrase, simplify, use analogies, work examples, write distractors, add misconception traps and role applications. Lessons **may not** redefine, contradict, or invent definitional/numeric facts.

6. **ID namespaces** `l-*`, `p-*`, `q-*` (prefix-disjoint from `G*`, node IDs, and the reserved `A*`). Item IDs are globally unique, though V1 additionally requires each lesson's checks to come from that lesson's own assessment file — reuse is a later, deliberate change requiring no renumbering.

7. **Validation** extends `pipeline/validate/validate.py` with `checks/lesson_checks.py`, called sequentially in `main()` per the existing pattern. Layer-2 errors fail validation like any content error; absent layer-2 directories are a vacuous pass.

8. **Independence invariant:** deleting `content/lessons|paths|assessments/`, `src/lib/lessons/`, and `app/learn/` loses zero canonical knowledge. Graph evolution remains append-only and unaware of the presentation layer.

## Consequences

**Positive:** graph integrity is machine-protected while real pedagogy becomes possible; presentation iterates at product speed (G1's "revise format" branch touches only layer 2 + renderers); `teaches[]`/`concept_ids[]` tagging makes a future mastery model computable without re-authoring; `content/*` and `product/*` branches merge independently.

**Negative / accepted:** paraphrased copy can go stale when nodes change — mitigated by the ID-link review procedure (design doc §5), accepted because derived-only lessons reproduce the node-dump failure mode; a second loader and hand-maintained type set; authors must learn the checklist. V-13's one-hop check is computed from canonical content and does **not** depend on generated `graph/*` being fresh.

**Rejected alternatives:** (a) lesson blocks embedded in node JSON — couples pedagogy to the graph and forces every presentation experiment through the migration pipeline; (b) purely derived lessons — cannot carry distractors, pacing, or misconception traps; (c) extending `activity.schema.json` — lacks `concept_ids` and per-option explanations, and repurposing a reserved-but-dormant family creates ambiguity for no reuse benefit; (d) globals-only `teaches[]` (the first draft) — forced lessons whose subject is a node-homed concept to misattribute themselves to an adjacent global, corrupting exactly the mastery signal the field exists to carry.
