# Graph Health & Generated Artifacts

Milestone 3 adds inspectable graph outputs on top of canonical `content/`.
Nothing under `graph/` is hand-edited — regenerate with the build pipeline.

## Canonical vs. experimental

| Artifact | Status | Purpose |
|---|---|---|
| `content/**` | **Canonical** | Source of truth |
| `graph/graph.json` | **Generated (canonical edges)** | Edge list from `connects_to`, `home_of`, `disambiguates` |
| `graph/inbound.json` | **Generated** | Reverse lookup: who points to each node/global |
| `graph/outbound.json` | **Generated** | Forward lookup: what each node/global points to |
| `graph/by_module.json` | **Generated** | Per-module edge subset |
| `graph/most_referenced_globals.json` | **Generated** | Globals ranked by inbound reference count |
| `graph/orphan_low_reference.json` | **Generated** | Orphan nodes, low-edge nodes, low-ref globals |
| `graph/cross_module_edges.json` | **Generated** | Reference edges spanning modules |
| `graph/module_dependencies.json` | **Generated** | Cross-module reference counts |
| `graph/graph_health_report.md` | **Generated** | Human-readable summary |
| `graph/prerequisites.json` | **Experimental** | Suggested learning order — **not canonical** |

## Regenerate

```bash
python pipeline/build/build_graph.py
python pipeline/validate/validate.py
python pipeline/validate/validate.py --strict   # content gate only
```

`build_graph.py` rebuilds `graph.json` and all derived indexes, the health
report, and experimental prerequisites in one pass.

## Edge kinds

| Kind | Source |
|---|---|
| `references` | Node `connects_to` |
| `home_of` | Node `global_id` or `hosts_globals` |
| `disambiguates` | Global `disambiguate_with` in `globals.json` |
| `prerequisite` | Reserved; not written to canonical content (experimental file only) |

Disambiguation edges are created **only** from explicit `disambiguate_with`
metadata. Legacy prose “this vs. that” pairs (e.g. alpha vs. beta) do not
become edges until a global pair is recorded in `globals.json`.

The current pair list and count live in the **generated**
`graph/graph_health_report.md` section “Disambiguation edges (canonical metadata
only)” — do not duplicate pairs here; they change as globals are added.

## Interpreting orphan / low-reference reports

**Orphan nodes** have zero inbound and zero outbound edges in `graph.json`.
Often these are front-door nodes (Z1.1) that only receive links later, or
nodes missing `connects_to`. Review before treating as content bugs.

**Low-reference nodes** have ≤2 total edges. May be leaf concepts or gaps in
cross-linking.

**Low-reference globals** have fewer than 2 inbound `references`/`home_of`
edges. These are *candidate demotions* or missing cross-module links — an
architect/content call, not an engineering failure. The validator emits
`[graph]` warnings for human review (non-fatal unless `--strict`).

## Graph checks in validation

`pipeline/validate/checks/graph_checks.py` is wired into `validate.py`:

- Self-edges → warning
- Orphan nodes → warning
- Globals referenced &lt;2 times → warning

Use `--strict` for CI-parity **content** validation (graph-quality warnings are
skipped). Normal `validate.py` includes `[graph]` warnings summarized in
`graph/graph_health_report.md`.

## Prerequisites (experimental)

`graph/prerequisites.json` suggests possible prerequisite relationships per
module using:

1. Zone + ordinal order (immediate predecessor)
2. Same-module `connects_to` targets that appear earlier in that order

**Do not** import this into the app or write it back to `content/` without an
explicit Milestone decision.
