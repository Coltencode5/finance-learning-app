# Investment Banking Module — Complete Node Map

**The third structural blueprint for the finance learning app — built as an exact mirror of the PE and Private Credit modules.** This is the fully-mapped Investment Banking module: every learning node, organized into the same five zones, with quick definitions, layered explainer scopes, and knowledge-graph connections. It is deliberately the *same shape* as the PE and Credit maps so all three interlock into one graph rather than sitting as three separate courses. Investment banking is the **connective tissue of the other two modules**: the banker advises on the sale a PE fund makes (PE Zone 4 exit), arranges the debt a private-credit fund competes to provide (Credit Zone 2–3), and runs the valuation engine both disciplines rely on. A large fraction of this module's value is in the edges that cross back into PE and Credit.

**Sources mapped:** *Investment Banking: Valuation, LBOs, M&A, and IPOs* (Rosenbaum & Pearl, Wiley) — **primary spine** for the valuation toolkit, M&A processes, and capital-raising mechanics; the **Breaking Into Wall Street IB Interview Guide** module set found in the same Drive folder — *Accounting & the Three Statements*, *Equity Value, Enterprise Value & Multiples*, *Valuation & DCF Analysis*, and *M&A Deals & Merger Models* — which supply the worked, step-by-step technical layer (DCF/WACC mechanics, public comps, precedent transactions, the football field, accretion/dilution, and merger-model construction). Where these run thin or out of date, gaps are flagged in Part 9 exactly as the PE and Credit maps do.

> **Source-access note (build-time).** The Rosenbaum & Pearl PDF in the Drive folder is a scanned/image copy with no extractable text layer (and exceeds the connector's 10 MB download limit), so its chapter *structure* was used to frame the zones while the BIWS guides — which extract cleanly — supplied the authoritative node-level mechanics. Any node leaning primarily on the scanned book rather than the BIWS guides carries a `GAP:` flag so content isn't written from memory. A text-based copy of Rosenbaum & Pearl should be added to the Drive to retire those flags. *(This mirrors how the PE map flagged its thin spots — the graph grows at its seams.)*

---

## How to read this map

Identical schema to the PE and Credit maps. Every entry is a **node** carrying four things:

| Field | What it is | Maps to app layer |
|---|---|---|
| **Quick definition** | One sentence, inline-able | Layer 1 — the hover/tap definition |
| **Explainer covers** | Bulleted scope, ordered basic → technical | Layers 2–4 — overview → mechanics → technical depth |
| **Connects to** | Every other node this links to | The graph edges |
| **Tag** | Node role (see legend) | Routing / page type |

**Legend**
- `★ GLOBAL` — a **canonical glossary node** with one standalone explainer page that everything links back to. Listed up front in the Global Glossary Layer; its deep explainer lives in a stated "home" zone.
- `[core]` — a foundational concept node within a zone.
- `[process]` — a step in a sequential workflow.
- `[branch]` — a sub-strategy or variant that opens its own sub-tree.

**Node IDs** use `Z{zone}.{n}`. Glossary nodes also get a `G{n}` index.

### ⚠️ The shared-glossary rule (the most important thing about this map)

The app has **one global glossary**, not one per module. This module does **not** recreate primitives it shares with PE or Private Credit. Throughout the "Connects to" lines:

- **Globals `G1`–`G57` are the PE-map glossary nodes; `G58`–`G82` are the Private Credit-map glossary nodes.** This module *reuses* both sets by number. When IB puts a new spin on one — e.g., "EBITDA" seen through the lens of comparable-company screening, "enterprise value" as the output of a football field, or "leverage" as the constraint a LevFin desk solves for — that nuance is added as **new context on the existing node**, not as a new node. IRR in PE, IRR in private credit, and IRR in an IB LBO model are the *same node*.
- **Globals `G83`–`G105` are new, and this module contributes them to the app's global graph.** They are the concepts genuinely native to investment banking: the sell-side/buy-side mandate, the three core valuation methodologies and the football field that stacks them, the comparable-companies and precedent-transactions methods, WACC, accretion/dilution, synergies, the control premium, the sell-side M&A auction, the IPO and its mechanics, the underwriting spread, the league table, and the fairness opinion. Several will be *reused* by the future Equity Research module (the valuation stack, WACC, comps) and the Real Estate and Restructuring content — see Part 10.

**The bridge to Private Credit (LevFin).** Branch 2D (Leveraged Finance) is where this module fuses with the Private Credit map. A leveraged loan or high-yield bond arranged by a LevFin desk *is the same instrument* a direct lender holds — so LevFin **reuses the credit glossary wholesale** rather than rebuilding it: `★ G68` unitranche, `★ G69` floating rate/SOFR, `★ G70` spread, `★ G71` OID, `★ G72` call protection, `★ G73` PIK, `★ G78` security/lien priority, `★ G79` intercreditor, `★ G80` credit agreement, `★ G33` debt stack, `★ G34` covenant. The difference is vantage point: the banker *arranges and distributes* the paper; the credit fund *holds* it. The two modules meet on these shared nodes.

**Shared PE + Credit globals this module leans on most** (referenced, never rebuilt):
`★ G1` IRR · `★ G2` MOIC · `★ G24` EBITDA · `★ G25` EV · `★ G26` Equity value · `★ G27` Valuation multiples · `★ G28` Due diligence · `★ G29` Leverage · `★ G30` Net debt · `★ G31` Working capital · `★ G32` Sources & uses · `★ G33` Debt stack · `★ G34` Covenant · `★ G36` SPA · `★ G37` Preferred equity · `★ G40` Cap table · `★ G42` Dilution · `★ G52` Exit · `★ G53` IPO (as exit — the *investor's* view; this module owns the *issuer/process* view) · `★ G54` Trade sale · `★ G55` Secondary buyout · `★ G68` Unitranche · `★ G69` Floating rate/SOFR · `★ G70` Spread · `★ G71` OID · `★ G72` Call protection · `★ G73` PIK · `★ G78` Security/lien · `★ G79` Intercreditor · `★ G80` Credit agreement.

---

# PART 1 · The Global Glossary Layer (new nodes contributed by this module)

These are the new cross-zone canonical nodes investment banking adds to the app. **Build these first** — they are the backbone the rest of the module links into, and several become shared assets for the Equity Research, Real Estate, and Restructuring content. Each is written once, lives at one URL, and is referenced everywhere it appears. "Home" says which zone holds the deep explainer; "Appears in" shows link density. *(For the primitives this module shares with PE and Credit, see the shared-glossary rule above — those are G1–G82 and are not relisted here.)*

### A. The franchise, the product & the mandate

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| G83 | **Sell-side vs. buy-side** | The two sides of every Wall Street transaction — the sell-side (banks, brokers) that advises, structures, and distributes, versus the buy-side (PE, hedge funds, asset managers) that invests; the line that defines a banking career. | Z1 | Z1, Z2, Z4, Z5 |
| G84 | **The advisory mandate / engagement** | A bank's signed appointment to act for a client on a transaction, defining scope, the success fee, and exclusivity — the thing a pitch competes to win. | Z1 | Z1, Z3, Z5 |
| G85 | **The pitch / pitchbook** | The presentation a bank builds to win a mandate — market read, strategic options, a valuation view, and "why us." | Z3 | Z1, Z3, Z5 |
| G86 | **Coverage vs. product groups** | How a bank is organized — industry "coverage" bankers who own the client relationship versus "product" bankers (M&A, ECM, DCM, LevFin) who execute the deal type. | Z1 | Z1, Z2, Z5 |

### B. The valuation toolkit (the analytical core)

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| G87 | **The valuation toolkit / "the three methodologies"** | The banker's standard trio for valuing a company — comparable companies, precedent transactions, and DCF — run together because each checks the others. | Z3 | Z2, Z3, Z4, Z5 |
| G88 | **Comparable companies analysis ("comps")** | Valuing a company off the trading multiples of similar public companies — a market-based, relative valuation. | Z3 | Z2, Z3, Z4 |
| G89 | **Precedent transactions analysis ("deal comps")** | Valuing a company off the multiples paid in prior M&A deals for similar companies — relative valuation that bakes in a control premium. | Z3 | Z2, Z3, Z4 |
| G90 | **Discounted Cash Flow (DCF)** | Valuing a company by projecting its unlevered free cash flow and discounting it to present value at WACC — the intrinsic, cash-flow-based method. | Z3 | Z2, Z3, Z4 |
| G91 | **WACC (Weighted Average Cost of Capital)** | The blended after-tax cost of a company's debt and equity, weighted by capital structure — the discount rate that pairs with unlevered free cash flow. | Z3 | Z2, Z3, Z4 |
| G92 | **Unlevered Free Cash Flow (UFCF)** | Cash flow from the core business available to *all* investors before financing — NOPAT + D&A ± change in working capital − CapEx; the numerator in a DCF. | Z3 | Z3, Z4 |
| G93 | **Terminal value** | The lump-sum value of a company's cash flows beyond the explicit forecast, via perpetuity-growth or an exit multiple — usually most of a DCF's value. | Z3 | Z3 |
| G94 | **Valuation football field** | The summary chart stacking the value range from each methodology side by side, framing where a company is "worth" — the banker's headline output. | Z3 | Z3, Z4, Z5 |
| G95 | **Equity Value ↔ Enterprise Value bridge** | The walk between what the *whole business* is worth (EV) and what the *shareholders' stake* is worth (equity value) — adding cash, subtracting debt and other claims. | Z3 | Z2, Z3, Z4 |

### C. M&A analytics

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| G96 | **Accretion / dilution analysis** | The test of whether an acquisition raises (accretive) or lowers (dilutive) the buyer's earnings per share — M&A's first-pass scorecard. | Z2 | Z2, Z3 |
| G97 | **Merger model** | The integrated model combining buyer and target, the financing, and the synergies to project the combined company's EPS and returns. | Z3 | Z2, Z3 |
| G98 | **Synergies** | The added value from combining two companies — cost savings and revenue gains — that justifies paying a premium. | Z2 | Z2, Z3 |
| G99 | **Control premium** | The extra amount above a target's unaffected share price an acquirer must pay to take control — typically 10–30%, and the reason deal comps run rich. | Z2 | Z2, Z3, Z4 |
| G100 | **Consideration mix (cash / stock / debt)** | How a buyer funds a purchase — its blend of cash on hand, new debt, and its own stock — which drives accretion/dilution and risk. | Z2 | Z2, Z3 |

### D. Capital raising & the franchise

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| G101 | **Underwriting** | A bank's commitment to raise capital for an issuer — buying the securities to resell, taking on placement risk for a fee. | Z2 | Z2, Z3, Z5 |
| G102 | **The IPO (issuer/process view)** | A company's first sale of shares to the public — the registration, pricing, and allocation process a bank runs (distinct from `G53`, the PE *exit* view of the same event). | Z2 | Z2, Z3 |
| G103 | **The underwriting spread / gross spread** | The discount underwriters take between the price paid to the issuer and the price sold to investors — the bank's fee on a securities offering. | Z2 | Z2, Z5 |
| G104 | **League tables** | The published rankings of banks by deal volume and fees — the scoreboard that drives the franchise, pitches, and banker prestige. | Z5 | Z1, Z5 |
| G105 | **Fairness opinion** | A bank's formal letter that a deal's price is fair to shareholders from a financial point of view — a board's due-diligence and litigation shield. | Z3 | Z3, Z4 |

> **23 new global nodes (G83–G105).** Note the term-collisions learners trip over — build explicit "this vs. that" cross-links:
> - **Enterprise Value (`★ G25`)** vs. **Equity Value (`★ G26`)**, joined by the **EV↔EqV bridge (G95).** The single most-tested distinction in all of banking: EV is the value of the *operations* to all investors; equity value is what's left for *shareholders* after net debt and other claims. Every multiple lives on one side or the other (EV/EBITDA is an EV multiple; P/E is an equity multiple) — *never mix them.*
> - **The IPO as *exit* (`★ G53`)** vs. **the IPO as *issuance process* (G102).** Same event, two vantage points: the PE module owns "listing to sell down a stake"; this module owns "the registration-to-allocation machine the bank runs." Cross-link them.
> - **Comparable companies (G88)** = multiples from *public, un-acquired* peers (no control premium) · **Precedent transactions (G89)** = multiples *paid in deals* (control premium included). Same multiple math, systematically different levels — the gap *is* the control premium (G99).
> - **Synergies (G98)** = the value created by combining · **Control premium (G99)** = the value *paid away* to the seller to do the deal. A deal creates value only if synergies exceed the premium.
> - **The DCF discount rate** is **WACC (G91)** when you discount **unlevered FCF (G92)** — but the **cost of equity** when you discount levered FCF or dividends. Same "discount rate" slot, different rate depending on whose cash flow you're valuing. *(Rhymes with the PE/Credit "leverage as return vs. leverage as risk" collision — same word, different vantage.)*

---

# PART 2 · Zone 1 — The Investment Banking Ecosystem

**What this zone is:** the foundational layer — what an investment bank actually does, how it's organized, who its clients are, the product/coverage split, the fee model, and where banking sits relative to the buy-side it serves. It is the mirror of PE's and Credit's Zone 1, and like them it doubles as the "how does Wall Street work" half of any finance primer. *(Source: Rosenbaum & Pearl, front matter & Ch. 1 framing; BIWS overview material.)*

**Learning sequence (logical path):**
`What is investment banking? → What banks actually do (the three franchises) → Sell-side vs. buy-side → Coverage vs. product groups → The client: who hires a bank and why → How banks make money (advisory fees + underwriting spreads) → The pitch and the mandate → The deal team & the analyst's life → The regulatory & reputational frame → League tables & the franchise → How IB connects to PE and Private Credit.`
The canonical beginner entry point is **Z1.1**.

---

### Z1.1 · What Is Investment Banking? `[core]`
**Quick definition.** A financial intermediary that helps companies, governments, and investors raise capital, buy and sell businesses, and value assets — advising on and executing the largest financial transactions rather than lending its own balance sheet long-term.
**Explainer covers (basic → technical).**
- The simple model: a bank sells *advice* and *access to capital markets*, earning fees rather than holding assets to maturity.
- The three core franchises: **advisory** (M&A and restructuring), **capital markets** (raising equity and debt), and the supporting **markets/sales & trading and research** businesses.
- Investment banking (the advisory + capital-raising business) vs. the broader "investment bank" (which also houses trading, research, and asset management).
- Bulge-bracket vs. elite-boutique vs. middle-market banks — who competes for what.
- Why companies hire bankers at all: specialized expertise, market access, a credible third-party valuation, and bandwidth at a transaction's peak.
**Connects to.** Z1.2, Z1.3 (`★ G83` sell-side/buy-side), Z2.1 (the product spectrum), `★ G87` valuation toolkit, and across the aisle: PE Z1.1 (the buy-side client) and Credit Z1.1 (the lender the LevFin desk syndicates to).

### Z1.2 · What Banks Actually Do: The Three Franchises `[core]`
**Quick definition.** The division of an investment bank into advisory, capital markets, and markets/research businesses — and how a "deal" flows across them.
**Explainer covers.**
- **Advisory:** sell-side and buy-side M&A, restructuring, fairness opinions — paid on success.
- **Capital markets:** equity capital markets (ECM) and debt capital markets (DCM) — raising money by issuing securities, paid via the underwriting spread.
- **Sales & trading and research:** the secondary-market machine that prices, distributes, and supports the securities the bank underwrites (the bridge to the buy-side).
- How one client need (e.g., "we want to grow") can touch all three (buy a competitor via M&A, fund it via DCM, support the stock via research).
**Connects to.** Z1.1, Z2.1, Z1.7 (the fee model), `★ G86` coverage vs. product, `★ G101` underwriting.

### Z1.3 · Sell-Side vs. Buy-Side `★ GLOBAL (G83)` `[core]`
**Quick definition.** The defining split of the industry — the sell-side (banks and brokers) that advises, structures, and distributes securities, versus the buy-side (PE, hedge funds, asset managers, pensions) that invests capital.
**Explainer covers.**
- Who sits on each side and what each is paid for (fees and spreads vs. investment returns and carry).
- Why the same person's skills transfer across the line — and why the classic career path runs sell-side analyst → buy-side associate.
- The information and incentive differences: the sell-side serves a transaction; the buy-side owns a position.
- How the two sides need each other: the sell-side originates and distributes what the buy-side buys.
**Connects to.** Z1.1, Z1.2, Z5.1 (the franchise), PE Z1.1 (a buy-side client), Credit Z1.1 (a buy-side lender), `★ G84` mandate.

### Z1.4 · Coverage Groups vs. Product Groups `★ GLOBAL (G86)` `[core]`
**Quick definition.** The two-axis way a bank is organized — industry "coverage" bankers who own the client relationship, and "product" bankers (M&A, ECM, DCM, LevFin, Restructuring) who execute a given transaction type.
**Explainer covers.**
- Coverage (a.k.a. industry groups): healthcare, TMT, industrials, FIG, etc. — relationship owners and sector experts.
- Product groups: M&A, ECM, DCM, Leveraged Finance, Restructuring — deep transactional specialists.
- How the two collaborate on a live deal (coverage brings the client and the strategic view; product brings the execution).
- Why this matters for a career: generalist relationship skills vs. specialist technical depth.
**Connects to.** Z1.2, Z2.1 (the product groups *are* Zone 2's branches), Z3.1 (the pitch), `★ G84` mandate.

### Z1.5 · The Client: Who Hires a Bank, and Why `[core]`
**Quick definition.** The range of entities that retain investment banks — public and private corporations, financial sponsors (PE), founders and families, governments, and other institutions — and the needs that bring them in.
**Explainer covers.**
- Corporates: sell a division, buy a competitor, raise growth capital, defend against a raider.
- **Financial sponsors (PE firms):** a bank's most repeat-heavy client — buying platforms, financing buyouts, and selling portfolio companies. *(The sponsor relationship is a franchise unto itself.)*
- Founders/families: succession, liquidity, a first institutional raise.
- The trigger events: growth, succession, distress, opportunism, activist pressure, going public.
**Connects to.** Z1.3, Z3.1 (winning the work), PE Z4.13 (the sponsor exit a banker runs), PE Z2.21 (the buyout a LevFin desk funds), `★ G84` mandate.

### Z1.6 · The Financial Sponsors Coverage Relationship `[core]`
**Quick definition.** The dedicated effort banks make to serve PE firms — the single most transaction-dense client type, generating M&A, financing, and exit mandates in a repeating cycle.
**Explainer covers.**
- Why sponsors are prized clients: they transact constantly and predictably across the fund lifecycle.
- The full sponsor wallet: buy-side advisory on acquisitions, LevFin to fund them, sell-side advisory on exits, IPOs as an exit route, dividend-recap financings.
- The "sponsor coverage" group and how it sits across product teams.
- The flywheel: win the buy-side, then the financing, then the eventual sell-side or IPO.
**Connects to.** Z1.5, Z2.4 (LevFin), Z2.5 (Restructuring), PE Z1.4 (the fund lifecycle that generates the deal flow), PE Z4.17 (dividend recaps), `★ G55` secondary buyout.

### Z1.7 · How Banks Make Money: Advisory Fees & Underwriting Spreads `★ GLOBAL (G103 — partial home)` `[core]`
**Quick definition.** The two engines of investment-banking revenue — success-based advisory fees on M&A/restructuring, and the underwriting spread earned on capital raised.
**Explainer covers.**
- **Advisory (M&A) fees:** success fees scaled to deal size (often with retainers and "Lehman formula"-style tiers); paid only if the deal closes.
- **Underwriting spread (`G103`):** the gross spread between what the bank pays the issuer and what it sells to investors — split into management fee, underwriting fee, and selling concession.
- Restructuring fees (monthly + completion); financing fees on arranged debt.
- Why advisory is capital-light and high-margin, and how league-table position drives pricing power.
**Connects to.** Z1.2, `★ G101` underwriting, `★ G103` underwriting spread (deep in Z2.10), `★ G104` league tables, Z5.2.

### Z1.8 · The Pitch and the Mandate `★ GLOBAL (G84)` `[process]`
**Quick definition.** The competitive process by which a bank wins the right to advise — pitching its market read, strategic options, and valuation view to earn a signed engagement.
**Explainer covers.**
- The pitchbook (`G85`): situation analysis, strategic alternatives, a preliminary valuation (the football field), and credentials.
- The "bake-off"/beauty parade where banks compete for the mandate.
- The engagement letter: scope, the success fee, exclusivity, indemnification, tail provisions.
- Why a pitch is mostly *judgment and relationship* wrapped around analysis.
**Connects to.** Z1.5, Z3.1 (deep on the pitch), `★ G85` pitchbook, `★ G94` football field, `★ G87` valuation toolkit, Z5.1.

### Z1.9 · The Deal Team & the Analyst's Role `[core]`
**Quick definition.** The staffing pyramid of a live deal — analyst, associate, VP, director, MD — and who does what from model to close.
**Explainer covers.**
- The hierarchy and the division of labor (analysts build, associates check, VPs manage, MDs originate).
- The analyst's core outputs: the model, the pitchbook, the comps, the data room, the buyer/lender outreach.
- The culture, hours, and the "two-year analyst program → buy-side or business school" path.
- How deal teams interface with coverage, product, legal, and the client.
**Connects to.** Z1.4, Z3.x (every process step the analyst executes), Z1.3 (the exit to the buy-side), `★ G87` valuation toolkit.

### Z1.10 · The Regulatory & Reputational Frame `[core]`
**Quick definition.** The rules and conflicts that govern banking — securities-law underwriting liability, the research/banking "wall," conflict management, and the reputational capital a franchise runs on.
**Explainer covers.**
- Underwriting due-diligence and liability under the securities laws (why the diligence is real).
- The information barrier ("Chinese wall") between banking and research/trading, post-Global-Settlement.
- Conflicts: stapled financing, advising both buyer relationships, fairness-opinion independence.
- Reputation as the asset — why league-table credibility and a clean record win mandates.
- *(Recency/coverage flag: post-2008 structural reforms and the modern conflict regime are sketched in the source spine — see Part 9.)*
**Connects to.** Z1.7, `★ G105` fairness opinion, Z3.13 (fairness opinions in process), Z5.4 (the franchise & regulation), `★ G101` underwriting.

### Z1.11 · League Tables & the Franchise (intro) `★ GLOBAL (G104)` `[core]`
**Quick definition.** The published rankings of banks by deal volume and fees — the industry scoreboard that shapes pitches, pay, prestige, and the pecking order.
**Explainer covers.**
- How league tables are compiled (by value and by count; by product and region) and gamed.
- Why position matters: credibility in pitches, pricing power, talent attraction.
- The gap between "bulge-bracket scale" and "boutique advisory quality" league positions.
- Pointer to the deep franchise node in Zone 5.
**Connects to.** Z1.7, `★ G104` (deep in Z5.2), Z5.1, Z1.1.

### Z1.12 · How IB Connects to PE and Private Credit `[core]`
**Quick definition.** The map of where investment banking touches the two sibling modules — as advisor, financier, and valuation engine to the buy-side.
**Explainer covers.**
- IB → PE: sell-side advisor on the deals PE buys and sells; the IPO route for exits; the LBO/valuation toolkit PE borrows wholesale.
- IB → Private Credit: the LevFin desk *originates and syndicates* the very loans direct lenders compete to hold (and increasingly lose share to).
- The shared analytical spine: EBITDA, EV/equity value, the debt stack, comps, the LBO model — *one glossary across all three modules*.
- Why studying all three together reveals one deal seen from three seats (advisor, owner, lender).
**Connects to.** Z1.3, Z2.4 (LevFin — the bridge), PE Z2.21 (the LBO), PE Z4.13 (exits), Credit Z1.7 (private credit vs. the syndicated market IB runs), `★ G87` valuation toolkit.

---

# PART 3 · Zone 2 — The Product Groups (Types of Investment Banking Work)

**What this zone is:** the strategy branches. Investment banking divides into five product lines, each its own sub-tree: **M&A advisory**, **Equity Capital Markets (ECM)**, **Debt Capital Markets (DCM)**, **Leveraged Finance (LevFin)**, and **Restructuring**. They map one-to-one onto the generalized "types" zone of the PE and Credit maps. *(Source: Rosenbaum & Pearl, Ch. 6–7 for M&A and the sell-side process; BIWS M&A guide for analytics; capital-markets framing throughout.)*

**Learning sequence (by transaction type):**
`The product spectrum → M&A advisory (the flagship) → ECM (raising equity) → DCM (raising investment-grade debt) → LevFin (raising leveraged debt — the bridge to Private Credit) → Restructuring (the distressed counter-cycle).`
The spectrum node (**Z2.1**) is the hub; each branch can be entered directly.

---

### Z2.1 · The Investment Banking Product Spectrum `[core]`
**Quick definition.** A map of the five core product lines by what they do — advise on ownership change (M&A, Restructuring) versus raise capital (ECM, DCM, LevFin) — and how risk, fees, and market cycle differ across them.
**Explainer covers.**
- The two families: **advisory** (M&A, Restructuring — paid on success, capital-light) and **capital markets** (ECM, DCM, LevFin — paid on the spread, distribution-driven).
- The cyclicality split: M&A and ECM boom in good markets; Restructuring booms in bad ones; DCM is the steady base; LevFin tracks the credit cycle.
- How the required skillset differs across branches (negotiation/process vs. markets/distribution vs. structuring/credit).
- Which buy-side clients each branch serves (strategics, sponsors, institutional investors, creditors).
**Connects to.** All Zone 2 branch nodes, `★ G87` valuation toolkit, Z1.4 (product groups), Z1.1.

## Branch 2A — Mergers & Acquisitions (M&A) Advisory

### Z2.2 · M&A Advisory Defined `[branch]`
**Quick definition.** Advising a company on buying, selling, or combining with another — the flagship advisory product, split into sell-side (representing a seller) and buy-side (representing an acquirer).
**Explainer covers.**
- Sell-side vs. buy-side *mandates* (distinct from the industry-wide `★ G83` sell-side/buy-side split — here it means which party in the deal the bank represents).
- What the advisor delivers: valuation, positioning, process management, negotiation, and the path to close.
- Strategic acquirers vs. financial sponsors as buyers, and how that shapes price and process.
- The core analytics the branch runs: the valuation toolkit, accretion/dilution, and the merger model.
**Connects to.** Z2.3, Z3.3 (the sell-side process, deep), `★ G87` valuation toolkit, `★ G96` accretion/dilution, `★ G99` control premium, PE Z4.13 (the sponsor sale a banker runs).

### Z2.3 · Buy-Side vs. Sell-Side M&A Mandates `[core]`
**Quick definition.** The two roles a bank can play in a deal — running a sale for an owner (sell-side) or hunting and negotiating a purchase for an acquirer (buy-side).
**Explainer covers.**
- **Sell-side:** prepare the asset, run the auction, maximize price and certainty (the bulk of fee revenue).
- **Buy-side:** source targets, value them, structure the offer, negotiate, arrange financing.
- Why sell-side mandates are more common and more lucrative (a motivated seller and a defined timeline).
- How the same deal looks different from each chair.
**Connects to.** Z2.2, Z3.3 (sell-side process), Z3.4 (buy-side process), `★ G84` mandate, PE Z3.1 (the sponsor's buy-side deal sourcing).

### Z2.4 · Accretion / Dilution & the Merger Model `★ GLOBAL (G96)` `[core]`
**Quick definition.** The first-pass test of whether an acquisition increases or decreases the buyer's earnings per share, built inside an integrated merger model.
**Explainer covers.**
- The mechanics: combine the two companies' net income, add the new financing cost and forgone interest, divide by the new share count.
- The intuition: a deal is accretive if the target's earnings yield exceeds the after-tax cost of funding it (cheap debt = accretive; expensive stock = dilutive).
- The consideration mix (`G100`) as the driver — cash vs. stock vs. debt changes the answer.
- The full merger model (`G97`): purchase-price allocation, synergies, combined projections, pro-forma credit stats.
- *(BIWS M&A guide: the 60-minute and 3-hour merger-model builds, the contribution analysis.)*
**Connects to.** Z2.2, `★ G97` merger model, `★ G98` synergies, `★ G100` consideration mix, `★ G42` dilution, Z3.6 (valuation feeds the model).

### Z2.5 · Synergies, Premiums & Value Creation in M&A `★ GLOBAL (G98)` `[core]`
**Quick definition.** The analysis of what combining two companies creates (synergies) against what the buyer pays away to get the deal done (the control premium) — the heart of whether a deal makes sense.
**Explainer covers.**
- Cost synergies (headcount, facilities, procurement) vs. revenue synergies (cross-sell, pricing) — and why cost synergies are credited and revenue synergies discounted.
- The control premium (`G99`): why an acquirer must pay above the unaffected price, and the 10–30% norm.
- Value creation test: synergies (net of integration cost) must exceed the premium for the deal to add value.
- How synergies are modeled, phased, and (often) over-promised.
**Connects to.** Z2.4, `★ G99` control premium, `★ G89` precedent transactions (premiums embedded), PE Z2.23 (a sponsor's value-creation logic), `★ G94` football field.

### Z2.6 · M&A Deal Structures & Consideration `★ GLOBAL (G100)` `[core]`
**Quick definition.** The menu of ways a deal is legally and financially structured — stock vs. asset purchase, merger forms, and the cash/stock/debt funding mix.
**Explainer covers.**
- Stock purchase vs. asset purchase vs. statutory merger — tax and liability consequences.
- Cash-free/debt-free deals and the role of net debt and working-capital pegs (ties to `★ G30`, `★ G31`).
- Consideration mix (`G100`): cash, acquirer stock, assumed/new debt — and the accretion/dilution and risk trade-offs.
- Earn-outs, escrows, and contingent value as bridges over valuation gaps.
**Connects to.** Z2.4, `★ G36` SPA, `★ G30` net debt, `★ G31` working capital, `★ G35` SPV, Z3.9 (documentation).

## Branch 2B — Equity Capital Markets (ECM)

### Z2.7 · Equity Capital Markets Defined `[branch]`
**Quick definition.** The product line that raises equity for companies — IPOs, follow-on offerings, and equity-linked securities — and advises on the timing, structure, and pricing of selling stock.
**Explainer covers.**
- What ECM does: take companies public, raise more equity from public companies, and structure convertibles.
- The underwriting role (`G101`): committing to sell the shares and bearing placement risk for the gross spread.
- Where ECM sits between the issuer and the buy-side investors who buy the offering.
- The product menu: IPO, follow-on/secondary, block trade, rights issue, convertible.
**Connects to.** Z2.8, Z2.9, `★ G101` underwriting, `★ G102` IPO process, `★ G103` underwriting spread, Z1.2.

### Z2.8 · The IPO (Issuer & Process View) `★ GLOBAL (G102)` `[process]`
**Quick definition.** A company's first sale of shares to the public — and the registration, marketing, pricing, and allocation machine a bank runs to get there.
**Explainer covers.**
- The process: organizational meeting → due diligence → registration statement (S-1) → SEC review → roadshow → pricing → allocation → first trade → stabilization.
- Bookbuilding: gauging demand, setting the range, and pricing (and why IPOs are often deliberately underpriced for a first-day "pop").
- The players: lead-left bookrunner, co-managers, underwriters' counsel, the syndicate.
- Lockups, the greenshoe (over-allotment), and aftermarket support.
- **The disambiguation:** this is the *same event* as PE's "IPO as exit" (`★ G53`), seen from the issuer/banker's chair rather than the selling shareholder's.
**Connects to.** Z2.7, `★ G53` IPO as exit (cross-link), `★ G101` underwriting, `★ G103` spread, `★ G105` fairness opinion (for related transactions), PE Z4.14 (the exit decision).

### Z2.9 · Follow-Ons, Converts & Other Equity Products `[core]`
**Quick definition.** The post-IPO equity toolkit — follow-on offerings, secondary block sales, rights issues, and convertible/equity-linked securities.
**Explainer covers.**
- Follow-on (primary, raising new money) vs. secondary (existing holders selling) offerings.
- Block trades and accelerated bookbuilds (ABBs) — fast, large, often bought-deal placements.
- Convertibles and equity-linked notes: debt with an equity option, and why issuers use them.
- How sponsors use follow-ons and block trades to sell down post-IPO stakes (the staged exit).
**Connects to.** Z2.7, Z2.8, `★ G37` preferred equity, `★ G42` dilution, PE Z4.14 (selling down after listing), `★ G101` underwriting.

## Branch 2C — Debt Capital Markets (DCM)

### Z2.10 · Debt Capital Markets Defined `★ GLOBAL (G103 — home)` `[branch]`
**Quick definition.** The product line that raises debt for primarily investment-grade issuers in the public bond markets — advising on timing, structure, ratings, and pricing, and underwriting the issue.
**Explainer covers.**
- What DCM does: investment-grade corporate bonds, and the steady "base-load" of capital-markets revenue.
- The underwriting spread (`G103`) on a bond deal and how it's split.
- Ratings advisory: positioning an issuer with the agencies to optimize cost of capital.
- The contrast with LevFin (Z2.11): DCM is investment-grade and rate-driven; LevFin is sub-investment-grade and credit-driven.
**Connects to.** Z2.11 (LevFin — the high-yield sibling), `★ G101` underwriting, `★ G103` (deep here), `★ G69` floating rate/SOFR, Credit Z1.7 (the public-market alternative to private credit).

## Branch 2D — Leveraged Finance (LevFin) — *the bridge to Private Credit*

### Z2.11 · Leveraged Finance Defined `[branch]`
**Quick definition.** The product line that arranges sub-investment-grade ("leveraged") debt — leveraged loans and high-yield bonds — most often to fund buyouts, recaps, and acquisitions for sponsor-owned and high-yield corporate borrowers.
**Explainer covers.**
- What LevFin does: structure, underwrite, and syndicate leveraged loans (Term Loan B) and high-yield bonds.
- The buyout connection: LevFin is the desk that finances the LBO — the debt side of the PE deal.
- **The bridge to Private Credit:** the leveraged loan a LevFin desk syndicates to institutional investors *is the same instrument* a direct lender holds privately. The two markets now compete head-to-head (broadly syndicated vs. private/direct).
- The arranger's role and risk: commitment letters, the "flex," and syndication risk (getting stuck with un-sold paper).
**Connects to.** Z2.12, Z2.13, PE Z2.21 (the LBO it funds), Credit Z1.7 (private credit vs. the BSL market), Credit Z2.2 (direct lending — the private-market mirror), `★ G33` debt stack, `★ G29` leverage.

### Z2.12 · The Leveraged Debt Toolkit `[core]`
**Quick definition.** The instruments a LevFin desk arranges — leveraged loans (Term Loan B), high-yield bonds, bridge loans, and unitranche — ranked by seniority and tailored to the deal.
**Explainer covers.**
- **Leveraged loans / Term Loan B:** senior secured, floating-rate (`★ G69` SOFR + `★ G70` spread), the staple of buyout financing.
- **High-yield bonds:** junior, often fixed-rate, longer-dated, with incurrence covenants and call protection (`★ G72`).
- **Bridge loans:** short-term financing that "bridges" to a permanent bond/loan takeout — a classic underwriting commitment.
- **Unitranche (`★ G68`):** the single blended instrument — *here arranged/distributed by the bank, vs. held by a direct lender in the Credit module.*
- Pricing levers shared with private credit: spread (`★ G70`), OID (`★ G71`), call protection (`★ G72`), PIK (`★ G73`).
**Connects to.** Z2.11, `★ G68` unitranche, `★ G69` SOFR, `★ G70` spread, `★ G71` OID, `★ G72` call protection, `★ G73` PIK, `★ G33` debt stack, Credit Z2.3 (unitranche held), Credit Z2.4 (second lien).

### Z2.13 · Syndication, Covenants & Documentation in LevFin `[core]`
**Quick definition.** How arranged leveraged debt is sold down to investors, and the credit-agreement terms — covenants, security, and intercreditor ranking — that govern it.
**Explainer covers.**
- The syndication process: underwrite/commit → launch → book the loan with institutional investors (CLOs, credit funds, BDCs) → allocate → close.
- Covenants: maintenance vs. incurrence, and the "cov-lite" drift in the syndicated market (ties to `★ G34`).
- Security, lien priority, and intercreditor terms (`★ G78`, `★ G79`) — *the same documents the Credit module's lender side negotiates.*
- The credit/facility agreement (`★ G80`) as the master contract — the debt analogue of the SPA.
- *(Recency/coverage flag: modern liability-management — uptiers, drop-downs — and the post-2020 doc-protection arms race sit at the edge of the source spine; shared gap with the Credit map — see Part 9.)*
**Connects to.** Z2.12, `★ G34` covenant, `★ G78` security/lien, `★ G79` intercreditor, `★ G80` credit agreement, Credit Z3.x (the lender's documentation view), Credit Z2.16 (CLOs as the buyer base).

## Branch 2E — Restructuring (RX)

### Z2.14 · Restructuring Advisory Defined `[branch]`
**Quick definition.** Advising financially distressed companies — or their creditors — on fixing an unsustainable balance sheet, in or out of bankruptcy; the counter-cyclical advisory product that booms when M&A slows.
**Explainer covers.**
- The two sides: **company-side** (debtor advisory) vs. **creditor-side** (representing lenders/bondholders).
- Out-of-court (amend-and-extend, exchanges, new money) vs. in-court (Chapter 11) restructuring.
- The toolkit: liability management, debt-for-equity swaps, distressed exchanges, 363 sales, DIP financing.
- Why RX is a specialist, valuation-intensive practice (recoveries hinge on enterprise value and seniority).
- The fee model: monthly retainers + a completion fee, regardless of market direction.
**Connects to.** Z2.15, Credit Z4.7 (workouts — the lender's side of the same table), Credit Z2.5 (distressed credit), `★ G61` recovery/LGD (where the value lands), `★ G81` workout.

### Z2.15 · Restructuring Analytics & the Distressed Toolkit `[core]`
**Quick definition.** The analytical core of RX — valuing a distressed enterprise, mapping recoveries across the capital structure, and structuring the fix.
**Explainer covers.**
- The valuation waterfall: enterprise value flows down the debt stack by seniority, determining who recovers and who's impaired (the "fulcrum security").
- Liquidation/NAV valuation as the floor (ties to the asset-based method in Z3.8).
- Modeling recoveries, the plan of reorganization, and new-money/DIP structures.
- How the same `★ G87` valuation toolkit is repurposed for distress (DCF and comps under going-concern doubt).
- *(Recency/coverage flag: the modern creditor-on-creditor / LME era post-dates much of the standard source material — shared gap with the Credit map, item flagged in Part 9.)*
**Connects to.** Z2.14, `★ G87` valuation toolkit, `★ G61` recovery/LGD, `★ G62` default/PD, `★ G78` lien priority, Credit Z4.8 (recovery analysis), Credit Z4.9 (bankruptcy/Chapter 11), `★ G33` debt stack.

---

# PART 4 · Zone 3 — Doing Deals: The Valuation Toolkit & Execution Process

**What this zone is:** the core process layer — highly sequential, and the analytical heart of the whole module. It splits in two: **the valuation toolkit** (the three methodologies every banker runs) and **the execution process** (pitch → mandate → diligence → marketing → negotiation → close). This is where the BIWS guides supply the deepest, most authentic mechanics. *(Source: Rosenbaum & Pearl, Ch. 1–3 for comps/precedents/DCF and Ch. 6–7 for the sell-side process; BIWS Valuation/DCF and M&A guides for the worked builds.)*

**Learning sequence (logical path):**
`Equity Value vs. Enterprise Value (the foundation) → the three methodologies overview → Comparable Companies → Precedent Transactions → DCF (UFCF → WACC → Terminal Value) → the Football Field → then the execution arc: the pitch → engagement → due diligence & the data room → marketing the deal → negotiation & documentation → fairness opinion → signing & closing.`
The canonical front-door is **Z3.1** (EV vs. equity value) for the analytics, or **Z3.10** (the pitch) for the process.

---

## Sub-zone 3A — The Valuation Toolkit

### Z3.1 · Equity Value vs. Enterprise Value & the Bridge `★ GLOBAL (G95)` `[core]`
**Quick definition.** The foundational distinction underneath all valuation — enterprise value (the worth of the operating business to all investors) versus equity value (what's left for shareholders) — and the bridge that walks between them.
**Explainer covers.**
- The real definitions: enterprise value = value of *core operations to all investors*; equity value = value of the *shareholders' residual*.
- The bridge: equity value + net debt + preferred + noncontrolling interests − non-core assets = enterprise value (and back).
- Why multiples must match: EV multiples pair with pre-interest metrics (EBITDA, EBIT, revenue); equity multiples pair with post-interest metrics (net income, EPS) — *never cross them*.
- How events (raising debt, buying back stock, issuing shares) move each — the single most-tested mechanic in banking.
- *(BIWS Equity/Enterprise Value guide: the 14 "key rules," the dilution and bridge mechanics.)*
**Connects to.** `★ G25` EV, `★ G26` equity value, `★ G30` net debt, `★ G27` multiples, `★ G42` dilution, Z3.2 (all three methods rest on this), Z2.4 (M&A uses the bridge).

### Z3.2 · The Three Methodologies (overview) `★ GLOBAL (G87)` `[core]`
**Quick definition.** The banker's standard valuation trio — comparable companies, precedent transactions, and DCF — run together because relative and intrinsic methods cross-check each other.
**Explainer covers.**
- Relative valuation (comps, precedents): value off the market's pricing of similar companies/deals — fast, market-grounded, but "the market can be wrong."
- Intrinsic valuation (DCF): value off the company's own projected cash flows — rigorous, but assumption-sensitive.
- Why you always triangulate: each method's weakness is another's strength.
- How the outputs converge into the football field (Z3.9).
**Connects to.** Z3.3, Z3.4, Z3.5, `★ G88` comps, `★ G89` precedents, `★ G90` DCF, `★ G94` football field, PE Z3.6 (the sponsor's valuation), Credit Z3.x (credit's valuation needs).

### Z3.3 · Comparable Companies Analysis `★ GLOBAL (G88)` `[process]`
**Quick definition.** Valuing a company off the trading multiples of similar public companies — selecting a peer set, calculating their multiples, and applying them to the target.
**Explainer covers.**
- The four steps: select the peer set (industry, geography, size) → spread the financials → calculate multiples (EV/EBITDA, EV/Revenue, P/E) → apply the median/percentiles to the target.
- Screening discipline: 5–10 truly comparable companies with *similar discount rates*; avoid conflicting screens.
- LTM vs. forward metrics, calendarization, and non-recurring add-backs.
- Why comps reflect *no control premium* (they're un-acquired public companies) — the key contrast with precedents.
- *(BIWS Valuation guide: the full Steel Dynamics worked comps set.)*
**Connects to.** Z3.1, Z3.2, `★ G24` EBITDA, `★ G27` multiples, `★ G89` precedents (the contrast), Z3.4, PE Z3.6.

### Z3.4 · Precedent Transactions Analysis `★ GLOBAL (G89)` `[process]`
**Quick definition.** Valuing a company off the multiples acquirers actually paid in prior M&A deals for similar companies — relative valuation that bakes in a control premium.
**Explainer covers.**
- The method: screen comparable *deals* (by seller industry/size and time) → gather purchase multiples → apply to the target.
- Why it runs richer than comps: the control premium (`G99`) embedded in every acquisition price.
- Data challenges: historical-only metrics, deal-structure noise (earn-outs, stock vs. cash), finding the data (fairness opinions, filings).
- When it's most useful: thin comps, hard-to-forecast cash flows, M&A context.
- *(BIWS Valuation guide: the precedents set and the control-premium discussion.)*
**Connects to.** Z3.3, `★ G99` control premium, `★ G89`, Z2.5 (premiums in M&A), `★ G105` fairness opinion (a common data source), PE Z4.11 (exit valuation).

### Z3.5 · Discounted Cash Flow Analysis `★ GLOBAL (G90)` `[process]`
**Quick definition.** Valuing a company intrinsically — projecting its unlevered free cash flow, discounting it at WACC, adding a terminal value, and bridging to equity value.
**Explainer covers.**
- The build: project UFCF (`G92`) over an explicit 5–10 year horizon → estimate WACC (`G91`) → calculate terminal value (`G93`) → discount and sum → bridge EV to equity value and per-share.
- Unlevered FCF defined: NOPAT + D&A ± Δ working capital − CapEx; why SBC is *not* added back; why it's capital-structure-neutral.
- Sensitivities and scenarios (discount rate vs. terminal growth) — why a DCF is a *range*, not a point.
- Mid-year convention, stub periods, and the normalized terminal year (the refinements).
- *(BIWS Valuation guide: the full Steel Dynamics UFCF → WACC → TV → football field build, plus APV and DDM variants.)*
**Connects to.** `★ G92` UFCF, `★ G91` WACC, `★ G93` terminal value, Z3.6, Z3.7, Z3.1 (the bridge), PE Z3.10 (the LBO/DCF the sponsor runs).

### Z3.6 · Unlevered Free Cash Flow `★ GLOBAL (G92)` `[core]`
**Quick definition.** The cash flow from the core business available to all investors before financing effects — the numerator a DCF discounts.
**Explainer covers.**
- The line items: revenue → EBIT → NOPAT (taxes on EBIT, not pre-tax income) → + D&A → ± change in working capital → − CapEx.
- Why "unlevered": it ignores interest and the capital structure, so it's consistent regardless of how the company is financed.
- What's deliberately excluded (net interest, most non-cash items, financing flows) and why.
- Projecting the drivers (revenue build, margin assumptions, CapEx vs. D&A discipline).
**Connects to.** Z3.5, `★ G91` WACC (its partner), `★ G24` EBITDA, `★ G31` working capital, `★ G92`, Credit Z3.x (cash-flow lending shares this logic).

### Z3.7 · WACC & Terminal Value `★ GLOBAL (G91)` `[core]`
**Quick definition.** The two hardest inputs to a DCF — the blended discount rate (WACC) and the value of all cash flows beyond the forecast (terminal value).
**Explainer covers.**
- **WACC:** cost of equity (CAPM: risk-free + β × equity risk premium) × %equity + after-tax cost of debt × %debt; un-levering and re-levering beta off the peer set.
- **Terminal value (`G93`):** perpetuity-growth (Gordon) method vs. exit-multiple method; cross-checking one against the other.
- Why terminal value is usually the majority of a DCF's value — and the discipline of keeping terminal growth below GDP.
- The sensitivity grid: WACC vs. terminal growth as the standard two-way table.
- *(BIWS Valuation guide: the full WACC build, beta un-levering, and both terminal-value methods.)*
**Connects to.** Z3.5, Z3.6, `★ G93` terminal value, `★ G29` leverage (capital-structure weights), `★ G91`, PE Z3.11 (ability-to-pay analysis).

### Z3.8 · Supplemental Valuation Methods `[core]`
**Quick definition.** The valuations beyond the core three — the LBO/ability-to-pay analysis, asset-based/liquidation (NAV), the dividend discount model, and M&A premiums analysis.
**Explainer covers.**
- **LBO analysis as a valuation:** what a financial sponsor *could pay* given a target IRR and available leverage — the floor under many M&A processes (ties directly to PE Z3.10–Z3.11).
- **Liquidation / NAV:** market-valuing assets minus liabilities — the floor for distressed companies and a key RX tool (ties to Z2.15).
- **Dividend Discount Model:** for banks, insurers, REITs — where FCF and EV multiples don't apply.
- **M&A premiums analysis:** valuing off premiums paid over unaffected share prices.
- *(BIWS Valuation guide: liquidation, DDM, future-share-price, and premiums analyses.)*
**Connects to.** Z3.5, PE Z3.10 (the LBO model), PE Z3.11 (ability to pay), Z2.15 (RX/liquidation), `★ G1` IRR, Credit Z3.x (asset-based lending shares the NAV lens).

### Z3.9 · The Valuation Football Field `★ GLOBAL (G94)` `[core]`
**Quick definition.** The summary chart that stacks the value range from each methodology side by side — the banker's headline output and the anchor of every pitch and fairness opinion.
**Explainer covers.**
- Construction: plot the 25th–75th percentile range from comps, precedents, DCF, and LBO on one bar chart.
- How to read it: where the ranges overlap is the defensible value; outliers (precedents high on control premium) are explained, not hidden.
- How it frames the advice — "what's it worth," "is now a good time to sell," "what premium to expect."
- Why it's the single most-reproduced slide in banking.
- *(BIWS Valuation guide: the Steel Dynamics football field and the board-advice framing.)*
**Connects to.** Z3.2, Z3.3, Z3.4, Z3.5, Z3.8, `★ G94`, `★ G105` fairness opinion, Z3.10 (it anchors the pitch), PE Z4.11 (exit valuation).

## Sub-zone 3B — The Execution Process

### Z3.10 · The Pitch & Winning the Mandate `★ GLOBAL (G85)` `[process]`
**Quick definition.** The competitive process of winning the right to advise — building the pitchbook, presenting the strategic and valuation view, and signing the engagement.
**Explainer covers.**
- The pitchbook anatomy: situation analysis → strategic alternatives → valuation (the football field) → credentials/"why us."
- The bake-off and the relationship dimension (mandates are won on trust as much as analysis).
- The engagement letter: scope, success fee, exclusivity, tail.
- How the pitch sets up the entire execution that follows.
**Connects to.** Z1.8, `★ G85`, `★ G84` mandate, `★ G94` football field, Z3.11 (what comes after the win), `★ G87` valuation toolkit.

### Z3.11 · Due Diligence & the Data Room `★ GLOBAL (G28 — IB context)` `[process]`
**Quick definition.** The systematic investigation of a target's business, financials, legal standing, and risk — organized through a (virtual) data room — that underpins valuation, the offering, and liability protection.
**Explainer covers.**
- Buy-side/commercial, financial, legal, and tax diligence workstreams.
- The data room: how information is staged, controlled, and tracked between seller and bidders.
- Underwriting due diligence and securities-law liability (why diligence is legally load-bearing, not box-ticking).
- How diligence findings feed price, structure, and reps & warranties.
- *(This is the same `★ G28` due-diligence node as PE Z3.4 and Credit Z3.5 — here seen from the advisor/underwriter's seat; cross-link all three.)*
**Connects to.** `★ G28` due diligence (shared), Z3.12 (marketing), Z1.10 (underwriting liability), PE Z3.4 (the sponsor's DD), Credit Z3.5 (the lender's credit DD), `★ G36` SPA.

### Z3.12 · Marketing the Deal: Auctions, CIMs & Buyer Outreach `[process]`
**Quick definition.** How a sell-side advisor markets an asset to the right buyers — the teaser, the CIM, the auction structure, and managing competitive tension to maximize price and certainty.
**Explainer covers.**
- The sell-side auction: broad vs. targeted vs. negotiated process; one-stage vs. two-stage.
- The marketing materials: the teaser (anonymous), the NDA, the Confidential Information Memorandum (CIM), the management presentation.
- The bid rounds: indicative bids → management meetings & data room → final binding bids.
- Creating and sustaining competitive tension — the core sell-side value-add.
- *(This is the bank-run mirror of PE Z3.1 deal sourcing and PE Z4.13 exits — the sponsor is on the other side of this process.)*
**Connects to.** Z2.3 (sell-side mandate), Z3.11 (the data room), Z3.13 (negotiation), PE Z3.1 (sponsor sourcing), PE Z4.13 (sponsor exit), `★ G84` mandate.

### Z3.13 · Negotiation, Documentation & the Fairness Opinion `★ GLOBAL (G105)` `[process]`
**Quick definition.** The end-game of a deal — negotiating price and terms, papering the definitive agreement, and (for boards) delivering a fairness opinion that the price is fair from a financial point of view.
**Explainer covers.**
- Negotiating price, structure, consideration mix, and risk allocation (reps, warranties, indemnities, MAC clauses).
- The definitive agreement (`★ G36` SPA / merger agreement) and the path from signing to closing.
- The fairness opinion (`G105`): what it is, the analysis behind it (anchored on the football field), and why boards require it (fiduciary and litigation protection).
- Conflicts and independence in fairness opinions (ties to Z1.10).
**Connects to.** Z3.12, `★ G105`, `★ G36` SPA, `★ G94` football field, Z1.10 (conflicts/independence), `★ G99` control premium, PE Z3.20 (transaction documentation).

### Z3.14 · Signing, Closing & Announcement `[process]`
**Quick definition.** The mechanics that take a negotiated deal from signed agreement to completed transaction — conditions, approvals, financing, and the public announcement.
**Explainer covers.**
- Signing vs. closing: the gap, and the conditions that must clear (regulatory/antitrust, shareholder vote, financing).
- Financing the close: how committed financing (a LevFin commitment letter) backstops a buyer's certainty of funds.
- Announcement, the stock reaction, and integration planning kickoff.
- Break fees, reverse break fees, and deal-protection devices.
**Connects to.** Z3.13, Z2.11 (LevFin commitment financing), Z4.1 (post-signing execution), `★ G100` consideration mix, PE Z3.20 (documentation/close).

---

# PART 5 · Zone 4 — Executing & Managing the Transaction

**What this zone is:** the "doing the work" layer that runs alongside and after a deal is struck — the ongoing execution mechanics, the cross-product workflows, and the post-deal realities. Where PE Zone 4 is the *holding period* and Credit Zone 4 is *monitoring & workout*, IB Zone 4 is **execution and deal management**: the work between mandate and close, and the bank's role as transactions play out. *(Source: Rosenbaum & Pearl, Ch. 6–7 process detail; BIWS merger-model mechanics.)*

**Learning sequence (logical path):**
`From mandate to close: managing the live deal → building & maintaining the model through the process → managing the financing → coordinating advisors & workstreams → post-announcement: integration support, stabilization, and follow-on work → when deals break or restructure.`
Front-door: **Z4.1**.

---

### Z4.1 · Managing a Live Transaction `[core]`
**Quick definition.** The project-management spine of execution — running the workstreams, timeline, and stakeholders that take a deal from signed mandate to close.
**Explainer covers.**
- The deal calendar and critical path; coordinating legal, accounting, tax, and financing advisors.
- Managing the client, the counterparty, and (in an auction) multiple bidders simultaneously.
- The analyst/associate workflow: keeping the model, the materials, and the data room current as facts change.
- Risk management: anticipating diligence findings, financing wobbles, and regulatory friction.
**Connects to.** Z3.12, Z3.14, Z1.9 (the deal team), Z4.2 (the model), `★ G84` mandate.

### Z4.2 · Building & Maintaining the Model Through the Deal `★ GLOBAL (G97)` `[process]`
**Quick definition.** The living analytical model — valuation, merger/LBO, and financing — that's continuously updated as the transaction evolves.
**Explainer covers.**
- The merger model (`G97`) end-to-end: purchase-price allocation, combined projections, synergies, accretion/dilution, pro-forma credit stats.
- Keeping valuation (the football field) and the model in sync as diligence and negotiation shift assumptions.
- Sensitivity and scenario updates for client and committee decisions.
- Hand-offs between the model and the financing/credit committee materials.
- *(BIWS M&A guide: the full merger-model construction and the contribution analysis.)*
**Connects to.** Z2.4, `★ G97`, `★ G96` accretion/dilution, `★ G98` synergies, Z3.5 (the valuation feeding it), PE Z3.10 (the LBO model variant).

### Z4.3 · Managing the Financing `[process]`
**Quick definition.** Coordinating the debt and equity that funds a transaction — from commitment to syndication to funding at close — the seam where M&A meets LevFin/ECM/DCM.
**Explainer covers.**
- Committed financing: the commitment letter, the "flex," and certainty of funds for an acquirer.
- Syndicating the debt (ties to Z2.13) and placing any equity (ties to Z2.7) to fund the deal.
- Managing financing risk: market windows, ratings, and the arranger's exposure to un-sold paper.
- The interplay with the merger model's pro-forma capital structure and credit stats.
**Connects to.** Z2.11 (LevFin), Z2.13 (syndication), Z2.7 (ECM), Z3.14 (funding the close), Credit Z2.2 (private credit as the competing/complementary funding source), `★ G33` debt stack.

### Z4.4 · Coordinating Advisors & Workstreams `[core]`
**Quick definition.** The bank's role orchestrating the full advisor cast — legal, accounting, tax, consultants, and other banks — across a complex transaction.
**Explainer covers.**
- Who does what: M&A counsel, financing counsel, auditors, tax structurers, commercial-diligence consultants.
- Managing co-advisors and the syndicate (multiple banks on one deal).
- Information flow, the data room, and keeping workstreams synchronized to the critical path.
- Where the lead bank adds value as conductor vs. where it executes directly.
**Connects to.** Z4.1, Z3.11 (diligence), Z3.13 (documentation), Z1.10 (conflicts across roles), `★ G36` SPA.

### Z4.5 · Post-Announcement: Integration Support, Stabilization & Follow-On `[core]`
**Quick definition.** The bank's continuing role after a deal is announced or priced — supporting integration thinking, stabilizing a new issue, and lining up the next mandate.
**Explainer covers.**
- M&A: high-level integration and synergy-tracking support; the (limited) banker role post-close.
- ECM: aftermarket stabilization, the greenshoe, research initiation, and follow-on planning.
- The franchise flywheel: a closed deal seeds the next one (refinancing, bolt-ons, the eventual sale).
- Why the relationship — not the single deal — is the real asset (ties to Zone 5).
**Connects to.** Z2.8 (IPO stabilization), Z2.5 (synergies realized), Z1.6 (the sponsor relationship), Z5.1 (the franchise), PE Z4.13 (the next exit).

### Z4.6 · When Deals Break or Restructure `[core]`
**Quick definition.** What happens when a transaction fails, is renegotiated, or the underlying company later distresses — and how the bank's role shifts.
**Explainer covers.**
- Deal breaks: failed conditions, financing falling through, regulatory blocks, walk-aways — and break/reverse-break fees.
- Renegotiation under a material adverse change or financing gap.
- The hand-off to Restructuring when a financed company later distresses (ties to Z2.14).
- Reputational and league-table consequences of broken deals.
**Connects to.** Z3.14 (conditions/break fees), Z2.14 (Restructuring), Z4.3 (financing risk), Credit Z4.7 (the lender's workout side), `★ G81` workout.

---

# PART 6 · Zone 5 — The Franchise, the Business & the Relationship

**What this zone is:** the meta-layer — investment banking *as a business*. League tables and the franchise, the client relationship as the durable asset, how a bank competes and gets paid over time, talent and the career, and the regulatory/structural forces shaping the industry. Mirrors PE Zone 5 (fund management & LP relations) and Credit Zone 5 (fund economics & the LP relationship). *(Source: Rosenbaum & Pearl framing; industry structure throughout.)*

**Learning sequence (logical path):**
`The franchise & league tables → the economics of a banking business → the client relationship as the asset → how banks compete (scale vs. boutique) → talent, the career & the buy-side exit → the regulatory & structural forces reshaping the industry → where investment banking is heading.`
Front-door: **Z5.1**.

---

### Z5.1 · The Franchise: What a Bank Is Really Selling `[core]`
**Quick definition.** The durable asset under a banking business — reputation, relationships, sector credibility, and distribution reach — that wins repeat mandates beyond any single deal.
**Explainer covers.**
- Why the franchise (not the deal) is the asset: trust, track record, and the ability to execute at scale.
- The components: brand, league-table credibility, sector expertise, distribution to the buy-side, and balance sheet.
- How a franchise compounds — each deal builds the relationship that wins the next.
- Bulge-bracket franchise (scale, balance sheet, full product) vs. boutique franchise (independence, advice, no conflicts).
**Connects to.** Z5.2, Z5.3, Z1.11 (league tables intro), Z1.1, `★ G104` league tables.

### Z5.2 · League Tables & Competitive Position `★ GLOBAL (G104)` `[core]`
**Quick definition.** The published rankings of banks by deal volume and fees — the scoreboard that signals competitive position and feeds the franchise flywheel.
**Explainer covers.**
- How tables are compiled and sliced (by value/count, product, region, sector) — and gamed (credit allocation on multi-bank deals).
- What position buys: pitch credibility, pricing power, and talent.
- The split between "volume" league position (balance-sheet-driven) and "advisory quality" reputation (boutiques punch above their volume).
- Reading league tables critically — what they reveal and conceal.
**Connects to.** Z1.11, Z5.1, `★ G104`, Z1.7 (fees), Z5.4.

### Z5.3 · The Client Relationship as the Asset `[core]`
**Quick definition.** The long-horizon relationship between a bank and its recurring clients — especially corporates and financial sponsors — that turns one mandate into a decades-long revenue stream.
**Explainer covers.**
- Relationship banking vs. transactional banking; the coverage banker's role as long-term steward.
- The sponsor relationship as the archetype (ties to Z1.6) — repeat M&A, financing, and exit mandates.
- Cross-selling across products (M&A → financing → ECM) over a client's lifecycle.
- Trust, continuity, and conflict management as relationship-preservers.
**Connects to.** Z1.5, Z1.6, Z5.1, Z2.1 (the product cross-sell), PE Z1.20 (the GP–LP relationship — the analogous trust bond on the buy-side).

### Z5.4 · How Banks Compete: Scale vs. Boutique, and Regulation `[core]`
**Quick definition.** The structural divide in the industry — full-service bulge brackets versus independent advisory boutiques — and the regulation that shapes how each competes.
**Explainer covers.**
- Bulge-bracket model: balance sheet, full product suite, financing power, global reach — and the conflicts that come with it.
- Elite-boutique model: conflict-free advice, senior attention, no lending — and why the model has gained share post-2008.
- The regulatory frame: capital rules, the research/banking wall, and conflict management (ties to Z1.10).
- How clients choose between scale and independence for a given mandate.
**Connects to.** Z5.1, Z5.2, Z1.10 (regulation/conflicts), Z1.1 (bank types), `★ G105` fairness opinion (independence as a selling point).

### Z5.5 · Talent, the Career & the Buy-Side Exit `[core]`
**Quick definition.** The human-capital engine of banking — the analyst-to-MD pyramid, the brutal apprenticeship, and the well-worn path from the sell-side to the buy-side.
**Explainer covers.**
- The career ladder and what changes at each rung (execution → management → origination).
- Recruiting and the two-year analyst program as a feeder to PE, hedge funds, and business school.
- Why banking is a training ground the whole buy-side recruits from (ties to `★ G83`).
- Compensation structure and the economics of a people business.
**Connects to.** Z1.9 (the deal team), Z1.3 (sell-side → buy-side), PE Z1.3 (where many analysts land), `★ G83` sell-side/buy-side.

### Z5.6 · Where Investment Banking Is Heading `[core]`
**Quick definition.** The forces reshaping the industry — the rise of private capital, boutique share gains, technology/AI in deal work, and the blurring line between banks and the buy-side.
**Explainer covers.**
- Private capital's rise: as sponsors and direct lenders grow, banks both serve them and compete with them (ties to the LevFin-vs-private-credit dynamic).
- Boutique advisory's structural share gains and the "independence" premium.
- Technology and AI in modeling, diligence, and origination.
- The blurring boundary: banks building private-capital arms; the buy-side disintermediating fees.
- *(Recency/coverage flag: the 2021–2025 private-credit surge and its competition with bank-led LevFin is a live, fast-moving story under-covered by the source spine — shared gap with the Credit map; see Part 9.)*
**Connects to.** Z5.4, Z2.11 (LevFin under pressure), Credit Z1.7 (private credit vs. BSL), Credit Z5.14 (private credit's future), `★ G104` league tables.

---

# PART 7 · Cross-zone & cross-module connective tissue

The graph's power is in the edges that **jump between zones and modules**. These are the highest-value links to build — they're what make IB feel like the connective hub of the whole app rather than a sixth silo. The strongest threads:

1. **The valuation toolkit (`G87`–`G95`) is the spine of the entire app's analytical layer.** It is introduced here (Z3.1–Z3.9), *reused by PE* (Z3.6 valuation, Z3.10–Z3.11 LBO/ability-to-pay), *reused by Private Credit* (credit underwriting and recovery valuation), and *becomes the core of the future Equity Research module*. EV/equity value, comps, the DCF, and WACC are one canonical set the whole product shares — build them deeply here.

2. **LevFin (Z2.11–Z2.13) is the literal bridge to Private Credit.** The leveraged loan a LevFin desk arranges *is* the instrument a direct lender holds: `★ G68` unitranche, `★ G69` SOFR, `★ G70` spread, `★ G71` OID, `★ G72` call protection, `★ G78` lien priority, `★ G79` intercreditor, `★ G80` credit agreement all live in *both* modules. Build the cross-link explicitly: "the bank arranges and distributes; the credit fund holds" — same paper, two seats.

3. **The IB ↔ PE deal loop.** A sell-side M&A process (Z3.12) *is* a sponsor's exit (PE Z4.13); a buy-side mandate (Z2.3) *is* a sponsor's acquisition (PE Z3.1); an IPO process (Z2.8) *is* a sponsor's IPO exit (PE Z4.14). The banker and the sponsor sit on opposite sides of the same table — cross-link each pair.

4. **The IPO double-node (`G53` ↔ `G102`).** PE owns "IPO as exit" (the selling shareholder's view); IB owns "IPO as issuance process" (the underwriter's view). Same event — explicitly link the two as the canonical example of one concept seen from two modules.

5. **Due diligence (`★ G28`) is a three-module shared node.** It appears as the sponsor's DD (PE Z3.4), the lender's credit DD (Credit Z3.5), and the advisor's/underwriter's DD (IB Z3.11) — same skill, three vantage points. One canonical node, three contextual entry points.

6. **Restructuring (Z2.14–Z2.15) meets Private Credit's workout side.** The RX banker advises the company or creditors; the credit fund *is* a creditor working out its loan (Credit Z4.7). The fulcrum-security/recovery analysis (`★ G61` LGD) is the shared analytical core — link the advisor's and the holder's views.

7. **EBITDA, EV, and the debt stack (`★ G24`, `★ G25`, `★ G33`)** thread through all three modules as the shared primitives: the unit of valuation (comps/DCF here), the thing a sponsor prices (PE Z3.6), and the thing a lender lends against (Credit Z3.x). One set, dozens of contextual uses.

8. **The franchise/relationship parallel.** The IB client relationship (Z5.3), the PE GP–LP relationship (PE Z1.20), and the credit-fund LP relationship (Credit Z5.x) are the same "trust is the durable asset" idea across the sell-side and buy-side — link them as a cross-module theme.

---

# PART 8 · Suggested master path (for the "guided sequence" mode)

The app lets users jump anywhere, but the **default suggested sequence** a professional would follow:

1. **Zone 1 — The IB Ecosystem** (what banking is, who it serves, how it's organized and paid) → this is also the "how Wall Street works" primer content.
2. **Zone 2 — The Product Groups** (the desk you'd join), entering at the spectrum (Z2.1) and branching to M&A, ECM, DCM, LevFin, or Restructuring.
3. **Zone 3 — Doing Deals** (the analytical and execution core), taught in order: the valuation toolkit first (Z3.1 → Z3.9), then the execution arc (Z3.10 → Z3.14). *This is the heart of the module.*
4. **Zone 4 — Executing & Managing the Transaction** (the live-deal mechanics), chronologically from mandate to close.
5. **Zone 5 — The Franchise & the Business** (the meta-layer), once the deal lifecycle makes sense.

**Cross-module on-ramp:** because a deal is one event seen from three seats, a natural advanced path is to study **IB Zone 3 (the advisor's toolkit)**, **PE Zone 3 (the sponsor's buyout)**, and **Private Credit Zone 3 (the lender's loan)** *side by side*, converging on the shared glossary spine (EBITDA, EV/equity value, the debt stack, the valuation toolkit, due diligence).

**Within-zone entry points for non-linear users:** Z1.1, Z2.1, Z3.1 (analytics) / Z3.10 (process), Z4.1, Z5.1 are the natural "front doors." Every other node is reachable directly and links back to its prerequisites via the glossary layer, so no user is ever stranded.

---

# PART 9 · Source gaps — material we need but don't have

Flagged exactly as the PE and Credit maps do. Every node carrying a `GAP:` concern should show a "source needed" flag in the CMS so content isn't written from memory where the books are thin, dated, or unreadable.

**High priority (blocks or weakens whole node clusters):**
1. **A text-based Rosenbaum & Pearl (the primary spine itself).** The copy in the Drive is a scanned/image PDF with no extractable text and is over the connector's download limit, so its *mechanics* couldn't be read directly — only its structure inferred. The BIWS guides carried the technical load, but the canonical M&A-process and capital-markets narrative (Ch. 6–7) is under-sourced as a result. → **Add a text-based PDF of Rosenbaum & Pearl** to retire the `GAP:` flags on the execution-process nodes (Z3.10–Z3.14, Z4.x) and the capital-markets branches.
2. **Capital-markets (ECM/DCM) depth.** The BIWS guides are valuation- and M&A-centric; the equity- and debt-issuance branches (Z2.7–Z2.10) lean on the scanned book and general knowledge. → Needs a dedicated capital-markets/securities-issuance source (e.g., an ECM/DCM practitioner text or current LSTA/ICMA materials).
3. **Restructuring depth (Z2.14–Z2.15).** Treated here at survey level; the distressed/RX analytics deserve a real spine. → **Moyer, *Distressed Debt Analysis*** (already in the Drive for the Credit module) is the natural shared source — wire RX here to the same nodes as Credit Zone 4. Still needs a *modern* LME/creditor-on-creditor supplement (see recency gaps).
4. **The financial sponsors / LevFin commitment mechanics (Z4.3, Z2.13).** Committed-financing structures, the "flex," and certainty-of-funds are sketched. → A dedicated leveraged-finance practitioner source.

**Medium priority (deepens existing nodes):**
5. **Merger-model and LBO-model mechanics at full depth (Z2.4, Z4.2, Z3.8).** The BIWS M&A guide gives the build, but a full case-driven LBO/merger modeling source would deepen it. → Ties to PE Z3.10 — a shared modeling-mechanics gap with the PE map (PE Part 9, item 2).
6. **Fairness opinions & deal-litigation context (Z3.13, Z1.10).** The fiduciary/legal frame around fairness opinions and deal protection is thin. → A deal-law/M&A-legal source.
7. **Sector-specific banking nuance (FIG, real estate, energy).** Valuation and deal conventions differ sharply by sector (banks use DDM/P-BV; real estate uses NAV/FFO). → Sector-specific sources (ties to the future Real Estate and sector modules).
8. **ECM/IPO market structure post-2020 (Z2.8–Z2.9).** Direct listings, SPACs, and modern bookbuilding have shifted the IPO landscape. → A current ECM-markets source.

**Recency gaps (the BIWS guides and the standard Rosenbaum & Pearl editions trail the market — flag for every node touched):**
9. **Private credit's competition with bank-led LevFin (Z2.11, Z5.6).** The 2021–2025 surge of direct lending taking share from (and converging with) broadly syndicated LevFin is the defining current shift and post-dates the spine. *Shared, live gap with the Credit map (Credit Part 9, items 12 & 15).*
10. **Modern liability management (LME) in Restructuring (Z2.13, Z2.15).** Uptier/priming exchanges, drop-down financings, and the doc-protection arms race are post-2020 and absent from the standard sources. *Shared living gap with the Credit map (Credit Part 9, item 1).*
11. **Boutique advisory's structural rise & the post-2008 industry restructuring (Z5.4, Z5.6).** The independent-advisory share gain and the modern conflict regime need a current industry source.
12. **AI/technology in deal execution (Z5.6, Z1.9).** The automation of modeling, diligence, and origination is moving fast and is unaddressed by the source texts.
13. **SPACs, direct listings & alternative IPO routes (Z2.8).** The 2020–2022 SPAC cycle and direct-listing precedents reshaped going-public options — a debate the standard editions predate.

**Build note:** as with the PE and Credit maps, every `GAP:`/recency-flagged node should attach to its future source at the flagged connection point — when a text-based Rosenbaum & Pearl, a capital-markets source, or a current LME primer enters the Drive, its concepts become new nodes that clip onto these seams. The graph grows where it's marked to grow.

---

# PART 10 · Using this as the template — and what it contributes to the global graph

This module was built to the PE template (and refined against the Credit module), and it in turn extends the shared glossary for every module after it — most directly the **Equity Research** and **Real Estate** modules, which inherit its valuation spine.

**The five-zone spine, instantiated for investment banking and ready for the next disciplines:**

| Generalized zone | Private Equity | Private Credit | **Investment Banking (this module)** | Equity Research (next) |
|---|---|---|---|---|
| Z1 Ecosystem | The PE fund, GP/LP, fees | The lender ecosystem, BDCs, fee model | **The franchise, sell-side vs. buy-side, coverage vs. product, the fee model** | The sell-side/buy-side, the research product |
| Z2 Types | VC · Growth · Buyout · Distressed · Real assets | Direct lending · Unitranche · Mezz · Distressed · Specialty | **M&A · ECM · DCM · LevFin · Restructuring** | By sector / by mandate |
| Z3 Doing Deals | Source → DD → value → structure → docs | Originate → credit DD → structure → price → document | **The valuation toolkit + pitch → DD → market → negotiate → close** | Initiate → model → thesis → rating → publish |
| Z4 Managing | The hold & value creation → exit | Monitor → covenants → workout → recover | **Execute & manage the live transaction to close** | Maintenance, earnings, estimate revisions |
| Z5 Meta | Fund management, LP relations, performance | Fund economics, the CDLI, manager selection | **The franchise, league tables, the client relationship, the career** | The franchise, ratings, distribution |

**What transferred directly from the PE/Credit template:**
- **The node schema** (quick def → layered explainer → connections → tag) — identical.
- **The glossary-first build order** — cross-zone canonical nodes first, everything links back.
- **The "this vs. that" disambiguation pattern** — applied here to EV-vs-equity-value, comps-vs-precedents, synergies-vs-premium, IPO-as-exit-vs-IPO-as-process, and WACC-vs-cost-of-equity.
- **The learning-sequence-but-jumpable convention** with designated front-door nodes and glossary back-links.
- **The `GAP:` flagging discipline** — every thin, dated, or (here) unreadable-source edge marked as a future attachment point.

**What this module *reuses* from the shared glossary (not rebuilt):**
- **From PE (G1–G57):** `★ G1` IRR · `★ G2` MOIC · `★ G24` EBITDA · `★ G25` EV · `★ G26` equity value · `★ G27` multiples · `★ G28` due diligence · `★ G29` leverage · `★ G30` net debt · `★ G31` working capital · `★ G32` sources & uses · `★ G33` debt stack · `★ G34` covenant · `★ G36` SPA · `★ G37` preferred equity · `★ G40` cap table · `★ G42` dilution · `★ G52` exit · `★ G53` IPO-as-exit · `★ G54` trade sale · `★ G55` secondary buyout.
- **From Private Credit (G58–G82), via LevFin and Restructuring:** `★ G61` recovery/LGD · `★ G62` default/PD · `★ G68` unitranche · `★ G69` floating rate/SOFR · `★ G70` spread · `★ G71` OID · `★ G72` call protection · `★ G73` PIK · `★ G78` security/lien · `★ G79` intercreditor · `★ G80` credit agreement · `★ G81` workout.
- *Each is the same node; this module simply adds the advisor's/underwriter's-side context where relevant.*

**What this module *contributes* to the global graph (the new shared assets, G83–G105):**
- **Reused by future modules wholesale:** the valuation toolkit — `G87` (the three methodologies), `G88` comps, `G89` precedents, `G90` DCF, `G91` WACC, `G92` UFCF, `G93` terminal value, `G94` football field, `G95` EV↔EqV bridge — becomes the analytical core of the **Equity Research** module and is reused by **Real Estate** (with NAV/FFO variants). `G105` fairness opinion and `G99` control premium recur anywhere deals are valued.
- **Largely IB-owned but cross-referenced:** `G83` sell-side/buy-side, `G84` mandate, `G85` pitch, `G86` coverage/product, `G96` accretion/dilution, `G97` merger model, `G98` synergies, `G100` consideration mix, `G101` underwriting, `G102` IPO process, `G103` underwriting spread, `G104` league tables.
- **Genuinely module-defining:** the sell-side/buy-side franchise frame (`G83`/`G86`) and the league-table scoreboard (`G104`) — the structural signature of the banking business.

**The shared-glossary insight, restated for scale:** investment banking is the *proof case* that the glossary is the app's connective spine, because IB is where the other modules' threads converge. The same deal is a *mandate* here, an *acquisition* in PE, and a *loan* in Private Credit; the same valuation toolkit values a target here, prices a buyout in PE, and sizes a recovery in Credit. Building this module against the existing glossary — reusing G1–G82 and contributing G83–G105 — is what turns three courses into one knowledge graph, and hands the next modules (Equity Research, Real Estate) a ready-made valuation spine to clip onto.
