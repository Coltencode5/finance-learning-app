# Module Factory

Milestone 5 adds safe infrastructure for creating future modules without
corrupting the nine active canonical modules.

## Purpose

- **Template** — `templates/module/` mirrors the canonical JSON structure
- **Scaffold script** — generates a draft five-zone module with placeholders
- **Validation gates** — `new_module_checks.py` enforces structure and new-global rules
- **Draft visibility** — draft modules are excluded from validation, graph build, and the app

## Module structure (actual repo conventions)

| Item | Convention |
|---|---|
| Metadata | `content/modules/{slug}/module.json` |
| Zones | `content/modules/{slug}/zones/z1.json` … `z5.json` |
| Node ID | `{slug}.z{zone}.{ordinal}` e.g. `private-equity.z1.5` |
| Local ID | `Z{zone}.{ordinal}` e.g. `Z1.5` |
| Global refs | `G{n}` in `connects_to` |
| Cross-module refs | `{other-slug}.z{zone}.{n}` |
| Gaps | `{ "kind": "source"\|"recency", "note": "..." }` on node `gaps` array |
| Graph edges | Derived from `connects_to` + `home_of` + `disambiguates` — never hand-edit `graph/` |

## Scaffold a module

```bash
# Preview (no files written)
python pipeline/scaffold/scaffold_module.py --slug sector-financials --title "Financials" --kind sector-layer1 --dry-run

# Create draft scaffold
python pipeline/scaffold/scaffold_module.py --slug sector-financials --title "Financials" --kind sector-layer1

# npm alias
npm run scaffold:module -- --slug sector-financials --title "Financials" --kind sector-layer1 --dry-run
```

The script:

- Validates slug format (`^[a-z][a-z0-9-]*$`)
- Rejects duplicate slugs
- Assigns `build_order` automatically (next sequential slot; see draft band below)
- Sets `visibility: draft` and `status: in-progress`
- Creates one placeholder front-door node per zone (`connects_to: []`)

## Build order convention

| Range | Use |
|---|---|
| `1`–`899` | Real modules — claim the next sequential slot via `next_build_order()` |
| `≥ 900` | Draft/scaffold placeholders — excluded from the sequential counter |

Draft modules may use `build_order: 999` (or any slot in the `≥ 900` band) to avoid
colliding with the sequential active-module counter. Draft modules in the sentinel
band are still excluded from validation, graph build, and the app.

## Active vs draft

| `visibility` | Validation | Graph build | App home page |
|---|---|---|---|
| `active` (default) | Full checks | Included | Shown |
| `draft` | Excluded | Excluded | Hidden (set `SHOW_DRAFT_MODULES=1` to reveal) |

Promote a module when content is ready:

```json
"visibility": "active"
```

Then run strict validation and rebuild the graph.

## Validation commands

```bash
python pipeline/validate/validate.py --strict   # active modules only
python pipeline/build/build_graph.py
npm run check:data
python -m unittest pipeline.scaffold.test_scaffold_module
```

### New-module rules (active modules)

- Five zone files (`z1.json`–`z5.json`) required
- Node IDs must match `{slug}.z{1-5}.{n}`
- New globals must start at **corpus_max + 1** (currently G236 after the nine
  role modules) and be contiguous
- New globals must not collide on normalized terms with existing glossary
- Active modules must appear in `graph/by_module.json` after graph build

## What not to do

- Do not add finance content during scaffolding — use placeholders
- Do not set `visibility: active` until validation passes
- Do not hand-edit `derived` blocks in `module.json`
- Do not make Markdown canonical — JSON only
- Do not skip validation after adding zones or globals

## Module 10 — Macro & Economics

`content/modules/macro-economics/` is migrated from
`legacy/markdown/Macro_Economics_Module_Node_Map.md` via
`pipeline/migrate/parse_macro.py`. It uses `kind: core-concept` and a
concept-progression zone spine per ADR-002.

## Sector modules (Milestone 8+)

Use `--kind sector-layer1` or `--kind sector-layer2` to scaffold with the canonical
sector spine placeholders (ADR-003). See `docs/SECTOR_LAYER_DESIGN.md` for the
standing build checklist.

## Tests

```bash
python -m unittest pipeline.scaffold.test_scaffold_module
```

Covers: dry-run plan, file creation, duplicate slug rejection, malformed slug
rejection, and broken `connects_to` detection.
