# finance-graph

The content platform for a finance education app built on a shared knowledge
graph: 12 modules, 292 global glossary concepts, 591 zone learning nodes,
4,185 graph edges — all as validated, structured JSON.

## The one rule

**`content/` (JSON) is the single source of truth.** The original markdown
node maps live frozen in `legacy/markdown/` for provenance only. Derived
artifacts (`graph/graph.json`, module `derived` blocks, rendered markdown) are
build outputs — never hand-edit them. See `docs/decisions/ADR-001`.

## Layout

```
schemas/            JSON Schemas: global, node, module, activity, edge
content/
  glossary/         globals.json — the shared glossary (G1–G292), the app's spine
  modules/{slug}/   module.json + zones/z1..z5.json per module
  activities/       learning activities (empty in V0; schema is ready)
graph/              graph.json + derived indexes (do not edit; see docs/GRAPH_HEALTH.md)
pipeline/
  migrate/          parse_markdown.py — one-time legacy migration (done)
  build/            build_graph.py, render_markdown.py
  validate/         validate.py — the correctness gate
  prompts/          reusable Cursor/LLM prompts per milestone
docs/               architecture, five-zone template, ADRs, defect register
legacy/markdown/    the original node maps, incl. macro (read-only reference)
app/                Next.js App Router pages (Milestone 4)
src/lib/graph/      Typed data access layer (reads content/ + graph/)
scripts/            App data check script
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

## Current state (post-Milestone 9)

- **12 active modules**: the 9 legacy role modules plus **macro-economics**
  (`kind: core-concept`, ADR-002), **fixed-income** (`kind: asset-class`, ADR-003),
  and **sector-financials** (`kind: sector-layer1`, ADR-003 — wave one, M9).
- Shared glossary: **292 globals (G1–G292)**, contiguous; sector-financials
  contributed G286–G292. The new-module gate is parameterized to `corpus_max + 1`,
  so the next active module starts at **G293**.
- **591 zone nodes**; graph rebuilt — 4,185 edges.
- Validation: **0 errors, 0 warnings** (strict content gate).
- See `PROJECT_STATUS.md` for milestone history and corpus totals.
- Module factory (Milestone 5) scaffolds new draft modules with kind-appropriate
  zone placeholders (`role`, `core-concept`, `sector-layer1`, `sector-layer2`).
- **Minimal Next.js app** (Milestone 4) reads canonical JSON at build time — no database, no auth.

## Milestone 4 — minimal app

Proof that canonical JSON powers a real product shell:

```bash
pip install jsonschema          # optional; required for --strict
python pipeline/validate/validate.py --strict
python pipeline/build/build_graph.py

npm install
npm run check:data              # verify JSON + graph indexes load
npm run typecheck
npm run dev                     # http://localhost:3000
npm run build                   # static production build
```

### Routes

| Route | Purpose |
|---|---|
| `/` | Module list (all active modules) |
| `/modules/[slug]` | Zone/node listing for one module |
| `/concepts/[id]` | Global (G1) or node (private-equity.z1.5) detail + graph refs |

### Sample URLs

- http://localhost:3000/
- http://localhost:3000/modules/private-equity
- http://localhost:3000/concepts/G1
- http://localhost:3000/concepts/G29
- http://localhost:3000/concepts/private-equity.z1.5

Data loading is centralized in `src/lib/graph/` — page components do not read the filesystem directly.

See `docs/MODULE_FACTORY.md` for scaffolding new modules (Milestone 5).

## Contributing content

1. Edit JSON under `content/` (or use pipeline tooling).
2. Run the validator; fix errors.
3. Rebuild the graph.
4. CI (`.github/workflows/validate.yml`) enforces the same gate on every PR.

New modules follow `docs/five_zone_template.md` — the template is locked.
