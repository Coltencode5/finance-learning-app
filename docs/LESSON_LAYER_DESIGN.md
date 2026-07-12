# Lesson Layer Design

**Status:** Canonical — ADR-004 Accepted 2026-07-11.
**Revision:** correction pass 1 (2026-07-11). Supersedes the first P0 draft.
**Peer document to:** `SECTOR_LAYER_DESIGN.md`. Governs `content/lessons/`, `content/paths/`, `content/assessments/`.
**Designed against:** the P0 read-only repository audit. Audit-derived facts are tagged **[AUDIT]**. Repo state: `main` @ `34c6a07` · 14 modules · G1–G313 · 615 nodes · 4,433 edges · strict 0/0 · `fixed-income` (asset-class, build order 11).
**Product track terminology:** P0 (this milestone: audit + lesson-layer architecture + authored FI pilot) → P1 (FI learning-loop implementation) → P2 (real-user pilot test) → **Gate G1** (evidence-based product decision). No new active-module migration after **M12** until G1.

## Executive summary of design rulings

1. Lessons, paths, and assessment items form a **second content family** under `content/`, with their own schemas, loader, and validator checks — never touching `content/glossary/**` or `content/modules/**`.
2. **Two canons:** the graph owns financial truth; this family owns pedagogy. Everything references the graph **by ID only**; the drift test governs all authored copy.
3. **`teaches[]` accepts any canonical graph reference — global *or* node** (revised; §2). Load-bearing concepts are not all homed as globals, and a lesson must be able to name its actual subject.
4. **ID namespaces** are prefix-disjoint: `l-*`, `p-*`, `q-*` — avoiding `G*`, node IDs, and the reserved `A*` of the dormant activity schema **[AUDIT §1]**, which stays untouched.
5. **Six screen block types, hard ceiling:** `explanation`, `key_point`, `example`, `comparison`, `misconception`, `check`. Formula is a `key_point` field; application is an `example` role tag; the connection screen is **generated** from `connects[]`, never authored.
6. All V1 assessment items are **single-choice**, one correct option, an explanation on **every** option, mandatory `concept_ids[]`.
7. **The one-hop edge-reality rule** (§4) makes `connects[]` mechanically checkable against canonical content — decorative connections are a schema-level lie.
8. Lesson routes get their **own small `/learn` tree**, SSG'd from path files, never joining the ~928-page `/concepts` enumeration **[AUDIT obs 6]**.
9. Validation extends `pipeline/validate/validate.py` via a new `checks/lesson_checks.py`, following the observed sequential-call pattern **[AUDIT §4]**.
10. V1 learner behavior is fixed by a **minimal behavioral contract** (§8) so P1 invents nothing: no grading, no mastery, no gating beyond simple prerequisites.

---

## 1. The five layers, mapped to this repo

| # | Layer | Location (actual) | Authority | Mutability | Validated by |
|---|---|---|---|---|---|
| 1 | Canonical knowledge graph | `content/glossary/globals.json`, `content/modules/{slug}/` (+ generated `graph/*`) | Financial truth | Append-only, M-track + ADRs | existing `validate.py --strict` |
| 2 | Canonical learning artifacts | `content/lessons/`, `content/paths/`, `content/assessments/` | Pedagogy | Authored freely, P-track | new `lesson_checks.py` |
| 3 | Generated / runtime presentation | connection screen, progress %, path duration, rendered blocks | — (recomputable) | n/a | n/a |
| 4 | Product configuration | `src/lib/lessons/` (loader), `app/learn/` (routes), renderers | App behavior | code review | `typecheck` + `build` |
| 5 | Learner state | localStorage (P1) → database (post-G1) | Runtime | runtime | n/a |

**[AUDIT obs 1]** No loader exists for layer 2 — P1 builds `src/lib/lessons/` analogous to `src/lib/graph/load.ts` (fs read at build, singleton store). **[AUDIT obs 3]** Types stay hand-maintained, mirroring the schemas; codegen is out of scope. **[AUDIT obs 5]** `getConceptOrNode` discriminates on `id.startsWith("G")`; the `l-`/`p-`/`q-` prefixes never collide with that branch and resolve only through the new loader.

### File layout

```
content/
  lessons/       {lesson-id}.json                one file per lesson
  paths/         {path-id}.json                  one file per path
  assessments/   {lesson-id}.items.json          one file per lesson's items
```

Items are grouped per lesson so authoring and review stay atomic — an item is only ever reviewed alongside the lesson that uses it. Item IDs remain **globally unique** so deliberate cross-lesson reuse can be introduced later without renumbering; **V1 additionally requires** each lesson's checks to reference items from that lesson's own file (§7).

## 2. The four reference fields — distinct, non-overlapping meanings

A **canonical graph reference** is either a global `G{n}` or a zone node `{slug}.z{zone}.{ordinal}`. One grammar, four uses:

| Field | Grammar | Means | Consumers |
|---|---|---|---|
| `teaches[]` (lesson) | global **or** node, ≥1 | The canonical concept(s) this lesson advances — its **subject** | drift review; mastery (future); misconception-pairing check |
| `draws_on[]` (lesson) | node only | Nodes consulted while authoring — the **fact-check trail** | node-change review; the one-hop anchor set |
| `connects[]` (lesson) | global only, ≥1 | Relationships surfaced on the **generated completion screen** | the learner-facing payoff; one-hop rule |
| `concept_ids[]` (item) | global **or** node, ≥1 | What the item **tests** | mastery (future); analytics event payload |

**Why `teaches[]` admits nodes** (correction, supersedes the globals-only first draft): pedagogically load-bearing concepts are not all homed as globals. Total Return lives at `fixed-income.z2.6` and has no global of its own; forcing that lesson to claim it teaches an adjacent global (`G265`, yield to maturity) would misattribute the mastery signal the field exists to carry and corrupt drift review. Accepting nodes costs nothing — the reference resolves, the review hook works, the mastery key is still a canonical entity. It grants the product layer **no** new power: it may not mint, re-home, or modify any graph entity.

`connects[]` stays **globals-only** because the completion screen offers the learner navigable *concepts*, and globals are the graph's concept currency.

## 3. Lesson anatomy

5–8 screens, one primary idea per screen, 2–3 checks interleaved, 4–7 minutes (authoring rules; the schema's bounds are looser — pacing is editorial judgment, not a validity condition).

| Field | Required | Meaning |
|---|---|---|
| `id` | ✓ | `l-fi-duration` — stable, human-readable (§6) |
| `title` | ✓ | Learner-facing |
| `teaches[]` | ✓ | Subject (§2), unique items |
| `draws_on[]` | ✓ | Fact-check trail (§2), unique items; may be empty only if every `teaches` entry is a node |
| `estimated_minutes` | ✓ | Honest single number, shown on the path page |
| `screens[]` | ✓ | Ordered blocks (§4) |
| `checks[]` | ✓ | The lesson's item IDs **in screen order** — the tooling index, so analytics and future mastery never parse screens |
| `connects[]` | ✓ | Completion-screen payoff; one-hop rule (§4) |
| `status` | ✓ | `draft` \| `authored` \| `reviewed` \| `published` — **required**, never defaulted |

## 4. Screen block types — the closed set of six

| Type | Fields | Notes |
|---|---|---|
| `explanation` | `heading?`, `body` | The teaching voice; one idea |
| `key_point` | `heading?`, `body`, `formula?` | The takeaway card; `formula` renders as the styled formula variant — **not** a seventh type |
| `example` | `heading?`, `body`, `role?` | Worked/practical instance; `role` turns it into an application screen — **not** a seventh type |
| `comparison` | `heading?`, `left{label,body}`, `right{label,body}`, `verdict?` | Two-column distinction card — the disambiguation workhorse |
| `misconception` | `myth`, `reality`, `why_it_matters?` | Names the confusion explicitly; a paired check must test it |
| `check` | `item` | References one `q-*` item; stem/options/feedback render from the item file |

The connection/completion screen is **generated** from `connects[]` (labels via the existing `resolveRefLabel`, links via `conceptHref` **[AUDIT §2]**) — authoring one is a schema violation.

### The one-hop edge-reality rule (governs `connects[]`)

Every `connects[]` entry must be reachable in **one hop** from one of the lesson's `teaches[]` or `draws_on[]` entities, along a **real canonical edge**. The permitted edge kinds are exactly those the graph build emits **[AUDIT §1]**:

- **`references`** — a node's `connects_to[].ref`
- **`home_of`** — a node's `global_id`, and each entry of its `hosts_globals[]`
- **`disambiguates`** — a global's `disambiguate_with[]`

Formally, the lesson's **anchor set** is `teaches[] ∪ draws_on[]`, and for each anchor *a* the allowed neighborhood is:

- *a* is a **node** → `a.connects_to[].ref` ∪ `{a.global_id}` ∪ `a.hosts_globals[]`
- *a* is a **global** → `a.disambiguate_with[]` ∪ `{home_node(a)}` ∪ `home_node(a).connects_to[].ref`
  *(a global's graph relationships are carried by its home explainer node — this is the `home_of` edge traversed once, not an extra hop)*

Every `connects[]` entry must lie in the union of those neighborhoods. Computed **from canonical content directly**, so it has no dependency on `graph/*` being freshly regenerated.

**Mechanically enforceable:** whether the relationship *exists*. **Not mechanizable, and therefore an editorial review item:** whether the relationship is *pedagogically worth surfacing*. The check proves a connection is real; a human still decides it is worth showing. Decorative connections — real-but-pointless, or worse, invented — are forbidden by rule 6 of §5.

## 5. Authoring rules — the two-canons checklist

Before any lesson merges, author and reviewer confirm:

1. **Facts flow one way.** Every definitional or numeric fact in the copy is expressible from the `teaches`/`draws_on` nodes. If a lesson needs a fact the graph lacks → defect/gap filing in `MIGRATION_DEFECTS.md`; never invent, never patch, never work around.
2. **The drift test, per screen:** *if the referenced node changed, would this text silently become wrong?* Paraphrase that the `teaches`/`draws_on` links make reviewable — yes. A hard-coded competing definition — forbidden.
3. **No re-homing by prose.** A lesson may mention a concept homed elsewhere only as that concept's home defines it.
4. **Authored, not derived.** Screens are written for a learner; node prose is the fact-checker, never the draft. A reader should never sense JSON underneath.
5. **Misconception blocks name the confusion explicitly**, and a check in the same lesson tests that exact confusion.
6. **`connects[]` entries are real and worth surfacing** — the one-hop rule proves the first; the reviewer judges the second.
7. **No absolutes the graph doesn't support.** "Always," "never," "identical," "riskless" get challenged at review: qualify for defaults, calls, restructurings, taxes, optionality, and liquidity wherever the canonical node does.

**Review procedure when a referenced node changes (M-track → P-track):** the milestone report lists changed graph IDs → grep `content/lessons|paths|assessments/` for those IDs (the reference fields make this mechanical) → every lesson whose `teaches`/`draws_on`/`connects` or item `concept_ids` hits a changed ID gets a human re-read against the new node text → outcome logged in `docs/LESSON_FEEDBACK.md`. Process, not schema — no review-tracking fields.

## 6. ID conventions

| Family | Pattern | Example | Rationale |
|---|---|---|---|
| Lesson | `^l-[a-z0-9-]+$` | `l-fi-duration-vs-maturity` | module-abbrev + concept slug; path-independent (lessons are reusable across paths) |
| Path | `^p-[a-z0-9-]+$` | `p-fi-foundations` | |
| Item | `^q-[a-z0-9-]+-[0-9]{2}$` | `q-fi-duration-01` | lesson-slug base + counter; `q-` avoids the `A{n}` namespace the dormant activity schema reserves **[AUDIT §1]** |

Lowercase-kebab throughout (matching the module-slug convention). IDs are stable once merged; renaming means a new ID, never renumbering — the same append-only spirit as G-numbers, enforced by review rather than by validator in V1.

## 7. Uniqueness and integrity policy (mirrored exactly in D3/D4)

- `status` is **required** on lessons, paths, and item files. Nothing relies on JSON Schema `default` to populate missing data.
- `teaches[]`, `draws_on[]`, `checks[]`, `connects[]`, `concept_ids[]`, `requires[]` are all **`uniqueItems: true`** — duplicates are never meaningful in any of them.
- **`draws_on[]` conditional invariant:** if any `teaches[]` entry is a global ID, `draws_on[]` must be non-empty; if every `teaches[]` entry is a node ID, an empty `draws_on[]` is permitted. Enforced by validator check V-4.
- A path may not list the **same lesson twice**.
- Item IDs are **globally unique** across `content/assessments/`.
- Option IDs are unique within an item, drawn contiguously from `a`, matching the option count.
- **Ordered equality:** the ordered list of item refs from a lesson's `check` screens must equal `checks[]` exactly — same items, same order, same length. Duplicates fail.
- **V1 item locality:** every ID in a lesson's `checks[]` must be defined in that lesson's own `{lesson-id}.items.json`.
- Exactly one option per item has `correct: true`; every option carries an `explanation`.
- Absent `content/lessons|paths|assessments/` directories are a **vacuous pass** — valid before P0 content is installed.

## 8. The V1 behavioral contract (minimum, so P1 invents nothing)

No grading, no mastery thresholds, no review queues, no streaks, no accounts, no server state.

| Question | V1 answer |
|---|---|
| When is a lesson's prerequisite satisfied? | When **every** lesson in its path step's `requires[]` has a `completed_at` in local progress. A step with an empty `requires[]` is always available. |
| Can a locked lesson be opened directly? | **No.** Direct navigation to a locked lesson redirects to the path page, where it renders as locked. (Locking must mean something; the pilot measures ordered progression.) |
| When is a question attempt recorded? | On **submit** of a selected option — and on every subsequent retry, as an additional attempt. Selecting without submitting records nothing. |
| How does feedback work? | Immediately on submit: correct/incorrect state, the explanation for the option chosen, and — when wrong — the correct option's explanation as well. No score is shown. |
| Does a wrong answer block progression? | **No.** The learner may continue after seeing feedback. Retry is offered and optional; retries record additional attempts. Correctness is never required to advance. |
| What marks a lesson complete? | The learner advances past the final screen (reaching the generated completion screen) **and** every `check` screen in that lesson has ≥1 recorded attempt. Questions cannot be skipped; they can be answered wrongly. |
| What marks a path complete? | Every lesson listed in the path has a `completed_at`. |
| How does a learner resume? | Reopening an incomplete lesson restores at the highest screen index reached; previously answered checks render in their answered state with feedback visible. No prior progress → screen 0. |

## 9. What P1 builds from this (one-sentence specs — the `content/` vs `src/` boundary)

Loader `src/lib/lessons/` mirroring `load.ts`; hand-written types mirroring the three schemas; route tree `app/learn/[pathId]/` + `app/learn/[pathId]/[lessonId]/` SSG'd from path files only; six block renderers plus one single-choice check renderer; the generated connection screen via `resolveRefLabel`/`conceptHref`; localStorage progress and the D5 event wrapper per §8. Everything authored is `content/`; everything rendered is `src/`.
