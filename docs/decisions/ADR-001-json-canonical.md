# ADR-001 — Canonical JSON, Generated Markdown

**Status:** Accepted · **Date:** 2026-07-01

## Decision

After the Milestone 1 migration is signed off, the structured JSON under
`content/` is the **single source of truth** for all knowledge content.
The nine legacy markdown node maps become a frozen read-only reference under
`legacy/markdown/` and are never edited again. Human-readable markdown is a
**build artifact**, rendered from JSON by `pipeline/build/render_markdown.py`
(Milestone 2), the same way `graph/graph.json` is rendered from node data.

## Why

1. **Nine modules already drifted.** With markdown as the medium, the corpus
   accumulated: two incompatible GAP-flag formats, one divergent zone-header
   syntax (Real Estate), one non-standard node tag (HF Z2.8), one hand-counted
   summary error (HF "29" vs actual 31), and eleven dangling cross-references.
   Every one of these is either impossible or machine-caught when JSON +
   schema + validator is canonical.
2. **Everything downstream is structured.** The app, the graph, dedup
   detection, activity generation, and validation all consume structured data.
   Markdown-as-source means re-parsing prose forever; JSON-as-source means
   parsing happened exactly once (the migration).
3. **Derived facts must be derived.** Global counts, ranges, reuse lists, and
   gap counts now live in `module.json → derived`, written only by the build.
   Prose restating them (the old "Part 10" template notes) is rendered, not
   authored.

## Consequences

- All content edits happen in JSON (directly, or via pipeline tooling).
- `legacy/markdown/` is kept for provenance and parser regression tests only.
- `connects_to_raw` fields preserve the original free-text connection lines
  losslessly; they can be dropped once Milestone 2's reference-repair pass is
  signed off.
- Contributors need a rendered view for review; `render_markdown.py` provides
  it (and the Next.js app supersedes it as the primary reading surface).
