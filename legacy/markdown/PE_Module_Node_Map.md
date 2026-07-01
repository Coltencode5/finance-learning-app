# Private Equity Module — Complete Node Map

**The structural blueprint for the finance learning app.** This is the fully-mapped PE module: every learning node, organized into the five zones, with quick definitions, layered explainer scopes, and knowledge-graph connections. Once the interaction patterns are validated on this module, this same structure becomes the template for Investment Banking, Private Credit, Equity Research, Venture Capital, and the sector modules.

**Sources mapped:** *Mastering Private Equity* (Zeisberger, Prahl & White, INSEAD/Wiley 2017) — primary spine; *Private Equity in Action* (same authors) — the real-world/case layer; *Private Capital Investing* (Ippolito, Wiley) — supplementary, found in Drive, partially fills the private-credit and modeling gaps.

---

## How to read this map

Every entry is a **node**. Each node carries four things, matching the app's progressive-depth design:

| Field | What it is | Maps to app layer |
|---|---|---|
| **Quick definition** | One sentence, inline-able | Layer 1 — the hover/tap definition |
| **Explainer covers** | Bulleted scope, ordered basic → technical | Layers 2–4 — overview → mechanics → technical depth |
| **Connects to** | Every other node this links to | The graph edges |
| **Tag** | Node role (see legend) | Routing / page type |

**Legend**
- `★ GLOBAL` — a **canonical glossary node**. It appears across multiple zones and gets **one standalone explainer page that everything else links back to**. These are listed up front in the Global Glossary Layer; their deep explainer lives in a stated "home" zone.
- `[core]` — a foundational concept node within a zone.
- `[process]` — a step in a sequential workflow.
- `[branch]` — a sub-strategy or variant that opens its own sub-tree.

**Node IDs** use `Z{zone}.{n}` so edges are concrete and buildable (e.g., `Z3.14`). Glossary nodes also get a `G{n}` index number.

---

# PART 1 · The Global Glossary Layer

These are the cross-zone canonical nodes. **Build these first** — they are the backbone the rest of the module links into. Each is written once, lives at one URL, and is referenced (not duplicated) everywhere it appears. The "Home" column says which zone holds its deep explainer; "Appears in" shows the link density.

### A. Returns & Performance metrics

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| G1 | **IRR** (Internal Rate of Return) | The annualized, time-weighted rate that discounts a fund's or deal's cash flows to zero — PE's headline return number. | Z5 | Z1, Z2, Z3, Z4, Z5 |
| G2 | **MOIC** / Multiple of Money | The absolute multiple capital returns — total value ÷ capital invested (e.g., 2.5×); ignores time. | Z5 | Z1, Z2, Z3, Z4, Z5 |
| G3 | **DPI / RVPI / TVPI** | The three multiples splitting fund value into cash already returned (DPI), value still held (RVPI), and the sum (TVPI). | Z5 | Z1, Z5 |
| G4 | **J-curve** | The shape of an LP's cumulative net cash flow — negative early (fees + drawdowns), turning positive as exits return capital. | Z1 | Z1, Z4, Z5 |
| G5 | **PME** (Public Market Equivalent) | A benchmark comparing a fund's return to what the same cash flows would have earned in a public index. | Z5 | Z5 |

### B. Fund economics & structure

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| G6 | **GP** (General Partner) | The fund's manager — makes all investment decisions, owes a fiduciary duty to LPs, and bears unlimited liability. | Z1 | all zones |
| G7 | **LP** (Limited Partner) | A passive investor in the fund whose liability is capped at its committed capital. | Z1 | all zones |
| G8 | **Management fee** | The annual fee (~1.3–2.5% of committed, then invested, capital) paid to the manager to run the fund. | Z1 | Z1, Z5 |
| G9 | **"2 and 20"** | The standard PE comp model: ~2% management fee + 20% of profits (carry) to the GP. | Z1 | Z1, Z5 |
| G10 | **Carried interest** ("carry") | The GP's ~20% share of net fund profits — the main performance incentive. | Z1 | Z1, Z4, Z5 |
| G11 | **Distribution waterfall** | The contractual order proceeds flow back: return capital → preferred return → GP catch-up → split profits. | Z5 | Z1, Z2, Z4, Z5 |
| G12 | **Hurdle rate / Preferred return** | The minimum annual return (typically 8%) LPs must get before the GP earns carry. | Z1 | Z1, Z5 |
| G13 | **Catch-up** | The waterfall step letting the GP collect profits until it holds its full ~20% once the hurdle is met. | Z1 | Z1, Z5 |
| G14 | **Clawback** | An LPA provision forcing the GP to return any carry it was overpaid across the fund's life. | Z1 | Z1, Z5 |
| G15 | **Capital call / Drawdown** | The GP's demand for a portion of committed capital as deals and fees arise. | Z1 | Z1, Z5 |
| G16 | **Committed / Contributed / Invested capital** | Capital pledged vs. capital actually called (paid-in) vs. capital deployed into deals. | Z1 | Z1, Z5 |
| G17 | **Dry powder** | Committed-but-not-yet-invested capital available to deploy (fund-level or industry-wide). | Z1 | Z1, Z3, Z5 |
| G18 | **Vintage year** | The year a fund first closes and starts investing — the basis for peer benchmarking. | Z1 | Z1, Z5 |
| G19 | **Blind pool** | A fund whose investors commit before knowing which companies it will buy, trusting the mandate. | Z1 | Z1, Z5 |
| G20 | **LPA** (Limited Partnership Agreement) | The fund's governing contract — mandate, economics, governance, and LP–GP rights. | Z5 | Z1, Z3, Z5 |
| G21 | **Commitment / Investment period** | The ~4–5-year window during which the GP can call capital for new investments. | Z1 | Z1, Z5 |
| G22 | **Holding period** | The ~3–7 years a fund owns a company, working to create value before exit. | Z1 | Z1, Z4 |
| G23 | **GP commitment** ("skin in the game") | The GP's own capital in the fund (typically 1–5%) that aligns it with LPs. | Z1 | Z1, Z4 |

### C. Valuation primitives

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| G24 | **EBITDA** | Earnings before interest, taxes, depreciation & amortization — the cash-earnings proxy PE prices and lends against. | Z3 | Z2, Z3, Z4 |
| G25 | **Enterprise Value (EV)** | The value of the whole business — what you'd pay to own its operations free of its capital structure. | Z3 | Z2, Z3, Z4 |
| G26 | **Equity Value** | What's left for shareholders after subtracting net debt from enterprise value. | Z3 | Z2, Z3, Z4 |
| G27 | **Valuation multiples** | Shorthand pricing ratios (EV/EBITDA, EV/Sales, P/E) that value a company relative to peers or precedents. | Z3 | Z2, Z3, Z4 |
| G28 | **Due diligence** | The systematic investigation of a target's business, finances, legal standing, and risks before committing. | Z3 | Z2, Z3, Z4 |

### D. Capital structure & deal mechanics

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| G29 | **Leverage** | Borrowed money used alongside equity to fund a deal, amplifying both returns and risk. | Z2 | Z2, Z3, Z4, Z5 |
| G30 | **Net debt** | Total debt minus cash — the figure that bridges enterprise value to equity value. | Z3 | Z2, Z3 |
| G31 | **Working capital** | The cash tied up in day-to-day operations; its "normal" level is pegged at closing. | Z3 | Z3 |
| G32 | **Sources & uses** | The deal-funding table showing where money comes from (debt + equity) and what it pays for. | Z2 | Z2, Z3, Z4 |
| G33 | **Debt stack / Funding instruments** | The layered mix of debt instruments ranked by seniority and risk (senior → mezzanine → PIK). | Z3 | Z2, Z3 |
| G34 | **Covenant** | A condition in a loan agreement that protects lenders and constrains the borrower. | Z3 | Z2, Z3 |
| G35 | **SPV** (Special Purpose Vehicle) | A holding company created to ring-fence a deal, house debt, and hold equity. | Z3 | Z1, Z3 |
| G36 | **SPA** (Sale & Purchase Agreement) | The master contract governing a company's sale — price, conditions, warranties, remedies. | Z3 | Z3, Z4 |

### E. Equity & shareholder terms

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| G37 | **Preferred equity** | Shares that rank ahead of common stock for distributions and carry special rights. | Z2 | Z2, Z3 |
| G38 | **Liquidation preference** | Preferred holders' right to get their money back (sometimes a multiple) before common in an exit. | Z2 | Z2, Z3, Z4 |
| G39 | **Anti-dilution** | Protections adjusting earlier investors' price if a later round is raised at a lower valuation. | Z2 | Z2, Z3 |
| G40 | **Cap table** | The ledger of who owns what — shares, options, and ownership percentages. | Z2 | Z2, Z3 |
| G41 | **Pre-money / Post-money** | A company's value before vs. after new investment (post = pre + new money). | Z2 | Z2, Z3 |
| G42 | **Dilution** | The drop in existing owners' percentage stake when new shares are issued. | Z2 | Z2, Z3 |
| G43 | **Drag-along / Tag-along** | Rights letting a majority force, or a minority join, a sale of shares. | Z2 | Z2, Z3, Z4 |
| G44 | **Minority shareholder rights** | The protections a non-controlling investor negotiates to safeguard its stake and influence. | Z2 | Z2, Z3, Z4 |
| G45 | **Sweet equity / Management equity** | The outsized-upside equity package given to portfolio-company management. | Z4 | Z2, Z3, Z4 |
| G46 | **Term sheet** | The non-binding document setting the headline economic and control terms of an investment. | Z2 | Z2, Z3, Z5 |

### F. Value creation & exit

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| G47 | **Active ownership** | PE's hands-on, urgency-driven involvement in a company during the holding period. | Z4 | Z2, Z4 |
| G48 | **Alignment of interest** | Structuring incentives so management, GP, and LPs all win from the same outcome. | Z4 | Z1, Z2, Z4 |
| G49 | **Operational value creation** | Growing returns by improving the actual business — revenue, margins, operations — not just leverage. | Z4 | Z2, Z4 |
| G50 | **100-Day Plan / Value Creation Plan** | The urgent post-close action plan setting priorities, metrics, and quick wins from day one. | Z4 | Z4 |
| G51 | **Corporate governance** | The board-level control and oversight structures PE uses to steer a portfolio company. | Z4 | Z2, Z4 |
| G52 | **Exit** | The sale or listing through which a fund realizes its investment and returns capital. | Z4 | Z2, Z3, Z4, Z5 |
| G53 | **IPO** (as exit) | Listing the company publicly to sell the stake down over time. | Z4 | Z4 |
| G54 | **Trade sale** | Selling the company to a strategic (corporate) buyer. | Z4 | Z4 |
| G55 | **Secondary buyout (SBO)** | Selling a portfolio company to another PE fund. | Z4 | Z2, Z4 |
| G56 | **Co-investment** | LPs investing directly alongside a GP in a specific deal, usually fee-free. | Z5 | Z1, Z5 |
| G57 | **Secondaries** | The market for buying/selling existing fund stakes and portfolios. | Z5 | Z1, Z5 |

> **57 global nodes.** Note two pairs that learners constantly confuse — build explicit "this vs. that" cross-links:
> - **Secondary buyout (G55)** = selling a *company* to another PE fund · **Secondaries (G57)** = selling a *fund stake* on the secondary market.
> - **Preferred return / hurdle (G12)** = the LP's minimum return threshold · **Preferred equity (G37)** = a class of shares. Same word, unrelated concepts.

---

# PART 2 · Zone 1 — The PE Ecosystem

**What this zone is:** the foundational layer. What PE is, who the players are, how a fund is structured, how it lives and dies, and how everyone gets paid. Everything else in the module assumes this. *(Source: Mastering PE, Ch. 1.)*

**Learning sequence (logical path):**
`What is PE? → The PE fund → Players & structure → The lifecycle → How capital flows (calls, commitments, dry powder) → How money is made (fees, carry, waterfall) → The J-curve → Returns intro → The GP–LP relationship.`
Users can enter at any node, but the canonical "start here for beginners" entry point is **Z1.1**, and this zone doubles as the onboarding primer's finance half.

---

### Z1.1 · What Is Private Equity? `[core]`
**Quick definition.** Long-term capital invested in private (or soon-to-be-private) companies in exchange for an equity stake that isn't traded on a public market, with the goal of improving the business and selling it at a profit.
**Explainer covers (basic → technical).**
- The simple business model: buy a stake, improve the company, sell after a limited holding period.
- PE vs. public equity: illiquidity, long horizon, control/influence, information access.
- The PE umbrella: venture capital, growth equity, buyouts, and alternative strategies — one spectrum by company maturity.
- "Organized" PE (professional funds) vs. "informal" private capital (angels, family money).
- Scale of the asset class and why companies seek PE at inflection points (growth, succession, turnaround, take-private).
**Connects to.** Z1.2, Z2.1 (the strategy spectrum), G29 Leverage, G52 Exit, Z5.22 (industry evolution).

### Z1.2 · The PE Fund `[core]`
**Quick definition.** A stand-alone, finite-life pooled vehicle that raises committed capital to buy and later sell equity stakes, with investors locked in for roughly ten years.
**Explainer covers.**
- Closed-end structure: finite life, no early redemption, capital committed up front but drawn over time.
- The blind-pool principle and the fund mandate.
- Fund (the vehicle) vs. firm (the manager) vs. family of funds.
- Why the limited-partnership form dominates (vs. LLC/corporate vehicles).
**Connects to.** ★ G19 Blind pool, ★ G20 LPA, ★ G16 Committed capital, ★ G6 GP, ★ G7 LP, Z1.3, Z5.1 (fund formation).

### Z1.3 · Fund Structure & Key Players `[core]`
**Quick definition.** The legal architecture linking the PE firm, the GP, the investment manager, the LPs, and the portfolio companies into one fund.
**Explainer covers.**
- **PE firm** vs. **GP** vs. **investment manager** — why they're separate legal entities (liability insulation).
- **GP**: fiduciary duty, decision-making authority, unlimited liability; the investment committee (IC).
- **LPs**: who they are — pensions, endowments, insurers, banks, family offices, sovereign wealth funds, funds-of-funds — and why they stay passive (limited-liability rule).
- **Portfolio / investee / target company** and the 10–15-company portfolio.
- **GP commitment** ("skin in the game") and the two relationships a GP must manage (LPs ↔ companies).
**Connects to.** ★ G6 GP, ★ G7 LP, ★ G20 LPA, ★ G23 GP commitment, Z1.4, Z5.1, Z5.8 (manager selection), G48 Alignment.

### Z1.4 · The PE Fund Lifecycle (10+2) `[core]`
**Quick definition.** The staged timeline over which a fund raises, deploys, holds, and harvests capital — typically ten years plus two one-year extensions.
**Explainer covers.**
- The four overlapping periods: fundraising → investment → holding → divestment/harvest.
- First close vs. final close; the 12–18-month fundraising window.
- Investment period (4–5 yrs), follow-ons and add-ons after it closes, recycling of capital.
- Extensions ("+2") and why funds need them.
- Successor funds, "re-ups," and the lifecycle of a successful firm running overlapping vintages.
**Connects to.** ★ G21 Investment period, ★ G22 Holding period, ★ G18 Vintage year, ★ G15 Capital call, ★ G17 Dry powder, ★ G4 J-curve, Z5.4 (fundraising).

### Z1.5 · Capital Calls & Drawdowns `★ GLOBAL (G15)` `[process]`
**Quick definition.** The GP's demands for portions of LPs' committed capital as deals and fees arise, rather than taking all the cash up front.
**Explainer covers.**
- Mechanics and the ~10-business-day notice period.
- Committed → contributed (paid-in) → invested capital.
- LP default remedies: penalty interest, forced secondary sale, loss of future profit share.
- Recycling provisions and "quick-flip" reinvestment rules.
**Connects to.** ★ G16 Committed/contributed capital, ★ G17 Dry powder, ★ G4 J-curve, ★ G57 Secondaries, Z5.7 (commitment pacing).

### Z1.6 · Committed, Contributed & Invested Capital `★ GLOBAL (G16)` `[core]`
**Quick definition.** The distinction between capital *pledged* (committed), capital actually *called* (contributed/paid-in), and capital actually *deployed* into deals (invested).
**Explainer covers.**
- Definitions and how they diverge over a fund's life.
- Uninvested committed capital = dry powder.
- How fees draw on committed vs. invested capital at different stages.
- Why the gap matters for LP cash management.
**Connects to.** ★ G15 Capital call, ★ G17 Dry powder, ★ G8 Management fee, ★ G4 J-curve.

### Z1.7 · Dry Powder `★ GLOBAL (G17)` `[core]`
**Quick definition.** Committed but not-yet-invested capital available to a fund — or, in aggregate, to the whole industry — waiting to be deployed.
**Explainer covers.**
- Fund-level vs. industry-level dry powder.
- Drivers and the deployment-pressure dynamic (and its effect on entry prices).
- Reading dry powder by vintage year.
**Connects to.** ★ G16 Committed capital, ★ G15 Capital call, ★ G18 Vintage year, Z3.2 (deal sourcing).

### Z1.8 · Vintage Year `★ GLOBAL (G18)` `[core]`
**Quick definition.** The year a fund holds its first close and starts investing — used to benchmark it against all other funds raised the same year.
**Explainer covers.**
- Definition and why benchmarking must be vintage-controlled.
- Macro/credit-cycle exposure baked into a vintage.
- Quartile-by-vintage performance comparison.
**Connects to.** ★ G1 IRR, Z5.4 (fundraising), Z5.10 (performance), ★ G17 Dry powder.

### Z1.9 · Blind Pool `★ GLOBAL (G19)` `[core]`
**Quick definition.** A fund whose investors commit capital before knowing which specific companies it will buy, trusting the GP's stated mandate.
**Explainer covers.**
- Definition; mandate breadth vs. GP discretion.
- Why LPs accept blind-pool risk (track record, trust).
- Implications for fundraising and manager selection.
**Connects to.** ★ G20 LPA, ★ G6 GP, Z5.4, Z5.8.

### Z1.10 · Fund Economics: "2 and 20" `★ GLOBAL (G9)` `[core]`
**Quick definition.** The standard PE compensation model — roughly a 2% annual management fee plus 20% of profits (carried interest) to the GP, with 80% of profits to LPs.
**Explainer covers.**
- The two components and the 80/20 profit split.
- How the structure is meant to align GP and LP incentives.
- Evolution and fee pressure since the 2008 crisis (offsets, discounted co-invest).
**Connects to.** ★ G8 Management fee, ★ G10 Carried interest, ★ G11 Distribution waterfall, ★ G12 Hurdle rate.

### Z1.11 · Management Fees `★ GLOBAL (G8)` `[core]`
**Quick definition.** The annual fee (~1.3–2.5%) paid to the investment manager to cover the cost of running the fund.
**Explainer covers.**
- Basis: committed capital during the investment period → invested capital after, often with a step-down.
- Fee drag over a fund's life; first-time vs. mega-fund differences.
- Paid quarterly/semi-annually in advance; drawn from commitments early, offset by exits later.
**Connects to.** ★ G9 "2 and 20", Z1.12 (other fees), ★ G16 Committed/invested capital.

### Z1.12 · Other Fees & Fee Offsets `[core]`
**Quick definition.** Transaction, monitoring, director, and broken-deal fees a manager may charge — increasingly rebated to LPs through management-fee offsets.
**Explainer covers.**
- The fee categories and where they're charged (often at the portfolio-company level).
- Management-fee offsets (historically 50–100%, trending to 100%) and what they do to economics.
- ILPA pressure and the shift of fee-based value from GP to the partnership.
**Connects to.** ★ G8 Management fee, ★ G20 LPA, Z5.5 (fundraising docs), Z4.2 (governance).

### Z1.13 · Carried Interest `★ GLOBAL (G10)` `[core]`
**Quick definition.** The GP's ~20% share of a fund's net profits — the single biggest performance incentive for PE professionals.
**Explainer covers.**
- Definition and being "in the carry."
- Tied to the waterfall, gated by the hurdle, trued-up by catch-up, protected by clawback.
- The tax debate (carry as capital gains vs. income).
**Connects to.** ★ G11 Distribution waterfall, ★ G12 Hurdle rate, ★ G13 Catch-up, ★ G14 Clawback, ★ G9 "2 and 20".

### Z1.14 · Distribution Waterfall `★ GLOBAL (G11)` `[core]`
**Quick definition.** The contractual order in which exit proceeds flow back: return LP capital → pay the preferred return → GP catch-up → split remaining profits 80/20.
**Explainer covers.**
- The standard steps, common to every waterfall.
- **European / "all-capital-first" (whole-fund)** vs. **American / "deal-by-deal" (with loss carry-forward and make-whole)**.
- Where it's defined (the LPA) — deep mechanics and worked math live in **Z5.3**.
**Connects to.** ★ G10 Carried interest, ★ G12 Hurdle, ★ G13 Catch-up, ★ G14 Clawback, ★ G20 LPA, **Z5.3** (deep), Z5.1.

### Z1.15 · Hurdle Rate / Preferred Return `★ GLOBAL (G12)` `[core]`
**Quick definition.** The minimum annual return (typically 8%) LPs must receive before the GP earns any carry.
**Explainer covers.**
- Definition and the 8% norm, negotiated during fundraising.
- Hard vs. soft hurdle and the effect on carry timing.
- Interaction with the catch-up.
**Connects to.** ★ G10 Carried interest, ★ G13 Catch-up, ★ G11 Distribution waterfall.

### Z1.16 · Catch-up Mechanism `★ GLOBAL (G13)` `[core]`
**Quick definition.** The waterfall step that lets the GP collect profits until it holds its full ~20% share, once the hurdle has been cleared.
**Explainer covers.**
- Definition; 100% catch-up vs. an 80/20 catch-up rate.
- How it interacts with the hurdle to make the GP "whole" on its carry.
**Connects to.** ★ G12 Hurdle rate, ★ G10 Carried interest, ★ G11 Distribution waterfall.

### Z1.17 · Clawback `★ GLOBAL (G14)` `[core]`
**Quick definition.** An LPA provision forcing the GP to return any carried interest it was overpaid across the fund's life.
**Explainer covers.**
- When it's triggered (typically under deal-by-deal carry after later losses).
- Escrows/holdbacks and other LP protections.
**Connects to.** ★ G11 Distribution waterfall, ★ G10 Carried interest, ★ G20 LPA.

### Z1.18 · The J-curve `★ GLOBAL (G4)` `[core]`
**Quick definition.** The curve of an LP's cumulative net cash flow — dipping negative early as fees and investments go out, then turning positive as exits return capital.
**Explainer covers.**
- The shape and its drivers; why it rarely dips below ~80% of committed capital.
- Breakeven (crossing the x-axis) and the final point = net profit.
- Single-fund J-curve vs. an LP's blended portfolio J-curve.
- How secondaries shorten and flatten the curve.
**Connects to.** ★ G15 Capital call, ★ G8 Management fee, ★ G16 Committed capital, ★ G57 Secondaries, Z5.7, Z5.10.

### Z1.19 · PE Returns — IRR & MOIC (intro) `[core]`
**Quick definition.** PE measures success two ways at once: a time-weighted rate (IRR) and an absolute multiple of money (MOIC), always assessed net of fees.
**Explainer covers.**
- Gross vs. net returns and why net is what LPs live on.
- IRR in one line; MOIC in one line; why you need both (IRR ignores scale, MOIC ignores time).
- Pointer to the deep performance node.
**Connects to.** ★ G1 IRR, ★ G2 MOIC, **Z5.10** (deep performance), ★ G4 J-curve.

### Z1.20 · The GP–LP Relationship (foundations) `[core]`
**Quick definition.** The fiduciary, economic, and reporting bond between fund managers and their investors that underpins all of PE.
**Explainer covers.**
- Fiduciary duty and the alignment toolkit (carry, GP commitment, hurdle, clawback).
- Information, transparency, and reporting expectations.
- Trust, track record, and conflicts of interest.
**Connects to.** ★ G6 GP, ★ G7 LP, ★ G48 Alignment, **all of Zone 5**, Z4.2 (governance).
*Real-world layer: PE in Action Case #1 (Beroni Group: Managing GP–LP Relationships).*

---

# PART 3 · Zone 2 — Types of Private Equity

**What this zone is:** the strategy branches. The PE spectrum runs from minority bets on pre-revenue start-ups to majority control of mature, cash-generative companies, plus special situations. Each branch is its own sub-tree. *(Source: Mastering PE, Ch. 2–5.)*

**Learning sequence (by company maturity — the natural ordering):**
`The spectrum → Venture Capital → Growth Equity → Buyouts/LBO → Alternative strategies (Distressed, Real Assets).`
The spectrum node (**Z2.1**) is the hub; each branch can be entered directly.

---

### Z2.1 · The PE Strategy Spectrum `[core]`
**Quick definition.** A map of PE strategies by company maturity, control, and leverage — from minority early-stage VC to majority mature-company buyouts to special situations.
**Explainer covers.**
- The axes: company stage · risk/return profile · minority vs. control · use of leverage.
- How required skillsets differ across the spectrum (financial vs. operational vs. process).
- Capital deployed by strategy (buyouts historically dominate; VC/growth rising).
**Connects to.** All Zone 2 branch nodes, ★ G29 Leverage, Z3.6 (valuation differs by strategy), Z1.1.

## Branch 2A — Venture Capital

### Z2.2 · Venture Capital Defined `[branch]`
**Quick definition.** Minority investment in pre-profit, often pre-revenue start-ups, betting on outsized growth from innovation.
**Explainer covers.**
- Defining characteristics: minority but highly active; vertical/stage specialization.
- The power-law return model and high deal-level target IRRs (40–80%).
- Why VCs diversify across many companies and fund in stages.
**Connects to.** Z2.3, Z2.5, ★ G46 Term sheet, ★ G38 Liquidation preference, ★ G1 IRR, ★ G2 MOIC, Z2.15.

### Z2.3 · Start-up Development Stages `[core]`
**Quick definition.** The path a start-up travels — proof-of-concept → commercialization → scaling up — with different capital needs at each step.
**Explainer covers.**
- The three stages and the milestones that gate each.
- Burn rate and runway; why most start-ups never reach scale.
- Who funds each stage (seed → early → mid/late VC → growth).
**Connects to.** Z2.4, Z2.6, Z2.16 (growth equity picks up at scaling), burn rate.

### Z2.4 · The VC Investor Ecosystem `[core]`
**Quick definition.** The range of early-stage backers — angels, incubators, accelerators, seed/early/late VC funds, and corporate VC.
**Explainer covers.**
- Business angels; incubators vs. accelerators (the real differences).
- Seed vs. early vs. late-stage VC funds and their specialization.
- Corporate VC (CVC) motives (strategic access over pure return).
- Crowdfunding and the "lean start-up" alternative path.
**Connects to.** Z2.2, Z2.3, Z2.5 (syndication).

### Z2.5 · The VC Investment Process `[process]`
**Quick definition.** How VCs source, value, structure, and support deals — a process distinct from buyouts at every step.
**Explainer covers.**
- Reputation-driven deal sourcing (demo days, networks, inbound).
- Subjective valuation (revenue/KPI multiples, team, addressable market).
- Staged funding as buying options; momentum signaling.
- Hands-on mentorship and syndicated/"club" deals with a lead investor.
**Connects to.** ★ G41 Pre/post-money, ★ G42 Dilution, ★ G40 Cap table, ★ G46 Term sheet, G47 Active ownership (Z4), Z3.9 (early-stage valuation).

### Z2.6 · Funding in Rounds & Staged Financing `[core]`
**Quick definition.** VC capital deployed in discrete rounds tied to milestones, each a fresh decision to double down or walk away.
**Explainer covers.**
- Round mechanics and milestone gating; progressively larger preferred rounds.
- "Buying an option" and momentum as proof of value.
- Up rounds vs. down rounds and their knock-on effects.
**Connects to.** ★ G41 Pre/post-money, ★ G42 Dilution, ★ G39 Anti-dilution, ★ G40 Cap table.

### Z2.7 · VC Term Sheet — Economic Terms `★ GLOBAL (part of G46)` `[core]`
**Quick definition.** The part of a VC term sheet that sets price, amount, and the economic rights of the newly created preferred share class.
**Explainer covers.**
- Share price and pre-money valuation; amount, shares, price per share; series naming.
- **Liquidation preference** (incl. participating vs. non-participating, and multiples).
- **ESOP**: pool size (~20%), vesting, strike price, dilution impact.
- **Anti-dilution** (full-ratchet vs. weighted-average) and **conversion rights**.
**Connects to.** ★ G46 Term sheet, ★ G38 Liquidation preference, ★ G39 Anti-dilution, Z2.14 ESOP, ★ G37 Preferred equity, ★ G41 Pre/post-money.

### Z2.8 · VC Term Sheet — Control Terms `★ GLOBAL (part of G46)` `[core]`
**Quick definition.** The governance rights VCs secure despite holding a minority stake.
**Explainer covers.**
- Board representation and observer rights; founder board planning.
- Protective/veto provisions on key corporate actions.
- Drag-along/tag-along; transfer rights, pre-emption, ROFR; information rights.
**Connects to.** ★ G46 Term sheet, ★ G43 Drag/tag, ★ G44 Minority rights, G51 Governance (Z4).

### Z2.9 · Liquidation Preference `★ GLOBAL (G38)` `[core]`
**Quick definition.** Preferred shareholders' right to get their money back — sometimes a multiple of it — before common shareholders in an exit or liquidation.
**Explainer covers.**
- Definition; 1× vs. multiple; participating vs. non-participating.
- Stacking/seniority across successive rounds.
- The effect on founder and common-shareholder payouts at exit.
**Connects to.** ★ G37 Preferred equity, ★ G40 Cap table, G52 Exit, ★ G46 Term sheet, (analogy) ★ G11 Waterfall.

### Z2.10 · Anti-dilution Provisions `★ GLOBAL (G39)` `[core]`
**Quick definition.** Protections that adjust earlier investors' conversion price downward if a later round is raised at a lower valuation (a down round).
**Explainer covers.**
- Full-ratchet vs. broad/narrow weighted-average mechanics.
- Why founders resist and how to negotiate severity.
- Interaction with the cap table and ESOP.
**Connects to.** ★ G42 Dilution, ★ G40 Cap table, ★ G41 Pre/post-money, ★ G46 Term sheet, down round.

### Z2.11 · Capitalization Table (Cap Table) `★ GLOBAL (G40)` `[core]`
**Quick definition.** The ledger of who owns what — shares, options, and ownership percentages — across all stakeholders.
**Explainer covers.**
- Common vs. preferred vs. options/ESOP; fully-diluted ownership.
- How each round changes it; the option-pool shuffle.
- The exit waterfall as read off the cap table.
**Connects to.** ★ G41 Pre/post-money, ★ G42 Dilution, Z2.14 ESOP, ★ G38 Liquidation preference, Z2.15.

### Z2.12 · Pre-money / Post-money Valuation `★ GLOBAL (G41)` `[core]`
**Quick definition.** A company's value before (pre) and after (post) new investment; post-money = pre-money + new money.
**Explainer covers.**
- Definitions and how they set ownership percentages.
- Round dynamics and the option-pool-before-vs-after wrinkle.
**Connects to.** ★ G40 Cap table, ★ G42 Dilution, Z3.9 (valuing early-stage), Z2.5.

### Z2.13 · Dilution `★ GLOBAL (G42)` `[core]`
**Quick definition.** The reduction in existing owners' percentage stake when new shares are issued.
**Explainer covers.**
- Mechanics; per-round dilution as valuations rise.
- Anti-dilution protection; ESOP-driven dilution; cumulative founder dilution.
**Connects to.** ★ G41 Pre/post-money, ★ G39 Anti-dilution, ★ G40 Cap table, Z2.14.

### Z2.14 · ESOP & Employee Equity `[core]`
**Quick definition.** A reserved pool of shares/options used to attract and retain start-up talent.
**Explainer covers.**
- Pool sizing (~20%), vesting schedules, strike price.
- Dilution impact and option-pool timing in negotiations.
**Connects to.** ★ G42 Dilution, ★ G40 Cap table, ★ G46 Term sheet, Z4.5 (management comp — the buyout analogue).

### Z2.15 · VC Economics & the Power Law `[core]`
**Quick definition.** The return math of venture — a few "home runs" returning 10–100× must carry a portfolio in which most investments fail.
**Explainer covers.**
- The "two-thirds lose money" reality and home-run dependence.
- Fund-level vs. deal-level target returns; portfolio sizing as risk management.
- The Kauffman Foundation critique of venture's contribution to LP portfolios.
**Connects to.** ★ G1 IRR, ★ G2 MOIC, Z2.2, Z5.10 (fund returns).

## Branch 2B — Growth Equity

### Z2.16 · Growth Equity Defined `[branch]`
**Quick definition.** Minority investment in established, fast-growing, often profitable companies that need capital to scale — without taking control.
**Explainer covers.**
- Defining characteristics; the space between VC and buyout.
- Primary (into the company) vs. secondary (to founders) capital.
- Minority but influential; emerging-markets relevance.
**Connects to.** Z2.2, Z2.20, ★ G44 Minority rights, G49 Operational value creation (Z4).

### Z2.17 · Growth Equity Targets `[core]`
**Quick definition.** The profile of companies growth funds back — proven model, strong growth, capital-constrained, often founder-led.
**Explainer covers.**
- Target characteristics and founder/owner motivations.
- Primary capital for expansion vs. founder partial liquidity.
- Why emerging markets are a natural hunting ground.
**Connects to.** Z2.16, Z3.2 (sourcing), emerging markets.

### Z2.18 · The Growth Equity Investment Process `[process]`
**Quick definition.** How growth investors win, structure, and add value in minority deals where they can't dictate terms.
**Explainer covers.**
- Sourcing proprietary deals; valuation on revenue/EBITDA multiples.
- Structuring minority protections; partnering with founders.
- Operational support without control.
**Connects to.** ★ G44 Minority rights, ★ G27 Valuation multiples, ★ G46 Term sheet, G49 Operational value creation.

### Z2.19 · Minority Shareholder Rights `★ GLOBAL (G44)` `[core]`
**Quick definition.** The contractual protections a non-controlling investor negotiates to safeguard its stake and influence key decisions.
**Explainer covers.**
- Board seats; veto/protective provisions; information rights.
- Anti-dilution; tag-along; exit rights and redemption.
- How these differ from a control investor's levers.
**Connects to.** Z2.8 (VC control terms), ★ G43 Drag/tag, G51 Governance (Z4), ★ G46 Term sheet, G52 Exit.

## Branch 2C — Buyouts

### Z2.20 · Buyouts Defined `[branch]`
**Quick definition.** Acquisition of a controlling (usually majority) stake in a mature company, often using significant debt — a leveraged buyout (LBO).
**Explainer covers.**
- Defining characteristics; control vs. minority; mature, cash-generative targets.
- The LBO concept in one breath.
- The skillset: financial + process + operational value creation.
**Connects to.** Z2.21, ★ G29 Leverage, Z2.25 (types), G49 Value creation (Z4), ★ G32 Sources & uses.

### Z2.21 · Leveraged Buyout (LBO) Mechanics `[core]`
**Quick definition.** Buying a company with a mix of equity and borrowed money, using the target's own cash flows to service and repay the debt.
**Explainer covers.**
- Why leverage amplifies equity returns (and risk).
- Sources & uses; debt capacity and cash-flow coverage; the equity cheque.
- Deleveraging over the hold; the three return drivers (deleveraging, EBITDA growth, multiple expansion).
**Connects to.** ★ G29 Leverage, ★ G32 Sources & uses, ★ G30 Net debt, ★ G24 EBITDA, Z3.14 (debt instruments), Z2.23, Z3.11 (LBO analysis).

### Z2.22 · Sources & Uses of Funds `★ GLOBAL (G32)` `[core]`
**Quick definition.** The deal-funding table showing where the acquisition money comes from (debt tranches + sponsor equity + management equity) and what it pays for (price, fees, refinancing).
**Explainer covers.**
- Structure of the table and how it must balance.
- The funding mix and where each layer sits in risk terms.
- Uses: equity purchase, existing-debt repayment, transaction fees, minimum cash.
**Connects to.** Z2.21, Z3.14 (debt stack), ★ G45 Sweet equity, Z3.15 (SPV structure).

### Z2.23 · Buyout Value Drivers & Returns `[core]`
**Quick definition.** The three engines of LBO returns — paying down debt, growing EBITDA, and exiting at a higher multiple.
**Explainer covers.**
- Deleveraging; operational/EBITDA growth; multiple expansion.
- How leverage magnifies the equity return on each.
- The value-attribution bridge (which engine did the work).
**Connects to.** ★ G29 Leverage, ★ G24 EBITDA, ★ G27 Valuation multiples, G49 Value creation (Z4), Z4.8 (measuring it), ★ G1 IRR/★ G2 MOIC.

### Z2.24 · Management Teams in a Buyout `[core]`
**Quick definition.** How buyout funds assess, retain, incentivize, and align the executives who'll run the company after the deal.
**Explainer covers.**
- Assessing management; rollover vs. replacement.
- Introducing sweet equity and management co-investment (full detail in Z4.5).
- Why alignment with management is the founding PE principle.
**Connects to.** ★ G45 Sweet equity, Z4.5 (management comp), G51 Governance (Z4), G48 Alignment.

### Z2.25 · Types of Buyout Transactions `[core]`
**Quick definition.** The deal situations buyouts arise from — public-to-private, carve-outs, privatizations, family successions, secondary buyouts, and management buyouts/buy-ins.
**Explainer covers.**
- **Public-to-private (P2P)**; **corporate carve-out/divestiture**; **privatization** (state asset).
- **Family-business succession**; **secondary buyout**.
- **MBO vs. MBI vs. BIMBO** — who's driving the deal.
- The distinct PE value-add angle for each.
**Connects to.** ★ G55 Secondary buyout (Z4 exit), Z3.2 (sourcing), Z3.12 (P2P pricing), G49 Value creation (Z4).

## Branch 2D — Alternative Strategies

### Z2.26 · Distressed Private Equity `[branch]`
**Quick definition.** Investing in troubled companies — either to turn around operations or to gain control through their distressed debt ("loan-to-own").
**Explainer covers.**
- Turnaround investing (operational fix) vs. distressed-debt-to-control.
- The typical turnaround process.
- Why Europe differs from the US; the specialist skillset.
**Connects to.** Z3.18 (debt docs/covenants), ★ G34 Covenant, ★ G33 Debt stack, G49 Value creation (Z4), **GAP: restructuring depth**.

### Z2.27 · Real Assets PE `[branch]`
**Quick definition.** Applying the PE operating model to real estate, infrastructure, and natural resources rather than to operating companies.
**Explainer covers.**
- Real estate PE; infrastructure (long-life, yield-oriented); natural resources.
- Project-stage risk: greenfield → brownfield → operating.
- How the fund model and return profile adapt to each vertical.
**Connects to.** Z1.3 (fund structure), Z5.1 (fund formation), **GAP: real-estate & infrastructure texts**.
*Real-world layer: PE in Action Case #3 (Pro-invest: launching a PE real-estate fund).*

---

# PART 4 · Zone 3 — Doing Deals

**What this zone is:** the deal process — the most sequential zone in the module. It runs end-to-end from finding a deal to signing the documents. *(Source: Mastering PE, Ch. 6–10; modeling depth supplemented by Ippolito Ch. 6–9 and, once readable, Rosenbaum & Pearl.)*

**Learning sequence (the process is the order):**
`Deal funnel → Sourcing → Due diligence → Valuation → Pricing → Structuring → Documentation.`
This zone is best taught *in order* but every node still links to its glossary primitives so a user can drop in mid-process.

---

### Z3.1 · The PE Deal Funnel & Value Chain `[core]`
**Quick definition.** The funnel narrowing many sourced opportunities down to the few deals actually closed — and the end-to-end value chain of a PE transaction.
**Explainer covers.**
- Funnel ratios: sourced → screened → diligenced → IC-approved → closed.
- The PE value chain overview as the spine of this zone.
- Conversion economics and why sourcing volume matters.
**Connects to.** Z3.2, ★ G28 Due diligence, all Zone 3 nodes, ★ G17 Dry powder.

### Z3.2 · Deal Sourcing & Generating Deal Flow `[process]`
**Quick definition.** How PE firms originate opportunities — from proprietary networks to intermediated, competitive auctions.
**Explainer covers.**
- Deal sources: proprietary/relationship, intermediated, and auctioned.
- Networks and reputation as the real edge; sourcing in emerging markets.
- Proprietary vs. auctioned trade-offs.
**Connects to.** Z3.1, Z3.3 (auctions), ★ G28 Due diligence, Z2.25 (buyout types as sources), ★ G17 Dry powder.

### Z3.3 · The Auction Process `[process]`
**Quick definition.** A structured, competitive sale (often bank-run) in which multiple bidders compete for a target, typically across two stages.
**Explainer covers.**
- One- vs. two-stage auctions; indicative (NBO) vs. binding bids.
- The data room and SPA mark-up dynamics.
- Strategic vs. financial buyers; competitive tension and the winner's curse.
**Connects to.** Z3.2, Z3.12 (pricing), ★ G36 SPA, ★ G28 Due diligence, Z4.15 (trade sale — the other side).

### Z3.4 · Due Diligence `★ GLOBAL (G28)` `[process]`
**Quick definition.** The systematic investigation of a target's business, finances, legal standing, and risks before committing capital.
**Explainer covers.**
- Purpose and the DD process; reliance and the role of advisors.
- The "areas" (see Z3.5); red flags and deal-breakers.
- Quality of earnings and how DD feeds the model and the SPA warranties.
**Connects to.** Z3.5, Z3.6 (valuation), ★ G24 EBITDA (adjustments), ★ G36 SPA (warranties), Z4.10 (ESG DD).

### Z3.5 · Due Diligence Areas `[core]`
**Quick definition.** The specific domains a DD effort covers — commercial, financial, legal, tax, operational, and beyond.
**Explainer covers.**
- Commercial/market DD; financial DD and quality of earnings.
- Legal and tax DD; operational and management DD.
- Environmental/ESG, IT, and insurance DD.
**Connects to.** ★ G28 Due diligence, Z3.6, quality of earnings, Z4.10 (ESG).

### Z3.6 · The Valuation Toolkit `[core]`
**Quick definition.** The core methods PE uses to value targets — DCF, comparable companies, precedent transactions, and LBO/ability-to-pay analysis.
**Explainer covers.**
- Intrinsic (DCF) vs. relative (comps, precedents) vs. LBO analysis.
- The "football field" of overlapping value ranges.
- When each method applies and its limits.
**Connects to.** Z3.7, Z3.8, Z3.9, Z3.10, Z3.11, ★ G25 EV, ★ G26 Equity value, ★ G27 Multiples.

### Z3.7 · Enterprise Value vs Equity Value `★ GLOBAL (G25, G26)` `[core]`
**Quick definition.** Enterprise value is the value of the whole business; equity value is what's left for shareholders after subtracting net debt.
**Explainer covers.**
- EV = equity value + net debt (+ minorities − associates, etc.); the EV→equity bridge.
- Why valuation multiples are usually built on EV.
- The classic mistakes (mixing EV and equity metrics).
**Connects to.** ★ G30 Net debt, ★ G27 Multiples, Z3.6, Z3.13 (pricing adjustments), ★ G32 Sources & uses.

### Z3.8 · Valuation Multiples `★ GLOBAL (G27)` `[core]`
**Quick definition.** Shorthand valuation ratios (e.g., EV/EBITDA) that price a company relative to peers or precedent deals.
**Explainer covers.**
- EV/EBITDA, EV/EBIT, EV/Sales, P/E; revenue/KPI multiples for early-stage.
- Choosing and normalizing the multiple; what drives it (growth, margins, sector, cycle).
- Reading historical multiple ranges.
**Connects to.** ★ G24 EBITDA, ★ G25 EV, Z3.6, Z2.23 (multiple expansion), Z4.8.

### Z3.9 · Valuing Early-stage vs Mature Companies `[core]`
**Quick definition.** Early-stage firms are valued on potential (revenue/KPI multiples and the VC method); mature firms on cash flows and earnings multiples.
**Explainer covers.**
- The VC method: target return → implied post-money.
- Growth/buyout valuation: DCF plus multiples.
- Why early-stage valuation is irreducibly subjective.
**Connects to.** Z3.6, ★ G41 Pre/post-money, Z2.5 (VC process), Z3.10 (DCF).

### Z3.10 · DCF & Cost of Capital `[core]`
**Quick definition.** Valuing a business as the present value of its future cash flows, discounted at its cost of capital.
**Explainer covers.**
- Free-cash-flow projection; WACC; terminal value.
- APV for leveraged structures; sensitivity analysis.
- *(Covered lightly in Mastering PE; modeling depth from Ippolito Ch. 7 / Rosenbaum & Pearl.)*
**Connects to.** Z3.6, ★ G25 EV, Z3.11 (LBO analysis), ★ G29 Leverage. **GAP: full modeling mechanics.**

### Z3.11 · LBO Analysis / Ability-to-Pay `[core]`
**Quick definition.** Working backward from a target equity return and the available leverage to the maximum price a buyout investor can pay.
**Explainer covers.**
- Entry leverage → debt capacity; required equity return; exit assumptions.
- How leverage sets the price ceiling; LBO as a valuation method, not just a financing plan.
**Connects to.** Z2.21 (LBO mechanics), ★ G29 Leverage, ★ G32 Sources & uses, Z3.6, Z3.12.

### Z3.12 · Deal Pricing Dynamics `[process]`
**Quick definition.** How the headline price actually gets set and competed for, and how leverage and auction tension shape it.
**Explainer covers.**
- Bidding strategy; leverage's effect on the price you can justify.
- Pricing "outside the model" — qualitative and relationship factors.
- Strategic vs. financial-buyer pricing; the winner's curse.
**Connects to.** Z3.3 (auctions), Z3.11 (LBO analysis), ★ G29 Leverage, Z2.25 (P2P).

### Z3.13 · Pricing Adjustments & Closing Mechanisms `[core]`
**Quick definition.** The mechanisms that adjust the final price between signing and closing — locked-box vs. completion accounts, plus net-debt and working-capital adjustments.
**Explainer covers.**
- **Locked-box** vs. **completion-accounts** mechanisms.
- The **net-debt** adjustment and the **target/normalized working-capital** peg.
- Cash-free/debt-free convention; earn-outs; post-closing disputes and remedies.
**Connects to.** ★ G30 Net debt, ★ G31 Working capital, Z3.7 (EV→equity bridge), ★ G36 SPA.

### Z3.14 · Buyout Funding Instruments / The Debt Stack `★ GLOBAL (G33)` `[core]`
**Quick definition.** The layered mix of debt and equity instruments used to fund a buyout, ranked by seniority and risk.
**Explainer covers.**
- **Senior debt** (Term Loan A/B, RCF); **second lien**; **mezzanine**; **PIK**.
- **High-yield bonds**; **unitranche**; **vendor loan/notes**.
- **Sponsor equity**, shareholder loans, and preferred — the bottom of the stack.
- The risk-return ladder and who holds each layer.
**Connects to.** ★ G29 Leverage, ★ G32 Sources & uses, ★ G34 Covenant, Z3.15 (SPV), Z2.26 (distressed). **GAP: private-credit depth (partly covered by Ippolito Ch. 2 & 11).**

### Z3.15 · Investment Structures & SPVs `★ GLOBAL (G35)` `[core]`
**Quick definition.** The stack of holding companies (TopCo / MidCo / BidCo) used to ring-fence the deal, place debt at the right level, and house the equity.
**Explainer covers.**
- Why SPVs are used; simple vs. complex structures.
- **TopCo / MidCo / BidCo** layering and where debt vs. equity sits.
- Tax and jurisdiction considerations; structural subordination.
- Equity vehicles within the structure (institutional strip + sweet equity).
**Connects to.** ★ G35 SPV, ★ G32 Sources & uses, ★ G33 Debt stack, ★ G45 Sweet equity, Z3.16 (docs), **GAP: tax structuring**.

### Z3.16 · PE Transaction Documentation `[core]`
**Quick definition.** The suite of legal agreements that execute a deal — the SPA, the shareholders' agreement, the disclosure letter, and more.
**Explainer covers.**
- The key-documents map for a buyout.
- "Clean exit" vs. purchaser-protection tension between seller and buyer.
- How DD findings flow into warranties and disclosure.
**Connects to.** Z3.17, Z3.18, Z3.19, ★ G28 Due diligence, G52 Exit (Z4).

### Z3.17 · Sale & Purchase Agreement (SPA) `★ GLOBAL (G36)` `[core]`
**Quick definition.** The master contract governing a company's sale — price, conditions, representations, warranties, and remedies.
**Explainer covers.**
- Structure; price and adjustment mechanism; conditions precedent.
- Reps & warranties, indemnities, and warranty & indemnity (W&I) insurance.
- Restrictive covenants; seller vs. buyer protections.
**Connects to.** Z3.13 (pricing adjustments), ★ G28 Due diligence, Z3.16, Z4.15 (trade sale uses it again).

### Z3.18 · Buyout Debt Documentation & Covenants `★ GLOBAL (G34)` `[core]`
**Quick definition.** The loan agreements — and the covenants — that govern the deal's debt and protect its lenders.
**Explainer covers.**
- The facility/loan agreement and the intercreditor agreement.
- **Maintenance vs. incurrence covenants**; the rise of **cov-lite**.
- Cash-flow cover / debt service; the security package; events of default.
**Connects to.** ★ G33 Debt stack, ★ G29 Leverage, ★ G30 Net debt, Z2.26 (distressed), **GAP: private-credit & restructuring depth**.

### Z3.19 · Equity Documentation `[core]`
**Quick definition.** The shareholders' agreement and articles that set ownership, governance, and the management-equity (sweet-equity) terms.
**Explainer covers.**
- Shareholders' agreement and articles of association.
- Key provisions: board, reserved matters, transfers, leaver provisions, drag/tag.
- The management-equity package: institutional strip + sweet equity + ratchets.
**Connects to.** ★ G45 Sweet equity, ★ G43 Drag/tag, G51 Governance (Z4), Z4.5 (management comp), ★ G44 Minority rights.

---

# PART 5 · Zone 4 — Managing Investments

**What this zone is:** the holding period — what PE actually *does* with a company between buying and selling it, ending with the exit that realizes the return. *(Source: Mastering PE, Ch. 11–15.)*

**Learning sequence (roughly chronological across the hold):**
`Active ownership → Governance → Securing & incentivizing management → Operational value creation → Responsible investment/ESG → Exit (paths & preparation).`

---

### Z4.1 · Active Ownership & the Holding Period `★ GLOBAL (G47, G22)` `[core]`
**Quick definition.** The post-close phase in which PE works hands-on with a company — with a sense of urgency — to create value before exit.
**Explainer covers.**
- The 3–7-year holding period; active vs. passive ownership.
- The shift from "financial engineer" to "industrialist."
- The value-creation mandate that frames everything in this zone.
**Connects to.** ★ G22 Holding period, G51 Governance, G49 Operational value creation, ★ G50 100-Day Plan, G52 Exit.

### Z4.2 · Corporate Governance in PE `★ GLOBAL (G51)` `[core]`
**Quick definition.** The board-level control and oversight structures PE uses to steer a portfolio company.
**Explainer covers.**
- Core governance principles in a control buyout; board composition and reserved matters.
- Reporting cadence and the information edge.
- Governance in minority/growth settings; the special case of family-owned businesses.
**Connects to.** G47 Active ownership, G48 Alignment, Z2.8 (board rights), ★ G44 Minority rights, Z4.4.

### Z4.3 · Alignment of Interest `★ GLOBAL (G48)` `[core]`
**Quick definition.** Structuring incentives so management, the GP, and LPs all win from the same outcome — value creation and a strong exit.
**Explainer covers.**
- The founding principle of PE (Kravis): owner-mindset management.
- The three alignment layers: management ownership, GP commitment, LP carry.
- How misalignment quietly destroys value.
**Connects to.** ★ G45 Sweet equity, Z4.5, ★ G23 GP commitment (Z1), ★ G10 Carried interest, G51 Governance.

### Z4.4 · Securing & Working with Management Teams `[core]`
**Quick definition.** How PE owners recruit, retain, motivate, and sometimes replace the executives running a portfolio company.
**Explainer covers.**
- Assessing management; what makes a great PE CEO.
- Rollover vs. new hires; the PE owner's role (two competing views).
- Aligning VC funds with founders (the minority analogue).
**Connects to.** ★ G45 Sweet equity, Z4.5, G51 Governance, G48 Alignment, G49 Value creation.

### Z4.5 · Management Compensation & Sweet Equity `★ GLOBAL (G45)` `[core]`
**Quick definition.** The equity incentive package — sweet equity, ratchets, leaver terms — that gives management outsized upside for hitting targets.
**Explainer covers.**
- **Sweet equity** vs. the **institutional strip**; the two-tiered structure.
- The **envy ratio**; **ratchets** (positive/negative); vesting.
- **Good-leaver / bad-leaver** provisions; cash-flow and sweet-equity returns at exit.
**Connects to.** Z3.19 (equity docs), G48 Alignment, Z2.14 (ESOP — the VC analogue), ★ G32 Sources & uses, G52 Exit.

### Z4.6 · Operational Value Creation `★ GLOBAL (G49)` `[core]`
**Quick definition.** Growing returns by improving the actual business — revenue, margins, operations, strategy — rather than relying on leverage or multiple expansion.
**Explainer covers.**
- The value-creation roadmap and the levers: revenue growth, margin/cost, capital efficiency, M&A/buy-and-build, strategic repositioning.
- Resources: in-house operating partners (e.g., KKR Capstone–style teams).
- The "skilled industrialists" model and the 100-day plan.
**Connects to.** ★ G50 100-Day Plan, Z2.23 (value drivers), Z4.9 (buy-and-build), Z4.8 (measuring it), operating partners.

### Z4.7 · The 100-Day Plan / Value Creation Plan `★ GLOBAL (G50)` `[core]`
**Quick definition.** The urgent post-close action plan that sets priorities, metrics, and quick wins from day one of ownership.
**Explainer covers.**
- Origins and rationale; upfront operating metrics that surface problems early.
- Quick wins vs. structural change; the ownership model in practice.
**Connects to.** G47 Active ownership, G49 Operational value creation, G51 Governance.

### Z4.8 · Measuring Operational Value Creation `[core]`
**Quick definition.** Frameworks that decompose a deal's return into how much came from operations vs. leverage vs. multiple expansion — "isolating alpha."
**Explainer covers.**
- The standard value-creation bridge.
- "IVC 2.0"–style driver decomposition; isolating alpha from market beta.
- Attribution analysis as a diligence and reporting tool.
**Connects to.** Z2.23 (value drivers), G49 Operational value creation, Z5.10 (performance), Z3.8 (multiples).

### Z4.9 · Buy-and-Build / Add-on Acquisitions `[core]`
**Quick definition.** Growing a platform company by acquiring smaller add-ons to gain scale, multiple arbitrage, and synergies.
**Explainer covers.**
- Platform + add-ons; multiple arbitrage (buy small cheap, sell big dear).
- Integration risk; follow-on capital during the holding period.
**Connects to.** G49 Operational value creation, ★ G32 Sources & uses, ★ G27 Multiples, Z1.4 (follow-on investment).

### Z4.10 · Responsible Investment & ESG `[core]`
**Quick definition.** Integrating environmental, social, and governance factors into PE investing — from risk management to genuine value creation.
**Explainer covers.**
- The responsible-investment continuum; ESG "from risk to opportunity."
- Three categories of ESG; the challenge of measuring impact.
- Emerging frameworks (PRI and successors); ESG in emerging markets; the impact-investing boundary.
**Connects to.** ★ G28 Due diligence (ESG DD), G51 Governance, G49 Value creation, Z5.6 (LP demands). **GAP: post-2017 ESG/impact frameworks (recency).**

### Z4.11 · Exit `★ GLOBAL (G52)` `[core]`
**Quick definition.** The sale or listing through which a PE fund realizes its investment and returns capital to LPs.
**Explainer covers.**
- Why exit is planned from entry; unrealized value sitting in funds.
- Exit timing and readiness; how the chosen route shapes the return.
- "The proof is in the exit."
**Connects to.** ★ G22 Holding period, Z4.12, Z4.13, ★ G53 IPO, ★ G54 Trade sale, ★ G55 SBO, ★ G11 Waterfall, Z5.10.

### Z4.12 · Exit Preparation / Exit Shaping `[process]`
**Quick definition.** The work of grooming a company and its equity story to maximize value and certainty at sale.
**Explainer covers.**
- The equity story; financial readiness and audited accounts.
- Management presentation; **vendor due diligence**; cleaning up the cap table and contracts.
- Timing the market.
**Connects to.** G52 Exit, ★ G28 Due diligence (vendor DD), ★ G36 SPA, ★ G53 IPO, ★ G54 Trade sale.

### Z4.13 · Exit Paths `[core]`
**Quick definition.** The menu of ways out — IPO, trade sale, secondary buyout, dual-track, recapitalization, or write-off.
**Explainer covers.**
- Each route's pros/cons and what drives the choice.
- Partial exits and staged sell-downs.
- Dual-track (run IPO and M&A in parallel) as a tension-creator.
**Connects to.** Z4.14, Z4.15, Z4.16, Z4.17, ★ G52 Exit.

### Z4.14 · IPO as an Exit `★ GLOBAL (G53)` `[branch]`
**Quick definition.** Listing the company on a public market to sell the stake down over time.
**Explainer covers.**
- IPO mechanics; partial exit and lock-up periods.
- Valuation vs. a trade sale; when an IPO wins.
- Dual-track with M&A.
**Connects to.** Z4.13, G52 Exit, Z2.25 (P2P — the reverse trade), dual-track.

### Z4.15 · Trade Sale `★ GLOBAL (G54)` `[branch]`
**Quick definition.** Selling the company to a strategic (corporate) buyer — often the highest-value, cleanest exit.
**Explainer covers.**
- Strategic-buyer synergies and why they can pay more.
- Clean break; auction vs. bilateral; SPA and warranties.
- Trade sale vs. secondary buyout.
**Connects to.** Z4.13, ★ G36 SPA, Z3.3 (auction), ★ G55 SBO.

### Z4.16 · Secondary Buyout (SBO) `★ GLOBAL (G55)` `[branch]`
**Quick definition.** Selling a portfolio company to another PE fund.
**Explainer covers.**
- Why SBOs happen; pricing dynamics.
- The "pass-the-parcel" critique vs. the speed/certainty advantages.
- How one fund's exit becomes another's entry (links Z2 buyout types ↔ Z4 exit).
**Connects to.** Z4.13, Z2.25 (buyout types), Z3.2 (sourcing), ★ G57 Secondaries (**not the same thing** — cross-link the distinction).

### Z4.17 · Dividend Recapitalization `[branch]`
**Quick definition.** Re-leveraging a portfolio company to pay its PE owner a dividend without selling the business.
**Explainer covers.**
- Mechanics; partial liquidity ahead of a full exit.
- Risk transferred to the company; LP and reputational optics.
**Connects to.** ★ G29 Leverage, ★ G33 Debt stack (Z3), G52 Exit, distributions.

---

# PART 6 · Zone 5 — Fund Management & the GP–LP Relationship

**What this zone is:** the meta-layer — running the fund itself, raising it, the LP's side of the table, measuring performance, winding down, and the modern evolution of the industry (co-invest, secondaries, listed PE, risk). *(Source: Mastering PE, Ch. 16–25.)*

**Learning sequence:**
`Fund formation → LPA → Waterfall (deep) → Fundraising → [LP side] Allocation → Portfolio construction → Manager selection → Managing the portfolio → Performance & metrics → Winding down → [Evolution] Co-investment → Direct → Secondaries → Listed PE → Risk → Industry future.`

---

### Z5.1 · Fund Formation & Vehicles `[core]`
**Quick definition.** How a PE fund is legally assembled — the partnership vehicle, parallel/feeder structures, and the governing LPA.
**Explainer covers.**
- Setting up a fund; the main fund plus complementary vehicles (parallel funds, feeders, co-invest vehicles, AIVs).
- Jurisdictions (Delaware, Cayman, Luxembourg) and the carry/GP vehicle.
- The LPA as the constitution of the fund.
**Connects to.** ★ G20 LPA, ★ G19 Blind pool (Z1), Z1.3 (structure), ★ G11 Waterfall, Z5.4.

### Z5.2 · The Limited Partnership Agreement (LPA) `★ GLOBAL (G20)` `[core]`
**Quick definition.** The governing contract of a PE fund — setting the mandate, economics, governance, and the rights of LPs and GP.
**Explainer covers.**
- Key terms: term & extensions, investment period, fees, carry, waterfall, hurdle, GP commit, key-man, no-fault divorce, LPAC, recycling, default remedies.
- ILPA principles as the LP-side standard.
- Negotiation, side letters, and MFN clauses.
**Connects to.** Z5.1, ★ G11 Waterfall, ★ G10 Carried interest, ★ G12 Hurdle, key-man, Z5.7.

### Z5.3 · The Distribution Waterfall (deep) `★ GLOBAL — deep home of G11` `[core]`
**Quick definition.** The detailed mechanics and worked math of how proceeds are split between LPs and the GP.
**Explainer covers.**
- **European / whole-fund** vs. **American / deal-by-deal** waterfalls, step by step.
- A full worked example: return capital → preferred return → catch-up → 80/20 carry split.
- Loss carry-forward, make-whole, and interim clawback.
**Connects to.** ★ G10 Carried interest, ★ G12 Hurdle, ★ G13 Catch-up, ★ G14 Clawback (all Z1), ★ G20 LPA, Z5.1.

### Z5.4 · The Fundraising Process `[process]`
**Quick definition.** How GPs raise a new fund — the roadshow, the documentation, the closings, and securing LP commitments.
**Explainer covers.**
- Fundraising timeline and success factors; the placement agent's role.
- First vs. final closing; re-ups; first-time-fund challenges.
- LP due diligence on the GP (the other side of Z5.8).
**Connects to.** ★ G18 Vintage year (Z1), ★ G19 Blind pool, Z5.5, Z5.8, ★ G46 Term sheet (fund-level).

### Z5.5 · Fundraising Documentation `[core]`
**Quick definition.** The documents GPs present to prospective LPs — the PPM, the DDQ, the fund term sheet, and the track record.
**Explainer covers.**
- PPM (private placement memorandum) contents; the fund term sheet.
- Track record and performance attribution; the DDQ.
- ILPA templates and standardization.
**Connects to.** Z5.4, ★ G20 LPA, Z5.10 (performance), Z5.8.

### Z5.6 · LP Allocation to PE `[core]`
**Quick definition.** How institutional investors decide how much of their portfolio to put into PE, and why.
**Explainer covers.**
- The rationale: historical return premium and diversification.
- Target allocation by investor type; the illiquidity budget.
- The denominator effect and strategic asset allocation.
**Connects to.** ★ G7 LP (Z1), Z5.7, Z5.21 (risk), ★ G4 J-curve.

### Z5.7 · LP Portfolio Construction & Commitment Pacing `[core]`
**Quick definition.** How LPs build and balance a PE portfolio across vintages, strategies, and managers while managing the cash-flow timing.
**Explainer covers.**
- Diversification by vintage, strategy, geography, and manager.
- **Commitment pacing** and **over-commitment**; the denominator effect.
- Portfolio-level J-curves; managing a "ballooning" portfolio.
**Connects to.** ★ G18 Vintage year, ★ G4 J-curve, over-commitment, Z5.8, ★ G57 Secondaries.
*Real-world layer: PE in Action Case #4 (Hitting the Target: optimizing a PE portfolio with Partners Group).*

### Z5.8 · PE Fund Manager Selection (GP Due Diligence) `[core]`
**Quick definition.** How LPs evaluate and pick GPs — on track record, team, strategy, and the persistence of returns.
**Explainer covers.**
- The manager-selection process and operational due diligence on GPs.
- Track record and quartiles by vintage; the persistence debate.
- The access problem (getting into top-quartile funds).
**Connects to.** ★ G18 Vintage year, Z5.10, Z5.4, ★ G19 Blind pool, Z5.21 (manager risk).

### Z5.9 · Managing an Existing PE Portfolio `[core]`
**Quick definition.** The ongoing work of monitoring funds, managing cash flows, and rebalancing exposure over time.
**Explainer covers.**
- Monitoring and reporting; cash-flow management.
- Re-ups vs. new managers; using secondaries to rebalance; NAV management.
**Connects to.** ★ G4 J-curve, ★ G57 Secondaries, Z5.10, ★ G56 Co-investment.

### Z5.10 · Performance Reporting & Measurement `★ GLOBAL — deep home of G1, G2, G3` `[core]`
**Quick definition.** The metrics and conventions used to measure and compare PE fund performance, net of fees.
**Explainer covers.**
- Gross vs. net; interim vs. final performance.
- **IRR**; **MOIC/TVPI**; **DPI** (realized) and **RVPI** (unrealized).
- The **"IRR conundrum"** (reinvestment assumptions, early-distribution distortion, manipulation) and **MIRR** as a partial fix.
- Benchmarking, vintage quartiles, and **PME**.
**Connects to.** ★ G1 IRR, ★ G2 MOIC, ★ G3 DPI/RVPI/TVPI, ★ G5 PME, MIRR, ★ G4 J-curve, ★ G18 Vintage year.

### Z5.11 · IRR `★ GLOBAL (G1)` `[core]`
**Quick definition.** The annualized, time-weighted discount rate that sets a fund's cash flows to zero — PE's headline return number.
**Explainer covers.**
- Definition; gross vs. net.
- Sensitivity to timing and early distributions; the conundrum and manipulation tactics.
- MIRR; since-inception vs. point-to-point IRR.
**Connects to.** ★ G2 MOIC, MIRR, ★ G4 J-curve, Z5.10, ★ G18 Vintage year.

### Z5.12 · MOIC / Multiple of Money `★ GLOBAL (G2)` `[core]`
**Quick definition.** The absolute multiple an investment returns — total value ÷ capital invested (e.g., 2.5×); time-blind by design.
**Explainer covers.**
- Gross vs. net MOIC; "cash-on-cash."
- Relation to TVPI/DPI/RVPI.
- Why it complements IRR (and where it misleads).
**Connects to.** ★ G1 IRR, ★ G3 DPI/RVPI/TVPI, Z5.10.

### Z5.13 · DPI, RVPI & TVPI `★ GLOBAL (G3)` `[core]`
**Quick definition.** The three "multiple" ratios splitting fund value into cash already returned (DPI), value still held (RVPI), and the two combined (TVPI).
**Explainer covers.**
- Definitions on a paid-in basis; DPI = realized, RVPI = NAV/unrealized, TVPI = DPI + RVPI.
- How they evolve over a fund's life (RVPI converts to DPI as exits happen).
**Connects to.** ★ G2 MOIC, ★ G4 J-curve, Z5.10, NAV.

### Z5.14 · PME (Public Market Equivalent) `★ GLOBAL (G5)` `[core]`
**Quick definition.** A benchmark that compares a PE fund's return to what the same cash flows would have earned in a public-market index.
**Explainer covers.**
- Why public benchmarking matters (opportunity cost).
- PME methods (Long-Nickels, Kaplan-Schoar, Direct Alpha).
- What the PE-vs-public-market record actually shows.
**Connects to.** ★ G1 IRR, Z5.10, Z5.21 (risk), Z5.6 (allocation).

### Z5.15 · Winding Down a Fund `[process]`
**Quick definition.** The end-of-life process of liquidating remaining assets, returning capital, and closing a fund.
**Explainer covers.**
- Liquidating a fund; tail-end / end-of-life options and extensions.
- GP-led secondaries and continuation funds as a wind-down tool.
- The transition into zombie-fund territory.
**Connects to.** Z5.16, ★ G57 Secondaries (GP-led), ★ G22 Holding period, Z1.4 (lifecycle).

### Z5.16 · Zombie Funds & Tail-end Solutions `[core]`
**Quick definition.** Funds stuck past their life with unexited assets and no new fund — plus the tools (secondaries, restructurings) used to resolve them.
**Explainer covers.**
- The zombie-fund lifecycle and tail-end assets.
- GP-led restructurings and continuation vehicles.
**Connects to.** Z5.15, ★ G57 Secondaries, Z5.10 (stuck NAV).

### Z5.17 · Co-investment `★ GLOBAL (G56)` `[branch]`
**Quick definition.** LPs investing directly alongside a GP in a specific deal, usually fee-free, on top of their fund commitment.
**Explainer covers.**
- What co-investment is and the LP attractions (lower blended fees, return enhancement, selection).
- GP motivations and risks; implementation challenges.
- The relative-value approach to using co-invest.
**Connects to.** Z5.18, ★ G9 Fund economics (fee reduction), Z5.21 (direct-investment risk), ★ G57 Secondaries.

### Z5.18 · LP Direct Investment ("Going Direct") `[branch]`
**Quick definition.** Large LPs building in-house teams to invest directly in companies, bypassing GPs and their fees.
**Explainer covers.**
- Going direct vs. co-investing; the CPPIB / Teachers' model.
- Attractions and risks; the talent/governance implementation challenge.
**Connects to.** ★ G56 Co-investment, ★ G9 Fund economics, Z5.21, G51 Governance.
*Real-world layer: PE in Action Case #2 (Going Direct: Teachers' Private Capital).*

### Z5.19 · PE Secondaries `★ GLOBAL (G57)` `[branch]`
**Quick definition.** The market for buying and selling existing fund stakes and portfolios, giving otherwise-illiquid LPs an exit.
**Explainer covers.**
- Why secondaries exist; **LP-led** vs. **GP-led**.
- Transaction types: LP stake sale, direct secondary, structured secondary, total-return-swap, **continuation funds**.
- Deal structuring and pricing (discount/premium to NAV); execution.
**Connects to.** ★ G15 Capital call / ★ G4 J-curve (liquidity), NAV, Z5.15 (GP-led/continuation), ★ G56 Co-investment, ★ G55 SBO (**clarify the difference**). **GAP: post-2017 continuation-fund boom (recency).**

### Z5.20 · Listed Private Equity `[branch]`
**Quick definition.** PE accessed through public markets — either listed PE firms (the manager) or listed PE funds/vehicles.
**Explainer covers.**
- Listed PE firms (GP/management-company IPOs) vs. listed PE funds.
- How listed-PE vehicles generate revenue; discount-to-NAV dynamics.
- Pros/cons for retail and LP access.
**Connects to.** ★ G6 GP, Z1.3 (structure), NAV/discount, ★ G53 IPO.

### Z5.21 · PE Risk Management `[core]`
**Quick definition.** Identifying and managing the distinct risks of PE — asset-class, portfolio, manager, and direct-investment risk — for both LPs and GPs.
**Explainer covers.**
- Asset-class risk (illiquidity, valuation lag, range of returns).
- Portfolio/idiosyncratic risk; fund-manager risk; direct-investment risk.
- FX risk ("hedge or hope"); risk management from the GP's side.
**Connects to.** ★ G4 J-curve, ★ G18 Vintage year, Z5.8, ★ G56 Co-investment, ★ G5 PME, ★ G29 Leverage.

### Z5.22 · The Evolution & Future of PE `[core]`
**Quick definition.** Where PE came from and the forces — scale, competition, diversity, returns sustainability, democratization — shaping where it's going.
**Explainer covers.**
- The history (from "barbarians" to "industrialists").
- AUM growth and maturation; can returns persist as the industry scales?
- Democratization/retail access; diversity; "quo vadis."
**Connects to.** Z1.1 (what is PE), Z5.20, ★ G56 Co-investment, ★ G57 Secondaries, **capstone — links back to all zones**. **GAP: post-2017 developments (NAV lending, evergreen/semi-liquid vehicles, private-wealth channel).**

---

# PART 7 · Cross-zone connective tissue

The graph's power is in the edges that **jump between zones**. These are the highest-value links to build — they're what make the app feel like a connected knowledge environment rather than five separate courses. The strongest cross-zone threads:

1. **IRR / MOIC** (G1/G2) thread through *every* zone: VC target returns (Z2.2/Z2.15) → buyout return drivers (Z2.23) → LBO ability-to-pay (Z3.11) → value-creation attribution (Z4.8) → fund performance (Z5.10). One canonical pair, dozens of contextual entry points.
2. **Leverage** (G29) connects buyout strategy (Z2.21) → the debt stack (Z3.14) → debt documentation/covenants (Z3.18) → return drivers (Z2.23) → dividend recaps (Z4.17) → risk (Z5.21).
3. **The waterfall + carry + hurdle + catch-up + clawback cluster** (G10–G14) is introduced in Zone 1, lives deeply in Zone 5 (Z5.3), and is the economic engine LPs evaluate in Z5.8/Z5.10. Build Z1's quick versions as links into Z5.3's deep version.
4. **Sweet equity** (G45) spans buyout management (Z2.24) → equity documentation (Z3.19) → management compensation (Z4.5) → alignment (Z4.3), and rhymes with the VC-side **ESOP** (Z2.14) — link the two as "the same idea in two strategies."
5. **Due diligence** (G28) reappears as *vendor* DD at exit (Z4.12) — same skill, opposite side of the table.
6. **The buyout entry ↔ exit loop:** "Types of buyout" (Z2.25) and "Exit paths" (Z4.13) are the same transactions seen from opposite ends — a P2P entry (Z2.25) is some public-market exit; a secondary buyout is one fund's exit (Z4.16) and another's entry. These should explicitly cross-link.
7. **Minority rights** (G44) connect VC control terms (Z2.8) ↔ growth equity (Z2.19) ↔ governance (Z4.2) — the through-line of "investing without control."
8. **Valuation** (Z3.6 + EV/equity/multiples) underpins VC pricing (Z3.9/Z2.5), buyout pricing (Z3.11/Z3.12), value attribution (Z4.8), and exit value (Z4.11).

---

# PART 8 · Suggested master path (for the "guided sequence" mode)

The app lets users jump anywhere, but the **default suggested sequence** a professional would follow:

1. **Zone 1 — PE Ecosystem** (what it is, who, how the money works) → this is also the onboarding primer's finance content.
2. **Zone 2 — Types of PE** (the strategy you'd specialize in), entering at the spectrum (Z2.1).
3. **Zone 3 — Doing Deals** (the process), taught in order, sourcing → documentation.
4. **Zone 4 — Managing Investments** (the hold), chronologically through to exit.
5. **Zone 5 — Fund Management** (the meta-layer), once the deal lifecycle makes sense.

**Within-zone entry points for non-linear users:** Z1.1, Z2.1, Z3.1, Z4.1, Z5.1 are the natural "front doors." Every other node is reachable directly and links back to its prerequisites via the glossary layer, so no user is ever stranded.

---

# PART 9 · Source gaps — material we need but don't have

Concepts the books *reference or assume* but don't cover deeply enough to build authoritative nodes from. Flagged by priority.

**High priority (blocks whole node clusters):**
1. **Private credit / direct lending (fund-level).** Mastering PE covers mezzanine and distressed debt only as buyout inputs. → *Partially solved:* **Ippolito's *Private Capital Investing* is now in the Drive** and covers debt products (Ch. 2), private debt structuring (Ch. 11), and distress (Ch. 13). Still ideal: **Nesbitt, *Private Debt***, for the direct-lending *fund* business (BDCs, fund economics, the asset class). Needed for Z2.26, Z3.14, Z3.18 and the future Private Credit module.
2. **LBO / DCF / comps modeling mechanics.** Z3.10 and Z3.11 are survey-level in Mastering PE. → **Rosenbaum & Pearl, *Investment Banking*** (already flagged in the project; needs a text-based PDF) is the canonical source; Ippolito Ch. 6–9 helps in the interim.
3. **Macroeconomics, interest rates & credit cycles.** The engine behind leverage availability, entry multiples, and exit windows — assumed throughout, taught nowhere. Needed for Core Concepts and to give Z2.21/Z3.12/Z5.21 their "why now" context. → need a dedicated macro/credit-cycle text.

**Medium priority (deepens existing nodes):**
4. **Dedicated venture capital text.** Mastering PE's VC chapter is a strong survey but predates modern instruments (SAFEs, convertible notes, valuation caps, pro-rata rights, modern seed mechanics, startup-secondary markets). → **Feld & Mendelson, *Venture Deals*** is the standard — and Brad Feld is already a guest author in Mastering PE. Needed to flesh out Z2.7–Z2.15 and the future VC module.
5. **Restructuring / distressed depth.** Turnaround and loan-to-own (Z2.26) need real mechanics. → **Moyer, *Distressed Debt Analysis***.
6. **Real estate & infrastructure.** Z2.27 (real assets) is thin; each vertical needs its own source for the sector modules. → real-estate (e.g., Linneman/Geltner) and an infrastructure-investing text.
7. **Tax structuring.** SPV/jurisdiction choices (Z3.15) are sketched, not explained. → a cross-border PE tax-structuring source.

**Recency gaps (both core books are 2017 — flag for every node touched):**
8. **ESG / impact frameworks** (Z4.10): the field has standardized since 2017 (PRI evolution, SFDR, the ISSB/SASB consolidation, the SDR regime). The book's "emerging frameworks" framing is now dated.
9. **Secondaries & continuation funds** (Z5.19, Z5.15): the GP-led / continuation-vehicle market barely existed in 2017 and is now a dominant exit and liquidity route. Needs a current source.
10. **Fund finance & NAV lending** (touches Z1.5, Z5.21): subscription lines and NAV facilities now materially shape reported IRRs and LP cash flows — absent from the 2017 text. Needs a current source.
11. **Retail / democratization** (Z5.22): evergreen, interval, and semi-liquid vehicles and the private-wealth distribution channel have moved fast since 2017. Needs a current source.
12. **Fund accounting & ILPA reporting standards** (Z1.12, Z5.5, Z5.10): referenced (ILPA, "Performance Reporting 2.0") but the operational detail needs a dedicated fund-accounting source.

**Build note:** every node with a `GAP:` tag in the map above should carry a visible "source needed" flag in the CMS so content isn't written from memory where the books are thin. When a gap-filling book is added to the Drive, its concepts become new nodes that attach at the flagged connection points — the graph grows at its seams, exactly as the architecture intends.

---

# PART 10 · Using this as the template for every other module

The whole point of mapping PE first is that its shape is reusable. The pattern that generalizes:

**The five-zone spine maps to any investing discipline:**

| PE zone | Generalized zone | IB module | Private Credit module | Equity Research module |
|---|---|---|---|---|
| Z1 Ecosystem | *Who/what/how the money works* | The IB franchise, products, fee model | The lender ecosystem, fund vs. BDC, fee model | The sell-side/buy-side ecosystem, the research product |
| Z2 Types | *The strategy branches* | M&A · ECM · DCM · Restructuring · LevFin | Direct lending · mezzanine · unitranche · distressed · specialty | By sector / by mandate (long-only, L/S, etc.) |
| Z3 Doing Deals | *The core process* | Pitch → mandate → diligence → valuation → execution | Origination → credit DD → structuring → documentation | Initiation → modeling → thesis → rating → publication |
| Z4 Managing | *The holding/ongoing work* | Deal execution & closing mechanics | Portfolio monitoring, covenants, workouts | Maintenance, earnings updates, estimate revisions |
| Z5 Meta | *The business & relationships* | League tables, the client relationship, the franchise | Fund management, LP relations, recoveries | The franchise, ratings, client distribution, regulation |

**What transfers directly:**
- **The node schema** (quick def → layered explainer → connections → tag) is identical across modules.
- **The glossary layer pattern**: build the cross-zone canonical terms first; everything links back. Many PE glossary nodes (IRR, MOIC, EBITDA, EV/equity, leverage, DCF, the debt stack, covenants, due diligence) are *shared* across modules — they should be **one canonical set the whole app reuses**, not re-created per module. IRR in the PE module and IRR in the Private Credit module are the same node.
- **The "this vs. that" disambiguation links** (e.g., secondaries vs. secondary buyout) are a reusable content type wherever two terms collide.
- **The learning-sequence-but-jumpable** convention: each zone gets a logical order and a designated front-door node, with glossary back-links so no one is stranded.
- **The `GAP:` flagging discipline**: every module will have edges to material not yet in the Drive; flag them so they become attachment points for future books.

**The shared-glossary insight is the most important one for scale.** As more modules come online, the glossary stops being per-module and becomes the app's connective spine: the place where PE, IB, credit, and equity research all touch the same primitives. That shared layer is what turns a set of courses into the single interconnected knowledge graph the product is aiming for.
