# Venture Capital Module — Complete Node Map

*The eighth module in the asset-class series. Where Private Equity funds mature, cash-generative companies and applies leverage to extract value, Venture Capital funds the earliest, riskiest bets — the companies that do not yet exist as viable businesses, in the belief that a tiny number of outsized winners will pay for every failure. VC is the headwaters of the corporate lifecycle: it finances the startups that eventually IPO, become equity-research-covered public companies, and are held in the portfolios of asset managers and hedge funds. It is also PE's closest sibling, sharing almost its entire vocabulary of fund mechanics and deal structure — making it the most inheritance-heavy module yet built.*

---

## A note on this module's sources and their character

This map is grounded in three canonical books, with a fourth as supplementary reference:

- **Feld & Mendelson, *Venture Deals*, 4th ed. (Wiley, 2019)** — THE term-sheet and cap-table mechanics spine. Every economic and control term in Zone 3 traces here: pre/post-money valuation and the founder arithmetic trap, the option pool and the pre-money shuffle, liquidation preferences (the two-component structure: the preference itself and participation), pay-to-play, anti-dilution (weighted average vs. full ratchet), board composition, protective provisions, and the convertible note. The book's organizing insight — that the term sheet has only two things that matter, **economics and control** — structures the entire Zone 3 treatment.
- **Kupor, *Secrets of Sand Hill Road* (Portfolio/Penguin, 2019)** — the LP/GP/fund and portfolio mechanics from the VC's chair, with the founder's perspective always in frame. Grounds: how LPs construct their allocations and why VC is the power-law asset class in those portfolios; how early-stage VCs evaluate (people → product → market); reserves and follow-on strategy; board governance and the board's legal duties; the mechanics of difficult financings (down rounds, recaps); and exits. The Yale endowment example — 77% annualized VC returns over twenty years, 16% allocation — is the sharpest illustration of why manager selection (★G156) matters above all else in this asset class.
- **Mallaby, *The Power Law* (Penguin Press, 2022)** — the conceptual organizing principle of the entire module. Grounds: the power-law return distribution (G201) as the empirical fact that dictates how venture is practiced; why the power law requires VCs to make non-obvious bets on what looks like bad ideas; the history of the asset class from ARD through Sequoia and a16z. The Kupor/Mallaby pairing is important — Kupor explains the mechanics, Mallaby explains why those mechanics exist.
- **Ramsinghani, *The Business of Venture Capital*, 3rd ed. (Wiley, 2021)** — comprehensive supplementary reference covering the art of raising a fund, structuring investments, portfolio management, and exits; provides additional context on deal flow, portfolio construction, and the LP relationship.

**Recency note / source gaps**: All three primary sources predate the 2021–22 venture boom and subsequent 2022–24 reset. The current cycle — the crossover retreat, the exit/liquidity drought, the AI-investment wave — is not covered. Flagged explicitly in Part 9 and at the relevant nodes.

---

## How to read this map

| Element | What it means |
|---|---|
| **Zone** | One of five structural layers (the canonical five-zone template, identical across all modules). |
| **Node** | A single learning unit: `Z{zone}.{n}` plus a stable ID. |
| **★ GLOBAL (G*n*)** | A concept that lives in the **one shared glossary** spanning every module. Defined once, referenced everywhere by its number. |
| **[core] / [process] / [branch]** | Node role: a core concept, a step in a workflow, or an optional specialization the learner can skip. |
| **Quick definition** | One sentence — the "say it in a breath" version. |
| **Explainer covers** | What the full node teaches, ordered basic → technical. |
| **Connects to** | The edges. `★ G*n*` for globals; `IB Z3.1`, `HF Z3.3`, `AM Z2.4` for cross-module references. Dense by design. |
| **GAP / recency** | A flag that the underlying sources are thin, dated, or silent here. |

---

## The shared-glossary rule (the scaling discipline)

There is **one** global glossary for the entire app, currently numbered **G1–G200** across the seven prior modules. This module does two things and only two things with it:

1. **Reuses G1–G200 by number.** The entire fund-mechanics layer (★G1–G23) and the private-company deal-mechanics layer (★G37–G46) — contributed by PE — are inherited wholesale. The IB valuation toolkit (★G87–G95), the HF/ER skill primitives (★G106, ★G115, ★G121), and the AM/WM LP infrastructure (★G156) are referenced where VC touches them. None of this is rebuilt.

2. **Contributes exactly 16 genuinely novel globals, G201–G216.** These are the concepts no prior module needed: the power law, the funding round, the SAFE, the option pool and its shuffle, pre/post-money, the 409A, pro-rata rights, the down round, VC governance, deal flow, the founder bet, burn/runway, crossover investing, the markup, and the venture platform. Each is net-new. Nothing below G201 is redefined.

The 16-global count is **below the series average (18–24) by design** — the correct, expected consequence of inheritance-first discipline. PE had already globalized both the fund- and deal-mechanics layers. The below-band count is not under-building; it is the inheritance principle working correctly. This is noted explicitly in Part 10.

---

# PART 1 · The Global Glossary Layer

The 16 new globals this module contributes, grouped by theme. *Home* = the zone node where the concept is taught in depth. *Appears in* = other modules that reference it.

### Group A — VC's organizing logic & returns

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| **G201** | The power law | The venture return distribution in which a tiny number of investments produce nearly all of a fund's returns — the empirical law that dictates how VC is sourced, sized, and managed. | VC Z1.2 | PE, HF, AM, ER |
| **G202** | Power-law portfolio construction & the "return-the-fund" test | The discipline of building a portfolio of bets each sized to be capable of returning the entire fund on its own, using ownership targets rather than diversification logic. | VC Z4.3 | PE, HF, AM |
| **G203** | The venture markup & mark-to-market | The convention of carrying a holding at its most recent round price, producing paper gains (TVPI) that may diverge sharply from realized cash (DPI) until exit actually occurs. | VC Z4.5 | PE, AM, WM |

### Group B — The financing structure (the round)

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| **G204** | The funding stages & the round | The sequence of discrete financing events (pre-seed → seed → Series A/B/C → growth) that take a startup from idea to scale, each funding the company to its next value-creating milestone. | VC Z2.1 | PE, IB, ER |
| **G205** | Pre-money & post-money valuation | The round-pricing identity (post-money = pre-money + new investment) that determines how much ownership new capital buys — the single most consequential arithmetic in a venture financing. | VC Z3.7 | PE, IB |
| **G206** | The SAFE & the convertible note | Early-stage instruments that accept money now and defer pricing to a future priced round, bridged by a valuation cap and/or a discount rate. | VC Z3.11 | IB |
| **G207** | The option pool & the pre-money shuffle | The employee equity reserve (ESOP), and the VC convention of expanding it *inside* the pre-money valuation so that the dilution falls on existing shareholders rather than new investors. | VC Z3.9 | PE |
| **G208** | The 409A valuation | The independent third-party valuation of a private company's common stock that sets the strike price for employee options — typically well below the preferred-share round price. | VC Z3.12 | PE, IB |

### Group C — Rights & ongoing participation

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| **G209** | Pro-rata rights, reserves & follow-on strategy | The contractual right to invest in later rounds to maintain ownership percentage, combined with the fund-level discipline of reserving capital to double down on the portfolio's winners. | VC Z4.4 | PE |
| **G210** | The down round & the recap | A financing priced below the prior round, triggering anti-dilution protections, reordering the liquidation-preference stack, and often damaging morale and the cap table simultaneously. | VC Z4.7 | PE |
| **G211** | VC governance: board seats, information rights & protective provisions | The minority-investor control toolkit — influence exercised through board representation and veto rights rather than through the majority-control ownership of a buyout. | VC Z4.2 | PE, IB |

### Group D — Sourcing, the founder & the company's clock

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| **G212** | Deal flow & sourcing | The top of the venture funnel — generating and accessing investable opportunities — where the power law makes *seeing* the best deals as decisive as picking well among average ones. | VC Z3.2 | PE, IB |
| **G213** | The founder bet | Underwriting the team over the financials at the earliest stages — "the jockey, not the horse" — as the central and often dominant judgment of early-stage venture investing. | VC Z3.3 | PE, ER |
| **G214** | Burn rate & runway | The startup's cash-consumption rate and the number of months of survival that current cash buys — the company's clock, driving every financing decision and every milestone target. | VC Z4.6 | PE, IB |

### Group E — Growth-stage & the firm

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| **G215** | Crossover & growth-stage investing | Late-stage pre-IPO venture in which public-market investors (hedge funds, mutual funds) cross into private financing rounds, blurring the boundary between private and public capital. | VC Z2.7 | HF, AM, ER |
| **G216** | The venture platform & the partnership | The VC firm as institution — the partnership structure, its principals, scouts, and platform team that source, win, and support deals beyond the check itself. | VC Z1.8 | PE, AM |

---

## Featured disambiguations (the high-confusion pairs)

> **Venture carry (★G10) vs. PE carry (★G10) — same global, different mechanics.**
> Both use the same global (★G10, contributed by PE) because carried interest is the same legal instrument in both asset classes: the GP's ~20% share of net fund profits. But the *source* of carry differs dramatically. PE carry is distributed deal-by-deal or across a diversified portfolio of moderate-multiple exits. Venture carry is driven almost entirely by a handful of power-law winners: Sequoia's Google stake, Accel's Facebook stake, a16z's Airbnb stake. In venture, being right once — spectacularly — can define a firm's franchise for a decade and drown out every loss. This is why venture carry dominates venture compensation in a way that makes the management fee (★G8) feel like an afterthought.

> **The venture J-curve (★G4) vs. the PE J-curve (★G4) — same global, different depth and length.**
> The J-curve (★G4, contributed by PE) describes the negative-then-positive net-cash-flow shape that all closed-end fund LP's experience. Venture's J is deeper and longer than PE's for two reasons: (1) early-stage venture has more outright failures than PE, pulling the curve lower in the trough; and (2) venture exits take longer — often 8–12 years from investment — extending the negative phase. A second complication is the markup convention (G203): portfolio companies are carried at their last round price, which can make the reported TVPI look healthy well before any cash arrives. The reported J-curve therefore looks shallower than the cash J-curve until exits finally materialize.

> **Pre-money vs. post-money (G205) — the founder's arithmetic trap.**
> The identity is simple: post-money = pre-money + new investment. Ownership percentage the investor buys = investment ÷ post-money. The confusion arises in verbal negotiations: when a VC says "I'll invest $5M at a $20M valuation," she almost always means $20M *post*, implying a $15M pre-money and a 25% ownership purchase. The founder who hears "$20M pre" will compute only a 20% stake — a 5-point gap that compounds through every subsequent round. Feld & Mendelson identify this as the single most common early negotiation miscommunication. The term sheet resolves it in writing; the verbal pitch does not.

> **The SAFE / convertible note (G206) vs. a priced round (G205) — deferring valuation vs. setting it.**
> A priced round sets the company's valuation now and issues stock at a fixed price per share. A SAFE or convertible note takes the investor's money today but defers pricing to a future round; the cap (the maximum valuation at which the instrument converts) and discount (a percentage below the next round's price) are the bridge. The SAFE (Simple Agreement for Future Equity, introduced by Y Combinator) is not debt — it carries no interest rate and no maturity date. The convertible note is debt — it accrues interest and has a maturity — but is expected to convert to equity at the next round rather than be repaid in cash. The practical difference matters most if the company fails before a next round: noteholders are creditors (ahead of equity in the liquidation); SAFE holders are not.

> **VC governance (G211) vs. PE control — influence vs. command.**
> A buyout investor (PE) typically owns a majority of the company and controls a majority of board seats: it can hire and fire the CEO, approve the budget, and set strategy without consulting anyone. A venture investor (G211) typically owns a minority stake and influences the company through board representation (often one of five seats), information rights, and protective provisions (veto rights on specified major actions). The venture investor *persuades* and *vetoes*; the buyout investor *decides*. The Kupor chapter on board governance and the Trados case both illustrate how this distinction matters when interests diverge — and how minority rights can still have teeth.

> **DPI vs. TVPI in venture (★G3, via G203) — cash vs. paper.**
> DPI (distributions to paid-in, ★G3) counts only realized cash returned to LPs. TVPI (total value to paid-in, ★G3) adds in the carried value of unrealized holdings, marked at the last round price (G203). In PE, the gap is real but bounded: most companies are held for 5–7 years, markups are modeled carefully, and exits are fairly predictable. In venture, the gap can be enormous and persistent: a Series D unicorn with a last-round valuation of $10B is carried at that price regardless of when (or whether) a liquidity event arrives. A fund can show a spectacular TVPI for years while LPs wait for DPI to materialize. The 2021–22 vintage illustrated this vividly: markups soared in 2021, then round prices fell in 2022–24, compressing TVPIs while DPI remained thin.

> **The two IPO globals — ★G53 (the VC/PE exit lens) vs. ★G102 (the bank's issuer/process lens).**
> Both globals involve the same event — a private company listing publicly — but they capture different vantage points. ★G53 (contributed by PE, home in PE Z4) is the *realization event*: the moment the fund begins converting its equity stake into public shares it can distribute or sell. ★G102 (contributed by IB, home in IB Z2) is the *issuance process*: how the bank prices and markets new shares, the roadshow, the book-build, the pricing. VC inherits both. For a venture-backed company going public, G53 is the founder's and VC's exit calculation; G102 is the bank's transaction; Equity Research (ER Z1.10) then covers the newly public stock.

> **The liquidation-preference stack (★G38) at a strong exit vs. a down exit — invisible vs. decisive.**
> The liquidation preference (★G38) grants preferred shareholders the right to be paid back their investment (typically 1×, sometimes with participation) before common holders receive anything. In a strong exit — say, a $2B acquisition of a company that raised $50M across five rounds — every preferred series converts to common, because the exit value is so large that all preferred holders do better as common. The stack is invisible. In a weak or down exit — say, a $40M acquisition of that same company — the $50M in aggregate liquidation preferences means common stockholders (founders, employees) receive nothing. The stack is everything. This is why preference terms that appear benign in a world of strong exits become devastating in a down scenario, and why Feld & Mendelson argue that entrepreneurs should analyze the term sheet across a wide range of exit values, not just the optimistic one.


---

# PART 2 · Zone 1 — The Venture Ecosystem

**What this zone is:** the foundational layer. What venture capital is, why the power law organizes everything about it, who the players are, how the fund is structured, and how it is measured. Most of this zone inherits from PE; it adds the venture-specific vantage and reframes the inherited infrastructure from the VC chair rather than the buyout chair.

**Learning sequence (canonical path):**
`What is VC? → The power law → Players: LPs, GPs, founders → VC vs. PE vs. growth equity → The fund structure (inherited) → Fund economics (inherited) → The J-curve in venture → The platform & partnership → Venture returns → Cross-module map.`

---

### Z1.1 · What Is Venture Capital? `[core]`

**Quick definition.** Venture capital is the financing of early-stage, high-risk, high-growth private companies in exchange for an equity stake, structured around the expectation that a handful of extraordinary winners will generate enough return to pay for many failures.

**Explainer covers.**
- The basic bargain: a VC provides capital (and often support) in exchange for an equity stake; neither the stake nor the capital is recovered until an exit, which may be years away.
- Why VC finances companies that cannot access debt: no cash flow, no collateral, uncertain survival — the opposite of what banks lend against.
- The risk/return profile: most VC-backed companies fail; the model survives because the winners can return 10×, 100×, or more on a single investment.
- VC as a subset of private equity broadly conceived: the same closed-end fund structure and LP/GP relationship (inherited from PE) but applied to earlier, smaller, higher-risk companies.
- Scale context: the US VC industry invests roughly $60–100B annually — a tiny fraction of global financial markets — yet the venture-backed companies it has produced (Apple, Google, Amazon, Facebook, Cisco) account for a disproportionate share of public-market value and R&D.

**Connects to.** ★G201 (the power law, the reason VC works this way), Z1.2, Z1.4 (VC vs. PE), Z1.5 (fund structure), ★G6 GP, ★G7 LP, Z1.10 (cross-module map), PE Z1.1.

---

### Z1.2 · The Power Law — Venture's Organizing Logic `[core]` `★ GLOBAL (G201)`

**Quick definition.** The venture return distribution in which a tiny number of investments produce nearly all of a fund's returns — the empirical law that dictates how VC is sourced, sized, and managed.

**Explainer covers.**
- The statistical shape: venture returns do not follow a normal (bell-curve) distribution. They follow a power-law (Pareto) distribution in which a small percentage of investments capture a large percentage of total returns. A single investment — Sequoia's Google stake, Accel's Facebook investment — can return more than an entire fund's invested capital.
- Why outliers dominate: in power-law environments, once a winner begins winning, success multiplies success (Mallaby's observation about Jeff Bezos walking out of the cinema — average wealth of remaining people plummets). Network effects, brand, talent attraction, and capital access all accelerate.
- The implication for practice: if a few investments make everything, VC must be practiced very differently from other investment disciplines. Missing the best deal matters more than avoiding the worst. A "bad" batting average (losing on 50% of investments) is acceptable — even expected — if the home runs are large enough. The goal is not a good batting average; it is "at-bats per home run."
- Why this single fact organizes everything: sourcing (see every deal, especially the best ones), ownership (hold enough of the winners), reserves (follow the winners with more capital), portfolio construction (size each bet as if it could return the fund), and exits (wait for the outsized outcome).
- The power-law curve applies not just within a single fund's portfolio but also across VC firms: a small set of top-quartile firms captures most of the industry's returns, and those firms' records tend to persist across fund cycles.

**Connects to.** Z4.3 (★G202, portfolio construction), Z3.2 (★G212, deal flow), Z1.9 (return metrics), PE (contrast — PE returns are more distributed), ★G115 (Fundamental Law of Active Management, the inverted version), AM Z5.x (manager selection, ★G156).

---

### Z1.3 · The Players: LPs, GPs, Founders & the Startup `[core]`

**Quick definition.** The venture ecosystem runs on LPs who fund the GPs who back the founders who build the startups — four actors bound by overlapping, sometimes diverging, incentives.

**Explainer covers.**
- Reuse ★G6 (GP) and ★G7 (LP): the same legal relationship as PE, with the GP managing a closed-end fund on behalf of passive LPs.
- The founder as the central new actor: unlike PE, where management teams are hired or retained, the VC relationship is built around the *founding team* — the people who identified the problem, built the initial product, and are asking a VC to bet on their judgment.
- Who LPs are in VC: university endowments (Yale, Stanford, MIT), foundations, pension funds, sovereign wealth funds, family offices, and funds-of-funds — the same LP base as PE, but with a higher tolerance for illiquidity and power-law risk (evidenced by Yale's 16% allocation to VC vs. 5% average, per Kupor).
- The syndicate: most rounds involve a lead investor (who sets terms and takes a board seat) plus co-investors (who participate at the lead's terms). The syndicate assembles quickly in competitive rounds.
- The four-actor tension: LPs want DPI (realized cash); GPs want TVPI (markups that support the next fundraise); founders want to keep building; employees want liquidity. These interests diverge in slow-exit environments.

**Connects to.** ★G6, ★G7, Z1.5, Z1.6, Z3.3 (★G213, the founder bet), ★G156 (manager selection, the LP's view), PE Z1.3, WM Z3.x.

---

### Z1.4 · VC vs. PE vs. Growth Equity vs. Angel `[core]` `[branch]`

**Quick definition.** Venture buys minority stakes in unprofitable high-growth companies using equity alone, while PE buys controlling stakes in mature, cash-generative businesses often using leverage — the two most important private capital strategies, and the most commonly conflated.

**Explainer covers.**
- The deal spectrum by company maturity: angel/seed (idea + founder) → early venture (product, pre-revenue) → growth equity (revenue, not yet profitable) → buyout (mature, profitable, cash-generative).
- Minority vs. control: VCs almost always hold minority stakes and influence through board seats and protective provisions (★G211); PE buyout funds almost always hold majority stakes and control through board domination. This is the single biggest structural difference.
- Leverage: PE buyouts are powered by debt (★G29, ★G33) amplifying equity returns; VC is almost entirely equity financed at the portfolio-company level (no cash flow to service debt).
- Return construction: PE returns are driven by multiple expansion, leverage, and operational improvement across a diversified portfolio; VC returns are driven by the power law (G201) — the math is different enough that the same word ("private equity") causes persistent confusion.
- Growth equity sits in between: it takes minority stakes in companies that have reached revenue but not yet profitability, typically without leverage; it shares features of both. The spectrum is a continuum, not a set of hard-edged boxes.

**Connects to.** PE Z1.1, Z1.2 (G201), Z2.7 (G215, crossover), ★G83 (sell-side vs. buy-side), ★G29, ★G33, AM Z2.x.

---

### Z1.5 · The Venture Fund Structure (inherited from PE) `[core]`

**Quick definition.** A venture fund is the same closed-end, ten-year limited-partnership vehicle as a PE fund — raising committed capital it draws down as it invests and returns over its life — with venture-specific nuances in scale and timing.

**Explainer covers.**
- The LP/GP structure: reuse ★G6 (GP), ★G7 (LP), ★G19 (blind pool), ★G20 (LPA), ★G15 (capital call), ★G16 (committed/contributed capital), ★G18 (vintage year), ★G21 (investment period).
- The ten-year life with the investment period (typically years 1–5, when new investments are made) and the harvest period (years 5–10, when holdings are managed and exited). Extensions of one to two years are common and more frequent in venture than PE, because startup exits take longer.
- The venture nuance on fund size: VC funds are typically smaller than PE buyout funds (micro-VCs at $10–50M; institutional seed funds at $50–200M; traditional Series A funds at $200–700M; crossover/multistage funds at $1B+). Smaller funds make more of them and diversify more bets.
- Capital calls in venture: called as the GP identifies opportunities and makes investments, usually over the first three to four years. Not called all at once because idle cash drags returns (★G4 J-curve logic).
- The blind-pool principle (★G19): LPs commit to the fund before knowing which companies will be invested in, trusting the GP's mandate.

**Connects to.** ★G6, ★G7, ★G19, ★G20, ★G15, ★G16, ★G18, ★G21, Z1.6, Z1.7 (J-curve), Z5.5 (raising the next fund), PE Z1.2–Z1.18.

---

### Z1.6 · Fund Economics: Carry, Fees & GP Commitment (inherited) `[core]`

**Quick definition.** Venture funds run on the same "2 and 20" economics as PE funds — roughly 2% annual management fee and 20% carried interest — but the power law means that carry from a single portfolio company can dwarf management fees across an entire fund's life.

**Explainer covers.**
- Reuse ★G9 ("2 and 20"), ★G10 (carried interest), ★G8 (management fee), ★G23 (GP commitment/"skin in the game"), ★G12 (hurdle/preferred return), ★G13 (catch-up), ★G14 (clawback), ★G11 (distribution waterfall).
- The management fee in venture: charged on committed capital during the investment period, often stepping down to invested capital in the harvest period. For a $500M fund, the management fee stream over ten years might total $70–90M — meaningful, but dwarfed by carry if the fund generates 3× net.
- Why carry dominates in venture: unlike PE, where carry is spread across many medium-sized wins, venture carry concentrates in the handful of power-law outcomes. A VC firm's carry from one investment in one fund can exceed the management fees earned across the firm's entire history. This is why VC professionals are willing to tolerate lower salaries than banking peers — they're buying lottery tickets on the best companies in the world.
- GP commitment (★G23): typically 1–5% of the fund, demonstrating conviction and aligning interests with LPs. In a $500M fund, a 2% GP commitment is $10M — real skin in the game.
- The waterfall (★G11): same contractual priority-of-distributions structure as PE. European (whole-fund) waterfalls are more common in venture than American deal-by-deal.

**Connects to.** PE Z1.10–Z1.17, ★G9, ★G10, ★G8, ★G23, ★G12, ★G13, ★G14, ★G11, Z1.2 (why carry matters so much in venture).

---

### Z1.7 · The J-Curve in Venture (inherited) `[core]`

**Quick definition.** The venture J-curve is deeper and longer than PE's — more early failures and exits 8–12+ years out — and the markup convention (G203) makes the *reported* curve look shallower than the *cash* curve until exits materialize.

**Explainer covers.**
- Reuse ★G4 (J-curve): the negative-then-positive net-cash-flow shape that all closed-end fund LPs experience, as management fees and early losses dominate before exits return capital.
- Why venture's J is deeper: a higher fraction of investments go to zero or near-zero in venture than in PE buyouts, pushing the trough lower. Seed and Series A failures are common and expected (part of the model).
- Why venture's J is longer: startups take a long time — often 8–12 years from founding to a liquidity event — compared with PE's typical 5–7 year hold. The harvest phase is pushed further right.
- The markup complication (G203): portfolio companies are marked at their last round price, creating paper TVPI gains that appear before any cash is realized. A fund can look like it's performing well (TVPI rising) while the J-curve in cash terms (DPI) remains negative for years. This is the deepest source of LP anxiety in venture.
- The implication for pacing: LPs who want to invest continuously in VC must tolerate long periods of negative J-curve before earlier-vintage funds begin to generate distributions.

**Connects to.** PE Z1.18 (★G4), Z4.5 (★G203, the markup), Z5.4 (DPI vs. TVPI), ★G1/G2/G3 (return metrics), AM Z5.x, WM Z3.x.

---

### Z1.8 · The Venture Platform & the Partnership `[core]` `★ GLOBAL (G216)`

**Quick definition.** The VC firm as institution — the partnership structure, its principals, scouts, and platform team that source, win, and support deals beyond the check itself.

**Explainer covers.**
- The partnership structure: general partners (GPs, senior decision-makers), principals/vice-presidents (deal-sourcing, diligence, board support), associates/analysts, and the growing category of "platform" employees who do not invest.
- The platform as competitive moat: at large firms like Andreessen Horowitz (described extensively in Kupor), the platform team provides portfolio companies with recruiting assistance, business development introductions, PR/communications support, and access to a network of potential customers, partners, and future employees. The platform is itself a sourcing edge — founders choose the firm partly for what it does beyond the check.
- Scouts: a network of trusted individuals (often founders or operators) who receive small amounts of capital to invest in early-stage companies in exchange for a carry share; they extend the firm's sourcing reach into networks the GPs don't personally access.
- The partnership decision-making process: investment committee (IC) structures vary, ranging from consensus-required to individual GP discretion; unanimous IC approval can kill contrarian bets.
- The brand as a compounding asset: a firm's track record signals quality to founders, employees, and LPs, creating a positive feedback loop (signaling → better deal flow → better returns → stronger brand → repeat). Mallaby documents this dynamic extensively in the histories of Sequoia and Kleiner Perkins.

**Connects to.** Z5.5 (raising the next fund), Z3.2 (★G212, deal flow as a sourcing advantage), PE Z5.1 (the GP franchise), AM Z5.x, ★G156.

---

### Z1.9 · Venture Returns: IRR, MOIC, DPI/TVPI (inherited) `[core]`

**Quick definition.** Venture funds are judged on the same return metrics as PE funds, but the power-law return distribution gives those metrics a distinctive shape — extreme dispersion, late realization, and a persistent gap between paper and cash.

**Explainer covers.**
- Reuse ★G1 (IRR), ★G2 (MOIC), ★G3 (DPI/RVPI/TVPI): the three return languages common to all private funds.
- The power-law shape in fund returns: venture fund returns are more dispersed than any other asset class. Kupor cites data showing median ten-year VC returns are 160 basis points *below* Nasdaq — meaning the average VC investor would have been better off in an index fund. But top-quartile returns are dramatically higher. In Yale's portfolio, VC has returned roughly 18% annualized over ten years and 77% over twenty years (a dot-com-era effect). Dispersion across funds dwarfs dispersion within funds.
- Why manager selection (★G156) is more important in VC than anywhere: because top-quartile returns persist (the same firms that win tend to keep winning, per Kupor), and because the gap between top- and bottom-quartile is so large (as much as 3,000 basis points, per Kupor), picking the right GP is the most important decision an LP can make. This is the most persistence-driven asset class in finance.
- The DPI/TVPI tension (G203): because venture markups are carried at last-round price, TVPI rises with every new up-round but DPI accumulates only when exits close. A fund can show 2.5× TVPI and 0.2× DPI for years.

**Connects to.** ★G1, ★G2, ★G3, Z1.2 (G201, the power law shapes the return distribution), Z4.5 (★G203, the markup), Z5.4, Z5.5, ★G156 (manager selection), PE Z5.10.

---

### Z1.10 · Where Venture Capital Sits — The Cross-Module Map `[core]`

**Quick definition.** Venture is the headwaters of the corporate lifecycle — it finances the companies that eventually IPO, become covered by equity research, and are held in public investors' portfolios — and its sibling relationship to PE is the densest inheritance link in the series.

**Explainer covers.**
- VC as headwaters: the companies venture funds back at the seed stage eventually (if successful) raise growth rounds, prepare for an IPO (★G102, IB's process), list on public markets, receive sell-side equity research coverage (ER Z1.10), and are owned by public market fund managers (AM/HF). The entire public-markets ecosystem inherits from venture's output.
- VC as PE's sibling: the two closest modules in the series. Both use the same closed-end LP/GP fund structure, the same economic terms (carry, fees, waterfall), and a substantial overlap in deal-mechanics vocabulary (term sheet, cap table, liquidation preference, anti-dilution). The differences are control vs. minority, leverage vs. equity-only, and power-law vs. diversified-portfolio return logic.
- VC as an LP's alternative allocation (AM/WM view): for asset managers and wealth managers, VC is an illiquid alternative allocation where the expected return (if the right managers are selected) is high but the dispersion is extreme and the J-curve is long. The LP's framework (★G156) for selecting VC managers is the bridge node.
- VC and the public/private blur (G215): in the 2010s and 2020s, the lines between venture and public markets blurred as hedge funds and mutual funds crossed into late-stage private rounds, creating a zone (crossover investing, G215) that the VC module maps at Z2.7 and that HF and AM modules reference.

**Connects to.** PE Z1.x, IB Z2.8, ER Z1.10, AM Z2.x, HF Z3.x, WM Z3.x, ★G53 (exit), ★G102 (the bank's IPO), Z2.7 (★G215).


---

# PART 3 · Zone 2 — Stages & Types

**What this zone is:** venture sorted by the stage of the company being financed and the type of firm doing the financing. The funding stages (G204) are the organizing spine; everything else is a branch off that spine.

**Learning sequence:** `The funding round sequence → Pre-seed & seed → Series A/B → Series C & growth → Angels & micro-VCs → Multistage platforms → Crossover → Sector/thesis lens.`

---

### Z2.1 · The Funding Stages & the Round `[process]` `★ GLOBAL (G204)`

**Quick definition.** The sequence of discrete financing events — pre-seed → seed → Series A → Series B → Series C → growth — each designed to fund the company to its next value-creating milestone and priced to reflect how much has been de-risked since the last round.

**Explainer covers.**
- The milestone logic: each round is sized to buy the company enough time (runway, G214) to reach a specific milestone — usually proof of team, then product, then product-market fit, then repeatable growth, then scale. The milestone achieved de-risks the company and justifies a higher valuation at the next round.
- The dilution treadmill: each round issues new shares, diluting all prior holders. Founders who start at 100% ownership typically hold 10–20% by IPO after five or six rounds. This is expected and acceptable if the company is worth vastly more.
- Round sizing: pre-seed ($100K–$2M), seed ($1–5M), Series A ($5–20M), Series B ($15–50M), Series C ($30–100M+), growth ($100M+). These ranges have inflated significantly since 2010 and compressed in 2022–24. *GAP / recency: round sizing figures are from the pre-2021 environment; the post-reset landscape is different.*
- The pricing event vs. the deferred instrument: most seed rounds and many pre-seed rounds use SAFEs or convertible notes (G206) to avoid setting a price; Series A and beyond are almost always priced rounds that set a valuation (G205), issue preferred stock (★G37), and generate a cap table (★G40).
- The financing treadmill risk: a company that raises on an optimistic round-price assumption must perform well enough to justify an up-round at the next raise. Missing the milestone — raising a flat or down round (G210) — damages the cap table and morale.

**Connects to.** Z2.2–Z2.4 (stage details), Z3.11 (G206, SAFEs/notes), Z3.7 (G205, pre/post-money), Z4.6 (G214, burn/runway), ★G40, ★G37, ★G42.

---

### Z2.2 · Pre-Seed & Seed: The Earliest Capital `[branch]`

**Quick definition.** The earliest institutional or near-institutional capital, funding a team and an idea toward initial product and first customers, often on SAFEs or convertible notes rather than priced rounds.

**Explainer covers.**
- What is being funded: the team (★G213, the founder bet) and an idea; there may be an MVP but almost never meaningful revenue. The bet is almost entirely on people and market.
- Who invests: angels (high-net-worth individuals investing personal capital), micro-VCs (small professional funds, typically $10–100M), accelerators (Y Combinator, Techstars — provide small checks plus structured mentorship in exchange for equity), and occasionally traditional VCs writing small checks.
- The instrument: most pre-seed and seed rounds use SAFEs (G206) or convertible notes (G206) because valuation negotiation at the idea stage is premature and can damage the relationship. A cap and discount are set instead of a price.
- The failure rate: seed-stage investments fail at the highest rate in the venture lifecycle — 50–70% return nothing. This is not dysfunction; it is the expected cost of funding a large enough sample of early bets to find the power-law winners.
- Check sizes: typically $25K–$2M per investor at pre-seed, $500K–$5M at seed.

**Connects to.** Z3.11 (G206, the SAFE), Z2.5 (angels/micro-VCs), Z3.3 (G213, the founder bet), Z2.1 (G204, the funding stages), ★G1/G2 (at this stage, impossible to compute — noted at depth layer).

---

### Z2.3 · Series A & B: The Classic Venture Round `[branch]`

**Quick definition.** The first and second priced institutional rounds, in which a lead VC sets a valuation, negotiates a full term sheet, takes a board seat, and backs a company that has demonstrated enough evidence to price its equity.

**Explainer covers.**
- The priced round: unlike seed, Series A is a full negotiated financing — pre-money valuation (G205), option pool expansion (G207), liquidation preference (★G38), board seat (G211), protective provisions (G211), anti-dilution provision (★G39). Feld & Mendelson's *Venture Deals* is the guide to every term.
- The lead investor: the firm that sets the terms, commits the largest check, and takes the board seat. Other investors participate at the lead's terms (the syndicate). Finding the lead is the most important fundraising task.
- What Series A evidence looks like: product built, early users or customers, some signal of product-market fit, a clear thesis for how the market is large enough (★G201 and the market-size requirement).
- Series B: typically larger, used to scale a business model that has already been proven at Series A. The lead may be the existing VC doubling down (following its pro-rata right, G209) or a new, later-stage firm.
- The time between seed and Series A: often 12–24 months. Companies that cannot raise a Series A ("die in the Series A crunch") are a recurring feature of the venture landscape. *GAP: the 2022–24 Series A crunch was severe by historical standards; no source covers it.*

**Connects to.** Z3.6 (★G46, the term sheet), Z4.2 (G211, board/governance), Z3.7 (G205, pre/post-money), Z3.9 (G207, option pool), ★G38, ★G39.

---

### Z2.4 · Series C & Growth Rounds: Scaling the Business `[branch]`

**Quick definition.** Later, larger rounds that fund the scaling of a proven business model, taken at higher valuations with lower risk, increasingly involving crossover capital from public-market investors.

**Explainer covers.**
- What is being funded: scaling the go-to-market, expanding into new geographies or products, building the management team that will lead the company to an eventual exit. The business model works; the question is how big it can get.
- Valuation dynamics: Series C+ companies are valued on metrics closer to public-company multiples (revenue, ARR, EBITDA growth) than on pure team-and-market judgment. The gap between the approaches to valuation at seed vs. Series C is significant.
- Crossover investors entering: at later stages, hedge funds (★G215) and mutual funds begin to participate in private rounds, providing larger checks but applying public-market return expectations. The 2020–21 surge of crossover capital into late-stage venture created a wave of unicorns ($1B+ private valuations) that struggled in the post-2021 environment.
- The unicorn threshold: "unicorn" (company with $1B+ private valuation) became a meaningful concept from roughly 2012; by 2021 there were hundreds. The term has lost some precision. *GAP / recency: the 2021–24 cycle dramatically altered what Series C and growth rounds look like; sources predate it.*

**Connects to.** Z2.7 (G215, crossover), Z5.2 (exit routes), IB Z2.8 (the IPO, the natural next step), ★G102, ★G27 (valuation multiples, now relevant).

---

### Z2.5 · Branch: Angel Investors & Micro-VC `[branch]`

**Quick definition.** Individual angels and small specialized funds that provide the earliest capital to startups, before or alongside institutional venture, often operating within personal networks and using higher-risk/higher-failure-rate economics.

**Explainer covers.**
- The angel: a high-net-worth individual — often a successful entrepreneur or operator — investing personal capital in early-stage companies. Angels may provide the first $25K–$500K into a company, before any institutional VC has looked.
- The micro-VC / nano-fund: small professional funds ($10–100M), often focused on a specific sector, geography, or founder community. Raised from institutional and high-net-worth LPs; make many small, early bets.
- Rolling funds: an innovation (prominent since ~2018) in which the GP raises capital on a rolling annual or quarterly basis from a subscriber base, rather than a traditional fixed-close fund. Allows continuous deployment but complicates vintage benchmarking.
- Scouts: a formal VC firm may extend its sourcing reach by providing capital to trusted individuals (often founders) to invest as "scouts," in exchange for a share of carry. A scout who discovers the next Airbnb gets paid; the firm gets access to a deal it wouldn't have seen.
- The risk profile: angels and micro-VCs have even higher failure rates than institutional venture, because they invest earlier with less evidence. Returns are correspondingly more power-law-skewed: a few early bets on Google, Twitter, or Uber defined angel fortunes.

**Connects to.** Z2.2 (the pre-seed/seed stage), Z3.2 (G212, deal flow), Z1.8 (G216, scouts as a firm strategy), Z2.1 (G204, the funding stages).

---

### Z2.6 · Branch: Multistage & Platform Funds `[branch]`

**Quick definition.** Large venture firms that invest at every stage — from seed through growth — out of large flagship funds, competing on brand, platform, and the ability to follow winners with very large checks.

**Explainer covers.**
- The multistage model: a firm like Andreessen Horowitz, Sequoia, or Accel invests at seed (small checks, establishing relationship), Series A, B, C, and growth (large checks, exercising pro-rata and follow-on rights). The goal is to own a meaningful stake in a winner from the earliest stage through exit.
- Fund size implications: large multistage funds ($1–15B+) must find companies capable of returning the entire fund (G202) — which means they need to target companies that can reach $5–15B+ valuations. This constrains what multistage funds can responsibly do at seed.
- The platform advantage: described in Z1.8 (G216), large firms offer founders recruiting, BD, PR, and network resources beyond capital. This is the explicit rationale for the platform model (Kupor documents a16z's platform team extensively).
- Concentration risk: large funds making large bets at every stage have high exposure to the same companies across multiple fund vintages. If a portfolio company underperforms dramatically, multiple funds can be marked down simultaneously.

**Connects to.** Z1.8 (G216, the platform), Z2.1 (G204, stages), Z4.4 (G209, follow-on and pro-rata), ★G202, ★G156.

---

### Z2.7 · Branch: Crossover & Growth-Stage Investing `[branch]` `★ GLOBAL (G215)`

**Quick definition.** Late-stage pre-IPO venture in which public-market investors — hedge funds and mutual funds — cross into private financing rounds, blurring the boundary between private and public capital.

**Explainer covers.**
- What crossover is: a hedge fund or long-only mutual fund (Tiger Global being the canonical example) makes an equity investment in a private company, often at Series C or later, expecting to hold through the IPO and into the public stock. The investment is at the intersection of the VC and public-market worlds.
- Why public investors cross over: they have access to large pools of capital, can move quickly, apply public-market valuation methodologies (revenue multiples, comps), and want earlier exposure to companies before they go public — and before the IPO premium is captured by others.
- The 2020–21 surge and the 2022–24 reversal: the crossover boom inflated late-stage private valuations dramatically; when public-market multiples compressed in 2022 (rising rates, risk-off environment), crossover investors withdrew rapidly, contributing to the private market valuation reset and the exit drought. *GAP / recency: the post-2021 crossover retreat is the largest source gap in this zone; no source covers it.*
- The blur: when hedge funds and mutual funds own large private positions, the distinction between public and private markets partially dissolves. Portfolio managers with both public and private holdings face mark-to-market complexity; their LPs face unexpected illiquidity.
- The link to ER: publicly covered stocks of crossover-funded companies provide the comps that crossover investors use to value the private round; the two valuation disciplines converge.

**Connects to.** HF Z3.x, AM Z2.x, ER Z1.10 (the public side), ★G102 (the IPO the crossover investor is betting on), ★G27 (valuation multiples).

---

### Z2.8 · The Sector & Thesis Lens `[branch]`

**Quick definition.** Venture firms specialize by sector — software, biotech, fintech, deep tech, AI — and invest from an explicit thesis about where in the technology landscape the next power-law outcomes will occur.

**Explainer covers.**
- Sector specialization: a generalist early-stage VC sees many industries; a specialist fund (biotech VC, fintech-focused fund, climate-tech fund) trades breadth for depth and can diligence companies more quickly and with more domain insight.
- The investment thesis (★G121): a VC firm's thesis is its structured argument for why a specific set of markets or technologies is about to produce venture-scale companies. It determines what deals the firm sees, how it evaluates them, and what support it can offer portfolio companies.
- Thesis-driven vs. opportunistic sourcing: thesis-driven firms proactively build relationships in their target sector before companies are even seeking capital; opportunistic firms respond to what comes through the door. The power law (G201) argues for thesis-driven sourcing — seeing the *best* deals in a category before everyone else sees them.
- AI as the current dominant thesis: as of 2022–24, the dominant venture investment thesis is the application of large language models and AI broadly across every sector. This has attracted both a wave of new companies and an enormous influx of capital. *GAP / recency: AI's role as both the dominant venture investment thesis and a tool reshaping company-building and diligence is the largest recency gap in this module; none of the sources cover it.*

**Connects to.** ★G121 (investment thesis), Z3.2 (G212, deal flow and sourcing), ★G201, Z2.1 (G204).


---

# PART 4 · Zone 3 — The Investment Process

**What this zone is:** the venture deal from funnel to close — the densest zone in the module. Feld & Mendelson (*Venture Deals*) is the primary source for the term-sheet mechanics; Kupor (*Secrets of Sand Hill Road*) provides the VC's evaluative framework for team, product, and market.

**Learning sequence:** `Overview → Deal flow → The founder bet → Market/product evaluation → Diligence → Term sheet overview → Pre/post-money → The cap table → Option pool → Economic terms (liq pref) → The SAFE/note → The 409A.`

---

### Z3.1 · The Venture Process Overview `[process]`

**Quick definition.** The venture investment process runs sourcing → selection → diligence → term sheet → structuring → close, shaped at every step by the power law's demand for picking the rare company capable of an outsized outcome.

**Explainer covers.**
- The funnel shape: a firm may see thousands of companies per year and invest in a handful. The funnel is very wide at the top (cold inbound, warm intro, conference, scout network) and very narrow at the bottom (check written, board seat taken).
- How the power law reshapes process: the standard investment discipline of "minimize downside" partially inverts in venture. The worst investment mistake is not making a bad bet on a loser (you lose the check); it is failing to back a winner (you lose the entire asymmetric upside). So the VC's error function is asymmetric: false positives (investing in a loser) are survivable; false negatives (passing on the next Google) are career-defining failures.
- Speed vs. diligence: competitive rounds, especially at seed, can close in days. Later-stage rounds take weeks to months. Speed-diligence trade-off is an active tension.
- The steps:
  1. **Sourcing** (Z3.2) — generating and accessing deal flow.
  2. **Selection** (Z3.3, Z3.4) — screening on team, product, market.
  3. **Diligence** (Z3.5) — evidence-gathering before term sheet.
  4. **Term sheet** (Z3.6) — economic and control terms.
  5. **Structuring** (Z3.7–Z3.12) — cap table, option pool, instruments.
  6. **Close** — legal documentation and funding.

**Connects to.** Z3.2 → Z3.12, Z1.2 (G201, the power law shapes the process), Z4.1 (post-close).

---

### Z3.2 · Deal Flow & Sourcing `[process]` `★ GLOBAL (G212)`

**Quick definition.** The top of the venture funnel — generating and accessing investable opportunities — where the power law makes *seeing* the best deals as decisive as picking well among average ones.

**Explainer covers.**
- Why sourcing is existential: if the power law is true (a few companies produce almost all the returns), then missing the best deals is the primary risk. The VC who never saw Google or Facebook couldn't have invested, regardless of skill. Sourcing is not just operational; it is competitive.
- The sourcing channels: warm introductions from trusted founders and operators; proprietary networks built through content, events, and thought leadership; platform advantages (Z1.8, G216); scout networks; accelerator relationships (YC, Techstars); cold inbound (less useful; most top firms don't invest heavily from cold inbound alone).
- Proprietary vs. competitive: proprietary deal flow — seeing and winning a deal before others — is the VC's most valuable operational advantage. It comes from reputation, relationship depth, and platform resources.
- The signal problem: at early stages, there are few objective metrics to assess deal quality. Investors rely heavily on signal-from-referral (who is recommending this founder?) and signal-from-credibility (does this founder have a track record?). Both signals are imperfect and systematically biased toward familiar networks.
- The power-law argument for sourcing discipline: because the return on missing the best deal (a zero return, versus a 100× return) is so asymmetric, a VC who wants to invest in the best companies should invest time and reputation in being the first call for the best founders, not in developing a better filter for average deals.

**Connects to.** Z1.9, Z2.1, Z3.3, Z1.8 (G216, platform as sourcing edge), ★G201 (the power law as the reason sourcing is decisive).

---

### Z3.3 · The Founder Bet `[core]` `★ GLOBAL (G213)`

**Quick definition.** Underwriting the team over the financials at the earliest stages — "the jockey, not the horse" — as the central and often dominant judgment of early-stage venture investing.

**Explainer covers.**
- Why team dominates early: at the seed and Series A stage, there are no financials to model, no proven product-market fit, and often no revenue. The VC is buying the founder's judgment, resilience, and ability to attract talent and capital. The business plan will change; the person executing it matters most.
- Founder-market fit (Kupor's concept): the specific link between this founder's background, experience, and insight and the market problem she is attacking. The most defensible founders are those for whom this particular idea is not just plausible but *inevitable* given their biography — Martin Casado inventing software-defined networking because his entire career led there.
- The founder evaluation framework (Kupor): three axes — people (track record, unique insight, leadership and recruiting ability, the will to walk through walls), product (whether the product will be 10× better or cheaper than existing solutions, not merely marginally better), and market (is the TAM large enough to sustain a power-law outcome?).
- "Egomaniacal" vs. "strong convictions weakly held": founders need sufficient self-belief to ignore the inevitable stream of doubters, but must also incorporate market feedback and pivot. The combination — conviction + adaptability — is the hardest combination to identify in advance.
- The jockey/horse tension: investing in a great team in a small market is a canonical VC mistake. The founder bet requires a believable large market too.

**Connects to.** ★G121 (variant perception — the founder has a non-consensus view of the market), Z3.4 (market and product evaluation), Z2.2, Mallaby (the history of founder bets) and Kupor (the evaluation framework) grounding.

---

### Z3.4 · Evaluating the Opportunity: Market, Product & Traction `[core]`

**Quick definition.** Alongside the founder assessment, the VC sizes the market (must be large enough to produce a power-law return), tests product-market fit, and reads the early traction metrics that signal whether the product is pulling customers or being pushed.

**Explainer covers.**
- Market size: the fundamental filter. A company that executes perfectly but in a small market cannot return a venture fund (G202). VCs require large addressable markets (TAM) — typically $1B+ to justify a Series A bet, much larger for later stages. Market size is hardest to estimate for genuinely new markets (the Airbnb case: did it expand the travel market or substitute for hotels?).
- Product-market fit: the state in which a product is so compelling to its target customers that they feel compelled to use it, return to it, and tell others. Evidence includes low churn, strong net promoter scores, organic growth, and customer retention curves that flatten (rather than decay). Paul Graham's characterization: "People are buying your product even though you have a buggy MVP and terrible customer service."
- Traction metrics by stage: at seed, evidence might be 100 active users or a single passionate customer cohort. At Series A, a VC might look for $100K–$500K ARR, strong growth rates (doubling monthly or better), and early cohort retention. At growth stage, revenue, growth rate, and unit economics matter.
- The 10× rule (Kupor): for a product to overcome customer inertia and institutional resistance, it typically needs to be 10× better or 10× cheaper than the current best alternative. Marginal improvements do not displace entrenched behavior.

**Connects to.** Z3.3 (the founder must be in a big enough market), Z3.2 (deal flow), Z4.6 (G214, burn and the runway-to-next-milestone), ★G201, G212.

---

### Z3.5 · Venture Due Diligence (inherited) `[core]`

**Quick definition.** Venture diligence is faster and lighter early-stage than PE diligence and heavier later, but follows the same evidence-gathering logic: verifying what the founder claims and identifying the risks that aren't in the pitch deck.

**Explainer covers.**
- Reuse ★G28 (due diligence): the same systematic investigation logic — financial, operational, legal, market — applied with different evidence sources and different time constraints.
- The speed tension: seed-stage rounds can close in a week; a VC that requires six months of diligence will lose the deal. Diligence depth scales with stage: seed is almost purely reference-based and conversation-based; growth-stage diligence is much closer to PE diligence with financial models, customer interviews, and legal review.
- Reference calls and founder background: at early stages, reference calls on the founder — from prior employers, co-founders, customers, and investors — are among the most valuable diligence inputs available.
- Customer and technical diligence: at Series B and beyond, a serious VC will call customers to verify usage, retention, and NPS claims, and may bring in a technical advisor to assess the engineering team's work.
- What diligence cannot answer: at early stages, no amount of diligence can tell you whether the product will find a market. This is why ★G213 (the founder bet) takes precedence over quantitative analysis at seed and Series A.

**Connects to.** ★G28 (the global, contributed by PE), Z3.4, Z3.6, PE Z3.x.

---

### Z3.6 · The Term Sheet (inherited, venture lens) `[core]`

**Quick definition.** The venture term sheet is the same non-binding document as in PE but splits into two buckets the founder must read together — economics (how the money is made) and control (who makes decisions) — and getting either wrong has lasting consequences.

**Explainer covers.**
- Reuse ★G46 (term sheet, contributed by PE): a non-binding document setting the headline terms of an investment. In venture, it is typically four to ten pages.
- The Feld & Mendelson organizing principle: the term sheet has only two things that actually matter — **economics** (valuation, option pool, liquidation preference, anti-dilution, pay-to-play) and **control** (board composition, protective provisions, drag-along). Everything else is a second-order term.
- Economic terms: set the price (G205), the option pool (G207), the liquidation preference and participation (★G38), the anti-dilution mechanism (★G39), vesting schedules, and pay-to-play provisions.
- Control terms: board composition (G211), protective provisions (G211, the veto rights), drag-along rights (★G43), information rights, right of first refusal.
- Founder-friendly vs. investor-friendly: the market cycle determines which side has more leverage. In a hot market, founders negotiate away board seats, eliminate liquidation preference participation, and set large pre-money valuations. In a down market, investors demand more protection and more control. The 2022 reset sharply shifted leverage back toward investors.

**Connects to.** ★G46, Z3.7 → Z3.12 (each key economic/control term in detail), Z4.2 (G211, governance), ★G38, ★G39, ★G43, Z1.2 (how the power law makes this the moment of maximum leverage for the VC if the deal is competitive).


### Z3.7 · Pre-Money & Post-Money Valuation `[core]` `★ GLOBAL (G205)`

**Quick definition.** The round-pricing identity (post-money = pre-money + new investment) that determines how much ownership new capital buys — the single most consequential arithmetic in a venture financing, and the source of the most common early negotiation miscommunication.

**Explainer covers.**
- The identity: post-money valuation = pre-money valuation + amount of new investment. New investor ownership % = new investment ÷ post-money. This is simple but routinely misunderstood.
- The verbal trap (Feld & Mendelson): when a VC says "I'll invest $5M at a $20M valuation," she almost always means $20M *post-money* — implying a $15M pre-money and 25% ownership. A founder who hears "$20M pre-money" calculates 20% dilution. The five-point gap is real and compounds through subsequent rounds.
- Why there is no model: at early stages, the pre-money valuation is negotiated, not derived from a DCF or from comps in any rigorous sense. There are no cash flows to discount. Comparables are loose. The number reflects market conditions, the GP's conviction, and the founder's leverage.
- The relationship to dilution (★G42): each round's pre-money sets the denominator that determines how much of the company each prior investor retains. A lower pre-money at any round shrinks prior holders' stakes.
- The relationship to the option pool (G207): the option pool expansion happens *inside* the pre-money, making the effective pre-money lower than the stated pre-money. This is the pre-money shuffle.

**Connects to.** ★G40 (cap table), ★G42 (dilution), Z3.8 (cap table mechanics), Z3.9 (G207, option pool shuffle), ★G205. Cross-module: PE Z2.x uses the pre/post identity too (★G41 in PE, which covers the same concept from the buyout side — venture is the dominant context for this arithmetic).

---

### Z3.8 · The Cap Table & Dilution (inherited, venture lens) `[core]`

**Quick definition.** The cap table is the evolving ledger of who owns what — shares, options, warrants, and ownership percentages — and each venture round dilutes existing holders pro-rata to make room for new capital.

**Explainer covers.**
- Reuse ★G40 (cap table, contributed by PE): the master ledger of equity ownership. In venture, the cap table grows dramatically more complex round over round, as each new series adds a new class of preferred stock with its own liquidation preference.
- The dilution mechanism (★G42): when new shares are issued, every existing holder's percentage ownership falls proportionally — this is dilution. If the company is worth more at each round, dilution is acceptable (you own less of a bigger pie). If the company is flat or down, dilution is damaging.
- Round-by-round evolution: at founding, the cap table is clean — founders hold common stock. After seed, a SAFE holder or note holder is added. After Series A, preferred Series A shares appear, with their own rights. After Series B, another preferred class. The table grows until the exit, when it determines the distribution (Z5.3).
- Founder dilution across stages: a typical founder starts at ~80% (the rest to a co-founder and initial employees), drops to ~60% after seed, ~45% after Series A, ~30% after Series B, ~20% by Series C. By IPO, founders may hold 10–20%. The dollar value of that stake can still be enormous if the company is worth $10B.
- SAFE mechanics in the cap table: SAFEs (G206) appear on the cap table only when they convert at the next priced round. Prior to conversion, they are not equity — but their conversion terms determine how much they will dilute existing holders.

**Connects to.** ★G40, ★G42, Z3.7 (G205, the pre/post-money sets the price), Z3.9 (G207, option pool), Z5.3 (exit waterfall).

---

### Z3.9 · The Option Pool & the Pre-Money Shuffle `[core]` `★ GLOBAL (G207)`

**Quick definition.** The employee equity reserve (ESOP), and the VC convention of requiring the option pool to be expanded *inside* the pre-money valuation — the "pre-money shuffle" — so that the dilution falls on existing shareholders rather than on new investors.

**Explainer covers.**
- The option pool: equity reserved for employees, advisors, and contractors, typically 10–20% of fully diluted shares at Series A. Options incentivize the team that will build the company between financing rounds.
- The shuffle mechanic (Feld & Mendelson): VCs typically insist that the option pool be expanded (or created) as part of the Series A *before* the new investment is priced. This means the option pool shares reduce the pre-money, not the post-money. Example: a $20M pre-money with a required 20% option pool that needs to be created from scratch effectively gives the founders a $16M pre-money (the 20% comes out of the existing holders). This reduces what founders were told they were getting.
- The negotiation: founders should understand the effective pre-money (pre-money minus the new-option-pool creation) and try to minimize the size of the option pool required at closing. VCs, conversely, want a large option pool so future hires don't require additional dilution before the next round.
- Issued vs. unissued options: Feld & Mendelson make explicit that the pool the VCs are discussing is *unissued* options — not the options already granted. Adding existing grants to the required pool is a trap to watch for.
- The 409A connection: the option pool determines how many options will be issued; the 409A valuation (G208) sets the strike price of those options.

**Connects to.** ★G42 (dilution), Z3.7 (G205, pre-money), Z3.8 (cap table), Z3.12 (G208, 409A). Source: *Venture Deals*, Chapter 5 (employee option pool section).

---

### Z3.10 · Economic Terms: Liquidation Preference & the Stack (inherited) `[core]`

**Quick definition.** The liquidation preference grants preferred shareholders their investment back (sometimes more) before common holders receive anything, and across multiple rounds these preferences stack into a structure that can dominate the exit outcome in weak scenarios.

**Explainer covers.**
- Reuse ★G38 (liquidation preference, contributed by PE) and ★G37 (preferred equity): the two globals that carry the core concept. In venture, preferred stock is the standard instrument for every priced round (G204).
- The two components (Feld & Mendelson, Chapter 5): the *preference* (how much preferred holders get back: typically 1×, meaning they recover their investment before common gets anything) and *participation* (do preferred holders also share in the remaining proceeds alongside common, after their preference is returned?). Non-participating preferred holders choose between taking their preference or converting to common; participating preferred holders take both.
- The multi-round stack: a company that has raised five priced rounds has five layers of preferred stock, each with its own liquidation preference. In a weak exit, the preferences are paid out in reverse chronological order (most recent first, in a senior/subordinate structure), and common holders — founders and employees — may receive nothing.
- Pay-to-play: a provision (Feld & Mendelson, Chapter 5) requiring existing investors to participate in a down round (G210) or lose some or all of their preferred-stock protections. Pay-to-play provisions are friendly to founders in difficult financings because they prevent investors from sitting on their preferences without supporting the company.
- When the stack is invisible vs. decisive: at a $2B exit for a company that raised $50M, every preferred series converts to common because the per-share value is so high. At a $40M exit for the same company, the $50M in preferences means common gets nothing. The disambiguation callout in Part 1 covers this.

**Connects to.** ★G38, ★G37, ★G39 (anti-dilution), Z5.3 (exit waterfall, where the stack resolves), Z4.7 (G210, the down round triggers the stack acutely).

---

### Z3.11 · The SAFE & the Convertible Note `[core]` `★ GLOBAL (G206)`

**Quick definition.** Early-stage instruments that accept an investor's money today and defer pricing to a future priced round, bridged by a valuation cap and/or a discount rate — the standard instruments of pre-seed and seed investing.

**Explainer covers.**
- The convertible note: a debt instrument with an interest rate, a maturity date (when the company must either repay or convert), a discount rate (the percentage below the next round's price at which the note converts), and often a valuation cap (the maximum valuation at which the note converts, regardless of how high the next round's pre-money is). It is debt until it converts; if the company fails before a priced round, noteholders are creditors.
- The SAFE (Simple Agreement for Future Equity, introduced by Y Combinator ~2013): similar economic terms (cap, discount) but not debt — no interest, no maturity. The investor receives no rights until conversion. SAFEs convert at the next priced round automatically. If the company fails, SAFE holders receive nothing because they are not creditors.
- The cap and discount bridge: a $1M SAFE with a $10M valuation cap will convert into as many shares as a $1M investment at $10M pre-money — *regardless* of what the Series A pre-money actually is. If the Series A is at $20M pre-money, the SAFE holder gets twice as many shares as someone investing $1M in the round at the round price. The cap protects early investors from having their early risk diluted away by a high subsequent round price.
- Why they exist: at pre-seed and seed, negotiating a full priced round (legal costs, valuation debate, preferred-stock terms) is disproportionately burdensome. SAFEs and notes are simple (a few pages), fast, and defer the hard conversation to when there is more information.
- The risk of stacking SAFEs: a company that raises multiple SAFEs before a priced round can find that the conversion at Series A creates substantial dilution for founders — all the SAFE holders convert at their capped prices and the resulting cap table can be surprising. This was a meaningful issue in 2020–22 for companies that raised large pre-seed and seed rounds on SAFEs.

**Connects to.** Z2.2 (seed stage, where SAFEs/notes are the norm), Z3.7 (G205, the priced round that SAFEs convert into), ★G205. Disambiguation: SAFE/note vs. priced round — covered in Part 1.

---

### Z3.12 · The 409A Valuation `[core]` `★ GLOBAL (G208)`

**Quick definition.** The independent third-party valuation of a private company's common stock required by the IRS under section 409A to set a fair-market-value strike price for employee stock options — and the reason the option strike price is always far below the preferred round price.

**Explainer covers.**
- Why it exists: IRS section 409A requires that options be granted at or above the fair market value of the underlying stock to avoid adverse tax treatment for the employee. If options are granted below fair market value, the holder owes taxes immediately on grant (not on exercise), plus penalties.
- Why common is worth far less than preferred: preferred stock carries liquidation preferences (★G38), conversion rights, and other protections that make it more valuable per share than common. The 409A valuation applies a discount to reflect the subordinate economic and control rights of common stock. A Series B preferred-stock round at a $500M post-money may yield a 409A common-stock value of $2–5 per share versus a preferred price of $10 per share.
- The independence requirement: 409A valuations must be conducted by a qualified, independent third-party appraiser. Common service providers include Carta and other cap-table-management platforms.
- Refresh cadence: companies typically refresh the 409A valuation every 12 months or after a material event (a new financing round, an M&A transaction, a significant change in business fundamentals). Options granted between a round close and the next 409A use the last 409A's common-stock value.
- The preferred/common gap and its effect on employee perception: employees who receive options priced at $1 per share while the company has a $50-per-share preferred round price may not intuitively understand the value of their equity. Communicating the gap — and what it means at various exit scenarios — is a governance and retention challenge.

**Connects to.** Z3.9 (G207, options are struck at the 409A price), Z3.7 (G205, the round price that the 409A sits below), Z3.10 (the preferred/common gap is the same economics as the liq-pref vs. common gap).


---

# PART 5 · Zone 4 — Portfolio & Value-Add

**What this zone is:** life after the check — the shift from picking to helping, the governance toolkit, portfolio construction logic, the company's survival clock, and the events (markups, down rounds) that reshape a portfolio's risk profile over time.

**Learning sequence:** `After the check → Board governance → Portfolio construction → Follow-on & reserves → The markup → Burn/runway → The down round.`

---

### Z4.1 · The Portfolio After the Check `[core]`

**Quick definition.** Once invested, the VC shifts from picking to helping — taking a board seat, providing strategic support, and accompanying the company through the long road to exit while monitoring whether the power-law bet is playing out.

**Explainer covers.**
- The pick-to-help transition: the investment decision is binary (invest or pass); the post-investment relationship is continuous. The VC's role changes from evaluator to partner, with a board seat (G211) as the formal mechanism.
- What "help" looks like: recruiting (the most common request from portfolio companies, per Kupor — VCs with large networks can open doors to executives, engineers, and early customers); strategic advice (framing the next round, navigating a pivot); business development (introductions to potential customers, partners, and acquirers); follow-on financing (exercising pro-rata rights and reserves, G209).
- The monitoring obligation: the VC also monitors. At each board meeting, she reviews financial performance against plan, headcount against budget, burn and runway (G214), and the company's progress toward the next financing milestone.
- The power law again: not all portfolio companies get the same time and attention. The best-performing companies attract the most support (and more capital via follow-on). This is rational given the power law — the few winners deserve the most help. The underperformers may be triage'd.
- The founder relationship: the VC-founder relationship can span 8–12 years. The quality of this relationship — built on trust and candor — often matters more than any specific tactical input.

**Connects to.** Z4.2 (G211, board/governance), Z5.1 (exit, the end of the relationship), Z1.8 (G216, platform support), Z4.4 (G209, follow-on), Z4.6 (G214, monitoring burn).

---

### Z4.2 · VC Governance: Board Seats, Information Rights & Protective Provisions `[core]` `★ GLOBAL (G211)`

**Quick definition.** The minority-investor control toolkit — influence exercised through board representation and veto rights rather than through the majority-control ownership of a buyout — the mechanism by which a VC shapes a company without owning it.

**Explainer covers.**
- The board of directors: a VC typically takes one board seat at Series A (often as part of a five-person board: two founders, two investors, one independent). The board seat is the formal channel for oversight, strategy, and — in extremis — management changes.
- Information rights: the contractual right (in the term sheet, Z3.6) to receive regular financial statements, board observer status, and access to audited financials. These rights matter most when things go wrong and the VC needs to monitor a company she doesn't control.
- Protective provisions (vetoes): contractual rights granted to preferred shareholders that require their consent before the company can take certain major actions — selling the company, issuing new securities, incurring debt above a threshold, changing the certificate of incorporation. These provisions let a minority investor block decisions that would damage its position.
- VC governance vs. PE control: the PE buyout investor owns a majority and decides; the VC minority investor persuades and vetoes. The critical consequence: a VC cannot force a founder to sell (unless drag-along rights apply, ★G43), cannot unilaterally replace the CEO (unless board dynamics allow it), and cannot set strategy over the founder's objection in most cases.
- The fiduciary complexity (Kupor, Chapter 13 — "In Trados We Trust"): board members owe fiduciary duties to all shareholders, including common holders (founders and employees). When a company is sold at a price that returns the preferred preferences but gives common nothing, board members face potential liability. The Trados case is the canonical VC governance cautionary tale.

**Connects to.** PE Z4.x (control contrast), Z3.6 (the term sheet provisions that create these rights), Z4.7 (G210, down round, where governance is tested), ★G43, ★G44.

---

### Z4.3 · Power-Law Portfolio Construction & the "Return-the-Fund" Test `[core]` `★ GLOBAL (G202)`

**Quick definition.** The discipline of building a portfolio in which every bet is sized and targeted to be capable of returning the entire fund on its own — using ownership targets rather than diversification to allocate capital.

**Explainer covers.**
- The return-the-fund test: for a $500M fund, each investment should have a plausible path to generating $500M+ in returns to the fund. This does not mean every investment will; it means that the analysis at the time of investment should make that outcome believable — otherwise the bet cannot be a power-law winner, and the VC is essentially making a diversified allocation that cannot justify the illiquidity or the fees.
- Ownership targets: the test is a function of ownership. If the VC needs a $500M return and the portfolio company is expected to be worth $2B at exit, the VC needs to own ~25% of the company at exit. This sets the minimum ownership target at investment, which in turn sets the check size relative to the round (you need to buy enough ownership to reach the target after dilution from future rounds).
- Portfolio concentration vs. diversification: this logic inverts the standard diversification argument. A VC running a $500M fund cannot afford to make fifty equal-sized $10M bets and call it diversification — no single investment can return the fund at $10M. The portfolio construction is concentrated in terms of conviction, even if there are many positions.
- The implication for follow-on: if the return-the-fund test passes at Series A, the VC should maintain ownership through subsequent rounds (pro-rata, G209) to ensure the stake hasn't been diluted away by the time the winner is worth enough to return the fund.
- The Fundamental Law of Active Management (★G115) — inverted: in quantitative and long-only active management, the Fundamental Law says returns scale with breadth (more bets × higher IC). Venture inverts this: the power law makes breadth a trap (spreading capital too thin can't produce fund-returners). Extreme low breadth + extreme high required skill-per-bet is the right framing.

**Connects to.** Z1.2 (★G201, the power law is the reason for this discipline), Z4.4 (G209, reserves and follow-on to maintain ownership), ★G115 (the Fundamental Law, inverted), HF Z3.2, AM Z4.x.

---

### Z4.4 · Pro-Rata Rights, Follow-On Strategy & Reserves `[core]` `★ GLOBAL (G209)`

**Quick definition.** The contractual right to invest in later rounds to maintain ownership percentage, combined with the fund-level discipline of reserving capital to double down on the portfolio's winners.

**Explainer covers.**
- Pro-rata rights: a contractual term (often in the original term sheet, Z3.6) giving a VC the right — but not the obligation — to invest in the company's next financing round at the same terms as new investors, in an amount sufficient to maintain its ownership percentage. Without pro-rata, every subsequent round dilutes the early investor.
- The reserve ratio: a fund's reserve ratio is the proportion of its committed capital set aside for follow-on investments (vs. new investments). Typical VC funds hold reserves of 50–70% of committed capital for follow-on into existing portfolio companies. The reserve allocation depends on the fund's strategy, stage focus, and expected company capital needs.
- The winners-only discipline: the key strategic decision is which companies to follow into subsequent rounds. A VC who follows every investment proportionally is not exercising judgment — they are passively maintaining dilution protection. The power law says: reserve your follow-on capital for the companies showing signs of being the rare winner. Doubling down on losers to recover cost is a trap.
- Reserves and fund timing: late-vintage investments (made in years 4–5 of the investment period) leave less time for the company to develop and require less reserve because there are fewer rounds remaining before the fund's harvest period. Kupor discusses this at length — for founders, understanding where the fund is in its lifecycle matters for predicting the VC's follow-on capacity.
- The pro-rata right and its market: in hot markets, pro-rata rights are often exercised and honored; in competitive rounds, companies sometimes exclude existing investors to add new strategic ones. The pro-rata right is a negotiated term, not an absolute guarantee.

**Connects to.** Z4.3 (G202, portfolio construction — reserves enable maintaining ownership in winners), ★G39 (anti-dilution is a different protection: adjusting price, not maintaining percentage), Z2.1 (G204, each new round triggers pro-rata considerations).

---

### Z4.5 · The Venture Markup & Mark-to-Market `[core]` `★ GLOBAL (G203)`

**Quick definition.** The convention of carrying a venture holding at its most recent round price, producing paper gains (TVPI) that may diverge sharply from realized cash (DPI) — the source of venture's distinctive reporting complexity and the reason "paper unicorn" and "realized returns" require separate tracking.

**Explainer covers.**
- The convention: when a VC-backed company raises a new round at a higher valuation, the VC marks up all its holdings in that company to the new price. A firm that invested $5M for 20% of a company that is now worth $500M (in a new round) marks its position to $100M — even if no shares have been sold.
- The paper vs. cash distinction (★G3): TVPI (total value to paid-in) counts both realized cash and marked-up unrealized holdings. DPI (distributions to paid-in) counts only realized cash. In PE, this gap is moderated by regular exits and audited valuations. In venture, the gap can be enormous: a fund with several "unicorn" holdings may show a 5× TVPI and a 0.1× DPI for years.
- Why markups matter to LPs: LPs report their portfolios to their own beneficiaries (university boards, pension fund trustees) using the marked-up valuations. A high TVPI is useful for reporting — but only DPI pays the university's operating budget. The 2021 vintage of VC funds saw massive TVPIs based on inflated late-stage round prices; when those companies' implied valuations collapsed in 2022–24, TVPIs compressed sharply.
- The markup game: critics argue that aggressive markups — carried at the most recent round price even when the company's trajectory has worsened — inflate apparent fund performance and assist in fundraising for subsequent funds. This is an incentive misalignment between the GP (who benefits from high TVPI for fundraising) and the LP (who needs DPI).
- Connecting to the J-curve (★G4): the markup convention makes the reported J-curve shallower than the cash J-curve. The trough is narrowed because marked-up positions look positive before any cash is returned. This can give LPs a false sense of how well the fund is doing in early years.

**Connects to.** Z1.7 (the J-curve), Z1.9 (return metrics), Z5.4 (DPI vs. TVPI at the fund level), ★G1/G2/G3, AM Z5.x (LPs use these marks).

---

### Z4.6 · Burn Rate & Runway `[core]` `★ GLOBAL (G214)`

**Quick definition.** The startup's cash-consumption rate and the number of months of survival that current cash buys — the company's clock, driving every financing decision, every milestone target, and every conversation with its board and investors.

**Explainer covers.**
- Burn rate defined: the net amount of cash a company spends each month — gross cash out minus any cash in from revenues. A pre-revenue company burning $300K/month has a gross burn equal to its net burn. A company with $100K of monthly revenue burning $400K gross has a net burn of $300K.
- Runway: burn rate ÷ cash on hand = months of runway (time to zero). A company with $3M in the bank burning $300K/month has 10 months of runway. This is the clock.
- Why runway to the *next milestone* matters more than runway to zero: a company that runs to zero is dead. But a company that raises its next round after a good milestone has a much better chance of survival than one that raises in desperation with three months left. The rule of thumb: start raising at 12–18 months of runway. By the time a round closes (typically 3–6 months), the company has 6–12 months left.
- The financing treadmill: if each new round buys only 12–18 months of runway, the company is perpetually on the treadmill — close a round, deploy, raise again. This is expected and normal; the question is whether each round's milestone justifies a higher valuation.
- Burn rate as a governance signal: the board (G211) monitors burn relative to plan. A company burning faster than planned without proportional progress is a warning signal that requires either a strategic change or an earlier-than-planned raise.
- The relationship to the down round (G210): a company that runs out of runway without achieving its next milestone must raise a flat or down round (G210), which is damaging to cap table and morale.

**Connects to.** Z2.1 (G204, runway determines when the next round must happen), Z3.4 (milestone achievement justifies a higher round price), Z4.7 (G210, what happens when burn exceeds plan), Z4.2 (G211, board monitors burn).

---

### Z4.7 · The Down Round & the Recap `[core]` `★ GLOBAL (G210)`

**Quick definition.** A financing priced below the prior round, triggering anti-dilution protections for existing preferred holders, potentially reordering the liquidation-preference stack, and damaging morale and the cap table simultaneously — venture's most painful event.

**Explainer covers.**
- Definition: a round in which the pre-money valuation (G205) is lower than the post-money valuation of the previous round. If a company raised a Series B at a $200M post-money and now raises a Series C at a $150M pre-money, that is a down round.
- Anti-dilution triggers (★G39): most preferred stock includes anti-dilution protection — when a down round occurs, the formula (weighted-average, or in extreme cases full-ratchet) adjusts earlier investors' effective price per share downward, issuing them additional shares. This protects their percentage ownership but further dilutes common holders (founders, employees).
- The preference stack reordering: new investors in a down round typically demand senior liquidation preferences (ahead of existing preferred series), further subordinating common holders. The cap table in a down round often leaves founders with little or no value in all but the most optimistic exit scenarios.
- Pay-to-play provisions (★G38 context): if the company included pay-to-play in its prior term sheets (Z3.10), investors who don't participate in the down round may lose some or all of their anti-dilution protections and convert from preferred to common — a forced conversion that can rebalance the cap table.
- Human consequences: down rounds are demoralizing. They signal that the company failed to achieve its projected growth, reset options (employee options are now often underwater — struck above the current common price), and can trigger founder vesting resets. The Kupor chapter on "difficult financings" (Chapter 14: "When Bad Things Happen to Good People") covers the dynamics in detail.
- *GAP / recency:* the 2022–24 down-round wave — following the peak-2021 valuations — is the largest cluster of venture down rounds in a decade. No primary source covers this cycle.

**Connects to.** ★G39 (anti-dilution, the mechanism triggered), ★G38 (liquidation preference, which reorders), Z3.10 (the full preference stack discussion), Z4.4 (G209, existing investors must decide whether to exercise pro-rata in a down round), Z4.6 (G214, running out of runway creates the down-round situation).


---

# PART 6 · Zone 5 — Exits & the Firm

**What this zone is:** where the power law finally pays out, and how the firm renews itself. Exit is the only mechanism by which LPs receive cash; the venture firm is renewed by raising successor funds on the strength of realized returns.

**Learning sequence:** `Why exits are everything → Exit routes (IPO, M&A, secondaries) → The exit waterfall → Fund returns (DPI/TVPI) → Raising the next fund → Careers & the future.`

---

### Z5.1 · The Exit: Why Everything Points Here `[core]`

**Quick definition.** Venture returns are realized only at exit — often 8–12+ years from the initial investment — and the power law means that a single exit can define a fund, a firm, and a career.

**Explainer covers.**
- Reuse ★G52 (exit, contributed by PE): the sale or listing through which a fund realizes its investment and returns capital to LPs.
- The illiquidity until exit: unlike public-market investments, a venture stake cannot be sold in the open market. From the day of the first check to the day of the exit, the investor holds an illiquid, unmarketable position (subject to lock-up and transfer restrictions). This is the fundamental illiquidity risk of the asset class.
- The power-law exit: the expected value of a venture portfolio is often dominated by one or two exits. The fund economics (carry, DPI, fund reputation) can turn on a single company's outcome. Kupor: the fund that backs Airbnb, even if 40 other portfolio companies fail, is likely a top-quartile fund.
- The time to exit: the median time from first investment to liquidity event has lengthened from roughly four years in the dot-com era to ten-plus years in the 2010s. Private companies are staying private longer (for complex reasons: more private capital available, regulatory burden of being public, founder control desire). This extends the J-curve (★G4) and tests LP patience.
- The exit as the moment of truth for the markup (G203): paper TVPI becomes DPI only at exit. The markup that looked like a 5× on paper may produce a 2× in cash if the exit price is below the last round's implied valuation.

**Connects to.** ★G52, Z5.2 (exit routes), Z5.3 (exit waterfall), Z4.5 (G203, the markup turns to cash), ★G4 (J-curve).

---

### Z5.2 · Exit Routes: IPO, M&A & Secondaries `[core]`

**Quick definition.** A venture stake is realized through an IPO (the company lists publicly), an acquisition (a buyer purchases the company), or increasingly a secondary sale (the VC sells its stake directly before either of those events).

**Explainer covers.**
- The IPO (★G53 — the VC/PE exit lens; ★G102 — the bank's issuer/process lens): reuse both globals. For the VC, an IPO is the realization event — the company lists, lockup periods apply (typically 180 days), and the VC then sells its stake on the public market over time. For the bank (IB Z2.8), the IPO is the transaction. Equity Research (ER Z1.10) covers the newly public stock. All three perspectives are linked at this node.
- The M&A exit (★G97 — merger model, IB): acquisition by a strategic buyer or a financial buyer. Acquisitions tend to generate cleaner, faster cash — the deal closes, the preference stack is resolved (Z5.3), and cash is distributed. M&A exits can be at any valuation: a distress acquisition may yield near zero; a strategic acquisition of a category winner may yield billions.
- The secondary market: VC funds and individual founders can sell their stakes to secondary buyers (institutional investors and funds-of-funds that specialize in buying private equity stakes before exit). The secondary market has grown substantially since 2015 and provides an additional liquidity option before IPO or M&A. Secondaries allow LPs to rebalance, allow VCs to early-return capital, and allow founders to receive partial liquidity. *GAP / recency: the post-2021 growth of the venture secondary market — driven by the exit drought — is significant and not covered in the primary sources.*
- Route choice: driven by company performance, market conditions (public market receptiveness to IPO), buyer demand, and the preference stack. In a strong exit, the VC prefers IPO (higher valuation, public-market premium) or a strategic acquisition at a premium. In a weak exit, secondaries and distress M&A become more important.

**Connects to.** IB Z2.8, ER Z1.10, ★G53, ★G102, ★G97, Z5.3 (exit waterfall follows the route). Disambiguation: the two IPO globals (★G53 vs. ★G102) — covered in Part 1.

---

### Z5.3 · The Exit Waterfall: Who Gets What `[core]`

**Quick definition.** At exit, the stacked liquidation preferences and participation rights determine the payout order — preferred shareholders are paid first according to their terms, and common holders (founders, employees) receive only what remains.

**Explainer covers.**
- The waterfall mechanics: in a company that has raised multiple rounds of preferred stock, the distribution at exit follows the contractual seniority of each series. Typically, the most recent round's preferred is senior to earlier rounds (Series C senior to Series B, which is senior to Series A). Each series receives its liquidation preference (★G38) before the next in line receives anything.
- Participating preferred vs. non-participating: non-participating preferred holders choose at exit between taking their preference or converting to common (they take the better outcome). Participating preferred holders take their preference and then participate in the remaining proceeds as if they had converted. In a strong exit, non-participating preferred almost always converts to common. In a mediocre exit, participating preferred extracts maximum value at the expense of common.
- Common holders last: founders, employees, and any investors holding common stock are paid after all preferred preferences are exhausted. If the exit price is less than the total liquidation preferences, common holders receive nothing. A company sold for $50M after raising $60M in preferred equity (with 1× non-participating preferences) returns $50M to preferred holders and nothing to common — even the most senior employee options are worthless.
- The employee option pool at exit: options that have vested give employees the right to buy stock at the strike price. If the exit price per share (after preference satisfaction) exceeds the 409A strike price (G208), options are "in the money." If the preferences consume all exit proceeds before common stock is reached, vested options expire worthless.
- Modeling the exit at signing: Feld & Mendelson's key advice for founders: model the term sheet's economic terms across a range of exit scenarios — $20M, $50M, $100M, $500M. The picture at each value reveals when the stack is advantageous and when it is devastating.

**Connects to.** Z3.10 (★G38, the preference stack as negotiated), Z3.7 (G205, the round prices that set preference amounts), Z4.7 (G210, down rounds make the stack worse), ★G11 (distribution waterfall — the PE concept; the venture exit waterfall is the same logic applied at the portfolio-company level), ★G40 (cap table determines who holds what at exit).

---

### Z5.4 · Fund Returns: DPI, TVPI & the Power Law (inherited) `[core]`

**Quick definition.** Venture funds report the same DPI/TVPI/IRR metrics as PE funds, but the gap between paper TVPI and realized DPI is wider here than anywhere, the return distribution is more extreme, and a handful of exits drives virtually the entire result.

**Explainer covers.**
- Reuse ★G1 (IRR), ★G2 (MOIC), ★G3 (DPI/RVPI/TVPI): the three return languages of all private funds. The mechanics are identical to PE; the interpretation differs.
- The DPI/TVPI gap in venture (via G203): a venture fund's TVPI rises with every up-round markup; its DPI rises only when exits close. The 2021 vintage of many VC funds showed spectacular TVPI numbers as late-stage valuations peaked; the 2022–24 correction compressed TVPI sharply, and DPI remained thin because the IPO and M&A markets largely closed.
- Return benchmarking (vintage-controlled): ★G18 (vintage year) is the foundation of fair comparison. A 2015-vintage fund should be compared with other 2015-vintage funds — comparing a 2015 fund to a 2019 fund during the boom year of 2021 would be misleading. The Cambridge Associates VC index and PitchBook/NVCA benchmarks are the standard references. *GAP: recency data is thin in the sources.*
- The top/bottom quartile gap: the difference between a top-quartile and a bottom-quartile venture fund can be 2,000–3,000 basis points (20–30 percentage points) in annual returns. No asset class has wider return dispersion. This makes the LP's fund-selection decision the most impactful variable in the asset class.
- The persistence finding (Kupor): unlike hedge funds and mutual funds, where past performance does not reliably predict future performance, VC shows meaningful persistence — top-quartile firms in one fund cycle tend to remain top-quartile in the next. This is because brand and reputation drive deal flow (G212), which drives returns, which reinforces the brand — the flywheel of the best franchise.

**Connects to.** Z4.5 (G203, markups drive TVPI), Z1.9 (return metrics in the ecosystem context), PE Z5.10 (same metrics, different dynamics), ★G156 (manager selection, the LP's response to dispersion and persistence), WM Z3.x.

---

### Z5.5 · Raising the Next Fund & the GP Franchise `[core]`

**Quick definition.** A VC firm renews itself by raising successor funds on the strength of its realized track record, its brand among the best founders, and LPs' confidence in the partnership's continued deal-flow access.

**Explainer covers.**
- The fundraising cycle: most successful VC firms raise a new fund every three to four years — roughly aligned with the investment period of the prior fund. Fund I → Fund II → Fund III, each typically larger than the last if the strategy is working.
- What LPs evaluate (★G156 — manager selection): the LP's due diligence on a VC fund is one of the most judgment-intensive processes in institutional investing. Key factors: track record (DPI of realized investments, TVPI of portfolio), team stability (has the partnership that generated the track record stayed together?), deal-flow access (is the firm seeing the best deals?), portfolio construction (does the firm understand the power law?), and ownership discipline.
- The DPI imperative: LPs who are deploying into VC Fund II are often doing so with capital that they expect Fund I to eventually return. If Fund I has high TVPI but low DPI, LPs have paper profits and no cash. This can create pressure on the GP to exit prematurely, or conversely, can make LP re-up decisions difficult if DPI hasn't materialized. The exit drought of 2022–24 created acute fundraising difficulty for firms that had strong 2018–21 vintage paper returns but had not yet realized them in cash.
- The brand franchise: the best VC firms have a self-reinforcing brand. Sequoia's track record means the best founders want Sequoia's backing; Sequoia's access to the best founders produces better returns; better returns reinforce the brand. Getting *into* this flywheel is the hardest task for a first-time fund.
- The GP transition risk: when a successful VC partnership retires or splinters, the franchise can deteriorate rapidly. LPs watch partnership stability closely. The departure of a founding partner who is the source of the deal flow can fundamentally change what a firm is.

**Connects to.** ★G156 (manager selection), PE Z5.4 (fund-raising from the PE context), Z1.8 (G216, the platform and partnership), Z1.9 (return metrics that LPs evaluate).

---

### Z5.6 · The Venture Career & Where VC Is Heading `[core]`

**Quick definition.** The venture career path runs analyst → associate → principal → general partner, with a constant revolving door between operating roles and investing, and the industry is being reshaped by the post-2021 reset and by AI's dual presence as both the dominant investment thesis and a tool disrupting how companies are built and funded.

**Explainer covers.**
- The career ladder: analyst or associate (2–4 years, sourcing support, diligence, board preparation) → principal or VP (deal-sourcing with some investment authority) → general partner (full investment decision-making authority, carry participation). The path from entry to GP typically takes 8–12 years in a traditional firm, though operators who join as "venture partners" or "EIR" (entrepreneurs-in-residence) may move faster.
- The founder ↔ VC revolving door: the most reliable path into a senior VC role is a successful exit as a founder or a high-profile operating role at a venture-backed company. Many GPs at top firms are former founders. Conversely, many GPs eventually spin out to start companies. The two roles are complementary and the careers blend.
- Compensation: junior VC salaries are significantly below banking or management consulting peers; the prize is carry participation. A junior investor who joins a fund in its early vintage and earns carry on a top-quartile fund can make career-defining money in year eight when exits arrive. Until then, the total comp is modest relative to Wall Street alternatives.
- The post-2021 reset: the 2021 venture boom (record capital raised, record valuations, crossover surge) was followed by a sharp 2022–24 contraction: fewer deals, lower valuations, almost no IPOs, cross-over retreat, staff reductions at several large firms. The industry is recalibrating to a more disciplined capital environment. *GAP / recency — the module's largest:* the 2021 boom and 2022–24 reset (including the exit drought, the down-round wave, and the AI thesis displacement of all other investment narratives) are not covered by any primary source and represent the largest gap in this map.
- AI as a dual disruptor: AI is simultaneously (1) the dominant investment thesis — virtually all early-stage capital is now flowing toward AI-application and foundation-model companies — and (2) a tool reshaping how venture itself operates (AI-assisted diligence, AI for sourcing, AI for portfolio monitoring) and how startups are built (smaller teams, faster product development, cheaper infrastructure). Neither dimension is covered in the sources. *GAP / recency — flagged here and in Part 9.*

**Connects to.** ER Z5.6/Z5.7 (career comparisons across the financial ecosystem). *GAP flags:* the 2021 boom, the 2022–24 reset, AI's dual role — all flagged for depth layers.


---

# PART 7 · Cross-Zone & Cross-Module Connective Tissue

The venture module sits at the structural center of the corporate lifecycle, inheriting more from prior modules than any other and feeding forward into the public-markets modules. The five key cross-module relationships:

**A. VC as the headwaters of the corporate lifecycle.**
The companies venture funds back at seed eventually raise growth rounds (Z2.4), prepare for an IPO via an investment bank (★G102, IB Z2.8), list on public markets, attract equity research coverage (ER Z1.10, Z3.x), and are held in the portfolios of asset managers (AM Z2.x) and hedge funds (HF Z3.x). The entire public-market ecosystem inherits from VC's output. Every major company in the S&P 500 that was founded after 1975 is likely venture-backed. The VC module should be understood as the origin node of a corporate lifecycle that runs continuously through to wealth management's allocation of public equities to end clients (WM Z3.x).

**B. VC as PE's sibling — the most inheritance-dense relationship in the series.**
The two modules share both the fund-mechanics layer (★G1–G23: IRR, MOIC, DPI/TVPI/RVPI, J-curve, GP, LP, management fee, "2 and 20," carried interest, distribution waterfall, hurdle, catch-up, clawback, capital call, committed capital, dry powder, vintage year, blind pool, LPA, investment period, GP commitment) and the deal-mechanics layer (★G37–G46: preferred equity, liquidation preference, anti-dilution, cap table, dilution, term sheet). The differences are structural: VC is minority/power-law/equity-only; PE is majority/diversified/levered. Understanding this distinction is the minimum requirement for discussing either asset class accurately.

**C. The LP's view (→ AM / WM): VC as the most extreme illiquid alternative.**
For the asset management modules (AM, WM), VC is the private-capital allocation with the most extreme properties: highest return dispersion, most persistence in manager returns, longest J-curve, most dependency on exit markets, and highest illiquidity premium (if the right managers are selected). The LP's manager-selection discipline (★G156, contributed by AM) is the critical bridge concept. The Yale endowment example — 16% VC allocation, ~18% annualized ten-year returns — is the canonical illustration of what the LP's VC program can produce and what the manager-selection discipline looks like in practice (Kupor, Chapter 4).

**D. The inverted Fundamental Law of Active Management (★G115 → HF).**
In long-short equity hedge funds, the Fundamental Law (★G115, contributed by HF) says that active returns scale with breadth (number of independent bets) × IC (skill per bet). The law assumes a normal return distribution. Venture inverts this: the power law (G201) makes breadth a trap (spreading capital across too many companies makes it impossible for any single investment to return the fund) and makes IC per bet the overwhelming variable. A VC who is right once — spectacularly, on the right company — can generate better outcomes than a VC with a higher batting average across a more diversified portfolio. This inversion is the sharpest structural difference between public-market active management (HF, AM) and venture.

**E. The crossover blur (G215 → HF / AM / ER).**
In the 2015–22 era, the boundary between venture and public markets was eroded by crossover investing (G215): hedge funds and mutual funds entering late-stage private rounds. This created a zone in which the same company was simultaneously in a venture portfolio and an active public-equity fund. The valuation methods converged: late-stage venture used revenue multiples from public comps (★G27, ★G88); equity research analysts began publishing "private company" notes. The 2022–24 reversal showed that crossover capital is pro-cyclical and flighty — when public-market multiples compressed, crossover investors withdrew rapidly, contributing to the private-market valuation reset. This crossover zone is shared territory for the VC, HF, AM, and ER modules.

---

# PART 8 · Suggested Master Learning Paths

Three paths through the module, each for a different learner:

**Path A: "How does a VC actually invest?" (The process spine)**
Follows the decision-making journey from first principles through to exit.

`Z1.1 (What is VC?) → Z1.2 (★G201, the power law) → Z1.3 (the players) → Z2.1 (★G204, the funding round sequence) → Z3.1 (process overview) → Z3.2 (★G212, deal flow) → Z3.3 (★G213, the founder bet) → Z3.4 (market/product/traction) → Z3.5 (diligence) → Z3.6 (★G46, the term sheet) → Z3.7 (★G205, pre/post-money) → Z3.9 (★G207, option pool) → Z3.10 (★G38, liquidation preference) → Z3.11 (★G206, SAFE/note) → Z4.1 (after the check) → Z4.2 (★G211, governance) → Z4.4 (★G209, follow-on) → Z4.6 (★G214, burn/runway) → Z5.1 (exit) → Z5.2 (routes) → Z5.3 (waterfall) → Z5.4 (fund returns)`

**Path B: "How does the venture fund/business work?" (The institutional path)**
Follows the VC's business model — from raising capital to returning it.

`Z1.1 → Z1.3 (LP/GP/founders) → Z1.4 (VC vs. PE) → Z1.5 (fund structure) → Z1.6 (economics: carry/fees) → Z1.7 (J-curve) → Z1.8 (★G216, the platform) → Z1.9 (returns) → Z4.3 (★G202, power-law portfolio construction) → Z4.4 (★G209, reserves) → Z4.5 (★G203, the markup) → Z5.4 (fund-level DPI/TVPI) → Z5.5 (raising the next fund) → Z5.6 (careers/future)`

**Path C: "I know PE — show me what's different" (The inheritance-aware path)**
For the learner who has already completed the PE module. Moves quickly through the inherited material and focuses on the 16 net-new globals in dependency order.

Start: Read Part 1 disambiguations (venture carry vs. PE carry; venture J-curve vs. PE J-curve; VC governance vs. PE control; the preference stack at strong vs. weak exits). Then follow the 16 new globals in their dependency chain:

`★G201 (power law — why VC is different from PE structurally) → ★G204 (the funding round sequence — the corporate development arc) → ★G213 (the founder bet — the early-stage evaluative primitive) → ★G212 (deal flow — the sourcing imperative created by the power law) → ★G205 (pre/post-money — the pricing arithmetic) → ★G206 (SAFE/note — the early-stage instrument) → ★G207 (option pool shuffle — the effective pre-money adjustment) → ★G208 (409A — the common/preferred pricing gap) → ★G211 (governance — minority influence vs. PE control) → ★G209 (pro-rata/reserves — maintaining ownership in winners) → ★G203 (markup — the paper-vs-cash gap specific to venture) → ★G214 (burn/runway — the company's clock) → ★G210 (down round — the painful reversal) → ★G202 (portfolio construction — the return-the-fund test) → ★G215 (crossover — the public/private blur) → ★G216 (the venture platform — the VC firm as institution)`

---

# PART 9 · Source Gaps (Consolidated)

Four categories of deliberate gap, flagged at node level and consolidated here for the depth layer:

**Gap 1: The 2021 boom and the 2022–24 reset (the module's largest gap).**
The three primary sources were published in 2019 (Feld/Mendelson, 4th ed.), 2019 (Kupor), and 2022 (Mallaby, but covering events only through ~2020). None covers the 2021 venture boom (record capital deployment, unicorn proliferation, crossover surge), the 2022–24 reset (interest rate shock, compressed multiples, IPO market closure, crossover retreat), or the resulting exit drought and down-round wave. Flagged at: Z2.3, Z2.4, Z2.7, Z4.7, Z5.2, Z5.4, Z5.5, Z5.6. The 2022–24 reset is the most important near-term context for any practitioner-level understanding of the current VC landscape. This gap should be the first depth-layer addition when this module is updated.

**Gap 2: AI's dual role in venture.**
AI is simultaneously the dominant venture investment thesis (virtually all early-stage capital as of 2023–24 flows toward AI applications and infrastructure) and a tool reshaping how venture firms operate (AI-assisted sourcing, diligence, portfolio monitoring) and how startups are built (smaller teams, faster iteration, lower infrastructure cost). Neither dimension appears in any primary source. Flagged at: Z2.8, Z5.6. This gap will require sources published in 2023 or later and practitioner interviews or firm publications.

**Gap 3: The venture secondary market's growth.**
The secondary market for venture stakes (fund stakes and direct company stakes) has grown substantially since 2015 and accelerated in 2022–24 as the primary exit market closed. Kupor mentions reserves and fund-transfer dynamics briefly; no source addresses the dedicated venture secondary market (Lexington Partners, Greenhill Cogent, Forge, Carta's secondary market) as an asset class. Flagged at: Z5.2. This gap is meaningful because the secondary market now provides a material liquidity option that sits between the primary investment and a traditional exit.

**Gap 4: Regulatory and legal depth.**
The venture deal has regulatory dimensions that none of the primary sources addresses comprehensively: Section 409A of the IRS code (covered at a practical level but not with regulatory depth), securities law exemptions that allow startups to raise capital from accredited investors without full registration, CFIUS review for foreign VC investors in US technology companies, and the evolving regulation of crypto/token-based financing. Kupor's Chapter 6 discusses accredited investor definitions and the JOBS Act crowdfunding provisions, which provides some grounding; everything else is thin. Flagged at: Z3.12.

**Note on book availability:** All three canonical sources (*Venture Deals*, *Secrets of Sand Hill Road*, *The Power Law*) were present in the Google Drive folder. No missing-book gap. The Ramsinghani *Business of Venture Capital* (3rd ed., 2021) was also present and served as supplementary reference. This is a stronger source base than several prior modules.

---

# PART 10 · Template Note — What This Module Contributes

**A. The five-zone template held.**
The canonical five-zone template — Ecosystem → Types → Process → Managing → Meta/Firm — applied cleanly to a module that is an *activity within an asset class* (venture investing) rather than an asset-class overview. Zone 1 (the ecosystem and fund structure) inherits heavily; Zone 2 (stages and types) is the branching layer; Zone 3 (the investment process) is the densest and most technically grounded zone; Zone 4 (portfolio and value-add) is the holding-period layer; Zone 5 (exits and the firm) closes the loop. The template held for the eighth time.

**B. The key finding: VC is the most inheritance-heavy module yet built.**
This module contributes only **16 net-new globals (G201–G216)** — the lowest count in the series (prior modules ranged from 19 to 57). This is the *correct, expected* result of the inheritance-first discipline, not a sign of under-building. The explanation: PE (the series' first and foundational module) had already globalized both the fund-mechanics layer (★G1–G23: every term from IRR to GP commitment) and the deal-mechanics layer (★G37–G46: preferred equity, liquidation preference, anti-dilution, cap table, dilution, term sheet). These layers cover approximately 80% of what a VC module would otherwise need to define from scratch. The 16 net-new globals capture precisely and only the concepts that no prior module had any occasion to define — the power law, the round sequence, the SAFE, the option pool shuffle, the 409A, the founder bet, the markup, governance-as-minority-influence, crossover investing, and the venture platform.

**C. What this module contributes to the standing infrastructure.**
The 16 new globals constitute a complete **early-stage private-company financing vocabulary** that any future module touching private companies can reference. Specifically:
- Any module covering startup formation, accelerators, or seed investing will anchor to G204 (the round sequence), G205 (pre/post-money), G206 (SAFE/note), G207 (option pool), G208 (409A).
- Any module covering private company governance will anchor to G211 (board/governance) and G210 (the down round).
- Any module covering portfolio management or GP performance will anchor to G203 (the markup/DPI-TVPI gap) and G202 (power-law portfolio construction).
- The crossover node (G215) serves as the structural bridge between the private-capital modules (PE, PC, VC) and the public-market modules (HF, AM, ER, WM) — the most important cross-series link contributed by this module.

**D. Known limits (Part 9), deferred by design.**
The 2021 boom/2022–24 reset, AI's dual role, the secondary market's evolution, and regulatory depth are all deliberately flagged as depth-layer seams rather than papered over. The structural map is complete at the breadth layer; the depth layers will require more recent sources and practitioner input.

---

*Eighth of the asset-class series; 43 zone nodes (10 + 8 + 12 + 7 + 6); 16 new globals (G201–G216); built on Feld & Mendelson (4th ed.), Kupor, and Mallaby, with Ramsinghani as supplementary reference; 2021–24 cycle and AI's dual role flagged as depth-layer gaps. The shared glossary now spans G1–G216.*
