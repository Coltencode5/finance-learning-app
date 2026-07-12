# 06 — Seam Map — cross-module attachment candidates

Grep-backed. For each: source → target, payload, whether existing node already forward-references Consumer Discretionary.

| Source node | Target (proposed CD door / concept) | What the link would carry | Existing forward-ref to this sector? |
|---|---|---|---|
| `equity-research.z2.3` | `sector-consumer-discretionary.z1.1` (future) | Bidirectional sector door: retailer KPIs (same-store sales, traffic, margin) already named in ER hub | **Partial:** ER lists retailer worked contrast and has forward-links for Financials, IT, Energy — **no CD forward-link yet** (M12 not landed). Mandatory door pattern matches prior sectors. |
| `equity-research.z2.3` | CD comps / traffic / margin nodes | Operating mosaic for retail coverage | Mentions “retailer on same-store sales, traffic, and margin” in explainer — **yes, conceptual forward mention, no module ref** |
| `sector-information-technology.z1.1` | CD Amazon / platform-retail boundary | GICS puts Amazon in Consumer Discretionary while platform/AWS economics taught in IT | **Yes, explicit:** “Amazon in Consumer Discretionary — sector boundary is administrative, not economic” |
| `sector-information-technology.z2.*` (SaaS/subscription) | CD Prime / retail subscription | Recurring membership vs SaaS NRR | IT teaches ★G294; does not forward-link CD |
| `macro-economics` (consumer spending / confidence / cycle nodes — search hits thin on exact strings) | CD demand / trade-up-trade-down / discretionary cycle | Consumer cycle drives discretionary volumes | `consumer spending / consumer cycle` corpus search: **1 node hit** — seam exists but sparse; architect should re-grep macro zone titles for “consumption,” “PCE,” “sentiment” |
| `fixed-income.z4.*` (ABS / consumer credit) | Retail/consumer credit card ABS, private-label credit | Funding of consumer demand | Search for “consumer ABS / retail credit”: **0 hits** in this pass — **flag: seam expected but not found under those strings** |
| `real-estate.z2.1` / `real-estate.z2.2` | Malls, shopping centers, retail leases, e-commerce industrial | Store as lease obligation; retail property demand; industrial logistics as e-com beneficiary; hotels/RevPAR overlap | **Yes:** retail property type + e-commerce pressure + RevPAR for hospitality taught in RE |
| `real-estate` hospitality metrics | Marriott RevPAR/ADR/occupancy | Shared hotel KPI language | RE already teaches RevPAR; CD hotels should back-link rather than re-home |
| `private-equity` LBO nodes (e.g. sponsored deals, consumer favorites) | Consumer/retail LBO playbook | Classic PE sector: brand + cash flow + leverage | Search “consumer LBO”: **0 direct hits**; PE corpus discusses LBOs generally — **seam is real industrially, thin as exact string** |
| `private-credit.z2.*` specialty / consumer loans | Point-of-sale / consumer specialty lending | Niche consumer credit | PC specialty lending node mentions consumer loans among asset types |
| `sector-financials` consumer banking / cards | Consumer credit cycle ↔ discretionary spend | Bank consumer loan losses as cycle mirror | Financials teaches consumer loan mix / consumer finance hybrids |
| `venture-capital` DTC / brand startups | New Luxury / DTC brand creation | Creation side of premiumization | Indirect; VC brand/DTC language may appear — not exhaustively listed here |
| `asset-management` / `wealth-management` | Consumer brands as portfolio holdings; DTC channels | Ownership lens | WM “direct-to-consumer” is advice-channel DTC (**collision with apparel DTC**) |

### Defining boundary problem (IT ↔ CD)
- **Fact:** GICS classifies Amazon as Consumer Discretionary; AWS + advertising + marketplace are platform/tech economics already in sector-IT.
- **Existing text:** `sector-information-technology.z1.1` already states the administrative-vs-economic border and names Amazon.
- **Architect task (not decided here):** whether CD homes retail/marketplace KPIs and back-links AWS to IT, or treats Amazon as dual-citizen with explicit disambiguation — dossier only maps the seam.
