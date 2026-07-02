# finance-graph

The content platform for a finance education app built on a shared knowledge
graph: 9 modules, 235 global glossary concepts, 478 zone learning nodes,
3,357 graph edges — all as validated, structured JSON.

## The one rule

**`content/` (JSON) is the single source of truth.** The original markdown
node maps live frozen in `legacy/markdown/` for provenance only. Derived
artifacts (`graph/graph.json`, module `derived` blocks, rendered markdown) are
build outputs — never hand-edit them. See `docs/decisions/ADR-001`.

## Layout

```
schemas/            JSON Schemas: global, node, module, activity, edge
content/
  glossary/         globals.json — the shared glossary (G1–G235), the app's spine
  modules/{slug}/   module.json + zones/z1..z5.json per module
  activities/       learning activities (empty in V0; schema is ready)
graph/              graph.json + derived indexes (do not edit; see docs/GRAPH_HEALTH.md)
pipeline/
  migrate/          parse_markdown.py — one-time legacy migration (done)
  build/            build_graph.py, render_markdown.py
  validate/         validate.py — the correctness gate
  prompts/          reusable Cursor/LLM prompts per milestone
docs/               architecture, five-zone template, ADRs, defect register
legacy/markdown/    the nine original node maps (read-only reference)
app/                Next.js app (Milestone 4)
```

## Commands

```bash
python3 pipeline/validate/validate.py            # must pass before any commit
python3 pipeline/validate/validate.py --strict   # content-only strict gate
python3 pipeline/build/build_graph.py            # regenerate graph + indexes + health report
python3 pipeline/migrate/parse_markdown.py       # re-run migration (idempotent;
                                                 # only until M2 sign-off)
```

See `docs/GRAPH_HEALTH.md` for generated graph artifacts and how to interpret
orphan/low-reference reports.

Requires Python 3.10+; `pip install jsonschema` for full schema validation
(structural checks run without it).

## Current state (post-Milestone 2)

- Migration complete: all 9 legacy modules parsed to canonical JSON.
- Validation: **0 errors, 0 warnings** (strict content gate).
- Graph health indexes and reports generated under `graph/` (Milestone 3).
- See `docs/MIGRATION_DEFECTS.md` for resolved migration defects.

## Contributing content

1. Edit JSON under `content/` (or use pipeline tooling).
2. Run the validator; fix errors.
3. Rebuild the graph.
4. CI (`.github/workflows/validate.yml`) enforces the same gate on every PR.

New modules follow `docs/five_zone_template.md` — the template is locked.
