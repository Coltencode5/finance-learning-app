# Equity Research Module — Complete Node Map

*The seventh module in the asset-class series. Where the first six modules built the **institutions** that raise, deploy, and steward capital, this one maps the **analytical engine** that tells those institutions what a security is worth and whether the consensus is wrong. Equity research is the sell-side's published view-making machine — and the single largest external input into every active buy-side decision in the app.*

---

## A note on this module's sources and their character

This map is grounded in four books, each carrying a different load:

- **Valentine, *Best Practices for Equity Research Analysts* (McGraw-Hill, 2011)** — the **workflow, franchise, sector, coverage, communication, and ethics spine.** Nearly every process node, every "what the analyst actually does all day" detail, and the franchise/rankings material traces here. Valentine organizes the job around **five primary analyst tasks**: identify and monitor the critical factors that move a stock, build and update the financial forecast, use valuation to set a price target, make the stock call, and communicate the idea. That five-task spine structures Zones 1, 3, and 4. **Recency caveat:** the book predates MiFID II (2018), the research-unbundling era, and the alt-data/AI disruption of the research product — so wherever the *business model* or the *toolkit* of modern research is at issue, the book is a period source, and the map flags the gap at the node.
- **Damodaran, *The Little Book of Valuation* (Wiley, 2024 update)** — the **intrinsic-versus-relative ("pricing") backbone** of the valuation zone. The four keys to a multiple, the **companion-variable** discipline (every multiple has a fundamental it should be read against), the narrative-and-numbers / three-P test, and — bluntly stated — the structural **buy-rating bias** in sell-side recommendations all come from here.
- **Koller, Goedhart & Wessels (McKinsey), *Valuation*, 7th ed. (Wiley, 2020)** — the **value-creation and market-efficiency depth.** ROIC × growth → cash flow → value (and the hard rule that growth only creates value when ROIC exceeds the cost of capital); the **expectations treadmill** — returns are driven by performance *relative to expectations*, not in absolute terms — which grounds the entire consensus/estimate/surprise/revision cluster; the "markets price public information well but cannot price information they do not have" framing that grounds channel-checks and the mosaic; and **conservation of value**, which grounds the earnings-quality and forensic nodes. Koller also supplies the candid observation that a leading sell-side analyst *values* in DCF but *communicates* in implied multiples — the hinge of the intrinsic-vs-pricing node.
- **Penman, *Financial Statement Analysis and Security Valuation*, 5th ed. (McGraw-Hill, 2013)** — the **financial-statement-analysis and quality-of-earnings** spine behind the modeling and forensic nodes: reading the accounting, separating operating from financing, and accrual-based earnings-quality diagnostics.

Three **recency / source gaps** are flagged at the node level rather than papered over:
1. **The modern research business model** (post-MiFID-II unbundling, the collapse in research budgets, the survival economics of the franchise) — *no source covers it; Valentine predates it.* Flagged on G197 and Z5.2.
2. **AI and alternative data as a disruption of the research product itself** (not just an input) — *Koller (2020) is the most recent source and does not reach it.* Flagged on G195 and Z5.7.
3. **The securities-regulation frame** (Regulation AC, the post-Spitzer Global Research Settlement, MiFID II's conflict provisions) — *Valentine covers Reg FD and the Spitzer settlement; the IB module frames the information wall; no securities-law source sits in the folder.* Grounded on Valentine's ethics chapter plus the IB frame plus general knowledge, and flagged on G199, G200, and Z5.4–Z5.5.

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
| **Connects to** | The edges. `★ G*n*` for globals; `IB Z3.1`, `HF Z3.3`, `AM Z2.4` for cross-module references. Dense by design — the graph *is* the product. |
| **GAP / recency** | A flag that the underlying sources are thin, dated, or silent here. |

---

## The shared-glossary rule (the scaling discipline)

There is **one** global glossary for the entire app, currently numbered **G1–G181** across the six prior modules. This module does two things and only two things with it:

1. **Reuses G1–G181 by number.** IRR, EBITDA, enterprise value, the DCF, comps, alpha, the information ratio, market efficiency, the thesis — these are *already defined*. Equity Research does not rebuild them. It points to them and adds the analyst's vantage as **context**, never as a new node.
2. **Contributes exactly 19 genuinely novel globals, G182–G200.** These are the concepts the first six modules never needed: the published research report, the estimate-and-consensus, the price target, the rating, the earnings cycle, the franchise, the unbundling economics, the conflict regime. Each is net-new. Nothing below G182 is redefined.

The inheritance is heavy on purpose. Like Asset Management and Wealth Management, Equity Research is mostly a **re-use** module: it takes Investment Banking's valuation toolkit (★G87–G95) and Asset Management's active-equity machinery (★G125, ★G149) and the skill primitives from Hedge Funds (★G106, ★G112–G115, ★G121, ★G124, ★G136), and it **reframes** them from the analyst's chair. The banker uses the toolkit to *price a deal*; the analyst uses the same toolkit to *publish a view*. Same math, different artifact, different reader, different conflict.

---

# PART 1 · The Global Glossary Layer

The 19 new globals this module contributes, grouped by theme. (Home = the zone where the concept is taught in depth. Appears in = other modules that reference it.)

### Group A — The published research product

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| **G182** | The research report (the note & the initiation) | The written, distributed artifact in which an analyst states a rating, a price target, and the reasoning — the unit in which sell-side research is actually delivered. | ER Z3 | IB, AM, HF |

### Group B — The analyst's linked outputs (the five-task chain made concrete)

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| **G183** | The earnings model | The analyst's living spreadsheet that projects a company's financial statements forward to produce the numbers every other output depends on. | ER Z3 | IB, PE, AM |
| **G184** | The estimate & the consensus | A specific forward forecast (EPS, revenue, EBITDA) for a company, and the average of all analysts' estimates against which surprise and revision are measured. | ER Z3 | AM, HF, IB |
| **G185** | The price target | A published, time-bounded estimate of where a stock's price should go, derived from the model and the chosen valuation method. | ER Z3 | IB, AM, HF |
| **G186** | The rating (buy / hold / sell) | The discrete, published recommendation that translates the gap between price target and current price into an instruction. | ER Z3 | AM, HF, IB |
| **G187** | The published thesis (the reputation-staked call) | The analyst's reasoned, *named-and-distributed* argument for why a stock will move — the same logical object as the internal thesis, but published, attributed, and career-bearing. | ER Z3 | HF, AM, PE |

### Group C — Coverage & the information edge

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| **G188** | Earnings revisions & the estimate-revision cycle | The continual process of raising or lowering estimates as new information arrives — itself one of the most-watched signals in markets. | ER Z4 | AM, HF |
| **G189** | Sector coverage & the coverage universe | The defined set of companies an analyst follows (typically one sector), the basis of the analyst's expertise and the boundary of their authority. | ER Z2 | AM, HF, IB |
| **G190** | Channel checks & the mosaic theory | The practice of building an information edge from many individually-immaterial, lawful data points — the legitimate counterpart to trading on inside information. | ER Z3 | HF, AM |
| **G191** | Critical factors (the stock's swing factors) | The few variables that actually determine a stock's performance — Valentine's signature idea that an analyst's whole job is finding and monitoring the 2% that matters. | ER Z3 | HF, AM, PE |

### Group D — The earnings cadence

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| **G192** | The quarterly earnings cycle (the print, the call, the update) | The recurring rhythm — results release, management call, model update, note — around which the entire research calendar is organized. | ER Z4 | AM, HF, IB |
| **G193** | The earnings surprise & company guidance | The gap between reported results and consensus, and the forward expectations management itself sets — the twin events that move stocks at the print. | ER Z4 | AM, HF |

### Group E — The branches (who else does this, and who pays)

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| **G194** | Buy-side (in-house) research | Research produced *inside* an asset manager or hedge fund for its own portfolio decisions, never published, judged only by returns. | ER Z2 | AM, HF, PE |
| **G195** | Independent & alternative research (incl. alt-data & AI) | Research from providers with no banking or brokerage conflict, increasingly built on alternative datasets and machine analysis rather than the traditional analyst note. | ER Z2 | HF, AM |

### Group F — The franchise & the economics

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| **G196** | The research franchise & analyst rankings (the II survey) | The reputational capital of a sell-side analyst — historically measured by the *Institutional Investor* poll — that determines client access, compensation, and influence. | ER Z5 | IB, AM, HF |
| **G197** | How research is paid for (the bundle, soft dollars & MiFID II unbundling) | The economics of the research product: historically bundled into trading commissions and soft dollars, then forcibly unbundled in Europe by MiFID II. | ER Z1 | AM, HF, IB |
| **G198** | The sales / trading / research triangle | The three-desk structure of a sell-side equities division and the flows of ideas, orders, and commissions that bind research to the rest of the firm. | ER Z1 | IB, HF, AM |

### Group G — The regulatory & conflict frame

| ID | Node | Quick definition | Home | Appears in |
|---|---|---|---|---|
| **G199** | The research/banking conflict & the Global Research Settlement (post-Spitzer) | The structural conflict between objective research and investment-banking revenue, and the 2003 settlement that walled them apart. | ER Z5 | IB, PE |
| **G200** | Regulation AC & the disclosure regime (Reg AC + Reg FD + quiet periods) | The rules requiring analysts to certify their own views, barring selective corporate disclosure, and silencing research around deals. | ER Z5 | IB, AM |

---

## Featured disambiguations (the high-confusion pairs)

These are the term-collisions most likely to trip a learner. Each gets a dedicated cross-linking callout in the app.

> **★G187 the *published* thesis vs. ★G121 the *internal* thesis.**
> They are the **same logical object** — a reasoned argument that a security is mispriced — seen from two chairs. The hedge-fund analyst's thesis (★G121, HF Z3) lives in an internal memo, is tested only by the portfolio's P&L, and can be wrong quietly. The sell-side analyst's thesis (★G187) is **published, attributed, time-stamped, and ranked**: it carries a name, a price target, and a rating, and being wrong is a public, reputational, II-poll-affecting event. The publication is the whole difference — it converts a private bet into a staked reputation.

> **★G184 the estimate vs. ★G185 the price target vs. ★G186 the rating.**
> A chain, often conflated. The **estimate** is a forecast of a *fundamental* (next quarter's EPS). The **price target** is a forecast of the *stock price*, produced by running the estimate through a valuation method. The **rating** is the *instruction* (buy/hold/sell) that falls out of the gap between the price target and today's price. You can disagree with an analyst at any link: their numbers, their multiple, or their call.

> **The valuation toolkit here ("valuing" / intrinsic) vs. in IB ("pricing" the deal).**
> Equity Research **reuses IB's toolkit wholesale** — the three methodologies (★G87), comps (★G88), precedents (★G89), the DCF (★G90), WACC (★G91), unlevered FCF (★G92), terminal value (★G93), the football field (★G94), the EV↔equity bridge (★G95). But the *purpose* differs. The banker prices a transaction that will actually clear at a negotiated number. The analyst forms a *view* about where a continuously-traded price *should* go — and (per Damodaran) must decide whether they are doing **intrinsic valuation** (what the business is worth on its cash flows, the investor's question) or **relative valuation / pricing** (what the market will pay, read off a multiple, the trader's question). Koller's candid note captures real practice: the leading analyst *values* in DCF but *communicates* in implied multiples.

> **Sell-side (★G83 / Z2.4) vs. buy-side (★G194) vs. independent (★G195) research.**
> The split is by **who pays and what conflict results.** Sell-side research is produced by brokers and banks, distributed to clients, and historically paid for through trading commissions — carrying the banking conflict (★G199). Buy-side research (★G194) is produced inside an asset manager for its own use, never published, conflict-free but invisible. Independent research (★G195) is sold directly, free of banking and brokerage conflicts, increasingly alt-data-driven. The sell-side/buy-side divide itself is ★G83, inherited from Investment Banking.

> **★G190 channel checks / the mosaic vs. material non-public information (MNPI).**
> The bright line of the whole job. The **mosaic theory** says an analyst may assemble many individually-immaterial, lawfully-obtained data points (a parking-lot count, a supplier's tone, a price change) into a *material* conclusion — and trade or publish on it. **MNPI** is a single material fact obtained in breach of a duty (a CFO's leak). Koller's framing is the principle underneath: markets price public information well but *cannot price information they do not have* — so the legitimate edge lives in the mosaic, not in the leak. The line between them is where careers and prison sentences are decided.

> **★G193 the earnings surprise vs. ★G188 the estimate revision.**
> Both are about the gap between expectation and reality, but they run in opposite directions. A **surprise** is the company moving relative to the analyst: results land above or below consensus *at the print*. A **revision** is the analyst moving relative to reality: the analyst raises or lowers the estimate *going forward*. A surprise often *triggers* a wave of revisions. Koller's expectations treadmill explains why both matter more than the absolute numbers: returns are driven by performance relative to expectations, so the *change* in expectations is the event.

> **★G196 the research franchise / II ranking vs. ★G104 the IB league table.**
> Both are reputational scoreboards, but they measure different things for different audiences. The **II survey / franchise** (★G196) ranks individual *analysts* by the quality and usefulness of their research, as voted by the buy-side clients who consume it. The **league table** (★G104, from IB) ranks *banks* by deal volume, as a marketing record of transactions closed. One measures whose *ideas* the buy-side values; the other measures whose *deals* won. They can diverge sharply — a top-ranked analyst at a mid-tier bank, or a league-table leader with a weak research franchise.

---

# PART 2 · Zone 1 — The Research Ecosystem

*What equity research is, who makes it, who reads it, who pays for it, and the conflict that shadows all of it. This zone sets the stage; the analytical craft comes in Zone 3.*

### Z1.1 · What Is Equity Research? `[core]`
**Quick definition.** Equity research is the discipline of analyzing publicly-traded companies to form and communicate a judgment about whether their shares are mis-priced.
**Explainer covers.**
- The one-sentence job: take a company, figure out what it's worth and where its stock is going, and tell people — with a rating and a price target attached.
- The product is *a view*, not a fact: research is fundamentally an argument about the future, made under uncertainty, that can be and often is wrong.
- The recurring theme that organizes everything downstream (Valentine): **generating alpha is all about finding where the consensus is wrong.** Knowing what a company will earn is worthless if everyone already knows it; the value is in a *differentiated, correct* view.
- Why it exists at all: markets aggregate information, but (Koller) they can only price information they actually have — so there is a permanent economic role for someone who digs up, organizes, and interprets what isn't yet in the price.
- The distinction from adjacent crafts: not accounting (which records the past), not investment banking (which transacts), not portfolio management (which owns). Research *judges*.
**Connects to.** Z1.2 (the outputs) · Z1.5 (the workflow) · ★G125 market efficiency *(AM Z2.3 — why an edge is possible at all)* · ★G106 alpha *(HF — the goal)* · ★G136 the edge *(HF Z5.1)* · ★G184 consensus *(the thing you're trying to beat)* · HF Z3.1 *(the buy-side analyst doing the same cognitive work)*.

### Z1.2 · The Research Product & the Five Outputs `[core]`
**Quick definition.** Every piece of equity research ultimately delivers five linked things: a set of estimates, a valuation, a price target, a rating, and the written report that carries them.
**Explainer covers.**
- The five concrete outputs and how they chain: the **earnings model** (★G183) produces the **estimates** (★G184); the estimates feed a **valuation** that yields a **price target** (★G185); the gap between target and price produces the **rating** (★G186); all of it is packaged in the **research report** (★G187, ★G182).
- The model is the engine, but the *rating* is what the firm is selling and what the client acts on — everything exists to support the call.
- Why the chain is auditable: a good analyst can be challenged at any link, and a sophisticated client reads the model and the assumptions, not just the headline.
- The two report formats this resolves into: the **initiation of coverage** (the long, foundational launch) and the **note** (the short, frequent update) — both are ★G182, taught in Z3.12 and Z4.
- The honest caveat: the five outputs are the *form*; whether they contain alpha depends entirely on whether the view inside them is differentiated and right (back to Z1.1).
**Connects to.** Z3.4 (model → ★G183) · Z3.6 (estimates → ★G184) · Z3.10 (target → ★G185) · Z3.11 (rating → ★G186) · Z3.12 (report → ★G182) · ★G94 the football field *(IB Z3.6 — how the valuation range is shown)*.

### Z1.3 · Sell-Side vs. Buy-Side vs. Independent Research `[core]` ★ GLOBAL (G83 — inherited)
**Quick definition.** Research splits into three worlds by who produces it and who pays: the sell-side (brokers/banks, published to clients), the buy-side (asset managers/hedge funds, kept in-house), and independents (sold directly, conflict-free).
**Explainer covers.**
- The inherited frame: ★G83 is the **sell-side/buy-side divide** from Investment Banking — the sell-side *sells* services and products to the buy-side, which *buys* and owns securities. Research sits on both sides plus a third.
- **Sell-side research** (the spine of this module, Z2.4): produced by investment banks and brokers, *distributed* to institutional clients, historically paid via trading commissions — and carrying the banking conflict (★G199).
- **Buy-side research** (★G194, Z2.5): produced *inside* an asset manager or hedge fund for its own decisions, never published, judged only by returns — invisible but conflict-free.
- **Independent research** (★G195, Z2.6): sold directly to investors by firms with no banking or brokerage arm, increasingly built on alternative data.
- The defining question across all three — *who pays, and what conflict does that create?* — is the thread that runs through Zone 5.
**Connects to.** Z2.4 (sell-side branch) · Z2.5 (★G194) · Z2.6 (★G195) · Z1.7 (★G197 — who pays) · Z5.4 (★G199 — the conflict) · IB Z1.2 *(the original sell-side/buy-side definition)* · AM Z1.1 *(the buy-side as asset owner's agent)* · HF Z1.1 *(the buy-side as absolute-return seeker)*.

### Z1.4 · Who Consumes Research & Why `[core]`
**Quick definition.** Sell-side research is consumed mainly by professional buy-side investors, who use it for ideas, for models, for access to the analyst, and for access to company management.
**Explainer covers.**
- The primary reader is **not** the retail investor — it is the institutional buy-side: the portfolio managers and analysts at asset managers and hedge funds (AM Z2.4, HF Z3.1).
- The four things the buy-side actually buys (Valentine, Ch6): (1) the *idea* and the differentiated view; (2) the *model* and the data work they'd otherwise do themselves; (3) *access to the analyst* — the ability to call and pressure-test; (4) *corporate access* — the analyst's relationships and conferences that get the PM in front of management.
- The asymmetry: the best buy-side shops use the sell-side as *one input* and do their own work (★G194); the point of sell-side research is to be a high-quality input, not the final answer.
- Why corporate access has historically been so valuable — and why MiFID II's unbundling (★G197) attacked exactly this, by forcing it to be priced separately.
- A second audience: corporate-issuer management teams themselves read the research written about them, and (carefully) the sell-side covering their competitors.
**Connects to.** Z1.7 (★G197 — and why unbundling reprices all four) · Z4.7 (managing the client relationship) · Z5.1 (★G196 — rankings come from these clients' votes) · ★G194 buy-side research *(the consumer who also produces)* · AM Z2.4 *(active managers as the core client)* · HF Z3.1 *(hedge-fund analysts as the most demanding client)*.

### Z1.5 · The Analyst's Workflow — The Five Tasks `[process]`
**Quick definition.** Valentine frames the entire job as five recurring tasks: find the critical factors, build the forecast, value the company, make the call, and communicate it.
**Explainer covers.**
- The five tasks in order (Valentine, Exhibit I.1), which structure Zones 3 and 4: **(1)** identify and monitor the **critical factors** (★G191) that actually move the stock; **(2)** build and continually update the **financial forecast** / model (★G183); **(3)** use **valuation** to translate the forecast into a **price target** (★G185); **(4)** make the **stock recommendation** (★G186); **(5)** **communicate** the idea persuasively (★G182, ★G187).
- Why the order matters: each task feeds the next, but task 1 — finding what *matters* — is the one that separates good analysts from spreadsheet operators, because most of a model's line items are noise.
- The loop never closes: maintaining coverage (Zone 4) means running all five tasks again every quarter as new information arrives.
- The "2% that matters" principle (Valentine): a company has hundreds of measurable attributes, but only a handful are *critical factors* that swing the stock — and the analyst's edge is in identifying and forecasting *those*.
- How this maps to the buy-side: the in-house analyst (★G194) runs the same five tasks minus the "communicate to clients" step — they communicate to one PM instead.
**Connects to.** Z3.2 (task 1 → ★G191) · Z3.4 (task 2 → ★G183) · Z3.7 (task 3 valuation) · Z3.11 (task 4 → ★G186) · Z3.12 (task 5 → ★G182) · ★G114 breadth *(HF — applying the process across the coverage universe)* · ★G124 second-level thinking *(HF Z3.2 — what "find where consensus is wrong" demands cognitively)*.

### Z1.6 · The Research Team & the Analyst's Role `[core]`
**Quick definition.** A sell-side research team is a senior analyst (the named, ranked decision-maker) supported by associates who build and maintain the models, organized by sector.
**Explainer covers.**
- The structure: the **senior/lead analyst** owns the coverage, the calls, and the franchise (★G196); **associates/junior analysts** build models, write first drafts, and do the channel-check legwork; the senior analyst's *name* is on the note and the reputation.
- The sector organization: teams are built around a **coverage universe** (★G189) — almost always a single sector — because the critical factors and the relationships are sector-specific.
- The career path this implies (taught in Z5.6): associate → senior analyst on the sell-side, or a jump to the buy-side, where the same analytical skill is rewarded with returns rather than rankings.
- The supporting cast around the analyst: the sales force that distributes the research (Z1.8), the editors and compliance officers who vet every published word (Z5.5), and the corporate-access team.
- The tension built into the role: the analyst is simultaneously a *researcher* (who must be right), a *salesperson* (whose ideas must be used), and a *franchise* (whose reputation must be maintained) — and these pull in different directions.
**Connects to.** Z1.8 (★G198 — the desk structure around the analyst) · Z2.2 (★G189 — the universe the team covers) · Z5.1 (★G196 — what the senior analyst is building) · Z5.6 (the career) · IB Z1.4 *(the analogous deal-team hierarchy)*.

### Z1.7 · How Research Is Paid For `[core]` ★ GLOBAL (G197)
**Quick definition.** Sell-side research was historically never sold directly — it was bundled into the trading commissions the buy-side paid, until MiFID II forced European managers to pay for it as a separate line item.
**Explainer covers.**
- The historical model: research was "free" — the buy-side paid inflated **trading commissions**, and a slice of those commissions (**soft dollars**) implicitly compensated the broker for the research and access. No invoice, no explicit price.
- Why that was fragile: it bundled a *research* payment inside a *trading* payment, obscured the true cost, and let mediocre research ride along on order flow.
- **MiFID II (2018)** detonated the bundle in Europe: asset managers must now pay for research with hard dollars, *separately* from execution, and budget for it explicitly — collapsing research budgets and forcing a brutal consolidation of who gets paid.
- The consequences (Zone 5.2): fewer analysts, fewer covered stocks (especially small-caps), pressure on the franchise model, and a opening for independents (★G195) who were always priced separately.
- **GAP / recency flag.** No source in the folder covers the post-MiFID-II economics — Valentine (2011) predates it entirely. This node is grounded in general knowledge of the regulation and its aftermath; the *quantitative* picture of the modern research business (budgets, headcount, survival economics) is a genuine source gap, flagged again at Z5.2.
**Connects to.** Z1.8 (★G198 — commissions flow through the trading desk) · Z5.2 (the economics in depth) · Z5.4 (★G199 — unbundling as a conflict remedy) · Z2.6 (★G195 — independents as beneficiaries) · ★G83 sell-side/buy-side *(the payment crosses this divide)* · AM Z5.x *(the manager's cost base that research budgets sit in)*.

### Z1.8 · The Sales / Trading / Research Triangle `[core]` ★ GLOBAL (G198)
**Quick definition.** A sell-side equities division has three desks — research (makes the ideas), sales (distributes them), and trading (executes the orders) — bound together because the trading commissions pay for the research.
**Explainer covers.**
- The three desks and their jobs: **research** produces the views and models; **sales** (the salesforce) carries those views to buy-side clients and gathers their feedback; **trading** executes the buy/sell orders the clients place.
- The circular economics (why it's a triangle): research generates ideas → sales gets clients to act → clients trade through the firm → commissions fund research. Break any leg and the model wobbles.
- The analyst's daily reality: a meaningful share of an analyst's time is spent on the **morning call** and on the phone *with the salesforce and clients*, not building models — communication (task 5) is a job, not an afterthought.
- How unbundling (★G197) strained the triangle: once research must be paid for separately, the commission-funds-research leg is cut, and the three desks' economics decouple.
- The conflict-management overlay: the **information wall** (IB Z1.10) must separate research from banking, but research, sales, and trading sit *together* — which is exactly why selective-disclosure and front-running rules (Z5.5) matter so much.
**Connects to.** Z1.7 (★G197 — the commissions that bind the triangle) · Z4.7 (working with the salesforce) · Z5.3 (the triangle in depth) · Z5.5 (★G200 — the rules governing the desks) · IB Z1.10 *(the banking-vs-public-side wall)* · HF Z1.x *(the prime-brokerage/trading relationship on the other side)*.

### Z1.9 · The Regulatory & Conflict Frame `[core]`
**Quick definition.** Equity research operates inside a cage of rules built largely in response to scandal: a wall against banking influence, a certification requirement, and bans on selective disclosure and trading on inside information.
**Explainer covers.**
- The two foundational conflicts research is regulated to contain: research being bent to win **banking** business (★G199), and research being used to traffic in **information** the public doesn't have (the MNPI line, Z3.3).
- The post-Spitzer **Global Research Settlement** (2003) — the regulatory earthquake that walled research off from investment banking after analysts were caught publicly touting stocks they privately disparaged (★G199, Z5.4).
- **Regulation AC** (Analyst Certification): every published report must contain the analyst's personal certification that the views are genuinely their own and that their pay isn't tied to the specific recommendation (★G200, Z5.5).
- **Regulation FD** (Fair Disclosure): companies may not selectively feed material information to favored analysts — everyone gets it at once, which is *why* the lawful mosaic (★G190) became the edge (Valentine, Ch9).
- **Quiet periods**: research must go silent around the firm's own banking deals (around an IPO especially), tying this frame directly to IB's ECM process (IB Z2.8).
- **GAP / recency flag.** No securities-law source sits in the folder; this frame is grounded in Valentine's treatment of Reg FD and the Spitzer settlement plus the IB module's wall plus general knowledge. MiFID II's *conflict* provisions (distinct from its unbundling) are part of the same gap.
**Connects to.** Z3.3 (★G190 vs. MNPI) · Z5.4 (★G199) · Z5.5 (★G200) · IB Z1.10 *(the information wall)* · IB Z2.8 *(the IPO quiet period)* · ★G83 *(the conflict lives at the sell-side/banking seam)*.

### Z1.10 · Where Equity Research Sits — The Cross-Module Map `[core]`
**Quick definition.** Equity research is the sell-side analytical engine that feeds every other module: it produces the views the buy-side consumes, using the toolkit investment banking built, judged by the skill metrics hedge funds live by.
**Explainer covers.**
- **Upstream from the buy-side:** ER is the largest external input into active management (AM Z2.4) and hedge-fund stock-picking (HF Z3.1–3.3). The sell-side analyst *researches*; the buy-side *decides and owns*.
- **Sharing IB's toolkit:** the valuation machinery (★G87–G95) was built in Investment Banking; ER reuses it wholesale, reframed from pricing-a-deal to publishing-a-view (Z3.7–3.8).
- **Judged by HF's metrics:** an analyst's track record is measured by the same skill statistics the buy-side is — the information ratio (★G112) and the hit rate / information coefficient (★G113) apply to a sequence of published calls exactly as to a sequence of trades.
- **Meeting banking at the IPO:** research and banking collide most visibly in equity capital markets (IB Z2.8–2.9, ★G102) — the analyst must stay walled off from the deal the bankers are doing, the tension the whole regulatory frame (Z1.9) exists to manage.
- **The map forward:** the modules still unbuilt (Venture Capital, Real Estate, Equity Research's own depth layers, and the macro/derivatives primitives) will plug into this same shared glossary; ER's contribution is the *view-making* vocabulary the others can now reference.
**Connects to.** *(this is the hub node — it links outward to)* AM Z2.4 · HF Z3.1 · IB Z2.8 · IB Z3.x *(the toolkit's home)* · ★G87–G95 *(the inherited methods)* · ★G112, ★G113 *(the skill metrics)* · ★G102 the IPO *(where research and banking meet)*.

---

# PART 3 · Zone 2 — Types of Coverage

*Equity research is not one job but a family of them, sorted two ways: by the **sector** an analyst covers, and by the **institution** the research is produced inside. This zone maps both axes. The sector axis explains the analyst's expertise; the institutional axis (the three branches) explains the conflict.*

### Z2.1 · Coverage by Sector & the Coverage Universe `[core]` ★ GLOBAL (G189)
**Quick definition.** An analyst covers a defined set of companies — almost always within a single sector — and that **coverage universe** is both the basis of their expertise and the limit of their authority.
**Explainer covers.**
- Why coverage is sector-bound: the **critical factors** (★G191) that move a bank are nothing like those that move a biotech or an oil major, so depth requires specialization — an analyst is a sector expert first.
- What "covering" a stock actually means (Valentine, Ch2): to **closely cover** a name is to publish a *price target derived from a maintained forecast* — not merely to comment on it. Coverage is a standing commitment to a model, a rating, and regular notes.
- The size of a universe: a sell-side analyst (with their team) typically covers on the order of **5–7 stocks per team member**; a buy-side analyst may be responsible for a far wider list (35–50 names) because they don't have to publish on each.
- The boundary it creates: an analyst has authority — and rateable reputation (★G196) — *only* within their universe; outside it they're just another reader.
- How a universe is chosen: by sector importance, client demand, the firm's banking relationships (carefully, given ★G199), and the analyst's edge — which is the subject of the next node.
**Connects to.** Z2.2 (how the universe is built) · Z2.3 (sector frameworks) · Z3.2 (★G191 — the factors within the sector) · Z1.6 (the team that covers it) · Z5.1 (★G196 — reputation is universe-specific) · AM Z2.4 *(the active manager who relies on this coverage)* · HF Z3.1 *(the buy-side analyst's wider universe)*.

### Z2.2 · Building the Coverage Universe `[process]`
**Quick definition.** Choosing which companies to cover is a deliberate analytical exercise — mapping a sector's value chain, grouping comparable companies, and deciding where an edge is possible.
**Explainer covers.**
- **Food-chain analysis** (Valentine): map the sector as a value chain — suppliers, producers, distributors, customers — so that covering one company illuminates its neighbors, and a data point about one (a supplier's order book) informs the whole universe.
- **Homogeneity**: a good universe is internally comparable, so the same critical factors and the same comps (★G88) apply across it — which makes relative valuation (Z3.8) and cross-reads tractable.
- The trade-off in universe size: more names mean more breadth (★G114) and more client touchpoints, but less depth per name; fewer names mean deeper edge but a narrower franchise.
- Where coverage gets *initiated* and *dropped*: launching coverage of a new name is a major event (the initiation report, Z3.12); dropping coverage is a quiet but meaningful signal, often driven by the post-MiFID-II economics (★G197) that made covering small-caps uneconomic.
- The link to breadth and the Fundamental Law: covering more names well multiplies the chances to be right — but only if the *per-name* skill (the information coefficient, ★G113) holds up across the wider list.
**Connects to.** Z2.1 (★G189 — the universe being built) · Z3.2 (★G191) · Z3.8 (relative valuation across the universe) · ★G88 comps *(IB — the comparable set the universe maps to)* · ★G114 breadth *(HF Z5.x)* · ★G115 the Fundamental Law of Active Management *(HF — breadth × skill)* · ★G197 *(the economics that shrink universes)*.

### Z2.3 · Sector Frameworks — How the Critical Factors Differ `[core]`
**Quick definition.** Each sector has its own analytical framework — the specific drivers, metrics, and KPIs that matter — so that the universal "find the critical factors" task takes a different concrete shape in every sector.
**Explainer covers.**
- The principle (Valentine, Ch7): critical factors (★G191, taught in Z3.2) are *sector-specific*. The analyst's first job in any sector is to learn which handful of variables the stocks actually trade on.
- Worked contrasts: a **bank** trades on net interest margin, credit losses, and capital ratios (and is valued on a DDM/book basis, per Damodaran's special cases); a **retailer** on same-store sales, traffic, and margin; a **commodity/cyclical** producer on the commodity price and the cycle (valued on *normalized* earnings, Damodaran); a **software** company on net revenue retention, bookings, and the growth-vs-margin trade.
- Why the valuation method follows the sector: the choice between DCF, multiples, and a sector-specific method (Z3.7–3.8) is driven by the sector's economics — banks and financials break the standard enterprise-value frame, young/high-growth names defy multiples, cyclicals defy spot earnings.
- The KPI layer beneath the financials: every sector has *operating* metrics (subscribers, load factors, rig counts, daily active users) that lead the reported financials — and the analyst's edge is often in forecasting the KPI before it shows up in EPS.
- The link to channel checks: the sector framework tells you *which* operating metrics to go check (Z3.3) — you can't build a useful mosaic without knowing what's material.
**Connects to.** Z3.2 (★G191 — the home of the critical-factors concept) · Z3.3 (★G190 — checking the sector-specific metrics) · Z3.7 (valuation method follows sector) · Z3.8 (sector-appropriate multiples, ★G88) · AM Z2.5–2.7 *(the value/growth/quality lenses that sectors cluster into)* · ★G149 style *(AM — sectors as style exposures)*.

### Z2.4 · Branch — Sell-Side Research `[branch]` ★ GLOBAL (G83 — inherited)
**Quick definition.** Sell-side research is the published, client-distributed product made by banks and brokers — the version of the job this whole module takes as its spine, and the version that carries the banking conflict.
**Explainer covers.**
- The defining features: research is **published** (attributed, rated, distributed to all clients), **paid for via commissions** (★G197), and **conflicted** by the firm's banking and trading interests (★G199).
- What the sell-side analyst optimizes for: a *differentiated, correct, and well-communicated* view that wins client votes and builds the franchise (★G196) — being right is necessary but not sufficient; being *used* is the currency.
- The structural pressures: the buy-rating bias (Damodaran — analysts issue far more buys than sells, to preserve management access and under employer pressure, Z3.11), the quiet periods (★G200), and the constant tension between the research call and the firm's banking pipeline.
- Why it's the spine: the sell-side analyst's workflow is the *fullest* version of the five tasks (all five, including communication), so the process zone (Z3) is written from the sell-side chair and the other branches are described as variations.
- The reader: the institutional buy-side (Z1.4) — which means the sell-side product is shaped by what PMs and buy-side analysts will pay attention to and vote for.
**Connects to.** Z1.3 (★G83) · Z3.x *(the full process, written sell-side)* · Z3.11 (the buy-rating bias) · Z5.1 (★G196 — the franchise this builds) · Z5.4 (★G199 — the conflict) · IB Z1.2 *(sell-side origin)* · ★G197 *(how it's paid)*.

### Z2.5 · Branch — Buy-Side Research `[branch]` ★ GLOBAL (G194)
**Quick definition.** Buy-side research is produced *inside* an asset manager or hedge fund, purely for that firm's own portfolio decisions — never published, never sold, and judged by one thing only: returns.
**Explainer covers.**
- The defining contrast with the sell-side: no publication, no rating to defend, no franchise to build, no banking conflict — and no audience but the firm's own portfolio managers.
- What changes about the job: the buy-side analyst runs the same five tasks *minus communication-to-clients* — they make the case to one PM (or run the book themselves), so the output is a *decision*, not a *note*.
- How the two relate: the buy-side analyst *consumes* sell-side research (Z1.4) as one input — using the sell-side model and access — but forms an independent, often contrarian view (★G124 second-level thinking).
- Why it's invisible but often better: freed of the buy-rating bias and the need to maintain management relationships, buy-side research can issue the conviction *sell* the sell-side rarely will — and its only scoreboard is P&L (the information ratio, ★G112).
- The career flow: the most common destination for a strong sell-side analyst is the buy-side (Z5.6), trading rankings for returns and publication for privacy.
**Connects to.** Z1.3 (★G83) · Z1.4 (the buy-side as consumer) · Z5.6 (the career path) · ★G124 second-level thinking *(HF Z3.2)* · ★G112 information ratio *(HF — the only scoreboard)* · ★G121 the internal thesis *(HF Z3 — the buy-side's unpublished call)* · AM Z2.4 *(the active manager's in-house team)* · HF Z3.1 *(the hedge-fund analyst)*.

### Z2.6 · Branch — Independent & Alternative Research `[branch]` ★ GLOBAL (G195)
**Quick definition.** Independent research is sold directly to investors by firms with no banking or brokerage arm — and increasingly, "alternative" research built on novel datasets and machine analysis rather than the traditional analyst note.
**Explainer covers.**
- The conflict-free pitch: with no investment bank to please and no order flow to chase, independent research can be genuinely objective — its only product *is* the research, so it lives or dies on being right (and on being priced separately, which MiFID II made the norm).
- Two flavors: **traditional independents** (boutiques selling deep fundamental work directly) and **alternative-data providers** (firms selling credit-card panels, satellite imagery, web-scraped pricing, app-download data — the raw mosaic, productized).
- How alt-data changes the edge: it industrializes the channel check (★G190) — what an analyst once gathered by phone, a vendor now sells as a dataset, compressing the informational advantage and pushing the edge toward *interpretation* rather than *gathering*.
- The AI frontier: machine reading of filings, earnings-call transcripts, and unstructured data is beginning to automate parts of the model-build and the first-pass analysis — a potential disruption of the research *product*, not just an input to it.
- **GAP / recency flag.** Koller (2020) is the most recent source and does not reach the alt-data/AI disruption of the research business; Valentine predates it entirely. This node's forward-looking content is grounded in general knowledge, and the "where it's heading" question is flagged again at Z5.7.
**Connects to.** Z1.3 (★G83) · Z3.3 (★G190 — alt-data as industrialized channel checks) · Z5.2 (★G197 — independents as unbundling beneficiaries) · Z5.7 (the AI/alt-data future) · HF Z3.x *(quant and data-driven hedge funds as the core buyers of alt-data)* · ★G125 market efficiency *(AM — alt-data compresses the inefficiency the edge feeds on)*.

### Z2.7 · The Style Lens on Coverage `[branch]`
**Quick definition.** The same value/growth/quality lenses that sort active managers also sort how an analyst frames a stock — because a "buy" only means something relative to *why* a stock is attractive.
**Explainer covers.**
- The reused frame (Asset Management Z2.4–2.7): **value**, **growth**, and **quality** are the three dominant lenses (★G149 style) — and an analyst implicitly adopts one when they argue a thesis, because the *reason* a stock is cheap differs by lens.
- How the lens shapes the call: a value-framed buy says "the market overweights the bad news, the multiple is too low for the companion variable" (Damodaran, Z3.8); a growth-framed buy says "the market underestimates the durability of the growth"; a quality-framed buy says "the market underpays for the ROIC and the moat" (Koller's ROIC-drives-value, Z3.5).
- Why this matters for the buy-side reader: a value PM and a growth PM want *different research* on the same stock, and the best analysts know which lens their differentiated view lives in.
- The connection to the companion variable: each style lens pairs a multiple with the fundamental it should be read against — value watches P/E vs. growth and P/B vs. ROE, growth watches the growth rate's durability, quality watches the ROIC-vs-WACC spread.
- The honest limit: style is a *framing* device, not a substitute for being right — a correctly-identified cheap stock in the wrong style framing is still a good call; the framing just determines which clients buy it.
**Connects to.** Z3.8 (Damodaran's multiples + companion variable) · Z3.9 (forming the thesis within a lens) · ★G149 style *(AM Z2.4 — the home of the style concept)* · AM Z2.5 *(value)* · AM Z2.6 *(growth)* · AM Z2.7 *(quality)* · ★G125 market efficiency *(the inefficiency each lens exploits)*.
---

# PART 4 · Zone 3 — The Research Process

*The analytical heart of the module. This is the sell-side analyst's five-task workflow rendered in full: from finding what matters, to gathering the edge, to building the model, to valuing the company, to forming and publishing the call. Every global this zone introduces is a link in that chain. The valuation toolkit (Z3.7–3.8) is **inherited wholesale from Investment Banking** and reframed; everything else is the analyst's own craft.*

### Z3.1 · Process Overview — From Blank Page to Published Call `[process]`
**Quick definition.** The research process runs the five tasks in sequence — factors, model, valuation, call, communication — but the order conceals a loop, because each new data point sends the analyst back to the top.
**Explainer covers.**
- The linear spine (the five tasks, Z1.5): identify the **critical factors** (Z3.2) → build the **model** (Z3.4) → check the work against reality (Z3.3, Z3.5) → set **estimates** (Z3.6) → **value** the company (Z3.7–3.8) → form the **thesis** (Z3.9) → publish a **target** (Z3.10) and a **rating** (Z3.11) in a **report** (Z3.12).
- Why it's really a loop: the model reveals which factors matter; the channel checks revise the model; the valuation exposes which assumption the whole call rests on — so the process iterates rather than marches.
- The single organizing question underneath every step (Valentine): *where is my view different from the consensus, and why am I right?* A step that doesn't move the analyst toward a differentiated, defensible view is wasted motion.
- The "2% that matters" discipline as a time-allocation rule: most of the process should be spent on the few critical factors, not on perfecting the immaterial line items of the model.
- How this zone maps to maintenance (Zone 4): initiating coverage runs the whole process once from scratch; maintaining coverage re-runs the loop every quarter (Z4.2) as the earnings cycle delivers new information.
**Connects to.** Z1.5 (the five tasks) · Z3.2 → Z3.12 *(the whole chain)* · Z4.2 (★G192 — the loop's quarterly heartbeat) · ★G121 the thesis *(HF — the object the process produces)* · ★G136 the edge *(HF Z5.1 — what the process is hunting for)*.

### Z3.2 · Identifying the Critical Factors `[core]` ★ GLOBAL (G191)
**Quick definition.** The critical factors are the few variables that actually determine a stock's performance — and Valentine's central claim is that finding and monitoring *those*, not building a bigger model, is the whole of the analyst's edge.
**Explainer covers.**
- The core idea (Valentine, Ch7–8): of the hundreds of things you *could* track about a company, only a handful are **critical factors** that genuinely swing the stock — "the 2% that matters." Everything else is detail that creates false precision.
- The two layers: **sector-level** critical factors (the commodity price, the regulatory regime, the cycle — Ch7) and **stock-level** critical factors (this company's specific volume driver, its key product, its one vulnerable margin — Ch8).
- Why this is where alpha lives: if you forecast the immaterial things better than consensus, you gain nothing; the edge comes from having a *differentiated and correct* view on the factor that actually moves the price.
- How to find them: historical sensitivity analysis (which variable, when it moved, moved the stock), management's own disclosures about what they watch, and the channel checks (Z3.3) that reveal which operating metric leads the financials.
- The link to second-level thinking: identifying the critical factor is necessary but not sufficient — you must then have a view on it that differs from the crowd's *and* be right (★G124), which is the cognitive core of the job.
**Connects to.** Z1.5 (task 1) · Z2.3 (sector frameworks — factors differ by sector) · Z3.3 (★G190 — checking the factors) · Z3.4 (the factors become the model's key drivers) · Z3.6 (★G184 — the estimate *is* the forecast of the critical factor) · ★G124 second-level thinking *(HF Z3.2)* · ★G136 the edge *(HF Z5.1)* · HF Z3.2 *(the buy-side's identical hunt for the variant driver)*.

### Z3.3 · Channel Checks & the Mosaic Theory `[core]` ★ GLOBAL (G190)
**Quick definition.** Channel checks are the practice of building an information edge from many individually-immaterial, lawfully-gathered data points — and the mosaic theory is the legal doctrine that says assembling them into a material conclusion is legitimate, even though trading on a single inside fact is not.
**Explainer covers.**
- What a channel check *is*: calling suppliers, surveying customers, counting cars in parking lots, tracking app downloads, pricing the product in stores — gathering primary data about the critical factors directly, rather than waiting for the company to report them.
- The **mosaic theory** (the legal and ethical core): an analyst may combine many pieces of *non-material, public or lawfully-obtained* information into a conclusion that is itself material and tradeable — the mosaic is greater than any tile.
- The bright line against **MNPI**: a single *material, non-public* fact obtained in breach of a duty (a leak from the CFO) is illegal to trade on. The skill — and the legal jeopardy — is in staying on the mosaic side of the line (the disambiguation callout in Part 1).
- The Koller grounding for *why this is the edge*: markets price public information well but cannot price information they do not yet have — so the legitimate informational advantage lives precisely in the mosaic the analyst assembles before it becomes public.
- The alt-data evolution (Z2.6): much of what analysts once gathered by hand is now sold as datasets (★G195), which compresses the gathering edge and shifts the advantage toward *interpretation* — and raises fresh questions about when a purchased dataset is itself MNPI.
**Connects to.** Z3.2 (★G191 — checking the critical factors) · Z2.6 (★G195 — alt-data as productized mosaic) · Z1.9 (the regulatory line) · Z5.5 (★G200 — Reg FD made the mosaic necessary by banning selective disclosure) · ★G125 market efficiency *(AM — the inefficiency the mosaic exploits)* · ★G136 the edge *(HF)* · HF Z3.3 *(the buy-side's identical primary-research process)*.

### Z3.4 · Building the Earnings Model `[process]` ★ GLOBAL (G183)
**Quick definition.** The earnings model is the analyst's living spreadsheet — a projection of the company's three financial statements forward in time — that turns a view about the critical factors into the specific numbers every downstream output depends on.
**Explainer covers.**
- What the model *is* (Valentine, Ch15–18): a linked **three-statement model** (income statement, balance sheet, cash flow) driven by assumptions about the critical factors, producing forecast revenue, margins, EPS, and free cash flow.
- The build logic: start from the **critical factors** (Z3.2) as the key drivers, forecast the operating line items they control, then let the accounting flow through to EPS and to the free cash flow the valuation will need (★G92, inherited).
- Why the model serves the view, not vice versa: the point of the model is not precision for its own sake but to express *where the analyst's assumptions differ from consensus* and to quantify what that difference is worth.
- The discipline against false precision: most line items should be simple; the analyst's effort belongs in the few driver assumptions that matter (the 2%), not in elaborately forecasting immaterial lines.
- The relationship to the buy-side and to IB: the same modeling skill builds the LBO model (PE), the deal model (IB), and the buy-side analyst's model — this is the shared engine of the whole asset-class series, here pointed at *forecasting to beat consensus* rather than *structuring a transaction*.
**Connects to.** Z3.2 (★G191 — the drivers) · Z3.5 (testing the model's accounting quality) · Z3.6 (★G184 — the model's output *is* the estimate) · Z3.7 (the model feeds the DCF, ★G90/G92) · ★G92 unlevered free cash flow *(IB Z3.4)* · PE Z3.x *(the LBO model — same engine)* · IB Z3.2 *(the deal model)* · Penman *(the financial-statement structure the model projects)*.

### Z3.5 · Quality of Earnings & Forensic Analysis `[core]`
**Quick definition.** Before trusting the reported numbers, the analyst interrogates them — separating durable, cash-backed earnings from accounting artifice — because a model built on manipulated inputs forecasts a mirage.
**Explainer covers.**
- The discipline (Penman): **quality of earnings** analysis separates *operating* performance from *financing* and *accounting* effects, and asks whether reported earnings are backed by cash and likely to persist, or inflated by accruals that will reverse.
- The forensic toolkit (Valentine, Ch11/14): **yellow flags** — aggressive revenue recognition, growing gaps between net income and operating cash flow, rising days-sales-outstanding, one-time items that recur, capitalized costs that should be expensed.
- The Koller grounding — **conservation of value**: accounting changes, buybacks, and EPS-accretive financial engineering do *not* create value because they don't change cash flows. An analyst fooled by an EPS bump that's really conservation-of-value theater has mis-valued the company.
- Why this sits between the model and the estimate: the model is only as good as the inputs; earnings-quality analysis is the audit that decides how much to trust the reported base before forecasting from it.
- The payoff as an edge: spotting deteriorating earnings quality *before* the market is one of the highest-conviction sources of a differentiated *negative* view — and one of the few places a sell-side analyst might justify a rare sell (Z3.11).
**Connects to.** Z3.4 (★G183 — auditing the model's base) · Z3.6 (★G184 — quality-adjusted estimates) · Z3.11 (★G186 — earnings-quality red flags drive the rare sell) · Z4.3 (★G193 — quality determines whether a "beat" is real) · ★G90 DCF *(IB — cash flows, not earnings, drive intrinsic value)* · Penman *(the residual-earnings and accrual-quality spine)* · Koller *(conservation of value)* · HF Z3.x *(short-sellers as earnings-quality specialists)*.

### Z3.6 · Setting Estimates & Forecasting Scenarios `[core]` ★ GLOBAL (G184)
**Quick definition.** The estimate is the model's headline output — a specific forward forecast for EPS, revenue, or EBITDA — and the consensus is the average of all analysts' estimates, the benchmark against which the analyst's differentiated view is defined and later judged.
**Explainer covers.**
- What an **estimate** is: the analyst's point forecast of a critical financial figure (next quarter's EPS, next year's revenue), produced by the model — the concrete, falsifiable expression of the analyst's view.
- What the **consensus** is: the mean (or median) of all covering analysts' estimates — the market's encoded expectation, and therefore (per Valentine) the thing the analyst must *disagree with correctly* to add value. An in-line estimate adds nothing.
- The forecasting point (Valentine, Ch18): the goal is not to nail the exact EPS but to be *right about the direction relative to consensus* — to know the company will beat or miss before the market does.
- Scenario forecasting (Koller's risk discipline): rather than a single guess, build **base / bull / bear** cases with probabilities, valuing each — both to size the risk and to locate the critical assumption the whole call hinges on.
- The expectations-treadmill grounding (Koller): returns are driven by performance *relative to expectations*, so the estimate-vs-consensus gap — not the absolute number — is what determines whether the stock moves. This is the conceptual bridge to the earnings surprise (Z4.3) and the revision (Z4.4).
**Connects to.** Z3.4 (★G183 — the model produces the estimate) · Z3.5 (quality-adjusting the base) · Z3.9 (★G187 — the estimate is the thesis's quantitative core) · Z4.3 (★G193 — surprise = actual vs. this estimate) · Z4.4 (★G188 — revising this estimate) · ★G125 market efficiency *(AM — consensus as the efficient baseline)* · AM Z3.3 *(the active manager's use of estimate dispersion)* · HF Z3.2 *(the "variant perception" = a differentiated estimate)* · Koller *(the expectations treadmill)*.
### Z3.7 · Valuation — The Toolkit, Reused `[core]`
**Quick definition.** To turn estimates into a price target, the analyst reaches for the exact valuation toolkit Investment Banking built — the three methodologies, comps, precedents, and the DCF — but uses it to form a *published view* rather than to *price a transaction*.
**Explainer covers.**
- The inherited toolkit (all from IB, reused wholesale, not rebuilt): the **three core methodologies** (★G87), **comparable companies** (★G88), **precedent transactions** (★G89), the **discounted cash flow** (★G90), **WACC** (★G91), **unlevered free cash flow** (★G92), **terminal value** (★G93), the **football field** (★G94), and the **enterprise-value-to-equity-value bridge** (★G95).
- The reframing (the disambiguation in Part 1): the banker prices a deal that will clear at a negotiated number; the analyst forms a view about where a *continuously-traded* price *should* go. Same math, different artifact — a **price target** (Z3.10), not a deal price.
- The ROIC grounding for the DCF (Koller): intrinsic value comes from ROIC × growth → cash flow; growth only adds value when ROIC exceeds WACC. The analyst's DCF is an expression of that value-creation logic, not a mechanical exercise.
- Why analysts lean on multiples even while modeling in DCF (Koller's candid note): the leading sell-side analyst *values* in DCF but *communicates* in implied multiples — because clients think in multiples and the multiple is the lingua franca of the call (Z3.8).
- The honest caveat: the toolkit produces a *range*, not a point (★G94, the football field); converting that range into a single defensible target is a judgment, and the assumption it's most sensitive to is usually a critical factor (Z3.2).
**Connects to.** Z3.6 (★G184 — estimates feed the valuation) · Z3.8 (intrinsic vs. relative) · Z3.10 (★G185 — the toolkit's output) · ★G87 three methodologies *(IB Z3.1)* · ★G88 comps *(IB Z3.2)* · ★G89 precedents *(IB Z3.3)* · ★G90 DCF *(IB Z3.4)* · ★G91 WACC · ★G92 UFCF · ★G93 terminal value · ★G94 football field *(IB Z3.6)* · ★G95 EV↔equity bridge · Koller *(ROIC → value)*.

### Z3.8 · Intrinsic vs. Relative Valuation & the Multiple `[core]`
**Quick definition.** Damodaran's central distinction: an analyst is either valuing the business on its own cash flows (intrinsic, the investor's question) or pricing it against what the market pays for comparables (relative, the trader's question) — and a multiple is only meaningful when read against the fundamental it should track.
**Explainer covers.**
- The two modes (Damodaran): **intrinsic valuation** asks what the business is worth from its cash flows, growth, and risk (the DCF, ★G90); **relative valuation / pricing** asks what the market will pay, read off a **multiple** (★G88) of comparable companies. Most analyst price targets are, in practice, relative.
- The **four keys to a multiple** (Damodaran): know what's in the numerator and denominator; know the *cross-sectional distribution* (what's high vs. low for this sector); know the **companion variable** that drives it; and know when the multiple breaks.
- The **companion-variable** discipline — the heart of the node: every multiple has a fundamental it should be read against, so "cheap" means a *low multiple relative to its companion variable*. P/E pairs with growth; P/B pairs with ROE; EV/EBITDA pairs with reinvestment/ROIC; EV/Sales pairs with margin. A stock is genuinely undervalued only when its multiple is low *and* its companion variable is high.
- The narrative-and-numbers bridge (Damodaran): a valuation is a *story disciplined by numbers* — and the **three-P test** asks whether the story is *possible*, *plausible*, and *probable*, with the numbers forcing the story to stay honest.
- Why this is the analyst's communication layer: clients debate *multiples*, not DCF assumptions, so the analyst translates the intrinsic view into "this deserves a higher multiple than its peers because its companion variable is better" — the actual language of the call.
**Connects to.** Z3.7 (the toolkit) · Z2.7 (style lenses map to companion variables) · Z3.9 (the thesis as disciplined story) · Z3.10 (★G185 — multiple × estimate = target) · ★G88 comps *(IB Z3.2 — the multiple's home)* · ★G90 DCF *(intrinsic)* · ★G149 style *(AM)* · Damodaran *(intrinsic vs. pricing, the companion variable, the 3P test)* · Koller *(ROIC as EV/EBITDA's companion)*.

### Z3.9 · Forming the Thesis `[core]` ★ GLOBAL (G187)
**Quick definition.** The published thesis is the analyst's reasoned, named, distributed argument for why a stock will move — the same logical object as the hedge-fund analyst's internal thesis, but staked publicly on the analyst's reputation.
**Explainer covers.**
- What a thesis *is*: not a number but an **argument** — "the market is wrong about *this critical factor*, here is why, and here is what the stock is worth when the market realizes it." The estimate and target are its quantitative expression; the reasoning is its substance.
- The contrast with the internal thesis (★G121, the Part 1 disambiguation): the hedge-fund analyst's thesis lives in a memo and is judged only by P&L; the sell-side **published** thesis is *attributed, time-stamped, rated, and ranked* — being wrong is a public, franchise-affecting event (★G196).
- What makes a thesis good (synthesis of the sources): it identifies where consensus is wrong (Valentine), it survives the three-P test as a disciplined story (Damodaran), it rests on a defensible view of the critical factors (Z3.2), and it demands **second-level thinking** (★G124) — a view the crowd doesn't already hold.
- The variant-perception framing (shared with HF Z3.2): a thesis only has value if it differs from consensus *and* proves right; a correct-but-consensus thesis is alpha-free.
- Why the thesis precedes the target, not the reverse: the discipline is to reason to a *view* first and let the target fall out — reverse-engineering a thesis to justify a predetermined target is how analysts fool themselves and their clients.
**Connects to.** Z3.2 (★G191 — the thesis rests on the factors) · Z3.6 (★G184 — the estimate is the thesis quantified) · Z3.8 (the thesis as disciplined story) · Z3.10 (★G185 — the thesis yields the target) · Z3.11 (★G186 — the thesis yields the rating) · ★G121 the internal thesis *(HF Z3 — the unpublished twin)* · ★G124 second-level thinking *(HF Z3.2)* · ★G136 the edge *(HF Z5.1)* · PE Z3.x *(the investment thesis in a deal memo)*.

### Z3.10 · The Price Target `[core]` ★ GLOBAL (G185)
**Quick definition.** The price target is the published, time-bounded number that says where the analyst expects the stock to trade — the bridge between the valuation work and the actionable rating.
**Explainer covers.**
- What a target *is*: a specific price (usually 12-month) the analyst expects the stock to reach, derived by applying the chosen valuation method — most often a target multiple (★G88) to a forward estimate (★G184), cross-checked against the DCF (★G90).
- How it's built in practice: pick the metric and the justified multiple (the companion-variable logic, Z3.8), apply it to the estimate, and sanity-check the implied intrinsic value — the target is where *method meets judgment*.
- The time bound and the implied return: a target implies an expected return from today's price, and that *implied upside/downside* is what mechanically drives the rating (Z3.11) — a 25% implied upside is a buy, a flat target is a hold.
- Why targets get revised (Z4.5): a new estimate, a re-rating of the multiple, or a change in the critical factors moves the target — and target changes are themselves market-moving events that the sell-side publishes constantly.
- The honest limit: a price target is a *judgment expressed as false precision* — clients know the number is softer than it looks, and the best analysts are transparent about the assumption the target is most sensitive to.
**Connects to.** Z3.7 (the toolkit produces it) · Z3.8 (multiple × estimate) · Z3.9 (★G187 — the thesis justifies it) · Z3.11 (★G186 — implied return → rating) · Z4.5 (revising the target) · ★G88 comps *(the target multiple)* · ★G90 DCF *(the intrinsic cross-check)* · ★G94 football field *(IB — the range the target is drawn from)* · AM Z3.3 *(how PMs use targets)*.

### Z3.11 · The Rating `[core]` ★ GLOBAL (G186)
**Quick definition.** The rating is the discrete, published recommendation — buy, hold, or sell — that translates the gap between price target and current price into a single instruction, and it is the output clients actually act on.
**Explainer covers.**
- What a rating *is*: the analyst's bottom line, usually a three-tier scale (buy/outperform, hold/neutral, sell/underperform), mechanically tied to the implied return from the price target but ultimately a *conviction-weighted judgment*.
- The seven critical elements of a stock call (Valentine, Ch20/25): a good recommendation specifies the thesis, the catalyst, the time frame, the target, the risk/reward, the variant view vs. consensus, and what would prove it wrong — a rating without these is just a label.
- The **buy-rating bias** (Damodaran — a structural, named distortion): analysts issue far more buys than sells, because a sell rating jeopardizes management access, angers a potential banking client (★G199), and invites institutional pushback. The honest analyst must fight this bias; the rare, well-reasoned sell is among the most valuable and credible calls on the Street.
- Why "hold" is often a disguised sell: given the buy-bias, a downgrade to hold frequently *means* sell, and sophisticated clients read the rating distribution and the direction of change, not just the label.
- The catalyst question: a rating needs a *reason the gap will close* — a catalyst (an earnings event, a product launch, a corporate action) that will force the market to re-rate, because a cheap stock can stay cheap without one.
**Connects to.** Z3.9 (★G187 — the thesis) · Z3.10 (★G185 — implied return drives the rating) · Z3.5 (earnings-quality flags → the rare sell) · Z4.5 (rating changes) · Z5.4 (★G199 — the conflict behind the buy-bias) · Damodaran *(the buy-rating bias)* · Valentine *(the seven elements of a call)* · AM Z3.3 *(how active managers weight ratings)* · HF Z3.x *(the buy-side's freedom to issue the conviction sell)*.

### Z3.12 · Initiating Coverage — Publishing the Report `[process]` ★ GLOBAL (G182)
**Quick definition.** The research report is the written, distributed artifact that carries the rating, target, and reasoning to clients — and the *initiation of coverage* is its grandest form: the long, foundational launch that establishes an analyst's view of a newly-covered stock.
**Explainer covers.**
- What the **report** is (Valentine, Ch23–26): the unit in which research is actually *delivered* — the **initiation** (a deep, comprehensive launch of coverage, often dozens of pages) and the ongoing **note** (a short, frequent update, taught in Zone 4). Both are ★G182.
- What an initiation contains: the investment thesis (★G187), the rating and target, the full model summary, the critical-factors analysis, the valuation, the risks, and the variant view vs. consensus — it is the analyst's complete argument, published.
- The craft of communication (task 5, Valentine): a report must *persuade* a busy professional — clear thesis up front, the differentiated view foregrounded, the reasoning auditable. Being right but unread adds no value; communication is a skill, not a formality.
- The compliance overlay (Z5.5): every published report carries the **Reg AC** certification (★G200), required disclosures of conflicts (★G199), and must clear the firm's editorial and legal review — and is silenced entirely during banking **quiet periods**.
- The distribution mechanics (Z1.8): the report goes out through the **sales force** to all clients at once (Reg FD-compliant, Z5.5), and is amplified on the morning call — the research triangle (★G198) in action.
**Connects to.** Z3.9 (★G187 — the thesis the report carries) · Z3.10 (★G185) · Z3.11 (★G186) · Z4.1 (the note as the maintenance unit) · Z5.5 (★G200 — the certification and review) · Z1.8 (★G198 — distribution) · ★G94 football field *(IB — the valuation exhibit in the report)* · IB Z2.8 *(quiet-period silencing around the firm's deals)* · AM Z2.4 *(the client who reads it)*.
---

# PART 5 · Zone 4 — Maintaining Coverage

*Initiating coverage (Zone 3) is a one-time event; maintaining it is the job. This zone is the analyst's ongoing life — organized entirely around the quarterly earnings cycle — where the five tasks run again and again as new information arrives, estimates get revised, and the relationships that make the information flow possible are tended.*

### Z4.1 · The Ongoing Job — Coverage as a Standing Commitment `[core]`
**Quick definition.** Once an analyst initiates coverage, they owe the market a continuous stream of maintained estimates, updated targets, and timely notes — coverage is a subscription the analyst keeps paying, not a report they file once.
**Explainer covers.**
- What "maintaining" means: keeping the model (★G183) live, the estimates (★G184) current, the target (★G185) and rating (★G186) defensible, and the client informed through a steady flow of **notes** (★G182) — the short-form report that is the daily unit of maintenance.
- The rhythm that organizes it all: the **quarterly earnings cycle** (★G192, Z4.2) is the metronome — everything in an analyst's calendar is "before the print," "the print," or "after the print."
- The re-running of the five tasks: every new data point (an earnings release, a channel check, a competitor's result, a macro shift) sends the analyst back through factors → model → valuation → call → communicate.
- The maintenance trade-off: an analyst covering more names (Z2.2) has more to maintain, which strains depth — the post-MiFID-II economics (★G197) made maintaining marginal small-cap coverage uneconomic, shrinking universes.
- Why timeliness is a franchise issue: being *first* with a correct revision after news is part of the value clients pay for and vote on (★G196) — a stale model is a dead franchise.
**Connects to.** Z4.2 (★G192 — the heartbeat) · Z3.x *(the tasks being re-run)* · Z5.1 (★G196 — timeliness builds the franchise) · ★G182 the note *(the maintenance unit)* · ★G197 *(economics of what's worth maintaining)* · AM Z2.4 *(the client depending on the maintained view)*.

### Z4.2 · The Quarterly Earnings Cycle `[process]` ★ GLOBAL (G192)
**Quick definition.** The earnings cycle is the recurring three-beat rhythm — the results *print*, the management *call*, and the analyst's model *update and note* — around which the entire research calendar is built.
**Explainer covers.**
- The three beats: **(1) the print** — the company releases quarterly results (the actuals that get compared to the estimate); **(2) the call** — management hosts the earnings call, giving color and, crucially, **guidance** (★G193) about the future; **(3) the update** — the analyst revises the model, the estimate, and possibly the target/rating, and publishes a note.
- The pre-print ritual: in the run-up, the analyst sharpens the estimate, runs final channel checks (★G190), and often publishes a preview laying out what to watch and where their view differs from consensus.
- Why the call matters as much as the print: the *forward* guidance management gives on the call often moves the stock more than the *backward* results — because (Koller's expectations treadmill) the market prices the change in expectations, not the quarter just ended.
- The compressed timeline: earnings season concentrates dozens of prints into a few weeks, and the analyst's value is partly *speed* — a fast, correct update beats a slow, perfect one (the franchise, ★G196).
- The loop closure: the earnings cycle is what makes the research process (Zone 3) iterative — each quarter delivers the new information that restarts the five tasks.
**Connects to.** Z4.1 (the ongoing job) · Z4.3 (★G193 — surprise and guidance happen here) · Z4.4 (★G188 — the cycle triggers revisions) · Z3.1 (the process loop the cycle drives) · ★G184 consensus *(what the print is measured against)* · Koller *(the expectations treadmill — why guidance moves stocks)* · AM Z3.3 *(PMs trading the cycle)* · HF Z3.x *(event-driven funds trading the print)*.

### Z4.3 · Earnings Surprises & Company Guidance `[core]` ★ GLOBAL (G193)
**Quick definition.** An earnings surprise is the gap between reported results and consensus; guidance is the forward expectation management itself sets — and these twin events, not the absolute results, are what move stocks at the print.
**Explainer covers.**
- The **surprise**: reported EPS/revenue *versus* the consensus estimate (★G184). A "beat" is above consensus, a "miss" below — and the *magnitude and direction* of the surprise, relative to what was already priced, drives the stock reaction.
- **Guidance**: the company's own forward forecast (next quarter, full year), issued on the call. Raised guidance signals confidence; cut guidance signals trouble; *withdrawn* guidance signals uncertainty — and guidance often matters more than the quarter reported.
- The expectations-treadmill core (Koller): because returns track performance *relative to expectations*, a company can beat consensus and *fall* (if the beat was smaller than the "whisper" number, or guidance disappointed) or miss and *rise* (if the miss was already feared). The analyst's job is to know where the *real* bar is.
- The earnings-quality overlay (Z3.5): not every beat is real — a beat driven by a low tax rate, a one-time item, or aggressive accruals (conservation of value, Koller) is a low-quality beat the analyst must flag rather than celebrate.
- Why this is dense with edge: having a differentiated, correct view on whether a company will beat/miss *and* on how guidance will land — before the print — is one of the most direct sources of alpha in the whole job (Z3.2, ★G124).
**Connects to.** Z4.2 (★G192 — surprise/guidance occur in the cycle) · Z4.4 (★G188 — a surprise triggers revisions) · Z3.5 (earnings quality — is the beat real?) · Z3.6 (★G184 — surprise = actual vs. estimate) · Koller *(the expectations treadmill, conservation of value)* · ★G124 second-level thinking *(knowing the real bar)* · AM Z3.3 · HF Z3.x *(event-driven trading)*.

### Z4.4 · Estimate Revisions & the Revision Cycle `[core]` ★ GLOBAL (G188)
**Quick definition.** An estimate revision is the analyst raising or lowering their forecast as new information arrives — and the *pattern* of revisions across the analyst community is itself one of the most powerful, most-studied signals in markets.
**Explainer covers.**
- What a **revision** is: a change to the published estimate (★G184) — and, often, to the target (★G185) and rating (★G186) — prompted by an earnings surprise, new guidance, a channel check, or a macro shift.
- The direction that matters: revisions tend to **cluster and trend** — one analyst's cut is often followed by others (the "revision cycle"), because new information diffuses gradually and analysts are reluctant to be the lone outlier.
- Why revisions are a tradeable signal (the AM/HF link): **estimate-revision momentum** is a well-documented factor — stocks with rising estimates tend to outperform — which is why the buy-side watches the *revision trend*, not just the level (AM Z3.3, HF Z3.x).
- The surprise-revision distinction (the Part 1 disambiguation): a *surprise* is the company moving relative to the analyst; a *revision* is the analyst moving relative to reality. A surprise typically *triggers* a wave of revisions — the two are cause and effect.
- The analyst's franchise stake: being *early and right* on a major revision (the first to cut before a miss, the first to raise before a beat) is exactly the differentiated, timely call that builds the franchise (★G196) and wins client votes.
**Connects to.** Z4.3 (★G193 — surprises trigger revisions) · Z4.2 (★G192 — the cycle's rhythm) · Z4.5 (revisions move targets/ratings) · Z3.6 (★G184 — what's being revised) · ★G125 market efficiency *(AM — gradual information diffusion = the inefficiency)* · AM Z3.3 *(revision momentum as a factor)* · HF Z3.x *(trading the revision trend)* · ★G196 *(early revisions build the franchise)*.

### Z4.5 · Ratings & Target Changes `[process]`
**Quick definition.** Changing a rating or a price target is the analyst's most visible public act — a discrete, market-moving event that publishes a shift in the view, and that clients and the media watch closely.
**Explainer covers.**
- The mechanics: an **upgrade/downgrade** (a rating change, ★G186) or a **target revision** (★G185) is published in a note, and because it's a discrete change in a named analyst's public stance, it can move the stock on its own — sometimes more than the underlying news.
- Why changes lag or lead: a brave analyst changes the call *ahead* of the news (the valuable, franchise-building move); a cautious one waits for confirmation (safer but alpha-free) — and the buy-bias (Damodaran, Z3.11) makes downgrades rarer and therefore more informative.
- The "double-edged" nature: a downgrade angers the covered company (straining the access the analyst needs, Z4.6) and may collide with the firm's banking relationship (★G199) — so a rating cut is never *only* an analytical act.
- How clients read the *change*, not the level: given rating inflation, the *direction and surprise* of a change carries more information than the absolute rating — a downgrade from buy to hold is a real signal even though "hold" sounds neutral.
- The link to revisions: rating/target changes are usually the *published consequence* of an estimate revision (Z4.4) — the revision moves the numbers, the changed numbers move the target, the moved target trips the rating.
**Connects to.** Z3.10 (★G185 — the target being changed) · Z3.11 (★G186 — the rating being changed) · Z4.4 (★G188 — revisions drive the changes) · Z4.6 (the relationship cost of a downgrade) · Z5.4 (★G199 — the banking-conflict overlay) · Damodaran *(the buy-bias that makes downgrades informative)* · AM Z3.3 · HF Z3.x.

### Z4.6 · Managing Company Relationships `[core]`
**Quick definition.** An analyst's information flow depends on access to the covered company's management — a relationship that must be cultivated without crossing into selective disclosure (Reg FD) or letting access compromise objectivity.
**Explainer covers.**
- Why the relationship matters: management is a primary source for understanding the critical factors (Z3.2) — earnings calls, investor days, conference fireside chats, and (compliant) one-on-ones are how the analyst calibrates the model.
- The **Regulation FD** boundary (Valentine, Ch9): since 2000, companies may *not* selectively disclose material information to favored analysts — everything material must be public and simultaneous. This is precisely *why* the lawful mosaic (★G190) became the analyst's edge: the company can no longer just whisper the number.
- The objectivity tension: too-cozy access creates pressure to stay bullish (lose the access if you downgrade), feeding the buy-bias (Z3.11) — the analyst must protect independence against the relationship that feeds them.
- Corporate access as a product (Z1.4): the analyst's management relationships are something the *buy-side* pays for — getting PMs in front of management — which MiFID II's unbundling (★G197) forced to be priced separately and scrutinized.
- The banking-conflict shadow (★G199): the covered company may also be a banking client of the analyst's firm, which is exactly the conflict the wall (IB Z1.10) and the Global Settlement (Z5.4) exist to manage.
**Connects to.** Z3.2 (★G191 — management as a factor source) · Z3.3 (★G190 — Reg FD made the mosaic necessary) · Z4.7 (the other relationship — clients) · Z5.4 (★G199 — company as banking client) · Z5.5 (★G200 — Reg FD) · Valentine *(Ch9, managing access)* · IB Z1.10 *(the wall)*.

### Z4.7 · Managing Client & Sales-Force Relationships `[core]`
**Quick definition.** The analyst's research only has value if it's *used*, so a large part of the job is communicating with the buy-side clients who vote on the franchise and the internal sales force who carry the ideas to them.
**Explainer covers.**
- The two audiences: **buy-side clients** (the PMs and analysts who consume the research, Z1.4) and the firm's own **sales force** (who distribute it, ★G198) — and the analyst spends real time on both, not just on analysis.
- The daily mechanics: the **morning call** (pitching the day's ideas to the sales force), client calls and visits, bespoke work for top clients, and conference/corporate-access hosting — communication (task 5) as a continuous activity.
- Why clients matter to the franchise: the buy-side clients are exactly who *vote in the II survey* (★G196, Z5.1) — so servicing them well is not just helpful, it's how the analyst's reputational capital and compensation are determined.
- The interaction-effort tension (Valentine, Ch6 from the buy-side view): clients are simultaneously demanding the analyst's best ideas, their model, their access, *and* their time — and the analyst must allocate a scarce resource (attention) across a ranked client list.
- The unbundling pressure (★G197): once research and access must be paid for separately (MiFID II), clients ruthlessly prioritize which analysts they pay for — raising the bar for the client-servicing that sustains the franchise.
**Connects to.** Z1.4 (the clients) · Z1.8 (★G198 — the sales force) · Z5.1 (★G196 — clients vote the franchise) · Z4.1 (servicing as part of maintenance) · ★G197 *(unbundling raises the servicing bar)* · AM Z2.4 *(the client institution)* · HF Z3.1 *(the most demanding clients)*.
---

# PART 6 · Zone 5 — The Franchise

*Zone 3 was the craft and Zone 4 the routine; this zone is the business and the institution around them. What is an analyst's reputation actually worth, how does the research product make money, what conflict shadows the whole enterprise, what rules cage it, and where is it all heading. This is also where the module's deepest source gaps live — the modern economics and the AI/alt-data future are flagged, not invented.*

### Z5.1 · The Research Franchise & Analyst Rankings `[core]` ★ GLOBAL (G196)
**Quick definition.** A sell-side analyst's franchise is their reputational capital — historically measured by the *Institutional Investor* poll — which determines their client access, their compensation, and their influence over how a stock trades.
**Explainer covers.**
- What the **franchise** is: the analyst's standing with the buy-side — the degree to which clients seek out, trust, and act on their work. It is an intangible asset that the analyst spends a career building and can lose with a few bad calls.
- The **Institutional Investor (II) ranking** (Valentine): the canonical scoreboard — buy-side clients vote annually for the best analysts in each sector, and a top-ranked ("II-ranked") analyst commands access, compensation, and corporate-access pull.
- What builds it: differentiated and *correct* calls (Z3.9), being early and right on revisions (Z4.4), deep sector expertise (Z2.3), responsive client service (Z4.7), and the corporate access the analyst can broker (Z4.6).
- The franchise-vs-league-table distinction (the Part 1 disambiguation): the II ranking measures whose *ideas* the buy-side values (★G196); the IB **league table** (★G104) measures whose *deals* won. A great analyst can sit at a mediocre bank, and vice versa.
- Why the franchise is the analyst's real product: in a world where the *information* is increasingly commoditized (alt-data, Z2.6), the durable asset is trust and judgment — the things a ranking actually measures.
**Connects to.** Z4.7 (client service builds it) · Z4.4 (early revisions build it) · Z3.9 (★G187 — good theses build it) · Z5.2 (★G197 — the franchise is what gets paid) · ★G104 the league table *(IB Z4.x — the deal-side scoreboard)* · ★G136 the edge *(HF)* · AM Z2.4 *(the clients who vote)* · HF Z3.1 *(the most influential voters)*.

### Z5.2 · How Research Makes Money `[core]`
**Quick definition.** Research is a cost center that justifies itself indirectly — historically by generating the trading commissions and banking goodwill that paid for it, a model that MiFID II's unbundling has thrown into crisis.
**Explainer covers.**
- The historical economics (★G197, Z1.7): research was paid for through **bundled trading commissions** and **soft dollars** — the buy-side over-paid on execution, and a slice funded the research and access. Research itself was never invoiced.
- The banking subsidy (the conflicted part): research also justified itself by supporting the bank's **equity capital markets** franchise (IB Z2.8) — a respected analyst helped win IPO and follow-on mandates, which is exactly the conflict the Global Settlement (Z5.4) attacked.
- The **MiFID II unbundling** rupture (2018): forcing European asset managers to pay for research separately and explicitly collapsed research budgets, triggered analyst layoffs, and shrank coverage — especially of small- and mid-caps that became uneconomic to follow.
- The survival reshaping: consolidation toward a few top-ranked analysts per sector, the rise of independents (★G195) who were always priced separately, and experiments with per-interaction and subscription pricing.
- **GAP / recency flag — the module's largest.** No source in the folder covers the post-2018 research economics; Valentine (2011) predates it entirely. The *direction* (unbundling → budget collapse → consolidation) is well-established general knowledge, but the *current quantitative state* of the research business model is a genuine gap, to be filled when this module's depth layer is authored.
**Connects to.** Z1.7 (★G197 — the home of the economics) · Z5.1 (★G196 — the franchise that gets paid) · Z5.3 (★G198 — commissions flow through the triangle) · Z5.4 (★G199 — the banking subsidy as conflict) · Z2.6 (★G195 — independents as beneficiaries) · IB Z2.8 *(the ECM franchise research supports)* · AM Z5.x *(the manager's research budget)*.

### Z5.3 · The Sales / Trading / Research Triangle, In Depth `[core]`
**Quick definition.** The sell-side equities division is a triangle of three desks — research makes the ideas, sales distributes them, trading executes the resulting orders — and the commissions from that trading historically funded the whole structure (the global ★G198 is introduced at Z1.8; this node deepens it).
**Explainer covers.**
- The three desks in depth (Z1.8 introduced them): **research** (the analysts and their notes), **sales** (the salespeople who carry ideas to clients and relay feedback), **trading** (the desk that executes client orders and provides liquidity).
- The flows that bind them: *ideas* flow research → sales → client; *orders* flow client → sales → trading; *commissions* flow client → firm → (historically) research. Cut any flow and the economics break.
- The morning call as the triangle's daily ritual: analysts pitch the sales force, sales arms itself with the day's ideas, and the best ideas convert into client orders that the trading desk fills.
- How unbundling (★G197) decoupled the triangle: once research must be paid for with hard dollars separately from execution, the "commissions fund research" leg is severed, and research's economic link to trading weakens — a structural strain the model is still absorbing.
- The compliance geometry: research, sales, and trading sit *together* on the public side of the **information wall** (IB Z1.10), walled off from banking — but selective-disclosure (Reg FD) and front-running rules (Z5.5) still govern how information moves *within* the triangle.
**Connects to.** Z1.8 (the triangle introduced) · Z5.2 (★G197 — the economics) · Z5.5 (★G200 — rules within the desks) · Z4.7 (the analyst's work with sales) · IB Z1.10 *(the wall around the triangle)* · HF Z1.x *(prime brokerage — the trading relationship from the buy-side)*.

### Z5.4 · The Research/Banking Conflict & the Global Research Settlement `[core]` ★ GLOBAL (G199)
**Quick definition.** The structural conflict at the heart of sell-side research is that investment-banking revenue can corrupt the objectivity of the research — and the 2003 Global Research Settlement, following Eliot Spitzer's investigations, was the regulatory response that walled the two apart.
**Explainer covers.**
- The conflict (the core): a bank earns enormous fees from **investment banking** (IPOs, M&A, IB Z2.x), and a covered company is often a banking client or prospect — creating pressure on the analyst to publish favorable research to win or keep the banking business.
- The scandal (Valentine; general knowledge): in the dot-com era, analysts were found privately disparaging stocks they publicly rated "buy" to support their banks' underwriting — the abuse that made the conflict undeniable.
- The **Global Research Settlement** (2003): the landmark settlement between regulators and the major banks that erected the **information wall** between research and banking (IB Z1.10), barred banking from influencing analyst pay, prohibited analysts from soliciting banking business, and funded independent research.
- The buy-bias connection (Damodaran, Z3.11): even after the wall, the *residual* pressure to maintain corporate access and avoid angering banking clients sustains the structural tilt toward buy ratings — the settlement curbed the conflict but did not erase its gravity.
- The link to the rest of the regulatory frame: the settlement is the *structural* remedy (separation); **Reg AC** and **Reg FD** (Z5.5) are the *behavioral* remedies (certification and disclosure) — together they form the cage around modern research.
- **GAP / recency flag.** Grounded in Valentine's ethics treatment plus the IB module's wall plus general knowledge; no securities-law source sits in the folder, and the post-settlement evolution (and MiFID II's distinct conflict rules) is part of the same gap.
**Connects to.** Z1.9 (the regulatory frame) · Z3.11 (★G186 — the buy-bias the conflict drives) · Z5.5 (★G200 — the behavioral remedies) · Z5.2 (★G197 — the banking subsidy the settlement attacked) · IB Z1.10 *(the information wall the settlement built)* · IB Z2.8 *(the ECM business at the conflict's center)* · PE Z1.x *(banks' advisory conflicts more broadly)*.

### Z5.5 · Regulation AC, Reg FD & Compliance `[core]` ★ GLOBAL (G200)
**Quick definition.** The behavioral rulebook of research: Regulation AC forces analysts to certify their views are genuinely their own, Regulation FD bars companies from selective disclosure, and quiet periods silence research around the firm's own deals.
**Explainer covers.**
- **Regulation AC (Analyst Certification)**: every published report must carry the analyst's signed certification that the views expressed are *truly their own* and that no part of their compensation was tied to the specific recommendation — a direct response to the Spitzer-era abuses (Z5.4).
- **Regulation FD (Fair Disclosure)**: companies must disclose material information to *everyone simultaneously*, not selectively to favored analysts (Z4.6) — which, as noted throughout, is *why* the lawful mosaic (★G190) became the analyst's edge.
- **Quiet periods**: research must go silent on a company around the firm's own underwriting of that company's securities (especially the IPO, IB Z2.8) — preventing research from being used as a marketing arm for the banking deal.
- The publication compliance stack (Valentine, Ch27): every note runs a gauntlet of required **conflict disclosures** (the firm's banking relationships, the analyst's holdings), editorial review, and legal/compliance sign-off before distribution.
- The MNPI prohibition as the criminal backstop (Z3.3): beyond these civil rules sits the bright line against trading or tipping **material non-public information** — the doctrine that separates the legitimate mosaic from insider dealing.
- **GAP / recency flag.** As with Z5.4, grounded in Valentine plus general knowledge; no dedicated securities-law source is in the folder. The rules are stated at the level a learner needs, not at the level of legal practice.
**Connects to.** Z1.9 (the regulatory frame) · Z3.3 (★G190 — Reg FD made the mosaic the edge) · Z3.12 (★G182 — the certification/disclosure on every report) · Z4.6 (Reg FD in the company relationship) · Z5.4 (★G199 — the structural remedy this complements) · IB Z2.8 *(the quiet period around the IPO)* · IB Z1.10 *(the wall)*.

### Z5.6 · The Career & the Sell-Side → Buy-Side Path `[branch]`
**Quick definition.** The classic equity-research career runs from associate to ranked senior analyst on the sell-side — and then, very often, across the aisle to the buy-side, where the same analytical skill is rewarded with returns instead of rankings.
**Explainer covers.**
- The sell-side ladder: **associate/junior analyst** (builds models, does channel-check legwork) → **senior/lead analyst** (owns coverage, makes the calls, builds the franchise, ★G196) — a path measured in II rankings and client votes.
- The defining career move: the jump to the **buy-side** (★G194) — joining an asset manager or hedge fund as an analyst or PM, trading publication and rankings for privacy and P&L (the information ratio, ★G112, becomes the scoreboard).
- Why the move is so common: the same skills (finding the critical factors, modeling, forming a thesis) transfer directly, and the buy-side offers freedom from the buy-bias, the quiet periods, and the client-servicing grind — plus, often, more money.
- What's lost and gained in the crossing: the sell-side analyst gives up the franchise and the platform but gains the ability to *act* on conviction (including the conviction short, Z3.11) and to be judged purely on being right.
- The reshaping of the path by economics (★G197): the unbundling-driven shrinkage of sell-side seats has made the sell-side a narrower funnel — intensifying the pull toward the buy-side and toward independents (★G195).
**Connects to.** Z1.6 (the team structure the ladder sits in) · Z2.5 (★G194 — the buy-side destination) · Z5.1 (★G196 — the sell-side scoreboard) · ★G112 information ratio *(HF — the buy-side scoreboard)* · ★G197 *(economics reshaping the path)* · HF Z3.1 *(the buy-side analyst role)* · AM Z2.4 *(the active-management destination)*.

### Z5.7 · Where Equity Research Is Heading `[core]`
**Quick definition.** Equity research is being reshaped by three converging forces — the unbundling aftermath, the rise of alternative data, and the arrival of AI — that together pressure the traditional analyst note and push the edge from *information-gathering* toward *judgment*.
**Explainer covers.**
- **The unbundling aftermath** (★G197): MiFID II permanently changed the economics — fewer analysts, shrunken coverage, a premium on the very top of the franchise, and an opening for differentiated independents. The traditional "research-for-commissions" model is structurally diminished.
- **The alt-data wave** (★G195): when the channel check (★G190) is sold as a dataset, the *gathering* edge erodes and the advantage migrates to *interpretation* — knowing which data matters (the critical factors, Z3.2) and what it means, rather than being the one who collected it.
- **The AI frontier**: machine reading of filings and transcripts, automated model-building, and natural-language synthesis threaten to commoditize the *mechanical* parts of research — raising the question of whether the analyst's durable value is the model or the *judgment* the model can't supply (echoing AM Z5.6's automation/passive pressures).
- The throughline (Koller): markets price public information well, so as information becomes cheaper and faster to gather, the durable edge is precisely in the things that *aren't* in the public data yet — original judgment about the critical factors and where the consensus is wrong (Z1.1).
- **GAP / recency flag — flagged throughout.** Koller (2020) is the most recent source and does not reach the AI disruption; all three forces' *current* state is beyond the folder's sources. This node frames the *direction* from first principles and general knowledge, and marks the forward-looking content as a deliberate seam for the depth layer.
**Connects to.** Z5.2 (★G197 — the economics being reshaped) · Z2.6 (★G195 — alt-data and AI) · Z3.3 (★G190 — the gathering edge being commoditized) · Z3.2 (★G191 — judgment about factors as the durable edge) · Z1.1 (what research is *for*, restated) · AM Z5.6 *(the passive/automation pressure on active management)* · Koller *(why judgment outlasts information)* · HF Z3.x *(quant/alt-data funds as the leading edge)*.
---

# PART 7 · Cross-Zone & Cross-Module Connective Tissue

*The map's edges are the product. This section makes the densest cross-module connections explicit — the wiring that makes Equity Research not a standalone module but the analytical engine plugged into the whole asset-class series.*

### The spine: Equity Research as the sell-side engine feeding the buy-side
The single most important bridge is **★G83**, the sell-side/buy-side divide inherited from Investment Banking. Equity Research *is* the sell-side's analytical output, and its entire reason for existing is to be consumed by the buy-side:
- **→ Asset Management (AM Z2.4, Z3.3):** active equity managers are the core institutional client. They consume sell-side estimates (★G184), targets (★G185), and ratings (★G186) as *one input*, then form their own view. The estimate-revision signal (★G188) is a documented factor in their process (AM Z3.3).
- **→ Hedge Funds (HF Z3.1–3.3):** the hedge-fund analyst does the *same cognitive work* as the sell-side analyst (find the variant view, build the thesis) but keeps it internal (★G194) and acts on it with leverage and shorts. The buy-side's freedom to issue the conviction *sell* is the mirror of the sell-side's buy-bias (Z3.11).
- The buy-side analyst and the sell-side analyst are the **same role split by who-publishes and who-pays** — the deepest structural symmetry in the module (★G187 vs. ★G121).

### The shared toolkit: built in Investment Banking, reused here
The entire valuation apparatus (**★G87–G95**) was authored in the IB module and is reused *wholesale* in Equity Research's Zone 3.7–3.8 — not rebuilt, only **reframed** from "pricing a deal that will clear" to "publishing a view on where a traded price should go." This is the clearest instance of the inheritance-first principle: the IB valuation toolkit is now standing infrastructure that every valuation-using module points to. Damodaran's intrinsic-vs-pricing distinction and Koller's ROIC→value logic are the *interpretive layer* the analyst adds on top of the inherited mechanics.

### The skill metrics: Equity Research judged by Hedge Fund's yardsticks
An analyst's track record is measured by the **same statistics the buy-side lives by**:
- **★G112 (information ratio)** and **★G113 (information coefficient / hit rate):** a sequence of published calls is a sequence of bets, scoreable exactly as a portfolio's returns. The franchise (★G196) is the reputational expression of a good IC.
- **★G114 (breadth)** and **★G115 (the Fundamental Law):** covering more names well multiplies the chances to add value — the same breadth×skill logic that governs portfolio construction governs the size of a coverage universe (Z2.2).
- **★G124 (second-level thinking)** and **★G136 (the edge):** "find where the consensus is wrong" (Valentine's recurring theme) *is* second-level thinking applied to a single stock — the cognitive core shared with HF Z3.2.

### Where research and banking collide: the IPO and the conflict
Equity Research meets Investment Banking most visibly at the **IPO (★G102, IB Z2.8–2.9)**: the analyst must stay *walled off* (IB Z1.10) from the deal the bankers are running, observe the **quiet period** (★G200), and resist the gravitational pull of the banking relationship (★G199). The entire regulatory frame (Z1.9, Z5.4–5.5) exists to manage this single seam — the **Global Research Settlement** is the historical scar tissue from when the wall didn't exist.

### The conceptual throughline: the expectations treadmill
Koller's **expectations treadmill** — returns are driven by performance *relative to expectations*, not in absolute terms — is the idea that unifies the consensus/estimate/surprise/revision cluster:
- It explains why a *differentiated* estimate (★G184), not an accurate one, is what matters (Z3.6).
- It explains why the **earnings surprise** (★G193) and the **guidance** move stocks more than the reported quarter (Z4.3).
- It explains why the **revision cycle** (★G188) is a tradeable signal — the *change* in expectations is the event (Z4.4).
- It connects all of these to the market-efficiency frame (**★G125**, AM): the market prices what it knows, so the edge is in the expectation it hasn't yet corrected.

---

# PART 8 · Suggested Master Learning Path

*Three routes through the 43 zone nodes and 19 new globals, depending on the learner's goal. Inherited globals (G1–G181) are assumed available as just-in-time references, not re-taught.*

### Path A — "What does an equity analyst actually do?" (the workflow path)
The narrative spine, following an analyst from blank page to published call and into the quarterly grind:
**Z1.1 → Z1.2 → Z1.5** (what it is, the five outputs, the five tasks) **→ Z3.1 → Z3.2 → Z3.3** (process overview, critical factors, channel checks) **→ Z3.4 → Z3.5 → Z3.6** (model, earnings quality, estimates) **→ Z3.7 → Z3.8** (valuation, intrinsic vs. relative) **→ Z3.9 → Z3.10 → Z3.11 → Z3.12** (thesis, target, rating, initiation) **→ Z4.1 → Z4.2 → Z4.3 → Z4.4 → Z4.5** (the maintenance loop) **→ Z4.6 → Z4.7** (the relationships). *This is the recommended default path.*

### Path B — "How does the research business work?" (the institutional path)
For the learner who wants the ecosystem, economics, and conflict rather than the craft:
**Z1.1 → Z1.3 → Z1.4** (what it is, the three branches, who consumes) **→ Z2.4 → Z2.5 → Z2.6** (sell-side, buy-side, independent) **→ Z1.7 → Z1.8** (how it's paid, the triangle) **→ Z1.9** (the regulatory frame) **→ Z5.1 → Z5.2 → Z5.3** (franchise, economics, triangle in depth) **→ Z5.4 → Z5.5** (the conflict, the rules) **→ Z5.6 → Z5.7** (the career, the future).

### Path C — "I already know finance; show me what's new here" (the inheritance-aware path)
For a learner who has done the IB, AM, and HF modules and wants only Equity Research's net-new contribution:
The **19 new globals in dependency order:** ★G189 (universe) → ★G191 (critical factors) → ★G190 (mosaic) → ★G183 (model) → ★G184 (estimate/consensus) → ★G187 (published thesis) → ★G185 (target) → ★G186 (rating) → ★G182 (the report) → ★G192 (earnings cycle) → ★G193 (surprise/guidance) → ★G188 (revisions) → ★G194 (buy-side research) → ★G195 (independent/alt-data) → ★G196 (franchise/II) → ★G197 (unbundling economics) → ★G198 (the triangle) → ★G199 (the conflict/settlement) → ★G200 (Reg AC/FD). Each is best learned at its home node, with the Part 1 disambiguations read first to fix the high-confusion pairs.

---

# PART 9 · Source Gaps (Consolidated)

*Every gap flagged at the node level, gathered here so the module's known blind spots are explicit rather than hidden. These are deliberate seams, to be addressed when the depth layer is authored.*

1. **The modern research business model (post-MiFID-II economics).** *Flagged at: Z1.7, Z5.2, Z5.7, ★G197.* No source in the folder covers research economics after the 2018 unbundling — Valentine (2011) predates it entirely. The *direction* (unbundling → budget collapse → consolidation → coverage shrinkage) is well-established general knowledge, but the *current quantitative state* of the research business (budgets, headcount, pricing models, survival economics) is the module's largest gap. **Highest-leverage fill:** a current source on the post-MiFID-II research industry.

2. **AI and alternative data as a disruption of the research product.** *Flagged at: Z2.6, Z5.7, ★G195.* Koller (2020) is the most recent source and does not reach the AI/alt-data reshaping of research; it is treated as an input (alt-data as productized channel checks) and a frontier (AI commoditizing the mechanical work), grounded in general knowledge. The forward-looking content is framed from first principles, not from a dedicated source.

3. **The securities-regulation frame.** *Flagged at: Z1.9, Z5.4, Z5.5, ★G199, ★G200.* No securities-law source sits in the folder. Reg AC, Reg FD, the Global Research Settlement, and MiFID II's conflict provisions are grounded in Valentine's ethics chapter (which covers Reg FD and the Spitzer settlement), the IB module's information wall, and general knowledge. The rules are stated at the level a learner needs, not at the level of legal practice.

4. **Sector-specific valuation depth (a deferred breadth item, not a true gap).** *Touched at: Z2.3, Z3.8.* Damodaran's special cases (banks → DDM, cyclicals/commodities → normalized earnings, young/high-growth → non-multiple methods) are flagged but not built out per sector; the sector frameworks node (Z2.3) maps the *principle* that methods differ by sector without authoring a node per sector. This is a depth-layer item, consistent with the breadth-before-depth strategy.

---

# PART 10 · Template Note — What This Module Contributes

*Each module is also a test of the canonical five-zone template and the shared-glossary architecture. This note records what Equity Research validated and what it contributed to the standing infrastructure.*

### What it confirmed about the architecture
- **The five-zone template held cleanly** for a module that is an *activity/discipline* rather than an *institution*: Ecosystem → Types → Process → Maintaining → Franchise mapped naturally onto what-it-is → who-does-it → the-workflow → the-routine → the-business. The template's generality survived a structurally different subject.
- **Inheritance-first scaled again.** With G1–G181 already standing, Equity Research needed only **19 net-new globals (G182–G200)** — and reused the IB valuation toolkit (★G87–G95) and the HF/AM active-equity machinery wholesale. The module is mostly *re-use*, exactly as Asset Management and Wealth Management were, confirming the glossary's compounding leverage: each new module contributes fewer novel primitives as the shared base grows.
- **The "same object, different chair" pattern proved a reliable disambiguation engine.** The richest teaching moments came from showing that the published thesis (★G187) and internal thesis (★G121), or the analyst's toolkit-use and the banker's, are the *same logical object seen from a different seat* — a pattern the template now has vocabulary for.

### What it contributed to the standing infrastructure
- **A complete view-making vocabulary** that downstream modules can reference: the estimate/consensus (★G184), the rating (★G186), the price target (★G185), the earnings cycle (★G192), and the surprise/revision cluster (★G188, ★G193) are now defined once and available to Venture Capital, Real Estate, and any future module that needs to talk about how a public-market view is formed.
- **The conflict-and-disclosure frame** (★G199, ★G200) extends the IB information-wall concept into a reusable treatment of research independence that any sell-side-adjacent module can point to.
- **The expectations-treadmill throughline** (grounded in Koller) gives the whole series a unifying concept for *why beating expectations, not absolute performance, drives returns* — connecting consensus, surprise, and revision to market efficiency (★G125) across modules.

### Known limits carried forward
- The three source gaps in Part 9 (modern economics, AI/alt-data, securities law) are the module's honest blind spots, flagged at the node level throughout.
- **Depth is deferred by design.** This is a *structural map* — the seventh in the breadth-first build. Technical depth layers (per-sector valuation, the full modeling mechanics, the legal detail of the regulatory frame) come after the full module set is mapped, consistent with the breadth-before-depth strategy that has governed all seven modules.

---

*End of the Equity Research module node map. Seventh of the asset-class series; 43 zone nodes; 19 new globals (G182–G200); built on Valentine, Damodaran, Koller, and Penman, with three source gaps flagged. The shared glossary now spans G1–G200.*
