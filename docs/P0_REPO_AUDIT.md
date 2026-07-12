# P0 Read-only repository audit — finance-learning-app

**Date:** 2026-07-11  
**Scope:** Factual reconnaissance for lesson/path presentation-layer design. No design proposals except labelled observations in §8.  
**Corpus at audit:** 313 globals (G1–G313), 14 active modules, 615 zone nodes, 4433 graph edges.

## Commands run

```text
pwd; ls; node -v; npm -v
Get-ChildItem / Get-ChildItem -Recurse (content, app, schemas, pipeline, etc.)
Test-Path vercel.json .env .env.local .env.example eslint.config.* .eslintrc*
python -c (globals sample / node sample / hosts_globals / jsonschema version)
python --version
python pipeline/validate/validate.py --strict
npm run typecheck
npm run check:data
npm run build
npm run lint
python -m unittest pipeline.scaffold.test_scaffold_module
npm run
Get-Content package.json, next.config.ts, validate.yml, schemas/*, src/lib/graph/*, app pages
rg / Grep across src, app, docs, pipeline for lesson|quiz|progress|localStorage|SHOW_DRAFT|home_of|etc.
```

Environment observed: Node `v24.18.0`, npm `11.16.0`, Python `3.12.10`, `jsonschema 4.26.0`. Package manager: **npm** (`package-lock.json` present). No `engines` field, no `.nvmrc` / `.node-version`.

---

## 1. Graph data shapes

### Global entry (`content/glossary/globals.json` + `schemas/global.schema.json`)

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | string `^G[1-9][0-9]*$` | yes | Append-only G-number |
| `term` | string (minLength 1) | yes | |
| `quick_definition` | string (minLength 1) | yes | |
| `home_module` | string | yes | Module slug |
| `home_zone` | string\|null `^Z[1-5](\.[0-9]+)?$` | yes | May be null |
| `contributed_by` | string | yes | Usually equals `home_module` |
| `category` | string | yes | |
| `aliases` | string[] | optional (default `[]`) | |
| `appears_in` | string[] | optional (default `[]`) | Informational |
| `disambiguate_with` | string[] of G-ids | optional (default `[]`) | Becomes `disambiguates` edges at graph build |
| `status` | enum `mapped\|expanded\|reviewed\|published` | optional (default `mapped`) | |

`additionalProperties: false`.

**Representative entry (simple):**

```json
{
  "id": "G2",
  "term": "MOIC / Multiple of Money",
  "aliases": [],
  "quick_definition": "The absolute multiple capital returns — total value ÷ capital invested (e.g., 2.5×); ignores time.",
  "home_module": "private-equity",
  "home_zone": "Z5",
  "contributed_by": "private-equity",
  "category": "Returns & Performance metrics",
  "appears_in": ["Z1", "Z2", "Z3", "Z4", "Z5"],
  "disambiguate_with": [],
  "status": "mapped"
}
```

**Representative entry (with disambiguation):**

```json
{
  "id": "G20",
  "term": "LPA (Limited Partnership Agreement)",
  "aliases": ["Limited Partnership Agreement"],
  "quick_definition": "The fund's governing contract — mandate, economics, governance, and LP–GP rights.",
  "home_module": "private-equity",
  "home_zone": "Z5",
  "contributed_by": "private-equity",
  "category": "Fund economics & structure",
  "appears_in": ["Z1", "Z3", "Z5"],
  "disambiguate_with": ["G306"],
  "status": "mapped"
}
```

Corpus at audit time: **313 globals**, `G1`–`G313`.

### Zone node (`content/modules/{slug}/zones/z{1-5}.json` + `schemas/node.schema.json`)

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | string `^[a-z0-9-]+\.z[1-5]\.[0-9]+$` | yes | e.g. `private-equity.z1.5` |
| `module` | string | yes | Module slug |
| `zone` | integer 1–5 | yes | |
| `ordinal` | integer ≥1 | yes | Position in zone sequence |
| `title` | string | yes | |
| `tag` | enum `core\|process\|branch\|global` | yes | `global` ⇒ home explainer |
| `quick_definition` | string | yes | |
| `explainer_covers` | string[] (minItems 1) | yes | |
| `connects_to` | `{ref, note?}[]` | yes | Authoritative edge source; `ref` is `G{n}` or `{slug}.z{z}.{n}` |
| `local_id` | string `^Z[1-5]\.[0-9]+$` | optional | Human-facing e.g. `Z1.5` |
| `global_id` | string\|null G-id | optional | If `tag=='global'`, required by validator |
| `hosts_globals` | G-id[] | optional (default `[]`) | Deep explainers hosted without `tag: global` |
| `connects_to_raw` | string\|null | optional | Legacy free-text |
| `gaps` | `{kind: source\|recency, note, needed_source?}[]` | optional (default `[]`) | |
| `real_world_layer` | string\|null | optional | |
| `source_refs` | `{source, location?}[]` | optional (default `[]`) | |
| `status` | enum | optional (default `mapped`) | |

**Not present as node fields:** `home_of`, `disambiguate_with`.

- `home_of` is a **generated edge kind** in `graph/graph.json`, emitted by `pipeline/build/build_graph.py` from `global_id` / `hosts_globals`.
- `disambiguate_with` lives on **globals**; graph build emits `disambiguates` edges.

**Representative global-hosting node (`tag: global`):**

```json
{
  "id": "asset-management.z1.3",
  "local_id": "Z1.3",
  "module": "asset-management",
  "zone": 1,
  "ordinal": 3,
  "title": "Active vs. Passive Investing — The Defining Split",
  "tag": "global",
  "global_id": "G137",
  "quick_definition": "The choice that organizes the entire discipline: passive investing buys and holds the whole market at minimal cost and accepts the market's return; active investing tries to beat a benchmark through security selection or timing, and charges more for the attempt.",
  "explainer_covers": ["…"],
  "connects_to": [
    {"ref": "hedge-funds.z1.3", "note": null},
    {"ref": "asset-management.z2.1", "note": null},
    {"ref": "G138", "note": null}
  ],
  "connects_to_raw": "`★ G138` index fund, …",
  "gaps": [],
  "real_world_layer": null,
  "source_refs": [],
  "status": "mapped"
}
```

**Representative local node (`tag: core`, with `gaps`):**

```json
{
  "id": "asset-management.z1.1",
  "local_id": "Z1.1",
  "module": "asset-management",
  "zone": 1,
  "ordinal": 1,
  "title": "What Is Asset Management?",
  "tag": "core",
  "global_id": null,
  "quick_definition": "The business of investing other people's money in public, mostly liquid securities — stocks and bonds — on their behalf, for a fee, under a fiduciary duty, with the goal of meeting a benchmark or a long-term objective rather than chasing absolute returns at any cost.",
  "explainer_covers": ["…"],
  "connects_to": [
    {"ref": "hedge-funds.z1.1", "note": null},
    {"ref": "G137", "note": null}
  ],
  "connects_to_raw": "…",
  "gaps": [
    {
      "kind": "recency",
      "note": "a current source for the modern scale, the Big Three, and the passive tipping point (recency",
      "needed_source": null
    }
  ],
  "real_world_layer": null,
  "source_refs": [],
  "status": "mapped"
}
```

Also present in corpus: nodes with `hosts_globals`, e.g. `asset-management.z1.5` hosts `["G152","G153"]` with `tag: "core"`, `global_id: null`.

### ID formats and generation / contiguity

| Entity | Format | Example |
|---|---|---|
| Module slug | `^[a-z0-9-]+$` (scaffold: `^[a-z][a-z0-9-]*$`) | `fixed-income` |
| Zone (module.json) | integer 1–5 | `3` |
| Local zone node | `Z{1-5}.{n}` | `Z1.5` |
| Node ID | `{slug}.z{1-5}.{n}` | `fixed-income.z2.4` |
| Global ID | `G{n}` (`^G[1-9][0-9]*$`) | `G313` |
| Activity ID (schema only) | `^A[1-9][0-9]*$` | not present in content |

**Where logic lives:**

- Next G-id: `pipeline/lib/module_utils.py` → `corpus_max_g()`, `next_global_id()` → `f"G{max+1}"`.
- Scaffold prints next id: `pipeline/scaffold/scaffold_module.py`.
- Contiguity from G1: `pipeline/validate/validate.py` → `check_ids`.
- New-module contiguous block from `corpus_max+1`: `pipeline/validate/checks/new_module_checks.py` → `check_new_module_globals`.
- Node ordinal contiguity per zone: `check_ids` (warnings, not errors).
- Architecture rule (ADR / workspace): G-numbers are append-only; never renumber or reuse.

---

## 2. Graph access layer

Directory: `src/lib/graph/` (`index.ts`, `load.ts`, `types.ts`, `check.ts`, `RefLink.tsx`).

### How canonical JSON is loaded

**Runtime `fs` read from `process.cwd()`, not static JSON imports.** `load.ts`:

- `fs.readFileSync` + `JSON.parse` via `readJson()`.
- Reads: `content/glossary/globals.json`, each active `content/modules/{slug}/module.json` + `zones/z*.json`, and generated `graph/graph.json`, `graph/inbound.json`, `graph/outbound.json`, `graph/module_dependencies.json`.
- Draft modules (`visibility: "draft"`) excluded from store nodes/modules; listed separately via `getDraftModulesFromDisk()`.
- Singleton cache: first `getStore()` builds `DataStore`; `resetStore()` clears it.
- Types are **hand-written TypeScript interfaces** in `types.ts` (not codegen from schemas).
- Used during Next.js SSG (`generateStaticParams` + page render at build); pages do not call `fs` directly.

### Public exports

**From `index.ts` (primary app API):**

```ts
getAllModules(): Module[]
getActiveModules(): Module[]
getDraftModules(): Module[]
getModule(moduleSlug: string): Module | undefined
getNodesByModule(moduleSlug: string): ModuleNode[]
getGlobalConcept(globalId: string): GlobalConcept | undefined
getNode(nodeId: string): ModuleNode | undefined
getConceptOrNode(id: string): ConceptOrNode | undefined  // G* → global else node
getInboundReferences(id: string): InboundRef[]
getOutboundReferences(id: string): OutboundRef[]
getConnectedNodes(id: string): ModuleNode[]  // outbound targets that are nodes only
getModuleDependencies(moduleSlug: string): Record<string, number> | undefined
resolveRefLabel(ref: string): string
refExists(ref: string): boolean
conceptHref(id: string): string  // `/concepts/${encodeURIComponent(id)}`
moduleHref(slug: string): string
searchConcepts(query: string): ConceptOrNode[]  // max 30
getAllConceptIds(): string[]
getDisplayTitle(item: ConceptOrNode): string
getHomeNodeForGlobal(globalId: string): ModuleNode | undefined
```

**From `load.ts`:** `DataStore`, `getDraftModulesFromDisk()`, `getStore()`, `resetStore()`, `REQUIRED_FILES`, `verifyRequiredFiles()`.

**From `types.ts`:** interfaces + `isGlobalConcept`, `isModuleNode`.

**From `check.ts`:** `CheckResult`, `runDataCheck()`, re-export `REQUIRED_FILES`.

**From `RefLink.tsx`:** `RefLink({ id })`, `ReferenceList({ title, refs, direction })`.

---

## 3. Routes and components

Next.js App Router under `app/`. No other page components under `src/` (only `src/lib/graph/`).

| Path | Static/dynamic | Component / behavior |
|---|---|---|
| `/` | Static (`○`) | `app/page.tsx` — `HomePage`; lists active modules via `getActiveModules()`; optional drafts if `SHOW_DRAFT_MODULES=1` |
| `/modules/[moduleSlug]` | SSG (`●`) via `generateStaticParams` → active module slugs | `app/modules/[moduleSlug]/page.tsx` — zones + node list with `quick_definition`, links to concepts |
| `/concepts/[...id]` | SSG (`●`) via `generateStaticParams` → all G-ids + node ids | `app/concepts/[...id]/page.tsx` — global or node detail, explainer bullets, inbound/outbound `ReferenceList` |
| `/_not-found` | Static | `app/not-found.tsx` |
| layout | — | `app/layout.tsx` — header/nav/footer; footer states “No auth, no database” |

Build reported **946** static pages (home + not-found + ~928 concepts + 14 modules).

### Display / reuse candidates for a lesson player

| Piece | Role |
|---|---|
| `RefLink` | Resolves ID → label + `/concepts/...` link; missing-ref UI |
| `ReferenceList` | Inbound/outbound graph lists |
| Concept page body | Quick definition + `explainer_covers` bullets + home-node link for globals |
| Module page `article.node-item` | Compact node card (tag, title, id, quick_definition) |
| `getConceptOrNode` / `refExists` / `resolveRefLabel` | ID lookup primitives |
| `conceptHref` / `moduleHref` | URL helpers |

No dedicated lesson/path/quiz UI components. No shared component library beyond the above.

---

## 4. Validation

### Locations

- `pipeline/validate/validate.py` — main gate; check families: schema, ids, references, duplicates, required; then `check_new_modules`; optionally `check_graph` (skipped when `--strict`).
- `pipeline/validate/checks/graph_checks.py` — `check_graph(...)` (self-edges, orphans, low-ref globals) → warnings.
- `pipeline/validate/checks/new_module_checks.py` — `check_new_modules(...)` (five zones, ID patterns, kind placeholders, sector compactness, new-global contiguity, `by_module.json` presence).
- App-side: `src/lib/graph/check.ts` + `npm run check:data` (file presence + broken `connects_to`).

### Registration pattern

Checks are **imported and called sequentially in `main()`**, not a plugin registry:

```python
check_schema(...)
check_ids(...)
check_references(...)
check_duplicates(...)
check_required(...)
check_new_modules(...)   # from checks/new_module_checks.py
if not args.strict:
    check_graph(...)     # from checks/graph_checks.py
```

### Strict command

```bash
python pipeline/validate/validate.py --strict
```

Audit run: `content: 313 globals, 14 modules, 615 zone nodes` → **0 errors, 0 warnings**, exit 0.

CI (`.github/workflows/validate.yml`): same `--strict`, then `build_graph.py` + `git diff --exit-code graph/`, then `npm ci`, `check:data`, `typecheck`, `build`. Node **22** in CI.

### Extension point for a new check (e.g. dangling refs over a new subtree)

Observed pattern:

1. Add `pipeline/validate/checks/<name>_checks.py` with a function signature like  
   `def check_X(root: Path, globals_, modules, nodes, errors: list[str], warnings: list[str]) -> None`.
2. Import it in `validate.py` and call it from `main()` after content load, appending to `errors` / `warnings`.
3. Errors fail always; warnings fail only with `--strict`.
4. Existing dangling-ref pattern for graph IDs is in `check_references`: build `gid_set` / `nid_set`, walk refs, `errors.append(f"[refs] … dangling …")`.

Activity schema exists (`schemas/activity.schema.json`); **no activity files** under `content/activities/` except `.gitkeep`. Validator does **not** currently load activities/lessons/paths.

---

## 5. Build, types, test

| Action | Command | Result at audit |
|---|---|---|
| Dev server | `npm run dev` (`next dev`) | not started (inspect-only); script present |
| Production build | `npm run build` | **PASS** exit 0; Next.js 15.5.20; 946 static pages |
| Type-check | `npm run typecheck` (`tsc --noEmit`) | **PASS** exit 0 |
| Lint | `npm run lint` | **not present** — `npm error Missing script: "lint"`; no eslint config files |
| App data check | `npm run check:data` | **PASS** (14 modules, 615 nodes, 313 globals, 4433 edges) |
| Scaffold tests | `npm run test:scaffold` / `python -m unittest pipeline.scaffold.test_scaffold_module` | **PASS** — 5 tests, OK |
| Content validate | `python pipeline/validate/validate.py --strict` | **PASS** |

**Node / package manager:** Node `v24.18.0` locally; CI uses Node `22`; **npm** + `package-lock.json`. No `engines` pin.

**Build warning (factual):** Next.js detected multiple lockfiles and selected `C:\Users\cfroo\package-lock.json` as workspace root (parent of the repo), in addition to the repo’s own lockfile.

---

## 6. Pre-existing product-ish code

| Topic | Status |
|---|---|
| `content/lessons/` | **not present** |
| `content/paths/` | **not present** |
| Lessons / paths UI or routes | **not present** in `app/` / `src/` |
| Quizzes / assessments (authored) | Schema only: `schemas/activity.schema.json` includes `"quiz"` in `type` enum; `content/activities/` has only `.gitkeep` — **no activity JSON** |
| Progress / learner state | **not present** in app code |
| `localStorage` / `sessionStorage` | **not present** under `src/` or `app/` |
| Analytics / events | **not present** in app code |
| User accounts / auth | **not present**; layout footer: “No auth, no database” |
| Product docs (planning only) | `PRODUCT_STATUS.md` (“P0 not yet started”); `docs/OPERATING_ROADMAP.md` describes future lesson/path/localStorage (design text, not code) |
| Architecture aspirational mentions | `docs/architecture.md` mentions quizzes / progress as product intent; also “No user accounts or progress tracking” |

---

## 7. Vercel / deployment readiness

| Item | Status |
|---|---|
| `vercel.json` | **not present** |
| Framework | Next.js 15 (`next.config.ts`: `reactStrictMode: true` only) |
| `output: 'export'` | **not set** — standard Next build (Node server / Vercel Next preset), not pure static export |
| Env vars in code | `SHOW_DRAFT_MODULES === "1"` on home page only; no `.env` / `.env.example` / `.env.local` in repo |
| Production build | Succeeds; all routes prerendered static/SSG; deployable as a normal Next.js app **if** `content/` + `graph/` ship with the deploy (loader uses `fs` at build from `process.cwd()`) |
| CI | Validates content + builds on GitHub Actions; no Vercel config in-repo |

---

## 8. Integration risks (observations only)

1. **Observation:** Runtime ID resolution for graph entities exists (`getConceptOrNode`, `refExists`, Maps in `getStore()`), but there is **no loader or type** for `content/lessons/`, `content/paths/`, or assessments — those trees would need new read paths analogous to `load.ts`, not just new JSON.

2. **Observation:** Validator reference checks only walk `nodes[].connects_to` and `global_id`; a dangling-ref check over a new subtree is **not registered** until a new function is imported and called from `validate.py` `main()`.

3. **Observation:** TypeScript types for content are hand-maintained in `types.ts` and are **not generated from** `schemas/*.schema.json`; lesson/path schemas would not automatically type the app.

4. **Observation:** Graph edges (`home_of`, `disambiguates`, `references`) are **build outputs**; presentation content that only cites G-/node IDs can use the access layer, but anything depending on edge kinds must read generated `graph/*` (or regenerate after content changes).

5. **Observation:** `getConceptOrNode` discriminates globals solely by `id.startsWith("G")`; non-G presentation IDs (e.g. planned `lesson-…` / `A…`) would not collide with that branch but also would not resolve through the current API.

6. **Observation:** SSG enumerates **all** concept IDs at build (`getAllConceptIds` → ~928 concept pages). Adding large lesson/path route trees would similarly bake into `next build` page count and build time unless routed differently.

7. **Observation:** Data loading depends on `process.cwd()` + filesystem; Next.js already warns about a **parent-directory lockfile** on this Windows/OneDrive machine (`C:\Users\cfroo\package-lock.json`), which can confuse workspace root / file tracing on Vercel-like builds.

8. **Observation:** Repo lives under `OneDrive\`; long paths and sync behavior are an environmental constraint for local `fs` reads and for CI parity (CI is Linux Ubuntu).

9. **Observation:** Architecture invariants treat `content/` JSON as sole editable SoT and `graph/` as generated; product docs (`OPERATING_ROADMAP.md`) already assert product track must not write `content/glossary/` or `content/modules/` — a separate lessons tree fits that split only if validators and loaders treat it as a second content family.

10. **Observation:** Activity schema targets are already defined as `G{n}` or `{slug}.z{z}.{n}`; quiz-like payloads are schema-ready but **unwired** to validation, build, or UI — parallel to (not integrated with) any future `content/assessments/` design.
