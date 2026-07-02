# ADR-002 — Core-concept zone semantics

**Status:** Accepted · **Date:** 2026-07-02

## Decision

Modules with `kind: "core-concept"` may use a **concept-progression zone spine**
instead of the role-module semantic template (Ecosystem → Types → Process →
Managing → Meta). The exception is scoped to **kind**, not to individual modules.

## Released for `core-concept` modules

- The **semantic template** of the five zones may differ. Core-concept modules
  use a concept-progression spine (e.g. Macro: Macro Framework → Money/Rates →
  Inflation → Credit Cycles → Global Macro).
- Zone titles reflect that spine. Each zone is expected to build on the prior;
  the dependency rationale belongs in the module header prose (as in the Macro
  node map).

## Not released — invariant for all kinds

The following remain locked for every module regardless of `kind`:

1. **Exactly five zones** — no sixth zone, no merged zones.
2. **`Zn.m` node-ID scheme** — `{slug}.z{zone}.{ordinal}` with local IDs `Z{n}.{m}`.
3. **Four required node fields** — quick_definition, explainer_covers,
   connects_to, tag.
4. **GAP-flag conventions** — structured `gaps[]` entries, not inline prose.
5. **Contiguous global numbering** — new globals append-only from `corpus_max + 1`.
6. **Back-link-don't-re-home** — existing globals are referenced, never redefined.

These invariants preserve M5 validation gates and scaffold assumptions (five zone
files, factory flow unchanged).

## Why

The schema already defines `kind: "core-concept"` as distinct from `"role"` at
M1 — the exception was anticipated but never documented. Macro & Economics is
not an industry with firms and a deal process; forcing the role spine would
mislabel every zone. Keeping structural invariants means core-concept modules
flow through the factory without bespoke tooling.

## Sector topology — explicitly out of scope

Whether sector modules are full five-zone peers or depth-layer clusters attached
at ER Z2.3 is **undecided**. That question is module **topology**, not zone
**semantics within** a module. It is reserved for **ADR-003** when Fixed
Income/sectors enter the build sequence. Do not fold it into this ADR.

## Consequences

- `scaffold_module.py` selects default zone title placeholders by `kind`.
- `new_module_checks.py` rejects role spine placeholders on active
  `core-concept` modules (and vice versa for role modules using concept spine
  placeholders).
- `parse_macro.py` (and future core-concept migrations) set `kind:
  "core-concept"` and custom zone titles; structural output matches role modules.
