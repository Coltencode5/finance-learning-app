# P0 — Schemas (D3), Validator Specifications (D4), Learner-State & Event Contract (D5)

> **Authority note.** This document governs the design contract for the lesson layer.
> The extracted executable schemas under `schemas/lesson.schema.json`,
> `schemas/path.schema.json`, and `schemas/assessment.schema.json` are the
> **executable schema authority** if transcription drift between this document and
> those files is ever discovered.

**Status:** Canonical design contract under ADR-004 (Accepted 2026-07-11). Revision: correction pass 1.
Schemas and validator checks are installed in **P0**. Client progress/event modules remain **P1**. Extracted executable schemas live at `schemas/lesson.schema.json`, `schemas/path.schema.json`, and `schemas/assessment.schema.json`; validator checks live at `pipeline/validate/checks/lesson_checks.py`. All schemas use `additionalProperties: false`, matching the existing schema house style **[AUDIT §1]**.

**Shared definition — canonical graph reference:**
```
graphRef  := ^(G[1-9][0-9]*|[a-z0-9-]+\.z[1-5]\.[0-9]+)$      (global or zone node)
globalRef := ^G[1-9][0-9]*$
nodeRef   := ^[a-z0-9-]+\.z[1-5]\.[0-9]+$
```

---

## D3.1 Lesson schema (`schemas/lesson.schema.json`)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Lesson",
  "type": "object",
  "additionalProperties": false,
  "required": ["id", "title", "teaches", "draws_on", "estimated_minutes", "screens", "checks", "connects", "status"],
  "properties": {
    "id":    { "type": "string", "pattern": "^l-[a-z0-9-]+$" },
    "title": { "type": "string", "minLength": 1 },
    "teaches": {
      "type": "array", "minItems": 1, "uniqueItems": true,
      "items": { "type": "string", "pattern": "^(G[1-9][0-9]*|[a-z0-9-]+\\.z[1-5]\\.[0-9]+)$" }
    },
    "draws_on": {
      "type": "array", "uniqueItems": true,
      "items": { "type": "string", "pattern": "^[a-z0-9-]+\\.z[1-5]\\.[0-9]+$" }
    },
    "estimated_minutes": { "type": "integer", "minimum": 2, "maximum": 12 },
    "screens": { "type": "array", "minItems": 3, "maxItems": 12, "items": { "$ref": "#/definitions/screen" } },
    "checks": {
      "type": "array", "minItems": 1, "uniqueItems": true,
      "items": { "type": "string", "pattern": "^q-[a-z0-9-]+-[0-9]{2}$" }
    },
    "connects": {
      "type": "array", "minItems": 1, "uniqueItems": true,
      "items": { "type": "string", "pattern": "^G[1-9][0-9]*$" }
    },
    "status": { "type": "string", "enum": ["draft", "authored", "reviewed", "published"] }
  },
  "definitions": {
    "screen": {
      "oneOf": [
        { "type": "object", "additionalProperties": false, "required": ["type", "body"],
          "properties": { "type": { "const": "explanation" }, "heading": { "type": "string" }, "body": { "type": "string", "minLength": 1 } } },
        { "type": "object", "additionalProperties": false, "required": ["type", "body"],
          "properties": { "type": { "const": "key_point" }, "heading": { "type": "string" }, "body": { "type": "string", "minLength": 1 }, "formula": { "type": "string" } } },
        { "type": "object", "additionalProperties": false, "required": ["type", "body"],
          "properties": { "type": { "const": "example" }, "heading": { "type": "string" }, "body": { "type": "string", "minLength": 1 },
            "role": { "type": "string", "enum": ["investment-banking","private-equity","private-credit","asset-management","wealth-management","equity-research","hedge-funds","personal-investing","markets"] } } },
        { "type": "object", "additionalProperties": false, "required": ["type", "left", "right"],
          "properties": { "type": { "const": "comparison" }, "heading": { "type": "string" },
            "left":  { "type": "object", "additionalProperties": false, "required": ["label","body"], "properties": { "label": {"type":"string","minLength":1}, "body": {"type":"string","minLength":1} } },
            "right": { "type": "object", "additionalProperties": false, "required": ["label","body"], "properties": { "label": {"type":"string","minLength":1}, "body": {"type":"string","minLength":1} } },
            "verdict": { "type": "string" } } },
        { "type": "object", "additionalProperties": false, "required": ["type", "myth", "reality"],
          "properties": { "type": { "const": "misconception" }, "myth": { "type": "string", "minLength": 1 }, "reality": { "type": "string", "minLength": 1 }, "why_it_matters": { "type": "string" } } },
        { "type": "object", "additionalProperties": false, "required": ["type", "item"],
          "properties": { "type": { "const": "check" }, "item": { "type": "string", "pattern": "^q-[a-z0-9-]+-[0-9]{2}$" } } }
      ]
    }
  }
}
```

**Field justifications (one line each).** `id` stable, prefix-disjoint key · `title` learner-facing label · `teaches` the canonical concept(s) advanced — **graphRef grammar: global or node**, the drift-review anchor and future mastery key · `draws_on` the fact-check trail and node-change review hook (nodes only; may be empty when every `teaches` entry is itself a node) · `estimated_minutes` honest pacing shown on the path page · `screens` the lesson · `checks` ordered tooling index so analytics and mastery never parse screens · `connects` fuels the generated completion payoff, governed by the one-hop rule · `status` explicit lifecycle, **required** (no schema `default` populating absent data). Screen fields: `heading` optional card title · `body` the one idea · `formula` the styled key_point variant (not a 7th type) · `role` the application variant of `example` (not a 7th type) · `left`/`right`/`verdict` the disambiguation card · `myth`/`reality`/`why_it_matters` explicit confusion-naming · `item` a single item ref whose content lives in the item file.

## D3.2 Path schema (`schemas/path.schema.json`)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Path",
  "type": "object",
  "additionalProperties": false,
  "required": ["id", "title", "tagline", "description", "outcome", "audience", "lessons", "status"],
  "properties": {
    "id":          { "type": "string", "pattern": "^p-[a-z0-9-]+$" },
    "title":       { "type": "string", "minLength": 1 },
    "tagline":     { "type": "string", "minLength": 1 },
    "description": { "type": "string", "minLength": 1 },
    "outcome":     { "type": "string", "minLength": 1 },
    "audience":    { "type": "string", "minLength": 1 },
    "lessons": {
      "type": "array", "minItems": 1,
      "items": {
        "type": "object", "additionalProperties": false, "required": ["lesson", "requires"],
        "properties": {
          "lesson":   { "type": "string", "pattern": "^l-[a-z0-9-]+$" },
          "requires": { "type": "array", "uniqueItems": true, "items": { "type": "string", "pattern": "^l-[a-z0-9-]+$" } }
        }
      }
    },
    "status": { "type": "string", "enum": ["draft", "authored", "reviewed", "published"] }
  }
}
```

**Justifications.** `tagline`/`description`/`outcome`/`audience` are exactly the four landing-page copy slots — nothing more · `lessons[].requires` explicit per-step prerequisites (`uniqueItems`), default-linear by authoring convention, editorially overridable where the graph justifies branching; an empty array marks an entry lesson · `status` required. Total path duration is **derived** at render from the lesson files (layer 3), never stored — the drift test applied to our own data. *(Duplicate lessons within one path are impossible to express meaningfully and are rejected by validator check V-6; JSON Schema cannot express uniqueness on an object property alone.)*

## D3.3 Assessment-item schema (`schemas/assessment.schema.json`)

One file per lesson: `content/assessments/{lesson-id}.items.json`.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "AssessmentItemFile",
  "type": "object",
  "additionalProperties": false,
  "required": ["lesson", "items", "status"],
  "properties": {
    "lesson": { "type": "string", "pattern": "^l-[a-z0-9-]+$" },
    "status": { "type": "string", "enum": ["draft", "authored", "reviewed", "published"] },
    "items": {
      "type": "array", "minItems": 1,
      "items": {
        "type": "object", "additionalProperties": false,
        "required": ["id", "concept_ids", "type", "stem", "options"],
        "properties": {
          "id": { "type": "string", "pattern": "^q-[a-z0-9-]+-[0-9]{2}$" },
          "concept_ids": {
            "type": "array", "minItems": 1, "uniqueItems": true,
            "items": { "type": "string", "pattern": "^(G[1-9][0-9]*|[a-z0-9-]+\\.z[1-5]\\.[0-9]+)$" }
          },
          "type": { "type": "string", "enum": ["directional-reasoning","comparison","scenario","formula-interpretation","cause-effect","ordering"] },
          "stem": { "type": "string", "minLength": 1 },
          "options": {
            "type": "array", "minItems": 3, "maxItems": 4, "uniqueItems": true,
            "items": {
              "type": "object", "additionalProperties": false,
              "required": ["id", "text", "correct", "explanation"],
              "properties": {
                "id":          { "type": "string", "pattern": "^[a-d]$" },
                "text":        { "type": "string", "minLength": 1 },
                "correct":     { "type": "boolean" },
                "explanation": { "type": "string", "minLength": 1 }
              }
            }
          }
        }
      }
    }
  }
}
```

**Justifications.** `concept_ids` mandatory, graphRef grammar — the entire forward-compatibility story for a future mastery model, and the payload carried on the `question_answered` event · `type` the cognitive taxonomy (trivia is excluded by construction) · **single-choice only** in V1, so P1 ships exactly one check renderer — `ordering` items are posed as choose-the-correct-sequence, and no multi-select, free-response, or drag-and-drop renderer exists · `stem` the question · `options` 3–4, each with an `explanation` — correct-answer reinforcement and wrong-answer correction are where the teaching actually happens · `status` required on the file. Exactly-one-correct and contiguous option IDs are not expressible in draft-07 and are enforced by validator checks V-9 / V-10.

---

## D4 — Validator specifications

New module `pipeline/validate/checks/lesson_checks.py`, following the observed pattern **[AUDIT §4]**: functions with the signature `check_X(root, globals_, modules, nodes, errors, warnings) -> None`, imported into `validate.py` and called sequentially in `main()` after `check_new_modules(...)`. The module loads the layer-2 trees itself (the validator does not load them today) and computes everything **from canonical content**, with no dependency on generated `graph/*` being fresh.

**Failure policy.** All checks below emit **errors** (fail always, and therefore fail the strict merge gate). The one editorial dimension — whether a real connection is *worth surfacing* — is deliberately **not** mechanized and lives in the §5 review checklist of `LESSON_LAYER_DESIGN.md`. **Absent `content/lessons|paths|assessments/` directories are a vacuous pass**, so validation stays green before P0 content is installed.

### Group A — Schema and structural integrity
- **V-1** Every file in the three trees validates against its D3 schema (same `jsonschema` mechanism as the existing families).
- **V-2** Filename ↔ ID agreement: `{lesson-id}.json` matches its `id`; `{path-id}.json` matches its `id`; `{lesson-id}.items.json` matches its `lesson` field, which must name an existing lesson.
- **V-3** Lesson IDs unique across `content/lessons/`; path IDs unique across `content/paths/`; **assessment item IDs globally unique** across all of `content/assessments/`.

### Group B — Reference resolution (dangling refs)
- **V-4** Every `teaches[]` entry resolves: `G{n}` ∈ globals, `{slug}.z{z}.{n}` ∈ nodes. Every `draws_on[]` entry resolves as a node. Every `connects[]` entry resolves as a global. Every item `concept_ids[]` entry resolves as a global or a node. (Reuses the `gid_set` / `nid_set` construction of the existing `check_references`.) **`draws_on[]` conditional invariant:** if any `teaches[]` entry is a global ID, `draws_on[]` must be non-empty; if every `teaches[]` entry is a node ID, an empty `draws_on[]` is permitted.
- **V-5** Every path `lessons[].lesson` and every `requires[]` entry resolves to an existing lesson; no step requires itself; every `requires[]` target appears **earlier** in the same path (acyclic and topologically ordered by construction).
- **V-6** No path lists the **same lesson twice**.

### Group C — Lesson ↔ item coherence
- **V-7 (ordered equality)** The ordered list of `item` refs from a lesson's `check` screens must equal `checks[]` **exactly** — same members, same order, same length. Any duplicate in either list fails. *(This replaces the first draft's set equality, which silently tolerated reordering and duplicates.)*
- **V-8 (V1 item locality)** Every ID in a lesson's `checks[]` is defined in that lesson's own `{lesson-id}.items.json`. Item IDs remain globally unique so cross-lesson reuse can be enabled later by relaxing this single check.
- **V-9** Each item has **exactly one** option with `correct: true`.
- **V-10** Option IDs within an item are unique and form the contiguous prefix of `a, b, c, d` matching the option count (3 options → `a,b,c`; 4 → `a,b,c,d`).
- **V-11 (concept-tag coverage)** Every item has ≥1 resolving `concept_ids` entry, and every option carries a non-empty `explanation`. Every item is referenced by ≥1 lesson.
- **V-12 (misconception pairing, mechanical proxy)** Every lesson containing a `misconception` screen has ≥1 check whose `concept_ids` includes at least one of that lesson's `teaches[]` entries. The proxy proves a topical link exists; that the check tests *that specific confusion* is a review-checklist judgment (design §5, rule 5).

### Group D — Edge reality
- **V-13 (one-hop rule)** For each lesson, build the anchor set `teaches[] ∪ draws_on[]` and the allowed neighborhood exactly as specified in `LESSON_LAYER_DESIGN.md` §4:
  - anchor is a **node** → `connects_to[].ref` ∪ `{global_id}` ∪ `hosts_globals[]`
  - anchor is a **global** → `disambiguate_with[]` ∪ `{home_node}` ∪ `home_node.connects_to[].ref`

  Every `connects[]` entry must lie in the union of those neighborhoods. `home_node(G)` is the node whose `global_id == G`, or which lists `G` in `hosts_globals[]`. Error on any entry that does not.

---

## D5 — Learner-state and event contract

Three tiers, cleanly separated. **No analytics vendor is selected here, and no implementation code is specified.** This section exists so P1 invents no behavior.

| Tier | Store | Contents |
|---|---|---|
| Local progress state | `localStorage` | resume + gating state (below); never leaves the device except by explicit user export |
| Anonymous product analytics | event beacon (vendor chosen in P1) | the 8 events below, anonymous, opt-out-respecting |
| Future authenticated records | database, post-G1 | out of scope; the event shape below is designed to be replayable into it |

### D5.1 Event envelope

Every event carries:

| Field | Meaning |
|---|---|
| `schema_version` | Integer, `1` for V1 — lets a future ingestion pipeline interpret old events |
| `event_id` | Unique per event (client-generated UUID) — makes the stream idempotent and de-duplicable on retry |
| `session_id` | Unique per learner session (client-generated UUID, held for the session) — lets returns and within-session behavior be reconstructed without accounts |
| `anon_id` | Random UUID generated once and stored in `localStorage`; regenerating it creates a new anonymous learner. **Not** derived from any personal attribute |
| `ts` | ISO-8601 client timestamp |
| `path_id`, `lesson_id` | Optional context, present where the event has it |
| `props` | Event-specific properties (below) |

**No PII, no fingerprinting, no server-derived identity.** Testers see a one-line notice; an opt-out suppresses all sends while leaving local progress fully functional.

### D5.2 The eight events

| Event | Context | `props` |
|---|---|---|
| `path_started` | path | `{}` — first lesson of a path opened with no prior progress on it |
| `lesson_started` | path, lesson | `{}` |
| `screen_advanced` | path, lesson | `{ index: int (0-based index of the screen just left), screen_type }` |
| `question_answered` | path, lesson | `{ item_id, concept_ids[], option, correct: bool, attempt: int }` — `concept_ids` is denormalized onto the event so a mastery model is computable from the stream alone |
| `lesson_completed` | path, lesson | `{ seconds_active: int }` (visibility-aware timer — the time-per-lesson metric) |
| `session_ended` | path? | `{ seconds_active: int }` — best-effort on `visibilitychange`/`pagehide`; **known-lossy**, which is why drop-off analysis keys on the last `screen_advanced`, never on this event |
| `path_completed` | path | `{}` |
| `return_session` | — | `{ hours_since_last: number }` — emitted at app open when `now − last_activity_ts > N` |

**Return-session threshold: N = 8 hours** (single tunable constant). It separates "finished in one evening with breaks" from "came back another day," is short enough to catch a morning/evening same-day return, and — unlike a midnight boundary — is timezone-indifferent.

### D5.3 Local progress state

Key `flp.progress.v1`. Shape (illustrative, not code):

```
{
  schema_version: 1,
  anon_id: "<uuid>",
  last_activity_ts: "<iso>",
  paths: {
    "p-fi-foundations": { started_at, updated_at, completed_at | null }
  },
  lessons: {
    "l-fi-duration": {
      path_id, started_at, updated_at,
      last_screen_index: int,            // highest screen index reached — the resume point
      completed_at: <iso> | null,
      checks: {
        "q-fi-duration-01": {
          answered: true,
          attempts: [ { option: "b", correct: false, ts }, { option: "a", correct: true, ts } ]
        }
      }
    }
  }
}
```

`started_at` / `updated_at` / `completed_at` / `last_screen_index` / per-item `attempts` are exactly what the §8 behavioral contract requires — nothing more. No scores, no mastery values, no scheduling fields.

### D5.4 Behavioral semantics (V1) — restated from `LESSON_LAYER_DESIGN.md` §8

- **Prerequisites satisfied** when every lesson in the step's `requires[]` has a non-null `completed_at`. Empty `requires[]` ⇒ always available.
- **Locked lessons cannot be opened**; direct navigation redirects to the path page, where the lesson shows as locked.
- **An attempt is recorded on submit** of a selected option, and again on each retry.
- **Feedback is immediate**: correct/incorrect, the chosen option's explanation, plus the correct option's explanation when the answer was wrong. No score displayed.
- **A wrong answer never blocks progression.** Retry is available and optional.
- **Lesson complete** = advanced past the final screen **and** every `check` screen has ≥1 recorded attempt. (Questions cannot be skipped; they can be answered wrongly.)
- **Path complete** = every lesson in the path has a `completed_at`.
- **Resume** restores `last_screen_index`, with answered checks rendered in their answered state.

No grading systems, mastery thresholds, review queues, streaks, accounts, or server state are introduced by any of the above.
