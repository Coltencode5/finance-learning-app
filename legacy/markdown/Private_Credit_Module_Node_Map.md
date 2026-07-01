# Private Credit Module — Complete Node Map

**The second structural blueprint for the finance learning app — built as an exact mirror of the PE module.** This is the fully-mapped Private Credit module: every learning node, organized into the same five zones, with quick definitions, layered explainer scopes, and knowledge-graph connections. It is deliberately the *same shape* as the PE map so the two modules interlock into one graph rather than sitting as two separate courses. Private credit and private equity are two sides of the same deal — the sponsor's equity and the lender's debt — so a huge fraction of this module's value is in the edges that cross back into PE.

**Sources mapped:** *Private Debt* (Stephen Nesbitt, Wiley) — **primary spine** for the asset class, the fund business, BDCs, and the Cliffwater Direct Lending Index; *Private Capital Investing* (Roberto Ippolito, Wiley) — debt products, credit structuring, and distress (the deal-mechanics layer); *Distressed Debt Analysis* (Stephen Moyer) — the distressed, workout, and recovery spine for Zone 4. Where these run thin or out of date, gaps are flagged in Part 9 exactly as the PE map does.

---

## How to read this map

Identical schema to the PE map. Every entry is a **node** carrying four things:

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

The app has **one global glossary**, not one per module. This module does **not** recreate primitives it shares with PE. Throughout the "Connects to" lines:

- **Globals `G1`–`G57` are the existing PE-map glossary nodes.** This module *reuses* them by number. When private credit puts a new spin on one (e.g., "leverage" seen from the lender's risk side instead of the sponsor's return side, or "EBITDA" seen through add-back scrutiny), that nuance is added as **new context on the existing node** — flagged below — not as a new node. IRR in PE and IRR in private credit are the *same node*.
- **Globals `G58`–`G82` are new, and this module contributes them to the app's global graph.** They are the concepts genuinely unique to credit (yield, the CDLI, recovery/LGD, BDCs, unitranche, OID, call protection, the borrowing base, intercreditor agreements, workouts, etc.). Several of these will be *reused* by the future Investment Banking (LevFin/restructuring), Equity Research (credit), and Real Estate modules — see Part 10.

**Shared PE globals this module leans on most** (referenced, never rebuilt):
`★ G1` IRR · `★ G2` MOIC · `★ G4` J-curve · `★ G6` GP · `★ G7` LP · `★ G8` Management fee · `★ G9` "2 and 20" · `★ G10` Carried interest · `★ G11` Distribution waterfall · `★ G12` Hurdle rate · `★ G15` Capital call · `★ G16` Committed/contributed capital · `★ G17` Dry powder · `★ G18` Vintage year · `★ G20` LPA · `★ G24` EBITDA · `★ G25` EV · `★ G26` Equity value · `★ G27` Valuation multiples · `★ G28` Due diligence · `★ G29` Leverage · `★ G30` Net debt · `★ G33` Debt stack · `★ G34` Covenant · `★ G35` SPV · `★ G52` Exit.

---

# PART 1 · The Global Glossary Layer (new nodes contributed by this module)

These are the new cross-zone canonical nodes private credit adds to the app. **Build these first** — they are the backbone the rest of the module links into, and many become shared assets for later modules. Each is written once, lives at one URL, and is referenced everywhere it appears. "Home" says which zone holds the deep explainer; "Appears in" shows link density. *(For the primitives this module shares with PE, see the shared-glossary rule above — those are G1–G57 and are not relisted here.)*

### A. Returns, yield & loss metrics

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| G58 | **Yield** | A loan's income return — cash coupon plus fees, expressed as cash yield, yield-to-maturity, or yield-to-3-year (assuming early take-out); credit's headline number, the way IRR is PE's. | Z5 | Z1, Z2, Z3, Z5 |
| G59 | **Cliffwater Direct Lending Index (CDLI)** | The benchmark tracking the total return of U.S. middle-market directly-originated loans (BDC-sourced) — the asset class's published track record. | Z5 | Z1, Z5 |
| G60 | **Credit loss rate** | Annualized losses on a portfolio = default rate × loss-given-default; the drag that turns gross yield into net return. | Z4 | Z1, Z4, Z5 |
| G61 | **Recovery rate / Loss Given Default (LGD)** | How many cents on the dollar a lender recovers when a borrower defaults — driven by seniority, security, and enterprise value. | Z4 | Z2, Z3, Z4 |
| G62 | **Default rate / Probability of Default (PD)** | The share of borrowers that breach or fail to pay over a period — distinct from *loss*, since a default with full recovery costs nothing. | Z4 | Z3, Z4, Z5 |

### B. Lenders, vehicles & the asset class

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| G63 | **Non-bank lending / Disintermediation** | The structural shift of corporate lending from regulated banks to asset managers — the force that created the asset class. | Z1 | Z1, Z5 |
| G64 | **Business Development Company (BDC)** | A U.S.-regulated, tax-pass-through (RIC) vehicle built to lend to private middle-market companies — the dominant access point for direct lending. | Z1 | Z1, Z4, Z5 |
| G65 | **Middle market** | The band of companies (segmented lower / core / upper by EBITDA) that private credit principally serves — too big for bank relationships, too small for the bond market. | Z1 | Z1, Z2, Z3 |
| G66 | **Sponsored vs. non-sponsored lending** | Whether a loan backs a PE-owned ("sponsored") company or is made direct to an independent borrower — the split that shapes sourcing, diligence, and pricing. | Z1 | Z1, Z3, Z5 |
| G67 | **Fund leverage & asset coverage** | Borrowing at the *fund* level (subscription lines, asset facilities, BDC debt) to lift a low-single-digit asset yield into a double-digit equity return — governed by asset-coverage limits. | Z5 | Z1, Z5 |

### C. Instruments & pricing

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| G68 | **Unitranche** | A single blended loan that fuses senior and subordinated debt into one instrument at one blended rate — private credit's signature product, often split first-out/last-out behind the scenes. | Z2 | Z2, Z3 |
| G69 | **Floating rate / Reference rate (SOFR)** | The base rate (SOFR, post-LIBOR) over which a loan's spread is set, usually with a floor — why private credit income rises with interest rates. | Z1 | Z1, Z3, Z5 |
| G70 | **Spread / Credit margin** | The fixed premium over the reference rate that compensates the lender for credit risk and illiquidity (e.g., SOFR + 550 bps). | Z3 | Z1, Z3, Z5 |
| G71 | **Original Issue Discount (OID)** | Funding a loan below par (e.g., at 98) so the lender earns the gap to par as extra yield — a routine pricing lever. | Z3 | Z1, Z3 |
| G72 | **Call protection / Prepayment economics** | Terms (non-call periods, make-wholes, soft-call 101, prepayment fees) that protect a lender's yield if the borrower repays early. | Z3 | Z1, Z3 |
| G73 | **PIK (Payment-in-Kind)** | Interest paid by adding to the loan balance instead of in cash — an upside feature in mezzanine, a stress signal when a healthy loan flips to PIK. | Z3 | Z2, Z3, Z4 |

### D. Credit metrics & underwriting

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| G74 | **Coverage ratios** | Tests of a borrower's ability to service debt from cash flow — interest coverage, fixed-charge coverage (FCCR), debt-service coverage (DSCR). | Z3 | Z3, Z4 |
| G75 | **Loan-to-Value (LTV)** | A loan sized as a percentage of an asset's value — the core risk gauge for asset-based and real-estate credit, where the asset, not cash flow, is the source of repayment. | Z3 | Z2, Z3 |
| G76 | **Borrowing base** | The dynamically-sized pool of eligible collateral (receivables, inventory, equipment) against which an asset-based revolver may draw, set by advance rates. | Z3 | Z2, Z3 |
| G77 | **Internal credit rating / Risk rating** | A lender's own scorecard grading each loan's risk — the engine behind watch-lists, pricing, reserves, and (mapped to agency scales) BDC/insurance reporting. | Z3 | Z3, Z4 |

### E. Security, seniority & documentation

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| G78 | **Security & collateral / Lien priority** | The assets pledged to a lender and the rank of its claim — first lien, second lien, unsecured — which sets who gets paid first in a default. | Z3 | Z1, Z2, Z3, Z4 |
| G79 | **Intercreditor agreement** | The contract ranking different lenders against each other — payment and lien subordination, standstills, and the Agreement Among Lenders that splits a unitranche. | Z3 | Z2, Z3, Z4 |
| G80 | **Credit / facility agreement** | The master loan contract — the credit analogue of the SPA — setting drawdown terms, covenants, representations, and events of default. | Z3 | Z3, Z4 |

### F. Workout & recovery

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| G81 | **Workout / Out-of-court restructuring** | The negotiated repair of a troubled loan outside bankruptcy — forbearance, amend-and-extend, new money, or debt-for-equity. | Z4 | Z2, Z4 |
| G82 | **Non-accrual & Watch-list** | The downgrade machinery for deteriorating credits — moving a loan onto a watch-list and stopping income recognition when repayment is in doubt. | Z4 | Z3, Z4 |

> **25 new global nodes (G58–G82).** Note the term-collisions learners trip over — build explicit "this vs. that" cross-links:
> - **Default (G62)** ≠ **Loss (G60).** A default is a missed payment or breach; a *loss* only happens if recovery (G61) falls short. Senior secured credit can have meaningful default rates and still tiny loss rates.
> - **Leverage as a *credit metric*** (Debt/EBITDA — the lender's risk gauge) vs. **Leverage as a *return amplifier*** (`★ G29`, the sponsor's tool). *Same ratio, opposite vantage point.* The borrower's leverage is the lender's risk; the lender's own fund-level leverage (G67) is yet a third thing.
> - **Unitranche (G68)** = one blended instrument · **Second lien (Z2.4)** = a separate junior tranche sitting behind a first lien. They solve the same junior-capital problem in opposite ways.
> - **Asset coverage (G67)** = a fund-/BDC-level regulatory leverage ratio · **Coverage ratios (G74)** = deal-level cash-flow tests. Same word "coverage," unrelated concepts.

---

# PART 2 · Zone 1 — The Private Credit Ecosystem

**What this zone is:** the foundational layer — what private credit is, why it exists, who lends, through what vehicles, and how a lender makes money. It is the mirror of PE's Zone 1, and like that zone it doubles as the credit half of any "how does lending work" primer. *(Source: Nesbitt, *Private Debt*, Pt. I; Ippolito, Ch. 1–2.)*

**Learning sequence (logical path):**
`What is private credit? → Why it exists (banks retreat) → The asset class & scale → Who lends (the ecosystem) → The middle market → Why borrowers choose it → vs. the syndicated loan market → Fund vehicles → BDCs → BDC rules & leverage → Sponsored vs. non-sponsored → How lenders make money → Seniority & security → Floating rate & income → Risk/return → The (missing) J-curve → Players inside a credit fund → The GP–LP relationship.`
The canonical beginner entry point is **Z1.1**.

---

### Z1.1 · What Is Private Credit? `[core]`
**Quick definition (basic → technical).** Privately negotiated, non-publicly-traded debt extended directly to companies by asset managers rather than banks or bond markets, generally held to maturity (or through a workout) for its contractual income.
**Explainer covers.**
- The simple model: originate a loan, earn the coupon and fees, get repaid (or restructure) — return is *contractual income*, not capital appreciation.
- Private credit vs. private equity: a lender's fixed, senior, downside-protected claim vs. an owner's residual, unlimited-upside stake — *two sides of the same deal*.
- Private credit vs. *public* credit (broadly syndicated loans, high-yield bonds): bilateral and illiquid vs. rated, traded, and liquid.
- The umbrella of strategies (direct lending → mezzanine → distressed → specialty) as one spectrum by seniority and risk.
- Why the asset class exists at all: a structural lending gap left by banks (Z1.2).
**Connects to.** Z1.2, Z2.1 (the strategy spectrum), `★ G29` Leverage, `★ G6` GP / `★ G7` LP, Z5.14 (evolution), and across the aisle: PE Z1.1 (*the equity counterpart*), PE Z2.21 (LBO — the deal private credit most often funds).

### Z1.2 · Why Private Credit Exists: Bank Retrenchment & Disintermediation `★ GLOBAL (G63)` `[core]`
**Quick definition.** The post-2008 regulatory and structural retreat of banks from middle-market and leveraged lending, which handed that lending to non-bank asset managers.
**Explainer covers.**
- The drivers: Basel III capital rules, Dodd-Frank, the Leveraged Lending Guidance, and post-crisis bank risk aversion.
- Disintermediation: lending moving from regulated deposit-funded balance sheets to fund-funded asset managers.
- Why this is *structural*, not cyclical — and the systemic-risk debate it raises (regulators now watching).
- The supply/demand fit: borrowers needing capital, institutions needing yield.
**Connects to.** Z1.1, Z1.3, Z1.7 (the market it took share from), Z5.14 (where it's heading), `★ G7` LP (the yield-seeking capital).

### Z1.3 · The Private Credit Asset Class & Its Growth `[core]`
**Quick definition.** The scale, shape, and rapid rise of private credit from a post-GFC niche into a multi-trillion-dollar pillar of institutional portfolios.
**Explainer covers.**
- Where it sits among alternatives (alongside PE, real assets, hedge funds).
- The growth story: AUM expansion since 2010 and the move from "alternative" to "core fixed-income substitute."
- The capital flywheel: strong relative returns → more LP allocation → more dry powder → competition.
- *(Recency flag: the books predate the 2021–2025 surge, the insurance-capital wave, and the "wall of money"/spread-compression debate — see Part 9.)*
**Connects to.** Z1.2, Z1.4, `★ G17` Dry powder, Z5.7 (the CDLI track record), Z5.14.

### Z1.4 · The Lender Ecosystem & Capital Sources `[core]`
**Quick definition.** The range of who actually lends — credit-focused asset managers, BDCs, insurance/annuity capital, separately managed accounts, and the institutions behind them.
**Explainer covers.**
- The manager landscape: standalone credit shops and the credit arms of mega-managers.
- Capital sources: pensions, endowments, sovereign wealth, *and especially insurers/annuity writers* (the defining modern source).
- Access vehicles: commingled funds, BDCs, SMAs, rated-note feeders, CLO financing.
- The convergence of "private credit" and "asset management" into one industry.
**Connects to.** `★ G7` LP, Z1.8 (the vehicles), Z1.9 (BDCs), Z5.4 (fundraising), Z5.12.

### Z1.5 · The Middle Market `★ GLOBAL (G65)` `[core]`
**Quick definition.** The segment of companies — typically split lower, core, and upper by EBITDA — that private credit principally finances.
**Explainer covers.**
- Segmentation: lower MM (≈ <$25M EBITDA), core MM (≈ $25–75M), upper MM (≈ $75–100M+); definitions vary by lender.
- Why the middle market is structurally underserved (too big for bank relationship lending, too small for the bond/BSL market).
- How segment choice drives everything: deal size, pricing, leverage, competition, and lender scale.
- The move *up-market* over time as funds got bigger (and the convergence with syndicated lending at the top).
**Connects to.** Z1.1, Z2.2 (direct lending lives here), Z3.2 (sourcing by segment), `★ G24` EBITDA (the unit of measure), Z1.7.

### Z1.6 · Why Borrowers Choose Private Credit `[core]`
**Quick definition.** The reasons a company takes a private loan over a bank facility or a bond — speed, certainty, confidentiality, flexibility, and a single relationship — and the price it pays for them.
**Explainer covers.**
- Speed and certainty of execution (one lender, no syndication/ratings process).
- Confidentiality, structuring flexibility, and a hold-to-maturity relationship partner.
- Certainty in volatile markets (private credit stays open when public markets shut).
- The trade-off: a higher coupon and tighter covenants than a syndicated loan.
**Connects to.** Z1.7 (the alternative), Z1.5, Z3.2 (origination), `★ G34` Covenant (the strings attached), Z2.2.

### Z1.7 · Private Credit vs. the Broadly Syndicated Loan (BSL) Market `[core]`
**Quick definition.** How a privately-held, bilateral, covenanted loan differs from a rated, widely-distributed, tradable syndicated loan (the Term Loan B market).
**Explainer covers.**
- BSL mechanics: arranger banks, credit ratings, hundreds of holders, secondary-market liquidity, mostly cov-lite.
- Private credit's contrast: bilateral or small-club, illiquid, hold-to-maturity, historically tighter covenants.
- Where they compete and *converge* (jumbo unitranche deals now rival BSL on size; covenant erosion at the top).
- How a borrower (and its sponsor) chooses between them.
**Connects to.** Z1.6, Z2.2, `★ G34` Covenant, Z2.16 (structured credit / CLOs sit in the BSL plumbing), Z5.8 (benchmarking against loan indices).

### Z1.8 · Fund Vehicles & Structures in Private Credit `[core]`
**Quick definition.** The legal wrappers used to hold private loans — closed-end drawdown funds, evergreen/perpetual funds, BDCs, SMAs, and rated structures.
**Explainer covers.**
- Closed-end drawdown funds (the PE-style 10-year vehicle) vs. open-end/evergreen perpetual funds.
- BDCs (Z1.9) and SMAs (large-LP custom mandates).
- Rated-note feeders and insurance-dedicated vehicles; CLOs as a *financing* technology for a loan book.
- Why the *perpetual/evergreen* structure fits an income product better than PE's finite life — and powers the private-wealth channel.
**Connects to.** `★ G20` LPA, Z1.9, Z5.1 (formation), Z5.12 (BDC structure), PE Z5.1 (the drawdown-fund template it borrows).

### Z1.9 · Business Development Companies (BDCs) `★ GLOBAL (G64)` `[core]`
**Quick definition.** A U.S.-regulated, tax-advantaged vehicle purpose-built to lend to private middle-market companies and pass its income through to shareholders.
**Explainer covers.**
- The legal basis (Investment Company Act of 1940, as amended) and RIC tax pass-through (distribute ≥90% of income, avoid entity tax).
- The ≥70% "qualifying assets" rule (private/thinly-traded U.S. companies).
- The three flavors: publicly-traded BDCs, non-traded (perpetual) BDCs, and private BDCs.
- Externally managed (most) vs. internally managed; the wealth-channel role of non-traded BDCs.
**Connects to.** Z1.10 (its rules), Z1.8, Z4.11 (its fair-value duty), Z5.12 (its economics), `★ G7` LP / retail access.

### Z1.10 · BDC Regulation, Leverage & Asset Coverage `★ GLOBAL (G67 — home)` `[core]`
**Quick definition.** The regulatory frame governing a BDC's borrowing, distributions, and valuation — most importantly the asset-coverage (leverage) limit.
**Explainer covers.**
- Asset coverage: the move from 200% (1:1 debt/equity) to **150% (2:1)** under the Small Business Credit Availability Act (2018), and what doubling allowable leverage did to returns *and risk*.
- The RIC distribution mandate and its cash-flow implications.
- Mandatory quarterly fair-value reporting and board valuation duties.
- How fund-level leverage (subscription lines, asset facilities) lifts a single-digit asset yield to a double-digit equity return.
**Connects to.** Z1.9, Z5.3 (fund leverage deep), `★ G29` Leverage, Z4.11 (valuation), Z5.13 (risk).

### Z1.11 · Sponsored vs. Non-Sponsored Lending `★ GLOBAL (G66)` `[core]`
**Quick definition.** Whether a loan backs a private-equity-owned company ("sponsored") or is made directly to an independently-owned business ("non-sponsored").
**Explainer covers.**
- Sponsored: relationship-driven repeat deal flow, a professional equity owner beneath the debt, an equity cushion, and reliance on the sponsor's diligence.
- Non-sponsored (direct-to-borrower): higher origination cost, more diligence to do yourself, often higher pricing and stronger terms, but harder to source at scale.
- How the split shapes sourcing, underwriting depth, pricing, and the lender–owner relationship.
**Connects to.** Z3.2 (sourcing channels), Z3.3 (diligence reliance), Z3.18 (sponsor doc leverage), PE Z1.3 (the sponsor is a PE GP), Z5.9 (a manager's origination edge).

### Z1.12 · How Private Lenders Make Money `[core]`
**Quick definition.** The components of a private-credit return — interest spread, upfront/OID, call protection, amendment fees — amplified by fund-level leverage.
**Explainer covers.**
- The income stack: spread over the reference rate, OID, arrangement/upfront fees, and ongoing amendment/consent fees.
- Call protection capturing yield when loans repay early.
- The leverage multiplier (fund-level borrowing on top of a senior loan book).
- Why this is a *yield* business, not a *capital-gains* business — and what that does to the return profile.
**Connects to.** `★ G70` Spread, `★ G71` OID, `★ G72` Call protection, `★ G67` Fund leverage, Z1.14, Z5.6 (yield metrics).

### Z1.13 · Seniority, Security & the Capital Structure `★ GLOBAL (part of G78)` `[core]`
**Quick definition.** Where private credit sits in a borrower's capital stack — usually at the top, first-lien and secured — and why that position is the heart of its downside protection.
**Explainer covers.**
- The capital structure from senior secured down to common equity; private credit's first-lien dominance.
- Security and collateral as downside protection; the equity cushion beneath the loan.
- How seniority maps directly to recovery in a default (the lender's safety net).
- The contrast with the sponsor's residual equity at the bottom of the stack.
**Connects to.** `★ G33` Debt stack (the PE-map node it deepens from the lender's side), `★ G78` Security/lien priority, Z2.4 (second lien), Z4.8 (recovery), `★ G29` Leverage.

### Z1.14 · Floating Rate & the Income Profile `★ GLOBAL (G69)` `[core]`
**Quick definition.** Private credit's predominantly floating-rate structure — a spread over a base rate (SOFR) with a floor — which makes its income rise as interest rates rise.
**Explainer covers.**
- The mechanic: reference rate + fixed spread, often with a base-rate floor.
- The LIBOR→SOFR transition and what changed.
- Why floating rate protects lenders (and stresses borrowers) when rates climb — the 2022–2024 rate cycle as the live case.
- The income-led, current-pay return profile this creates.
**Connects to.** `★ G70` Spread, Z3.10 (rates & floors), Z1.15, Z5.6 (yield), Z5.13 (rate risk), `★ G58` Yield.

### Z1.15 · Risk & Return Positioning of Private Credit `[core]`
**Quick definition.** Where private credit sits on the risk/return map — higher yield than public credit for bearing illiquidity and complexity, with historically low losses thanks to seniority.
**Explainer covers.**
- The illiquidity premium and complexity premium over public credit.
- Historically low realized loss rates in senior direct lending (seniority + security + covenants + workout effort).
- The position relative to high-yield bonds, leveraged loans, and equity.
- Where the *real* risk hides: leverage-on-leverage, vintage/cycle timing, and spread compression.
**Connects to.** `★ G58` Yield, `★ G60` Loss rate, `★ G61` Recovery, Z1.16, Z5.13 (risk), Z5.7 (the CDLI evidence).

### Z1.16 · The Private Credit J-curve (or the lack of one) `[core]` *(deepens `★ G4`)*
**Quick definition.** Private credit's near-absent J-curve — because loans pay current income from day one, an LP's cash flow turns positive far faster than in PE.
**Explainer covers.**
- Why the PE J-curve (`★ G4`) is deep and slow but the credit one is shallow and short: income arrives immediately, there's no multi-year "blind period" of fees-only.
- Current yield vs. capital appreciation as the source of return.
- How this changes LP cash-flow planning, pacing, and the appeal to income-seeking investors.
- *This is one of the highest-value cross-links in the app: same J-curve node, opposite shape, told from the credit side.*
**Connects to.** `★ G4` J-curve (*the canonical node — credit adds the "flat J-curve" contrast*), `★ G15` Capital call, `★ G58` Yield, Z5.5 (performance), PE Z1.18 (the equity-side J-curve).

### Z1.17 · Key Players & Roles Inside a Credit Fund `[core]`
**Quick definition.** The functional teams that run a private-credit platform — origination, underwriting/credit, portfolio management, capital markets, and workout — coordinated by a credit committee.
**Explainer covers.**
- Origination/coverage (sourcing), credit/underwriting (analysis and the credit memo), portfolio management (monitoring), capital markets (syndication/financing), and the workout team.
- The investment/credit committee as the decision body (the credit analogue of PE's IC).
- Why *workout capability* is a distinguishing competence, not an afterthought.
**Connects to.** PE Z1.3 (the structural parallel), Z3.3 (underwriting), Z4.1 (monitoring), Z4.5 (workouts), Z5.9 (what LPs diligence).

### Z1.18 · The GP–LP Relationship in Private Credit `[core]` *(deepens `★ G6`/`★ G7`)*
**Quick definition.** The manager–investor bond in credit — structurally like PE's, but reshaped by current income, lower fees, fund leverage, and a heavy insurance-capital presence.
**Explainer covers.**
- The fiduciary and reporting relationship (shared with PE) but with *income distributions* rather than back-ended carry.
- Lower fee load, incentive fees on income, and the alignment questions fund-level leverage raises.
- SMAs and the rise of the insurer-as-anchor-LP (and even owner-of-the-manager) model.
- Transparency expectations on marks, loss rates, and leverage.
**Connects to.** `★ G6` GP / `★ G7` LP / `★ G20` LPA (*shared nodes — credit nuance added here*), Z5.2 (fund economics), Z5.4 (the insurance LP), PE Z1.20 (the equity-side relationship).

---

# PART 3 · Zone 2 — Types of Private Credit

**What this zone is:** the strategy branches, ordered by seniority and risk — from the safest senior secured lending to the most opportunistic distressed and special-situations capital. The mirror of PE's Zone 2, with the spectrum node as the hub. *(Source: Nesbitt; Ippolito Ch. 2 & 11; Moyer for the distressed branch.)*

**Learning sequence (by seniority/risk — the natural ordering):**
`The spectrum → Direct Lending (senior) → Unitranche → Second Lien → Mezzanine → Distressed & Special Situations → Specialty Finance → Asset-Based Lending → Venture Debt → Real Estate Debt → Infrastructure Debt → NAV/Fund Finance → Opportunistic → Structured Credit/CLOs.`
The spectrum node (**Z2.1**) is the hub; each branch can be entered directly.

---

### Z2.1 · The Private Credit Strategy Spectrum `[core]`
**Quick definition.** A map of credit strategies by seniority, security, and target return — from senior secured direct lending (≈8–12%) through mezzanine (≈12–18%) to distressed/opportunistic (≈15–25%+).
**Explainer covers.**
- The axes: position in the capital structure · secured vs. unsecured · cash-flow vs. asset-based · sponsored vs. non-sponsored.
- How risk, return, and required skillset rise together down the stack (underwriting → structuring → restructuring).
- Where each strategy's capital comes from and who plays in it.
**Connects to.** All Zone 2 branch nodes, `★ G29` Leverage, `★ G78` Seniority, Z1.13, Z1.1.

## Branch 2A — Senior & Core Strategies

### Z2.2 · Direct Lending `[branch]`
**Quick definition.** The core strategy: senior secured, first-lien, floating-rate term loans made directly to middle-market companies (mostly PE-sponsored) and held to maturity.
**Explainer covers.**
- Defining characteristics: first-lien senior secured, floating rate, 5–7-year tenor, bilateral or small-club.
- The sponsored bias and the relationship/origination flywheel.
- Typical economics (spread + OID + fees + call protection) and the low historical loss rate.
- Why this is the strategy the CDLI measures and the asset class is built on.
**Connects to.** Z2.3, `★ G65` Middle market, `★ G66` Sponsored lending, `★ G69` Floating rate, `★ G78` Seniority, `★ G59` CDLI, PE Z2.21 (the LBOs it funds).

### Z2.3 · Unitranche `★ GLOBAL (G68)` `[branch]`
**Quick definition.** A single blended loan that fuses first-lien and subordinated debt into one instrument at one blended rate, frequently split first-out/last-out among lenders behind the scenes.
**Explainer covers.**
- The concept: one facility, one rate, one lender relationship — replacing a senior+sub structure.
- The hidden plumbing: first-out/last-out (FOLO) tranching via an **Agreement Among Lenders (AAL)**.
- The borrower appeal (speed, certainty, simplicity) and why it took share from both syndicated senior and mezzanine.
- Jumbo unitranche and the convergence with the BSL market at the large end.
**Connects to.** Z2.2, Z2.5 (the mezzanine it displaced), `★ G79` Intercreditor (the AAL), Z3.6 (structuring), Z3.16, Z1.7.

### Z2.4 · Second Lien Loans `[core]`
**Quick definition.** Junior secured debt that ranks behind a first lien on the same collateral but ahead of unsecured and equity.
**Explainer covers.**
- Where it sits: secured but subordinated; higher spread than first lien.
- The intercreditor relationship with the first lien (payment vs. lien subordination, standstills).
- When a borrower uses a 1L/2L structure vs. a unitranche.
- Recovery implications of being second in line on the collateral.
**Connects to.** `★ G78` Lien priority, `★ G79` Intercreditor, `★ G33` Debt stack, Z2.3 (the alternative), Z4.8 (recovery).

## Branch 2B — Junior & Subordinated

### Z2.5 · Mezzanine Debt `[branch]`
**Quick definition.** Subordinated debt — often unsecured — carrying a cash coupon plus PIK and sometimes warrants, sitting between senior debt and equity in both risk and return.
**Explainer covers.**
- The classic structure: cash interest + PIK + an equity kicker (warrants); 12–18% blended target.
- Its role bridging the gap between senior debt and the sponsor's equity cheque.
- Why mezzanine *shrank* as unitranche absorbed the junior-capital role — and where it persists.
- Subordination, intercreditor terms, and downside in a restructuring.
**Connects to.** `★ G72` PIK, `★ G33` Debt stack, `★ G79` Intercreditor, Z2.3 (its replacement), Z2.15, `★ G29` Leverage.

## Branch 2C — Distressed & Special Situations *(Moyer spine)*

### Z2.6 · Distressed Debt & Special Situations `[branch]`
**Quick definition.** Investing in the debt of stressed or distressed companies — buying at a discount to par to earn a high return on recovery, a restructuring, or a control outcome.
**Explainer covers.**
- The spectrum: stressed/performing-distressed (mispriced but paying) vs. deep distressed (default likely or underway).
- Trading distressed paper vs. originating rescue capital.
- The Moyer analytical frame: value the enterprise, find where value "breaks," and price the security accordingly.
- Why Europe and the U.S. differ (insolvency regimes) and why this is a specialist skillset.
**Connects to.** Z2.7, Z2.8, `★ G81` Workout, `★ G61` Recovery, Z4.6 (Chapter 11), PE Z2.26 (*distressed PE — the equity-control cousin*).

### Z2.7 · Loan-to-Own / Distressed-for-Control `[core]`
**Quick definition.** Using a distressed debt position to take equity control of a company through a restructuring, by holding the security that converts to ownership.
**Explainer covers.**
- The strategy: buy the *fulcrum* debt, drive the restructuring, convert to controlling equity.
- Why it blurs the credit/PE line (a lender becomes an owner).
- Execution risk: the restructuring process, creditor classes, and contested control.
**Connects to.** Z2.8 (the fulcrum), `★ G82` Watch-list, Z4.6 (in-court process), PE Z2.26 (the equity outcome), `★ G61` Recovery.

### Z2.8 · The Fulcrum Security `[core]`
**Quick definition.** The layer of the capital structure where enterprise value runs out — the security that absorbs losses and typically converts to equity in a restructuring.
**Explainer covers.**
- How to identify it: estimate enterprise value, walk down the stack, find where value "breaks."
- Why owning the fulcrum is the key to a loan-to-own play.
- How valuation uncertainty makes fulcrum identification the central analytical bet (the core Moyer skill).
**Connects to.** Z2.7, `★ G61` Recovery / LGD, `★ G33` Debt stack, `★ G25` Enterprise Value (*shared PE node — the valuation it rests on*), Z4.8.

## Branch 2D — Asset-Based & Specialty

### Z2.9 · Specialty Finance `[branch]`
**Quick definition.** Niche, often non-corporate lending against specific cash-flowing assets — equipment, receivables, royalties, consumer loans, litigation claims, trade finance, and more.
**Explainer covers.**
- The breadth: equipment finance, factoring/receivables, royalty/IP finance, consumer/point-of-sale, litigation finance, trade finance.
- The common thread: lend against a defined asset or cash-flow stream, not a corporate balance sheet.
- Mostly non-sponsored, structurally complex, and the frontier of "asset-based finance" (ABF).
- *(Source thin — see Part 9; the ABF boom largely post-dates the books.)*
**Connects to.** Z2.10 (ABL is its corporate sibling), `★ G75` LTV, `★ G76` Borrowing base, Z5.14 (the ABF frontier), `★ G78` Security.

### Z2.10 · Asset-Based Lending (ABL) `[branch]`
**Quick definition.** Revolving credit secured by and sized to specific working-capital assets — receivables, inventory, equipment — via a dynamically-measured borrowing base.
**Explainer covers.**
- The mechanic: a borrowing base = eligible collateral × advance rates (e.g., 85% of receivables, 50% of inventory).
- Why ABL is lower-risk/lower-yield than cash-flow lending (repayment comes from the assets).
- Monitoring via borrowing-base certificates and field exams.
- When a borrower is an ABL candidate vs. a cash-flow candidate.
**Connects to.** `★ G76` Borrowing base, `★ G75` LTV, Z3.13 (ABL structuring), Z2.9, `★ G78` Security.

## Branch 2E — Sector & Specialist Credit

### Z2.11 · Venture Debt `[branch]`
**Quick definition.** Debt extended to venture-backed, often pre-profit start-ups — typically alongside equity, with warrants — to extend runway without further dilution.
**Explainer covers.**
- The model: lend against the backing of strong VC investors and growth, not current cash flow.
- Warrants and the equity kicker; runway extension between equity rounds.
- The risk profile (binary, sponsor-of-record-dependent) and why it's a distinct discipline.
**Connects to.** PE Z2.2 / Z2.5 (*the VC equity it complements*), `★ G72` PIK, `★ G40` Cap table (shared), Z2.9.

### Z2.12 · Real Estate Debt / CRE Lending `[branch]`
**Quick definition.** Property-secured lending across the capital stack — senior mortgages, mezzanine, bridge, and construction loans — sized on loan-to-value.
**Explainer covers.**
- The property capital stack: senior mortgage → mezz → preferred → equity.
- Bridge, transitional, and construction lending; LTV as the master risk gauge.
- How the cycle, rates, and asset type drive credit risk.
- *(Needs a dedicated real-estate-credit source — see Part 9.)*
**Connects to.** `★ G75` LTV, `★ G78` Security, PE Z2.27 (*real assets — the equity side*), Z2.13.

### Z2.13 · Infrastructure Debt `[branch]`
**Quick definition.** Long-dated lending to infrastructure and project-finance assets, prized for stable, often investment-grade-like, yield.
**Explainer covers.**
- Project-finance structures and long tenors; greenfield vs. brownfield vs. operating risk.
- The yield/duration appeal to insurers and long-horizon LPs.
- How the return and risk profile differs from corporate direct lending.
- *(Needs a dedicated infrastructure-finance source — see Part 9.)*
**Connects to.** PE Z2.27 (real assets), `★ G69` Floating vs. fixed, Z5.4 (insurance capital), Z2.12.

## Branch 2F — Fund-Level & Structured

### Z2.14 · NAV Lending & Fund Finance `[branch]`
**Quick definition.** Lending against the assets or uncalled commitments of investment funds themselves — subscription (capital-call) lines, NAV facilities, and GP financings.
**Explainer covers.**
- Subscription lines (secured on LP commitments) vs. NAV facilities (secured on portfolio value) vs. GP/management-company loans.
- Why this market exploded — and how subscription lines *flatter reported IRRs* by deferring capital calls.
- The risk debate (leverage on leverage at the fund level).
- *This node directly fills PE-map gap #10 (fund finance / NAV lending).*
**Connects to.** `★ G15` Capital call (*the commitments it lends against*), `★ G4` J-curve / `★ G1` IRR (*the metrics it distorts*), `★ G67` Fund leverage, PE Z5.7 (LP pacing).

### Z2.15 · Opportunistic & Capital-Solutions Credit `[branch]`
**Quick definition.** Flexible, all-weather mandates that provide bespoke capital — rescue financing, structured equity, preferred, and hybrid solutions — across the cycle.
**Explainer covers.**
- Capital-solutions / "rescue" financing for companies shut out of normal markets.
- Hybrid instruments (structured preferred, PIK toggles, warrants) blending debt and equity features.
- Why these mandates flex toward distress in downturns and growth-financing in upturns.
**Connects to.** `★ G72` PIK, `★ G81` Workout, Z2.6 (distressed overlap), `★ G37` Preferred equity (shared), Z2.5.

### Z2.16 · Structured Credit & CLOs (as a strategy) `[branch]`
**Quick definition.** Investing in — or issuing — collateralized loan obligations and other structured credit, including the equity and mezzanine tranches, and using CLOs to finance a loan book.
**Explainer covers.**
- CLO mechanics in brief: a pool of loans tranched into rated debt and an equity residual.
- Investing across the tranches (CLO equity/mezz) vs. *issuing* a CLO to finance direct lending.
- How structured credit connects private origination to the public/BSL plumbing.
- *(Light coverage — a dedicated structured-credit source is flagged in Part 9.)*
**Connects to.** `★ G33` Debt stack, Z1.7 (the BSL world), Z5.3 (CLO as fund financing), `★ G77` Credit ratings.

---

# PART 4 · Zone 3 — Originating & Structuring Deals

**What this zone is:** the deal process — the most sequential zone in the module, mirroring PE's Zone 3 but told from the *lender's* side: not "what do we pay to own it," but "can they repay us, what protects us if they can't, and how do we paper it." *(Source: Ippolito Ch. 6–11; Nesbitt; Moyer for distressed structuring.)*

**Learning sequence (the process is the order):**
`Origination funnel → Sourcing → Credit due diligence → Credit analysis → EBITDA & add-backs → Structuring the facility → Pricing → OID → Call protection → Spread/rates → Covenants → Security & lien priority → Borrowing base → LTV → The credit agreement → Intercreditor agreement → Internal ratings → Sponsor/doc dynamics.`
Best taught *in order*, but every node links to its glossary primitives so a user can drop in mid-process.

---

### Z3.1 · The Credit Origination Funnel & Value Chain `[core]`
**Quick definition.** The funnel narrowing many sourced lending opportunities down to the few loans actually closed — and the end-to-end value chain of a private-credit transaction.
**Explainer covers.**
- The stages: source → screen → indicative term sheet → credit committee → diligence → documentation → close → fund.
- Sponsored vs. direct channels feeding the top of the funnel.
- Conversion economics and why origination *volume and selectivity* both matter.
**Connects to.** Z3.2, `★ G28` Due diligence, all Zone 3 nodes, `★ G66` Sponsored lending, PE Z3.1 (*the equity-side funnel*).

### Z3.2 · Deal Sourcing & Origination Channels `[process]`
**Quick definition.** How private lenders originate loans — through sponsor coverage, agented/club deals, proprietary direct relationships, and incumbency in existing portfolios.
**Explainer covers.**
- Channels: sponsor coverage (the dominant one), agented/club deals, proprietary/direct, and add-ons to existing borrowers (incumbency).
- Why relationships and scale are the real origination edge.
- Sourcing differences between sponsored and non-sponsored markets.
**Connects to.** Z3.1, `★ G66` Sponsored lending, Z3.3 (what comes next), PE Z3.2 (the sponsor's own sourcing), Z1.6.

### Z3.3 · Credit Due Diligence & Underwriting `[process]` *(deepens `★ G28`)*
**Quick definition.** The lender's systematic investigation of a borrower — focused on *ability to repay and downside recovery* rather than upside — culminating in a credit memo and committee decision.
**Explainer covers.**
- The domains: business/market, financial (quality of earnings), legal, and sponsor diligence.
- The lender's distinct lens vs. PE's: *can they service and repay the debt, and what do we recover if not?*
- The credit memo, the downside/recovery case, and the role of third-party advisors.
- How diligence findings drive structure, covenants, and pricing.
**Connects to.** `★ G28` Due diligence (*shared node — credit-underwriting nuance added here*), Z3.4, `★ G24` EBITDA, `★ G61` Recovery, PE Z3.4 (the equity-side DD).

### Z3.4 · Credit Analysis: Cash Flow, Leverage & Coverage `[core]`
**Quick definition.** The analytical core of underwriting — testing whether a borrower can pay interest, repay principal, and what a lender recovers if it can't.
**Explainer covers.**
- The three questions: interest serviceability (coverage), principal repayment (deleveraging / free cash flow), and downside (recovery).
- Key metrics: Debt/EBITDA, FCCR, DSCR, and free-cash-flow conversion.
- Building the base, downside, and recovery cases.
- *Leverage seen as the lender's risk gauge, not the sponsor's return amplifier.*
**Connects to.** `★ G29` Leverage (*shared node — the credit-metric lens*), `★ G74` Coverage ratios, `★ G24` EBITDA, Z3.5, `★ G61` Recovery.

### Z3.5 · EBITDA, Add-Backs & Adjusted EBITDA in Credit `[core]` *(deepens `★ G24`)*
**Quick definition.** The contested practice of "adjusting" a borrower's EBITDA upward — through add-backs and pro-forma synergies — which directly inflates how much debt a deal can carry.
**Explainer covers.**
- Why EBITDA is the denominator of every leverage and coverage test, so its *definition* is a battleground.
- Add-back types: run-rate, pro-forma, synergy, "one-time" costs — and the erosion of standards in hot markets.
- How aggressive add-backs understate true leverage and overstate covenant headroom.
- The lender's discipline: haircutting management's adjusted EBITDA.
**Connects to.** `★ G24` EBITDA (*shared node — the add-back controversy is the credit nuance*), `★ G34` Covenant, Z3.11, Z3.18 (doc leverage), `★ G29` Leverage.

### Z3.6 · Structuring the Facility `[process]`
**Quick definition.** Assembling the loan itself — facility types, tranching, amortization, tenor, and the leverage decision — to balance return against risk.
**Explainer covers.**
- Facility types: Term Loan A/B, revolving credit, delayed-draw term loans, accordion/incremental.
- Tranching (1L/2L vs. unitranche), amortization profiles, and tenor.
- Setting leverage and the size of the equity cushion required beneath.
**Connects to.** `★ G33` Debt stack, `★ G68` Unitranche, Z3.7 (pricing it), `★ G29` Leverage, Z2.2.

### Z3.7 · Loan Pricing & Economics `[core]`
**Quick definition.** How a loan's all-in return is built — spread over the reference rate, plus OID, upfront fees, and call protection — and the yield/IRR math that results.
**Explainer covers.**
- The components: spread (G70), base rate + floor (G69), OID (G71), arrangement/upfront fees, and call protection (G72).
- Translating those into cash yield, yield-to-maturity, and yield-to-3-year.
- How competition compresses spreads and erodes OID and call protection.
**Connects to.** `★ G58` Yield, `★ G70` Spread, `★ G71` OID, `★ G72` Call protection, `★ G69` Floating rate, Z5.6.

### Z3.8 · Original Issue Discount (OID) `★ GLOBAL (G71 — home)` `[core]`
**Quick definition.** Funding a loan below par (e.g., at 98) so the lender earns the difference to par as additional yield on top of the coupon.
**Explainer covers.**
- The mechanic and how OID converts into incremental yield over the loan's life.
- Why lenders use it (yield enhancement, downside buffer) and borrowers accept it.
- How OID widens or compresses with market conditions.
**Connects to.** `★ G58` Yield, Z3.7, `★ G70` Spread, Z1.12.

### Z3.9 · Call Protection & Prepayment Economics `★ GLOBAL (G72 — home)` `[core]`
**Quick definition.** Terms that protect a lender's expected yield if a borrower repays early — non-call periods, make-wholes, soft-call (101), and prepayment fees.
**Explainer covers.**
- The toolkit: hard non-call periods, make-whole premiums, soft-call step-downs (e.g., 101 in year one), and prepayment penalties.
- Why early repayment is the lender's enemy (loans rarely run to maturity — hence yield-to-3-year).
- How call protection erodes in competitive markets.
**Connects to.** `★ G58` Yield, Z3.7, Z5.6 (yield-to-3-year), Z1.12.

### Z3.10 · Spread, Reference Rates & Floors `★ GLOBAL (G70 — home; deepens G69)` `[core]`
**Quick definition.** The pricing engine of a floating-rate loan — a credit spread set over a base rate (SOFR), usually with a floor that protects income when rates fall.
**Explainer covers.**
- The build: reference rate + credit spread; the role and level of base-rate floors.
- The LIBOR→SOFR transition and its mechanics.
- What drives the spread (credit quality, leverage, seniority, market supply/demand).
**Connects to.** `★ G69` Floating rate, `★ G58` Yield, Z1.14, Z5.13 (rate risk), Z3.7.

### Z3.11 · Financial Covenants `[core]` *(deepens `★ G34`)*
**Quick definition.** The contractual financial tests — leverage, coverage, FCCR, capex limits — that act as the lender's early-warning and control system, distinguishing covenanted private loans from cov-lite syndicated debt.
**Explainer covers.**
- Maintenance covenants (tested every period) vs. incurrence covenants (tested only on actions).
- Setting covenant levels and headroom/cushion against the base case.
- The cov-lite debate: private credit's *tighter-covenant* advantage vs. the erosion of that edge in large deals.
- How a covenant breach hands the lender a seat at the table early.
**Connects to.** `★ G34` Covenant (*shared node — financial-covenant detail and the cov-lite debate are the credit nuance*), `★ G74` Coverage ratios, `★ G29` Leverage, Z4.2 (compliance), Z3.15.

### Z3.12 · Security, Collateral & Lien Priority `★ GLOBAL (G78 — home)` `[core]`
**Quick definition.** The package of assets pledged to a lender and the rank of its claim — first lien, second lien, or unsecured — which determines who gets paid first if the borrower fails.
**Explainer covers.**
- The security package: all-asset pledges, guarantees from group companies, and perfection.
- Lien ranking (first vs. second vs. unsecured) and structural subordination.
- Why security and seniority are the foundation of recovery.
**Connects to.** `★ G33` Debt stack, `★ G79` Intercreditor, Z1.13, Z4.8 (recovery), Z2.4.

### Z3.13 · The Borrowing Base (ABL structuring) `★ GLOBAL (G76 — home)` `[core]`
**Quick definition.** The dynamically-sized pool of eligible collateral against which an asset-based revolver may draw, set by advance rates on each asset class.
**Explainer covers.**
- Eligible collateral and advance rates (e.g., 85% of eligible receivables, 50% of inventory).
- The borrowing-base certificate and how availability flexes with the assets.
- Reserves, ineligibles, and field exams.
**Connects to.** `★ G75` LTV, Z2.10 (ABL), `★ G78` Security, Z4.1 (monitoring).

### Z3.14 · Loan-to-Value & Asset Coverage in Structuring `★ GLOBAL (G75 — home)` `[core]`
**Quick definition.** Sizing a loan as a percentage of an underlying asset's value — the master risk lever for asset-based and real-estate credit, where the asset is the source of repayment.
**Explainer covers.**
- LTV mechanics and the equity cushion it implies.
- How LTV (asset value) differs from leverage (cash flow) as a sizing tool.
- LTV in real estate, infrastructure, and asset-based deals.
**Connects to.** `★ G76` Borrowing base, Z2.12 (RE debt), Z2.10 (ABL), `★ G29` Leverage (the cash-flow alternative).

### Z3.15 · The Credit / Facility Agreement `★ GLOBAL (G80 — home)` `[core]`
**Quick definition.** The master loan contract — private credit's analogue of the SPA — setting drawdown terms, covenants, representations, and the events of default.
**Explainer covers.**
- Structure: conditions precedent, representations, affirmative/negative/financial covenants, baskets, and events of default.
- How diligence findings and structuring decisions become contractual terms.
- Negotiation flashpoints: EBITDA definitions, baskets, MFN, and portability.
**Connects to.** `★ G34` Covenant, Z3.11, Z3.16, Z4.4 (events of default), PE Z3.18 (*the buyout debt-doc node it parallels*).

### Z3.16 · The Intercreditor Agreement `★ GLOBAL (G79 — home)` `[core]`
**Quick definition.** The contract that ranks different lenders against one another — payment and lien subordination, standstills, and the Agreement Among Lenders that internally splits a unitranche.
**Explainer covers.**
- Ranking first vs. second lien; payment vs. lien subordination; standstill periods.
- The Agreement Among Lenders (AAL) and first-out/last-out mechanics inside a unitranche.
- Why intercreditor terms decide outcomes in a restructuring.
**Connects to.** `★ G68` Unitranche, `★ G33` Debt stack, `★ G78` Security, Z2.4 (second lien), Z4.7 (LME exploits these).

### Z3.17 · Internal Credit Rating & Risk Assessment `★ GLOBAL (G77 — home)` `[core]`
**Quick definition.** A lender's own scorecard grading each loan's risk — the engine behind pricing, reserves, watch-lists, and (mapped to agency scales) BDC and insurance reporting.
**Explainer covers.**
- Internal scorecards and rating scales; the inputs (leverage, coverage, sector, sponsor).
- Estimating probability of default and loss-given-default per credit.
- Private ratings from agencies for BDC/insurance capital; mapping internal to external scales.
**Connects to.** `★ G62` Default/PD, `★ G61` Recovery/LGD, Z4.3 (rating migration), Z4.11 (valuation), Z5.13 (risk).

### Z3.18 · Sponsor Dynamics & Documentation Leverage `[core]`
**Quick definition.** How a borrower's PE sponsor — and competition among lenders — shapes loan terms, pushing toward looser documentation in hot markets.
**Explainer covers.**
- Sponsor-driven doc trends: generous EBITDA definitions, large baskets, portability, MFN sunsets.
- The negotiation balance of power and how it shifts with the cycle.
- The erosion of lender protections in competitive, capital-flooded markets.
**Connects to.** `★ G66` Sponsored lending, `★ G34` Covenant, Z3.5 (EBITDA add-backs), Z3.15, PE Z1.3 (the sponsor is a PE GP).

---

# PART 5 · Zone 4 — Portfolio Management, Monitoring, Workouts & Recovery

**What this zone is:** the holding period from the lender's side — surveilling loans, catching deterioration early, and managing defaults through to recovery. Where PE's Zone 4 is about *creating* value in a company, this zone is about *protecting* the lender's principal. It is also where this module is *deepest* relative to PE, since restructuring/recovery was a flagged PE gap. *(Source: Nesbitt on monitoring/losses; Moyer on distress, workout, and recovery; Ippolito Ch. 13.)*

**Learning sequence (roughly chronological across the hold):**
`Monitoring & surveillance → Covenant compliance & amendments → Risk-rating migration & watch-list → Default & events of default → Workouts (out-of-court) → In-court restructuring (Ch. 11) → The modern LME toolkit → Recovery & LGD → Default rates & PD → Loss rates → Valuation/fair value → Non-accrual & PIK in stress.`

---

### Z4.1 · Portfolio Monitoring & Credit Surveillance `[core]`
**Quick definition.** The ongoing work of tracking a loan after funding — financial reporting, covenant testing, KPI triggers, and the relationship with the borrower and its sponsor.
**Explainer covers.**
- The reporting cadence (monthly/quarterly financials, compliance certificates).
- Tracking covenants, KPIs, and early-warning triggers.
- The information edge of a private, relationship lender vs. a public bondholder.
**Connects to.** `★ G34` Covenant, `★ G77` Internal rating, Z4.2, Z4.3, Z3.13 (borrowing-base monitoring).

### Z4.2 · Covenant Compliance, Headroom & Amendments `[core]` *(deepens `★ G34`)*
**Quick definition.** Testing a borrower against its covenants, tracking headroom, and managing the requests for waivers and amendments that breaches trigger.
**Explainer covers.**
- Covenant testing and the difference between a technical (covenant) and a payment breach.
- Amendment and waiver requests; amend-and-extend; the fees lenders charge for consent.
- How shrinking headroom is an early-warning signal, not just a paperwork event.
**Connects to.** `★ G34` Covenant, `★ G80` Credit agreement, Z4.1, Z4.4 (when amendments fail), `★ G73` PIK (amendments often add it).

### Z4.3 · Risk-Rating Migration & the Watch-List `★ GLOBAL (G82 — home)` `[core]`
**Quick definition.** The downgrade machinery for deteriorating credits — moving a loan to a watch-list, escalating monitoring, and ultimately stopping income recognition.
**Explainer covers.**
- Internal rating downgrades and the watch-list process.
- Early-warning indicators (covenant erosion, liquidity stress, missed plan).
- The non-accrual decision and its income/NAV impact (links to Z4.12).
**Connects to.** `★ G77` Internal rating, `★ G62` Default/PD, Z4.4, Z4.12 (non-accrual), Z4.11 (valuation).

### Z4.4 · Default & Events of Default `[core]`
**Quick definition.** The triggers that put a loan formally in default — missed payments, covenant breaches, cross-defaults — and the decision tree that follows.
**Explainer covers.**
- Payment default vs. covenant default vs. cross-default; acceleration rights.
- The lender's options at default: waive, amend, forbear, restructure, or enforce.
- How the decision depends on recovery prospects and the borrower's viability.
**Connects to.** `★ G80` Credit agreement, `★ G34` Covenant, Z4.5 (workout), Z4.6 (in-court), `★ G61` Recovery.

### Z4.5 · Workouts & Out-of-Court Restructuring `★ GLOBAL (G81 — home)` `[process]`
**Quick definition.** The negotiated repair of a troubled loan *outside* bankruptcy — forbearance, amend-and-extend, new money, or a debt-for-equity swap.
**Explainer covers.**
- The workout process and the goals (preserve value, avoid costly bankruptcy).
- Tools: forbearance, maturity extensions, covenant resets, rescue/new-money financing, debt-for-equity.
- The "amend-extend-and-pretend" critique and when forbearance just defers a loss.
- Why workout capability is a core competitive edge for a lender (Z1.17).
**Connects to.** `★ G61` Recovery, `★ G82` Watch-list, Z4.6 (the in-court alternative), Z2.6 (distressed), PE Z2.26 (distressed PE).

### Z4.6 · In-Court Restructuring & Bankruptcy (Chapter 11) `[process]`
**Quick definition.** The formal court-supervised restructuring of a defaulted company — DIP financing, asset sales, and a plan of reorganization that re-cuts the capital structure.
**Explainer covers.**
- The Chapter 11 frame (U.S.): the automatic stay, DIP financing, the 363 sale, the plan of reorganization.
- Cramdown, the absolute priority rule, and creditor-class voting.
- How the fulcrum security (Z2.8) converts to equity through the plan.
- *(The Moyer spine; note insolvency regimes differ by country.)*
**Connects to.** Z2.8 (fulcrum), `★ G61` Recovery, Z4.5, `★ G25` Enterprise Value (the valuation fight), Z2.7 (loan-to-own).

### Z4.7 · The Modern Restructuring Toolkit & Liability Management `[core]`
**Quick definition.** The aggressive, post-2020 playbook of liability-management exercises (LMEs) — uptier/priming exchanges and drop-down financings — that pit creditors against each other.
**Explainer covers.**
- Uptier (priming) transactions and non-pro-rata drop-down financings.
- "Creditor-on-creditor violence" and how loose documentation (Z3.18) enables it.
- Landmark precedents (e.g., J.Crew, Serta, TriMark, Envision) and the doc-protection arms race.
- *(Major recency gap: Moyer (2005) predates the entire LME era — see Part 9.)*
**Connects to.** `★ G79` Intercreditor (what LMEs exploit), `★ G80` Credit agreement, Z3.18 (doc leverage), Z4.5, Z4.8.

### Z4.8 · Recovery Analysis & Loss Given Default `★ GLOBAL (G61 — home)` `[core]`
**Quick definition.** Estimating how many cents on the dollar a lender recovers in a default — driven by seniority, security, and enterprise value.
**Explainer covers.**
- The enterprise-valuation approach to recovery; walking value down the capital stack to the fulcrum.
- Recovery by seniority and security (first lien vs. second lien vs. unsecured).
- Historical recovery rates by instrument and why senior secured fares best.
- LGD = 1 − recovery, and how it feeds loss-rate math.
**Connects to.** `★ G62` Default/PD, `★ G60` Loss rate, `★ G33` Debt stack, Z2.8 (fulcrum), `★ G25` Enterprise Value.

### Z4.9 · Default Rates & Probability of Default `★ GLOBAL (G62 — home)` `[core]`
**Quick definition.** The frequency with which borrowers breach or fail to pay over a period — and crucially, why a high default rate need not mean high losses.
**Explainer covers.**
- Measuring default rates; sponsored vs. non-sponsored and by vintage/sector.
- Probability of default in internal ratings and pricing.
- *The default-vs-loss distinction*: a default with strong recovery (G61) costs little.
**Connects to.** `★ G61` Recovery, `★ G60` Loss rate, `★ G77` Internal rating, Z4.4, Z5.7 (the historical record).

### Z4.10 · Credit Loss Rates & Loss Experience `★ GLOBAL (G60 — home)` `[core]`
**Quick definition.** The annualized losses on a loan portfolio — default rate × loss-given-default — the figure that turns gross yield into the net return LPs actually earn.
**Explainer covers.**
- The arithmetic: loss rate = PD × LGD; gross yield − loss rate − fees = net return.
- The historically low loss experience of senior direct lending across cycles.
- Realized vs. unrealized losses and why marks lag reality.
**Connects to.** `★ G61` Recovery, `★ G62` Default, `★ G58` Yield, Z5.5 (net performance), Z5.7 (CDLI loss data).

### Z4.11 · Valuation & Fair Value of Private Credit Assets `[core]`
**Quick definition.** The quarterly marking of illiquid private loans to fair value — a board-level obligation for BDCs and the source of the "are the marks real?" debate.
**Explainer covers.**
- Fair-value measurement (ASC 820) and the valuation-committee process.
- Why private-credit marks are smoother (and slower) than public prices — and the credibility questions that raises.
- The link from internal ratings and non-accruals to carrying value.
**Connects to.** `★ G64` BDC (its fair-value duty), `★ G77` Internal rating, Z4.3, Z4.12, Z5.5.

### Z4.12 · Non-Accrual Loans & PIK in Stress `[core]` *(deepens `★ G73`)*
**Quick definition.** Two stress signals on a lender's books — moving a loan to non-accrual (stopping income recognition) and a healthy loan flipping to PIK (paying interest in kind rather than cash).
**Explainer covers.**
- Non-accrual: when repayment is doubtful, income stops being recognized — hitting reported yield and NAV.
- PIK as upside (mezzanine) vs. PIK as a *red flag* (a struggling borrower conserving cash).
- The portfolio-level warning when PIK income rises as a share of total income.
**Connects to.** `★ G73` PIK (*shared node — the stress-signal nuance lives here*), `★ G82` Watch-list, Z4.3, Z4.11, Z4.10.

---

# PART 6 · Zone 5 — Fund Management & the LP Relationship

**What this zone is:** the meta-layer — running the credit fund itself, its economics, how it's measured, and the LP's side of the table. The mirror of PE's Zone 5, but reshaped around *income* (yield, loss rates, the CDLI) rather than *carry* (IRR, the waterfall). *(Source: Nesbitt — the fund business, BDC economics, and the Cliffwater Direct Lending Index; Ippolito.)*

**Learning sequence:**
`Fund formation → Fund economics & fees → Fund-level leverage → Fundraising & the LP base → Performance measurement → Yield metrics → The CDLI → Benchmarking → Manager selection → LP allocation → Portfolio construction → BDC economics & the public market → Risk management → Evolution & future.`

---

### Z5.1 · Private Credit Fund Formation & Vehicles `[core]` *(deepens `★ G20`)*
**Quick definition.** How a credit fund is assembled — the drawdown or evergreen vehicle, BDCs, SMAs, and rated structures, all governed by an LPA tuned for an income product.
**Explainer covers.**
- Drawdown LP funds vs. evergreen/perpetual funds vs. BDCs vs. SMAs.
- Rated-note feeders and insurance-dedicated vehicles; CLOs as fund financing.
- How the LPA differs from a PE LPA (distribution mechanics, leverage provisions, redemption in evergreens).
**Connects to.** `★ G20` LPA (*shared — credit-fund nuance added*), Z1.8, Z5.3 (leverage), `★ G19` Blind pool (shared), PE Z5.1.

### Z5.2 · Private Credit Fund Economics & Fees `[core]` *(deepens `★ G8`/`★ G9`/`★ G10`)*
**Quick definition.** The fee model of a credit fund — lighter than PE's "2 and 20," with management fees often on invested or gross assets and an incentive fee on *income* above a hurdle.
**Explainer covers.**
- The lower load: ~1% management fee, incentive ~10–15% — often on income (not just gains) above a hurdle (≈6–7%).
- The BDC twist: management fee on *gross assets* (including leverage) — and the misalignment critique that it rewards levering up.
- Why a yield product carries different economics than a capital-gains product.
**Connects to.** `★ G8` Management fee / `★ G9` "2 and 20" / `★ G10` Carried interest (*shared nodes — credit-fee nuance lives here*), `★ G12` Hurdle, Z5.3, Z5.12.

### Z5.3 · Fund-Level Leverage & Financing Lines `★ GLOBAL (G67 — deep home)` `[core]`
**Quick definition.** The borrowing a fund does *on top of* its loan book — subscription lines, asset facilities, and BDC debt — that converts a single-digit asset yield into a double-digit equity return.
**Explainer covers.**
- The leverage layers: subscription/capital-call lines, asset-level facilities, CLO financing, BDC debt.
- The return mechanic: ~6–9% asset yield + modest-cost leverage → ~10–12% equity return.
- The risk it adds (and the asset-coverage limits that cap it).
- *This is the credit-side counterpart to PE's use of deal leverage — same idea, fund level.*
**Connects to.** `★ G29` Leverage, Z1.10 (BDC asset coverage), Z2.14 (NAV/fund finance), Z5.13 (leverage risk), `★ G16` Committed capital (sub lines).

### Z5.4 · Fundraising & the LP Base in Private Credit `[process]` *(deepens PE Z5.4)*
**Quick definition.** How credit managers raise capital — and why the *insurance/annuity* investor has become the defining LP of the modern asset class.
**Explainer covers.**
- The investor mix: pensions, endowments, sovereigns, *insurers*, and (increasingly) private wealth.
- Perpetual-capital fundraising and the always-open evergreen model.
- The insurance tie-up (the asset-manager-owns-an-insurer model) as a permanent capital engine.
**Connects to.** Z1.4 (the ecosystem), `★ G18` Vintage year, PE Z5.4 (the fundraising template), Z5.12 (the wealth channel), Z5.10.

### Z5.5 · Performance Measurement in Private Credit `[core]` *(deepens `★ G1`/`★ G2`)*
**Quick definition.** How credit-fund performance is measured — yield, IRR, and MOIC all appear, but *loss-adjusted net return* is the number that matters most for an income product.
**Explainer covers.**
- Cash yield and total yield; gross vs. net IRR; MOIC/multiple.
- Why net-of-losses return (gross yield − loss rate − fees) is the truest measure.
- Income vs. realized/unrealized appreciation in the total-return split.
- The role of marks (Z4.11) in interim performance.
**Connects to.** `★ G1` IRR / `★ G2` MOIC (*shared nodes — credit measures them but leads with yield/loss*), `★ G58` Yield, `★ G60` Loss rate, Z5.6, Z5.7.

### Z5.6 · Yield & Income Metrics `★ GLOBAL (G58 — home)` `[core]`
**Quick definition.** The family of income-return measures that headline a credit investment — cash yield, yield-to-maturity, and yield-to-3-year (assuming early take-out).
**Explainer covers.**
- Cash yield (current income) vs. yield-to-maturity (income to full term) vs. yield-to-3-year (the realistic average-life assumption).
- How OID and fees lift yield above the coupon; how call protection defends it.
- Why yield is to credit what IRR is to PE — the headline, with the same need for a "net of losses" caveat.
**Connects to.** `★ G69` Floating rate, `★ G70` Spread, `★ G71` OID, `★ G72` Call protection, `★ G60` Loss rate (the offset), `★ G1` IRR (the cousin metric).

### Z5.7 · The Cliffwater Direct Lending Index (CDLI) `★ GLOBAL (G59 — home)` `[core]`
**Quick definition.** The benchmark — built by Cliffwater (Stephen Nesbitt's firm) — tracking the total return of U.S. middle-market directly-originated loans held by BDCs, serving as the asset class's published track record.
**Explainer covers.**
- What it measures: a large universe of U.S. MM direct loans sourced from BDC holdings.
- Total-return decomposition: income vs. realized vs. unrealized gains/losses.
- How it's used to evidence the asset class's yield and (low) loss experience over time.
- Its limits: BDC-sourced (a survivorship/selection question), U.S.-only, direct-lending-only.
**Connects to.** `★ G58` Yield, `★ G60` Loss rate, Z5.8 (comparisons), Z5.5, Z1.3 (the growth story it documents).

### Z5.8 · Benchmarking & Index Comparisons `[core]`
**Quick definition.** Placing private-credit returns against public alternatives — leveraged loans, high-yield bonds, and the BSL market — including public-market-equivalent-style comparisons.
**Explainer covers.**
- The CDLI vs. leveraged-loan indices (Morningstar/LSTA) vs. high-yield.
- PME-style comparison: what the same cash flows would have earned in public credit.
- Reading the illiquidity/complexity premium out of the spread.
**Connects to.** `★ G59` CDLI, `★ G5` PME (*shared PE node — applied to credit here*), `★ G1` IRR, Z1.7 (the BSL comparator), Z5.5.

### Z5.9 · Manager Selection & GP Due Diligence (Credit) `[core]` *(deepens PE Z5.8)*
**Quick definition.** How LPs evaluate credit managers — judging them on loss experience through a cycle and workout capability, not just headline yield.
**Explainer covers.**
- The diligence focus: track record *through a downturn*, realized loss rates, origination edge, and restructuring capability.
- Why a high yield with hidden losses is worse than a modest yield with none.
- Platform scale, sourcing reach, and the persistence-of-returns debate.
**Connects to.** `★ G60` Loss rate, `★ G61` Recovery, Z1.17 (workout capability), PE Z5.8 (the GP-DD template), Z5.7.

### Z5.10 · LP Allocation to Private Credit `[core]` *(deepens PE Z5.6)*
**Quick definition.** How institutions decide how much to allocate to private credit — and whether it belongs in the fixed-income bucket, the alternatives sleeve, or its own category.
**Explainer covers.**
- The rationale: yield premium over public credit, floating-rate protection, diversification.
- Fixed-income substitution vs. an alternatives allocation; the illiquidity budget.
- The natural fit for insurance and long-horizon capital.
**Connects to.** `★ G7` LP (shared), PE Z5.6 (the allocation template), `★ G58` Yield, Z5.4, Z5.13.

### Z5.11 · Portfolio Construction & Diversification (Lender Side) `[core]`
**Quick definition.** How a credit fund builds a *granular* portfolio — many small loans diversified across borrowers, sectors, sponsors, and vintages — the opposite of PE's few concentrated bets.
**Explainer covers.**
- Diversification by borrower, sector, sponsor, geography, and vintage; concentration limits.
- Granularity as the core risk-management tool (no single loss sinks the fund).
- The contrast with PE's high-conviction, concentrated portfolio.
**Connects to.** `★ G62` Default (diversifying it away), PE Z5.7 (the LP portfolio-construction parallel), Z5.13, Z2.1 (strategy mix).

### Z5.12 · BDC Structure, Economics & the Public Market `[core]` *(deepens `★ G64`)*
**Quick definition.** How a BDC works as an *investment* — its price-to-NAV behavior, fee model, dividend coverage, and the non-traded/perpetual variant powering the private-wealth channel.
**Explainer covers.**
- Traded BDC valuation: price-to-NAV premiums/discounts and what drives them.
- The BDC fee model (gross-asset fees + income/gains incentive) and dividend coverage.
- Non-traded/perpetual BDCs and the retail/wealth distribution wave.
**Connects to.** `★ G64` BDC (*shared node — the investor's-eye view*), `★ G67` Fund leverage, Z5.2 (fees), Z5.4 (the wealth channel), Z4.11 (NAV).

### Z5.13 · Private Credit Risk Management `[core]` *(deepens PE Z5.21)*
**Quick definition.** Identifying and managing the distinct risks of private credit — credit/default, leverage (both borrower and fund), liquidity/redemption, rate, and concentration.
**Explainer covers.**
- Credit/default risk (mitigated by diligence, seniority, covenants, diversification).
- Leverage risk on *two* levels — the borrower's and the fund's (G67).
- Liquidity/redemption risk in evergreen vehicles; rate risk (floating-rate mitigates); concentration risk.
- The cycle risk that matters most now: spread compression in a capital-flooded market.
**Connects to.** `★ G29` Leverage, `★ G60` Loss rate, `★ G69` Floating rate, PE Z5.21 (the risk-framework parallel), Z5.11, Z1.15.

### Z5.14 · The Evolution & Future of Private Credit `[core]`
**Quick definition.** Where private credit came from and the forces shaping where it's going — scale, the move up-market, insurance capital, retail democratization, asset-based finance, and the first real cycle test.
**Explainer covers.**
- The arc: post-GFC niche → mainstream pillar; the move up-market and convergence with the BSL market.
- The insurance-capital engine and the asset-based-finance (ABF) frontier.
- Democratization through evergreen/perpetual vehicles and the private-wealth channel.
- The open questions: can returns persist as the industry scales, is there systemic risk, and how does it hold up through a full default cycle? — *the capstone debate.*
- *(Recency-heavy: much of this post-dates the source books — see Part 9.)*
**Connects to.** Z1.2 (where it began), `★ G64` BDC, `★ G59` CDLI, Z2.9 (ABF), **capstone — links back to all zones**, PE Z5.22 (the equity-side "future of" node).

---

# PART 7 · Cross-zone connective tissue

The graph's power is in the edges that jump between zones — and, uniquely for this module, the edges that jump *into the PE module*. These are the highest-value links to build.

**Within private credit:**
1. **Yield (G58)** threads through every zone: how lenders make money (Z1.12) → pricing a deal (Z3.7) → loss-adjusted net return (Z5.5) → the CDLI (Z5.7). One canonical metric, dozens of contextual entry points — the credit analogue of how IRR threads through PE.
2. **The default → recovery → loss chain (G62 → G61 → G60)** is the spine of Zones 4 and 5: a default (Z4.9) is only a loss (Z4.10) net of recovery (Z4.8), and the *loss rate* is what turns gross yield into the net return LPs earn (Z5.5). Build the three as an explicit linked sequence.
3. **Leverage appears three times, meaning three different things** — the *borrower's* leverage as the lender's risk gauge (Z3.4), the *deal's* leverage in structuring (Z3.6), and the *fund's* leverage as the return engine (Z5.3). Cross-link all three to the shared `★ G29` node with the vantage-point distinction made explicit.
4. **The covenant cluster (`★ G34` + financial covenants Z3.11)** is set at structuring (Z3.11), tested in monitoring (Z4.2), and exploited in liability management (Z4.7) — the through-line of "the lender's control system, from drafting to default."
5. **Seniority & security (G78)** connects the capital-structure position (Z1.13) → the security package (Z3.12) → recovery (Z4.8): *where you sit in the stack is the single biggest driver of what you get back.*
6. **The unitranche / intercreditor pairing (G68 + G79)** links a product (Z2.3) to the agreement that makes it work (Z3.16) to the LME battles that test it (Z4.7).

**Across the aisle into PE (the most important edges in the whole app):**
7. **The same deal, two sides.** A leveraged buyout is a PE equity investment (PE Z2.21) *and* a private-credit loan (Z2.2) — built on the same EBITDA (`★ G24`), the same sources & uses (`★ G32`), and the same debt stack (`★ G33`). Link the buyout from both modules so a user can flip between the sponsor's and the lender's view of one transaction.
8. **The J-curve, inverted.** PE's deep, slow J-curve (`★ G4`, PE Z1.18) vs. private credit's flat, fast one (Z1.16) — the single clearest illustration of how an income product differs from a capital-gains product. Same node, opposite shape.
9. **Distressed, from both ends.** Distressed PE (PE Z2.26) seeks *control*; distressed credit (Z2.6) and loan-to-own (Z2.7) often *become* that control by owning the fulcrum (Z2.8). This module supplies the restructuring/recovery depth (Z4.5–Z4.8) that the PE map explicitly flagged as a gap.
10. **The sponsor *is* the GP.** Sponsored lending (Z1.11/Z3.18) means the borrower's owner is a PE GP (`★ G6`, PE Z1.3) — the lender is underwriting the sponsor as much as the company. Link the two modules at the sponsor relationship.
11. **Sweet equity meets the debt stack.** Management's sweet equity (`★ G45`, PE Z4.5) sits at the bottom of the very capital structure the lender sits atop (Z1.13) — link them to show the full stack from first-lien loan to management's last-money equity.

---

# PART 8 · Suggested master path (for the "guided sequence" mode)

The app lets users jump anywhere, but the **default suggested sequence** a credit professional would follow:

1. **Zone 1 — The Private Credit Ecosystem** (what it is, why it exists, who lends, through what) → also the credit half of any lending primer.
2. **Zone 2 — Types of Private Credit** (the strategy you'd specialize in), entering at the spectrum (Z2.1).
3. **Zone 3 — Originating & Structuring Deals** (the process), taught in order, sourcing → documentation.
4. **Zone 4 — Portfolio Management, Workouts & Recovery** (the hold), chronologically through default to recovery.
5. **Zone 5 — Fund Management & the LP Relationship** (the meta-layer), once the deal lifecycle makes sense.

**Cross-module on-ramp:** because a buyout is one deal seen from two sides, a natural advanced path is to study **PE Zone 2–3 (the sponsor's buyout)** and **Private Credit Zone 2–3 (the lender's loan)** *side by side*, then converge on the shared glossary spine (EBITDA, leverage, the debt stack, due diligence).

**Within-zone entry points for non-linear users:** Z1.1, Z2.1, Z3.1, Z4.1, Z5.1 are the natural "front doors." Every other node is reachable directly and links back to its prerequisites via the glossary layer, so no user is ever stranded.

---

# PART 9 · Source gaps — material we need but don't have

Flagged exactly as the PE map does. Every node carrying a `GAP:` concern should show a "source needed" flag in the CMS so content isn't written from memory where the books are thin or dated.

**High priority (blocks or weakens whole node clusters):**
1. **Modern liability management (LME) / creditor-on-creditor mechanics (Z4.7).** Moyer (2005) is the recovery spine but *predates the entire LME era* — uptier/priming exchanges, drop-down financings, and the doc-protection arms race are all post-2015 (and mostly post-2020). → Needs current sources: leading restructuring law-firm primers, recent case write-ups (J.Crew, Serta, TriMark, Envision, At Home), and updated distressed texts. No single canonical book yet exists — flag as a living gap.
2. **The LIBOR→SOFR transition & modern loan pricing (Z3.7–Z3.10, Z1.14).** The books predate the completed SOFR transition. → Needs a current rates/loan-market source (e.g., LSTA materials) so pricing nodes reflect SOFR conventions, credit-spread adjustments, and current floor practice.
3. **Asset-based finance & specialty finance depth (Z2.9, Z5.14).** The ABF "frontier" (lending against pools of consumer, equipment, royalty, and receivable assets) barely existed at the books' scale. → Needs a dedicated ABF/structured-finance source; currently the largest white space in Zone 2.
4. **The insurance-capital convergence (Z1.4, Z5.4, Z5.12).** The asset-manager-owns-an-insurer model (annuity liabilities funding investment-grade private credit) is *the* defining modern development and is under-covered. → Needs current industry/insurance-investment sources.

**Medium priority (deepens existing nodes):**
5. **Real estate debt (Z2.12).** Thin — each property-lending vertical needs its own source. → a dedicated CRE-debt text (e.g., real-estate-finance reference).
6. **Infrastructure debt (Z2.13).** Sketched only. → a dedicated infrastructure-/project-finance source.
7. **Venture debt (Z2.11).** A genuine sub-discipline treated briefly. → a dedicated venture-debt source (ties to the future VC module and PE Z2.2–Z2.15).
8. **Structured credit & CLOs (Z2.16).** Light. → a dedicated CLO/structured-credit text covering tranching, the equity residual, and CLO-as-financing.
9. **BDC & RIC operational/regulatory detail (Z1.9, Z1.10, Z5.12).** The 1940-Act/RIC/asset-coverage machinery needs a dedicated regulatory source for authoritative depth.
10. **NAV lending / fund finance (Z2.14, Z5.3).** A fast-moving market under-covered by all three books (and a *shared* gap with the PE map, item 10 there). → a dedicated fund-finance source.

**Recency gaps (Nesbitt ~2019, Ippolito ~2020, Moyer 2005 — flag for every node touched):**
11. **The 2022–2024 rate cycle and its stress test (Z1.14, Z4.x, Z5.13).** The first real test of floating-rate private credit under sharply higher base rates — rising interest burdens, PIK usage, and defaults — post-dates the sources.
12. **Private-credit "mainstreaming" and the wall-of-money / spread-compression debate (Z1.3, Z5.13, Z5.14).** The scale, competition, and return-sustainability questions of 2021–2025 are live and unaddressed.
13. **Retail democratization via evergreen/non-traded BDCs (Z5.12, Z5.14).** The private-wealth distribution channel and perpetual vehicles have moved fast since the books.
14. **Systemic-risk scrutiny (Z1.2, Z5.13).** Regulators (FSB, IMF, central banks) now examine private credit's financial-stability footprint — a debate that did not exist in the source texts.
15. **Convergence with the BSL market (Z1.7, Z2.3).** Jumbo unitranche deals now compete head-to-head with syndicated loans — a recent structural shift.

**Build note:** as with the PE map, every `GAP:`/recency-flagged node should attach to its future source at the flagged connection point — when an ABF text, a current LME primer, or a fund-finance source enters the Drive, its concepts become new nodes that clip onto these seams. The graph grows where it's marked to grow.

---

# PART 10 · Using this as the template — and what it contributes to the global graph

This module was built to the PE template, and it in turn extends the template and the shared glossary for every module after it.

**The five-zone spine, instantiated for credit and ready for the next disciplines:**

| Generalized zone | Private Equity | **Private Credit (this module)** | Investment Banking (LevFin) | Equity Research |
|---|---|---|---|---|
| Z1 Ecosystem | The PE fund, GP/LP, fees | **The lender ecosystem, BDCs, non-bank lending, fee model** | The financing franchise, the loan/bond markets | The sell-side/buy-side, the research product |
| Z2 Types | VC · Growth · Buyout · Distressed · Real assets | **Direct lending · Unitranche · Mezz · Distressed · Specialty · ABL** | Syndicated loans · High-yield · Bridge · DCM | By sector / by mandate |
| Z3 Doing Deals | Source → DD → value → structure → docs | **Originate → credit DD → structure → price → document** | Originate → structure → syndicate → close | Initiate → model → thesis → rating |
| Z4 Managing | The hold & value creation → exit | **Monitor → covenants → workout → recover** | Deal execution & syndication | Maintenance, earnings, estimate revisions |
| Z5 Meta | Fund management, LP relations, performance | **Fund economics, the CDLI, leverage, manager selection** | League tables, the client relationship | The franchise, ratings, distribution |

**What transferred directly from the PE template:**
- **The node schema** (quick def → layered explainer → connections → tag) — identical.
- **The glossary-first build order** — cross-zone canonical nodes first, everything links back.
- **The "this vs. that" disambiguation pattern** — applied here to default-vs-loss, unitranche-vs-second-lien, leverage-as-risk-vs-leverage-as-return, asset-coverage-vs-coverage-ratios.
- **The learning-sequence-but-jumpable convention** with designated front-door nodes and glossary back-links.
- **The `GAP:` flagging discipline** — every thin or dated edge marked as a future attachment point.

**What this module *reuses* from the shared glossary (not rebuilt):**
`★ G1` IRR · `★ G2` MOIC · `★ G4` J-curve · `★ G6/G7` GP/LP · `★ G8/G9/G10` fees & carry · `★ G11` waterfall · `★ G12` hurdle · `★ G15` capital call · `★ G16` committed capital · `★ G17` dry powder · `★ G18` vintage · `★ G20` LPA · `★ G24` EBITDA · `★ G25/G26` EV/equity value · `★ G27` multiples · `★ G28` due diligence · `★ G29` leverage · `★ G30` net debt · `★ G33` debt stack · `★ G34` covenant · `★ G35` SPV · `★ G37` preferred equity · `★ G40` cap table · `★ G45` sweet equity · `★ G52` exit. *Each is the same node; this module simply adds the lender's-side context where relevant.*

**What this module *contributes* to the global graph (the new shared assets, G58–G82):**
- **Reused by future modules wholesale:** `G69` floating rate, `G70` spread, `G74` coverage ratios, `G78` security/lien priority, `G79` intercreditor, `G80` credit agreement, `G81` workout, `G77` internal ratings — these become canonical for the **IB LevFin/DCM and Restructuring** parts and the **credit side of Equity Research**. `G75` LTV is the master node the future **Real Estate** module is built on. `G62/G61/G60` (default/recovery/loss) are shared by anything that touches credit risk.
- **Largely credit-owned but cross-referenced:** `G58` yield, `G64` BDC, `G65` middle market, `G66` sponsored lending, `G67` fund leverage, `G68` unitranche, `G71` OID, `G72` call protection, `G73` PIK, `G76` borrowing base, `G82` watch-list.
- **Genuinely module-specific:** `G59` (CDLI) and `G63` (non-bank lending) — particular to this asset class, though they anchor the "future of private credit" capstone.

**The shared-glossary insight, restated for scale:** private credit is the *proof case* that the glossary is the app's connective spine, not a per-module appendix. The buyout in the PE module and the loan funding that buyout in this module *are the same deal* — they share EBITDA, leverage, the debt stack, due diligence, and the sponsor. Building this module against the existing glossary (rather than forking a parallel one) is what turns two courses into one knowledge graph — and the same discipline will fold in Investment Banking, Equity Research, and the sector modules as they come online.
