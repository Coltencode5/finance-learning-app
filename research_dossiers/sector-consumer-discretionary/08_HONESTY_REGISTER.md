# 08 — Honesty Register

Every limitation in one place. Architect converts to structured `gaps[]`.

1. **Title mismatch — Stephens:** Expected “Reengineering Retail”; actual upload/book is **Resurrecting Retail** (Doug Stephens).
2. **Tier-B source set:** Business history + frameworks + four 10-Ks — not a technical retail-ops or auto-engineering corpus.
3. **OceanofPDF quality:** All books have text layers, but TOCs/page numbers are approximate; figure pages sometimes empty; chapter boundaries reconstructed for Moon/Stephens/Trading Up.
4. **Damodaran not re-extracted:** Reused M10 IT extracts by instruction; CD-specific reading depth is shallow by design.
5. **Automobiles coverage = thin outside EV/direct-sales/VI (revised):** Ludicrous added; does **not** make Automobiles “covered.” Still thin on ICE, broad dealer economics, captive finance, post-2019 facts.
6. **No auto OEM 10-K:** Tesla/GM/etc. FY2025 filing not in the four-filing set.
7. **Booking Holdings not fetched:** Gross bookings / OTA take-rate KPIs absent; Marriott fee model only.
8. **Starbucks “system-wide sales” / restaurant-level margin:** Not cleanly disclosed as McDonald’s-style labels in the pulled MD&A; co-op vs licensed mix used instead.
9. **Nike inventory days:** Inventories $7.5B disclosed; “days” not a named filing KPI in highlights.
10. **Amazon gross margin:** Company explicitly prefers operating income over gross margin; segment OP is the native lens.
11. **Consumer ABS / retail credit seam:** Expected in FI; exact-string corpus search returned 0 — may exist under other labels; not verified beyond this pass.
12. **Consumer LBO seam:** Industrially classic; exact “consumer LBO” string absent — PE LBO nodes are generic.
13. **Macro consumer-cycle seam:** Sparse exact hits (`consumer spending/cycle` ≈1); needs deeper macro title grep in architecture session.
14. **Moat still unhomed:** MIGRATION_DEFECTS §G #16 OPEN — do not silently home in CD.
15. **Low-confidence inventory rows:** Apostles-as-metric; DOE-as-general-concept; some Ludicrous numeric asides needing page re-pull.
16. **Extract recovery path:** Book chapter notes recovered from subagent transcripts after an initial failed write; content paraphrased from PDF dumps — still not verbatim transcripts.
17. **HTML 10-K text flattening:** Filing text dumps are whitespace-collapsed; KPIs cross-checked via keyword windows — table column alignment occasionally ambiguous without the HTML binary (binaries retained in `_source_filings/`).
18. **Inheritance script heuristics:** “Already homed” counts are string matches (often collisions). Architect must read `05_COLLISION_MAP.md` before back-linking.
19. **Brand / differentiation node flood:** “differentiat*” and “brand” match many unrelated nodes — treat unhomed lists as starting points, not precise homes.
20. **No canonical writes performed:** Only `research_dossiers/sector-consumer-discretionary/**` touched.

### Top three for the short report
1. Automobiles still **thin outside Tesla EV/direct-sales/VI** despite Ludicrous.
2. **Comps collision with ★G88** is load-bearing.
3. **Stephens title mismatch** + **Booking/OTA KPI gap** + **moat still OPEN**.
