# 05 — Collision Map

Facts only — architect decides `disambiguate_with` topology. Verified against live `globals.json` (313 entries) and node text.

| Candidate CD meaning | Existing global | Existing meaning | Share mechanics? | Notes |
|---|---|---|---|---|
| **Comps** = comparable store / same-store sales | **★G88** Comparable companies analysis (“comps”) | Relative valuation via peer trading multiples (IB Z3) | **No** — shared slang only | **Near-certain trap.** ER z2.3 already uses “same-store sales” for retailers while G88 means peer multiples. |
| **Margin** = gross/operating margin (retail P&L) | **★G70** Spread / Credit margin; **★G286** NIM; **★G307** crack spread; **★G293** zero marginal cost | Credit spread; bank NIM; refining spread; software marginal cost | Weak analogy (spread vs % of sales) | Multi-sense already in corpus; retail gross margin currently **unhomed as its own global** but word collides everywhere |
| **Margin of safety** (if used casually) | Search: no exact “margin of safety” global in sample pull | — | — | Value-investing sense may appear in node prose; not a dedicated G-id in the collision sample |
| **Inventory** = merchandise / retail WC asset | **★G31** Working capital (includes inventory conceptually) | Deal WC peg at closing (PE) | Partial — inventory is a WC component, but retail inventory *turns/markdowns* are sector ops | No global titled “inventory”; IB/PE teach WC; retail inventory science would collide if minted carelessly |
| **Churn / retention** = membership/loyalty commerce | **★G301** NRR (net revenue retention) | SaaS dollar retention/expansion (IT) | Partial — retention math rhyme; commerce churn ≠ NRR | WM also uses client retention language without a dedicated churn global |
| **Subscription** = Prime / retail membership | **★G294** SaaS & the subscription model | Software recurring revenue | Partial — recurring billing rhyme; retail membership benefits differ | Amazon “Subscription services” is filing label |
| **Brand** | No global titled brand/brand equity | — | — | Widely used in nodes; unhomed as global |
| **Moat** | **No global** — MIGRATION_DEFECTS **§G #16 OPEN** | Used across VC/ER/AM/WM/sector-financials (7 nodes / 5 modules per backlog) | Metaphor only | **Still homeless.** Do not assume sector can quietly mint corpus-wide moat |
| **Franchise** = licensed/franchised stores or auto dealer franchise | **★G196** The research franchise & analyst rankings | Sell-side research franchise / II survey | **No** | Lodging/restaurant franchise ≠ research franchise |
| **Platform** = retail marketplace | IT platforms (★G-linked in sector-IT; e.g. network-effects teaching) | Software/two-sided tech platforms | Partial — multi-sided markets rhyme; Amazon is the boundary case | sector-IT.z1.1 already notes Amazon sits in Consumer Discretionary administratively |
| **EV** as enterprise value vs electric vehicle | **★G25** Enterprise Value (EV) | Whole-firm value | **No** — acronym collision | Ludicrous “EV” = electric vehicle |
| **ADR** = average daily rate (hotels) | Possible ADR = American Depositary Receipt in finance slang | Not checked as a dedicated global in this pass | **No** if ADR means depositary receipt | Lodging ADR vs capital-markets ADR |
| **Take rate** | No global | — | — | Absent; mint-safe on string basis but define vs marketplace vs lodging fees |
| **Direct sales** (auto) vs **DTC** (apparel) | No globals | — | Related channel ideas, different legal regimes | Dealer franchise law ≠ Nike Direct |

### Verified status checks requested in prompt
- **Moat:** Still OPEN unhomed in `docs/MIGRATION_DEFECTS.md` §G row 16 (as of this dossier build).
- **Comps:** G88 confirmed IB peer-multiples meaning; CD store-comps is the trap.
- **Subscription:** G294 is SaaS; Amazon Prime subscription is a collision candidate.
- **Inventory:** G31 WC home exists; retail inventory ops unhomed.
- **Churn/retention:** G301 NRR is the IT home; commerce retention unhomed / colliding.
