# The Five-Zone Template (Locked)

Validated 9/9 across Private Equity, Private Credit, Investment Banking,
Hedge Funds, Asset Management, Wealth Management, Equity Research, Venture
Capital, and Real Estate. This is standing architecture: new modules apply it;
they do not re-derive it.

## The spine

| Zone | Generalized meaning | Front door |
|---|---|---|
| Z1 Ecosystem | What it is, who the players are, how the money works | Z1.1 |
| Z2 Types | The strategy/style/product branches | Z2.1 |
| Z3 Process | The core workflow, taught in sequence | Z3.1 |
| Z4 Managing | The ongoing/holding-period work | Z4.1 |
| Z5 Meta | The firm, the economics, the relationships, the future | Z5.1 |

Zone *titles* may be domain-flavored ("Maintaining Coverage" for ER's Z4);
zone *meaning* and count may not. A module that appears to need a sixth zone or
a merged zone is an architecture escalation, not a local decision.

## The node contract (four fields, unchanged since PE)

quick_definition (one inline-able sentence) → explainer_covers (bullets,
basic → technical) → connects_to (the graph edges) → tag
(core | process | branch | global).

## Standing rules

1. **Inheritance first.** A concept already in the glossary is referenced by
   G-number, never redefined. New globals are minted only when genuinely
   net-new. Falling per-module global counts are the expected sign of health
   (57 → 25 → 23 → 31 → 22 → 23 → 19 → 16 → 19).
2. **One home per global.** Every global has exactly one deep-explainer home
   (a zone node). "Same node, different seat" context lives at referencing
   nodes, not in forked definitions.
3. **Disambiguation pairs are first-class.** Terms learners confuse
   (secondaries vs. secondary buyout; hurdle vs. preferred equity; G53 vs.
   G102 IPO lenses) get explicit `disambiguate_with` links.
4. **GAP flags, one format.** Source/recency gaps are structured entries on
   the node's `gaps` field. No inline prose tags, no consolidated prose
   sections — both legacy formats are retired.
5. **Derived facts are derived.** Counts, ranges, and reuse lists come from
   the build, never from prose.
6. **Sector modules** (open question, resolve before first sector build):
   recommended as compact depth-layer clusters (8–12 nodes) attached at
   ER Z2.3, not full five-zone peers. Decide once, record as ADR-002, apply
   uniformly.
