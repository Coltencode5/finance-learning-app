# Cursor Prompts — Milestones 2–5

Each prompt is self-contained: paste it into Cursor at the repo root. Every
milestone ends at a human review checkpoint; do not chain milestones in one
session.

---

## Milestone 2 — Content repair & canonical lock (~3–4 h)

```
You are working in the finance-graph repo. Read README.md, docs/decisions/ADR-001,
docs/five_zone_template.md, and docs/MIGRATION_DEFECTS.md before changing anything.

Tasks, in order:
1. For each OPEN defect in docs/MIGRATION_DEFECTS.md section A: open the
   referenced node's connects_to_raw in content/modules/.../zones/, read the
   surrounding context in legacy/markdown/ if needed, apply the "likely intent"
   fix to the connects_to entry in the JSON (never edit legacy/), and set the
   defect row to DECIDED with a one-line justification. If intent is genuinely
   ambiguous, leave OPEN and add a question for the reviewer.
2. Record the IPO dual-lens pair: add G102 to G53.disambiguate_with and vice
   versa in content/glossary/globals.json.
3. Host-node assignment (defect register section C): add a "hosts_globals"
   array field to schemas/node.schema.json (list of G-ids, default []). For each
   of the 45 orphan globals, find the zone node whose legacy text contains its
   deep explainer (the global's home_zone column is the strong hint) and add the
   G-id to that node's hosts_globals. Update pipeline/validate/validate.py so the
   "no hosting zone node" check accepts either global_id or hosts_globals.
4. Attach the consolidated Part 9 gaps from ER/VC/RE (see legacy files) to the
   correct nodes' gaps fields (~12 items).
5. Write pipeline/build/render_markdown.py: renders each module back to a
   markdown file in a build/ directory (gitignored) matching the canonical
   heading format in docs/five_zone_template.md. This is a review surface, not
   a source file.
6. Run: python3 pipeline/validate/validate.py — target: 0 errors. Warnings
   only for items explicitly deferred in the defect register.

Do not renumber any existing G-number or node ID. Do not edit graph/graph.json
by hand. Commit in small steps with the defect number in each message.

STOP after validation passes. Output: the validation summary, the updated
defect register, and a diff summary for human review.
```

**Expected output:** 0 validation errors; defect register fully DECIDED/FIXED;
`hosts_globals` live; render_markdown.py producing readable module docs.

**Human checkpoint:** review every section-A fix against its legacy context
(11 items, ~20 minutes); spot-check 5 of the 45 host-node assignments.

---

## Milestone 3 — Graph completion & derived views (~3 h)

```
Read README.md and schemas/edge.schema.json.

1. Extend pipeline/build/build_graph.py:
   - add "disambiguates" edges from globals' disambiguate_with fields
   - add reverse-lookup index files: graph/inbound.json (target → [sources])
     and graph/by_module.json (module → its edge subset), both generated.
2. Add pipeline/validate/checks/graph_checks.py, wired into validate.py:
   - no self-edges
   - warn on nodes with zero inbound AND zero outbound edges (orphans)
   - warn on globals referenced fewer than 2 times (candidate demotions)
3. Add a prerequisite derivation pass (behind a flag, output to
   graph/prerequisites.json): topological ordering per module using zone order
   + ordinal as the base sequence and connects_to as hints. Mark it
   experimental; no UI consumption yet.
4. Regenerate everything; validation must pass; CI stays green.

STOP. Output: edge/orphan/low-reference statistics for human review.
```

**Human checkpoint:** review the orphan and low-reference lists — they are
candidate content bugs or demotions, an Opus/architect call, not an engineering
call.

---

## Milestone 4 — Minimal Next.js app (~4 h)

```
Read README.md. Build the V0 reading app in app/ with Next.js (App Router,
TypeScript). No database: read the JSON in content/ and graph/ directly at
build time (static generation). No auth, no styling framework beyond minimal
CSS, no client state libraries.

Pages:
1. /                     — module list from content/modules/*/module.json
                           (title, zone count, derived stats)
2. /m/[slug]             — module page: five zones, each zone's nodes in
                           ordinal order with quick definitions
3. /m/[slug]/[nodeId]    — node page: title, tag, quick definition, explainer
                           bullets, connects_to rendered as links (globals link
                           to /g/[gid], nodes to their node pages), gaps shown
                           as flagged callouts
4. /g/[gid]              — concept page: term, definition, category, home
                           module link, "appears in" via graph/inbound.json

Add a lib/content.ts data layer that is the ONLY code reading the JSON files,
typed against the schemas (generate TS types from schemas/ with
json-schema-to-typescript). Every ref string resolves through one function.

Acceptance: `npm run build` succeeds with zero broken internal links —
add a build-time link check that walks every rendered ref through the same
resolver the validator uses.

STOP. Output: build log and the route list.
```

**Human checkpoint:** click through PE Z1.5 (Capital Calls) → G16 → its home
node and back; confirm the graph feels connected, which is the product's core
claim.

---

## Milestone 5 — Module-10 pipeline dry run (~2 h setup + content work)

```
Read docs/five_zone_template.md and pipeline/prompts/.

1. Create content/modules/macro-economics/ scaffolding: module.json
   (kind: "core-concept", build_order: 10, zones titled per the existing Macro
   draft), empty zones files.
2. Write pipeline/migrate/import_macro.py adapting parse_markdown.py to ingest
   the in-progress Macro markdown (same node grammar) once provided.
3. Add pipeline/validate/checks/new_module_checks.py: a new module's globals
   must start at exactly G236 and be contiguous; must not redefine any
   normalized term already in globals.json (error, not warning, for new
   modules).
4. Prove the gate: add a deliberately duplicated term to a scratch fixture and
   show the validator rejects it; then remove the fixture.

STOP. Output: the passing + failing validation runs.
```

**Human checkpoint:** this is where the architect (Opus) re-enters — the Macro
module's remaining zones get built as JSON against this scaffold, with the
validator running after every zone instead of once at the end.
