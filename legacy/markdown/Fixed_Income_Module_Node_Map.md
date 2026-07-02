# Fixed Income — Module Node Map

**Module type:** **Asset-class** module (`kind: asset-class`, suggested slug `fixed-income`, `build_order: 11`). Lives alongside the role modules and the Macro core-concept module. Per **ADR-003 ruling 3**, asset-class modules are authorized to use a **concept-progression spine** rather than the role spine; all six structural invariants (five zones, `Zn.m` IDs, four node fields, structured gaps, contiguous globals, back-link-don't-re-home) apply unchanged.

**Position in the build:** Eleventh module mapped. The corpus ends the shared glossary at **G263**; this module's new globals begin at **G264** and run to **G285** (**22 net-new globals** — deliberately low, because Fixed Income is the most inheritance-heavy module yet built: it is the *market-side instantiation* of Macro's rates machinery and the *public-market sibling* of Private Credit).

**Zone spine (concept-progression — ratified order per architecture sign-off):**
> **Z1 The Bond & Its Market → Z2 Bond Math & the Curve → Z3 The Instrument Universe → Z4 Credit & Spread → Z5 Trading, Financing & the Portfolio**

The order is math-before-universe, matching four of the five structural sources (Fabozzi: analytics before securities; Parameswaran: TVM/curve/duration before money market/floaters/MBS; Tuckman: entirely math-first; even Thau does basic bond math before her securities tour). The graph reason is stronger than the pedagogical one: the universe zone *needs* the math — you cannot explain why MBS behave differently (negative convexity, extension risk) or what TIPS do (real vs. nominal, `★ G249`) without duration and the curve already placed. Math-first lets Z3–Z5 compound instead of forward-referencing.

---

## What this module is for

Every module in the app touches bonds and none teaches them. Macro built the *variables* — the policy rate (`★ G247`), the risk-free rate and term structure (`★ G248`), the yield curve as signal (`★ G257`), inflation (`★ G252`) — but explicitly deferred the *market*: the instruments, the math, the trading. Asset Management's Z2.8 ("Active Fixed Income") describes what a bond manager *decides* and flags that the underlying machinery "runs on macro and credit" taught elsewhere. Private Credit teaches lending economics in the *private, bilateral, hold-to-maturity* world and marks the seam to the public market at Z1.7 (the BSL market). Wealth Management assumes bond funds and ladders; Real Estate homes the CMBS (`★ G227`) but not securitization in general; Hedge Funds reference fixed-income relative value and distressed credit as strategies whose instruments are untaught.

This module builds the market: what a bond is, how it's priced, the full instrument universe (Treasuries → TIPS → money market → munis → corporates → MBS/ABS → EM), how credit is rated and spread over the curve, and how the whole thing is traded, financed (repo), and assembled into portfolios. The discipline throughout: where a concept already has a home (`G58` yield, `G69` SOFR, `G70` spread, `G61`/`G62` recovery/default, `G72` call protection, `G77` internal ratings, `G90` DCF, `G227` CMBS, `G248`/`G257` the curve), this module **back-links and disambiguates** — it never re-homes. Every FI-minted global gets **exactly one** home (the known 26-global multi-home defect is not worsened by a single node here).

**Scope boundaries (deliberate, per the standing build sequence FI → Sectors → Derivatives):**
1. **Rates derivatives are referenced at usage level only.** Interest-rate futures, swaps, swaptions, and bond options appear as *tools a desk uses* (Z5.4) with structured gaps pointing at the future **Derivatives** module — their mechanics and pricing are not homed here. The one exception is the **CDS (`★ G278`)**: it is homed here because the sources (Tuckman Ch. 14, Fabozzi Part 7, Huggins Ch. 13) treat it as inseparable from the traded-credit market itself; the future Derivatives module will own general swap/option *mechanics* and back-link G278 rather than re-home it.
2. **CMBS stays homed in Real Estate (`★ G227`).** FI's securitization nodes (Z3.10–Z3.11) home the *mechanism* and *agency residential MBS*; commercial mortgage securitization back-links.
3. **Sector-level credit analysis** (utilities, banks, energy issuers) is deferred to the sector modules hanging off ER Z2.3 — Z4.8 names the craft and points forward.

---

## Sources mapped

This module is built on the **Fixed Income** folder of the Drive library (parented under the Macro folder — a known layout asymmetry, flagged, not blocking). Read in depth:

- **Sunil Parameswaran, *Fixed Income Securities: Concepts and Applications* (De Gruyter, 2020)** — the **pedagogical math spine** for Zones 1–2: TVM from first principles, bond anatomy and valuation, par/premium/discount and the pull to par, day counts and accrued interest, the full yield-measure family, bootstrapping and term-structure theories, duration/convexity/immunization — plus Treasury auctions, STRIPS, and when-issued trading for Z3.1, and money-market instruments, floaters, and linkers for Z3.
- **Annette Thau, *The Bond Book*, 3rd ed. (McGraw-Hill, 2011)** — the **investor-lens spine**: "the many meanings of yield" (the Z2.5 disambiguation is hers), the life of a bond, why bond prices go up and down, Treasuries/TreasuryDirect/savings bonds, munis and taxable-equivalent yield, GNMAs and the vocabulary of prepayment, bond funds vs. individual bonds, ladders and portfolio structures (Z5.7).
- **Frank Fabozzi & Steven Mann (eds.), *The Handbook of Fixed Income Securities*, 7th ed. (McGraw-Hill)** — the **encyclopedic reference** underwriting the whole map: the risk taxonomy (Ch. 2), primary/secondary market structure (Ch. 3), bond indexes (Ch. 4), yield measures and total return (Ch. 5), the structure of interest rates (Ch. 7), duration/convexity/PVBP (Ch. 9), and the deepest instrument coverage in print — Treasuries/agencies, munis, money-market instruments, corporates and high yield with default/recovery data, MTNs, linkers, floaters, international/Eurobond, EM debt and Bradys, mortgages, agency and non-agency MBS, CMOs, ABS (cards/autos/residential), CDOs — plus corporate credit analysis (Part 4), OAS and lattice valuation (Part 5), portfolio management, financing positions, and immunization (Part 6), and credit derivatives (Part 7).
- **Bruce Tuckman & Angel Serrat, *Fixed Income Securities: Tools for Today's Markets*, 4th ed. (Wiley, 2022)** — the **modern quantitative spine**, deliberately post-LIBOR (the preface frames the edition around the SOFR transition): discount factors and arbitrage, swap/spot/forward rates, returns/spreads/P&L attribution, DV01/duration/convexity and key-rate '01s, term-structure models, **repo and financing** (Ch. 10), note/bond futures, short-term rates and their derivatives (SOFR/fed-funds futures), swaps, **corporate debt & CDS** (Ch. 14), and MBS.
- **Doug Huggins & Christian Schaller, *Fixed Income Relative Value Analysis*, 2nd ed. (Wiley, 2024)** — the **practitioner RV spine** for Z4.9/Z5: reference rates and the repo market in institutional detail (SOFR construction, the secured–unsecured basis, the September 2019 repo spike, balance-sheet shadow costs post-Basel III), asset swaps and swap-spread drivers, CDS structure and the bond–CDS basis, intra- and cross-currency basis swaps, fitted bond curves, and the analytic process for government bond markets.
- **Dirk Willer, Ram Bala Chandran & Kenneth Lam, *Trading Fixed Income and FX in Emerging Markets* (Wiley, 2020)** — the **EM spine** for Z3.12/Z5.10: the local-vs-external debt universe (GBI-EM/EMBI/CEMBI), the 65%-global/35%-local rule, the Fed and DXY as EM drivers, the EM rates cycle and central-bank reaction functions, linkers, EM credit (the 3–5yr BB sweet spot, defaults and recovery), and portfolio construction.

> **Source-character note (build-time).** The six sources split into three registers: **pedagogy** (Parameswaran, Thau) supplies the Zone 1–2 definitions and the investor lens; the **reference** (Fabozzi) underwrites the Zone 3 instrument tour and the Zone 4 credit machinery; **practitioner-quant** (Tuckman, Huggins, Willer) supplies Zones 2, 4, and 5's modern mechanics — crucially *post-SOFR*, which matters because two of the six sources (Thau 2011, Fabozzi 7th ed.) predate the LIBOR transition and several market-structure shifts (electronic trading, ETF-driven liquidity, post-Basel III dealer balance sheets). Every node whose currency outruns its source carries a `GAP:` tag, exactly as the prior ten maps do. The graph grows at its seams.

---

# PART 1 · Disambiguation callouts (read these first)

*Fixed income is where the app's worst near-synonym collisions live — several were flagged in the kickoff brief as first-class seams. Each becomes a load-bearing `disambiguate_with` cross-link in the graph, not just a definition.*

> **Public/traded credit (this module) vs. private credit (the Private Credit module) — one borrower, two markets.** *(The module's front-door seam, Z1.8, pairing with Private Credit Z1.7.)* Both are lending. **Private credit** is bilateral, privately negotiated, covenant-heavy, illiquid, hold-to-maturity, floating-rate, and priced as a *spread over SOFR set at origination* (`★ G69`, `★ G70`). **Public/traded fixed income** is standardized, rated by agencies, distributed to many holders, *repriced continuously in a secondary market*, mostly fixed-rate, and quoted as a *yield or a spread over the Treasury curve*. The same company can appear in both (a syndicated Term Loan B and a high-yield bond side by side). The tells: who holds it (one lender vs. many), how it's priced (negotiation vs. the market), what happens when you want out (nothing vs. a bid). Private Credit Z1.7 marks this seam from the private side; FI Z1.8 marks it from the public side; the app should render them as two doors on one wall.

> **The many meanings of "yield" — `★ G265` (YTM) vs. `★ G58` (private-credit yield) vs. the coupon vs. current yield vs. yield-to-worst.** *(Thau's chapter title; the brief's second seam.)* The **coupon** is what the bond *pays* (a contractual rate on face). **Current yield** is coupon ÷ price (income now, ignoring pull-to-par). **Yield to maturity (`★ G265`)** is the IRR of *all* cash flows at today's price — the market's quoted number, with a reinvestment assumption buried inside. **Yield to worst** is YTM recomputed to the most adverse call date (`★ G285`). **`★ G58` (Private Credit's "yield")** is the all-in return of a *loan* — SOFR + spread + OID amortization + fees — a lender's underwriting arithmetic, not a market quote. When Wealth Management says "the portfolio yields 5%," when Private Credit says "unitranche yields 11%," and when the bond desk says "the 10-year yields 4.3%," those are three different calculations. One word; the app must never let them collide.

> **Duration vs. maturity — `★ G267` vs. the calendar.** *(The brief's third seam.)* **Maturity** is *when the last payment arrives* — a date. **Duration** is *how sensitive the price is to yield changes* — a risk number (≈ the PV-weighted average time to the cash flows, and, in modified form, the %-price-change per 1% yield change). A 30-year bond has 30-year maturity but ~18-year duration; a 30-year *zero* has duration equal to its maturity; a floater (`★ G69`) has 30-year maturity and ~0.25-year duration because its coupon resets. "Long-maturity" describes the calendar; "long-duration" describes the risk. VC's discount-rate sensitivity, RE's cap-rate sensitivity, and equities' "duration" metaphor all borrow this word — G267 is the home they borrow it from.

> **Three vantages on one curve — `★ G248` (the risk-free term structure) vs. `★ G257` (the curve as macro signal) vs. `★ G269` (the curve as pricing toolkit).** Macro homed the risk-free rate and term structure (G248: the "price of time") and the curve's *shape as recession signal* (G257: inversion). This module adds the third vantage: **G269**, the curve as a *pricing machine* — discount factors extracted from bond prices, spot rates, forward rates, par rates, bootstrapping. Same object; three uses: G248 anchors *valuation* (WACC `★ G91`), G257 anchors *macro reading*, G269 anchors *bond arithmetic and trading*. The app links all three and says which hat the curve is wearing.

> **Two spreads — `★ G277` (FI's market spreads: G, Z, OAS) vs. `★ G70` (Private Credit's pricing spread).** *(The brief's fourth seam.)* **`G70`** is a *contractual* spread: the margin over SOFR written into a loan agreement at close — it changes only if the loan is repriced. **`G277`** is a *market-derived* spread: the extra yield a traded bond offers over the Treasury curve, recomputed tick by tick (G-spread against the interpolated curve; Z-spread against the whole spot curve; OAS after stripping embedded-option value). One is set in a negotiation and *is* the price of the loan; the other is observed in a market and *moves* as the price of the bond moves. Both compensate credit risk; they are different objects.

> **Two ratings — `★ G276` (the public agencies: Moody's/S&P/Fitch) vs. `★ G77` (internal credit ratings).** **`G77`** (Private Credit) is a *lender's own* risk grade — proprietary, portfolio-monitoring, no market consequence. **`G276`** is the *public* scale — letter grades published by licensed agencies, with hard-wired market consequences: the IG/HY line (`★ G275`) determines index membership (`★ G283`), who may hold the paper, and what it costs to issue. A downgrade through BBB−/Baa3 ("the fallen angel") forces selling; an internal downgrade to watch-list (`★ G82`) forces a conversation. Related craft, different institutions, different stakes.

> **Call protection, two markets — `★ G285` (callable bonds & embedded options) vs. `★ G72` (loan call protection / prepayment economics).** Private Credit's `G72` is the *lender's shield*: prepayment penalties and non-call periods negotiated so early repayment compensates the lender. FI's `G285` is the *issuer's option embedded in a security*: the right to redeem a bond at a set price, which the *market prices* — via yield-to-worst, negative convexity, and OAS (`★ G277`). Same underlying economics (the borrower's refinancing option), opposite framing: one is a contract term you negotiate, the other is an option you value.

> **The money market vs. money market funds.** **The money market (`★ G272`)** is a *market segment*: instruments maturing inside a year (T-bills, commercial paper, CDs, fed funds, repo). A **money market fund** is a *vehicle* (a mutual fund holding those instruments, Wealth Management's cash bucket, touched at Z5.7). The segment is homed here; the vehicle stays with the fund modules.

---

# PART 2 · The global glossary contribution (G264–G285)

*22 net-new globals. Each is a primitive referenced across the existing ten modules but homed nowhere until now. Nothing below G264 is redefined; every prior-module concept this module touches (yield `G58`, SOFR `G69`, spread `G70`, recovery `G61`, default `G62`, call protection `G72`, internal ratings `G77`, collateral/liens `G78`, workouts `G81`, DCF `G90`, WACC `G91`, underwriting spread `G103`, asset allocation `G143`, cap rate `G219`, CMBS `G227`, and the entire macro rates chain `G243`–`G263`) is **back-linked**, not re-homed.*

| G# | Node (home zone) | One-sentence quick definition | Reused by |
|----|------------------|-------------------------------|-----------|
| **G264** | **The bond (the debt security)** (Z1.2) | A tradable IOU — a promise to pay fixed coupons on set dates and return the face value at maturity — the atomic unit of the fixed-income market. | ALL |
| **G265** | **Yield to maturity (& the meanings of yield)** (Z2.5) | The single discount rate that equates a bond's price to the PV of its remaining cash flows — the market's quoted "yield," one of several yield concepts that must never be conflated. | ALL |
| **G266** | **Bond pricing & the price–yield inversion** (Z2.2) | A bond's price is the present value of its cash flows, which makes price and yield move inversely — the mechanical reason bond prices fall when rates rise. | ALL |
| **G267** | **Duration (& DV01)** (Z2.9) | The sensitivity of a bond's price to a change in yield — the master risk number of fixed income (DV01 is the same idea in dollars per basis point). | AM, WM, HF, RE, ER, Macro |
| **G268** | **Convexity** (Z2.10) | The curvature in the price–yield relationship — why duration understates gains and overstates losses, and why prepayable bonds can have *negative* convexity. | AM, HF, RE |
| **G269** | **Spot, forward & par rates (the curve toolkit)** (Z2.7) | The pricing machinery extracted from bond prices — discount factors, zero-coupon spot rates, implied forwards, and par yields — the arithmetic form of the term structure. | HF, AM, IB, future Derivatives |
| **G270** | **The U.S. Treasury market** (Z3.1) | The market for U.S. government debt — bills, notes, and bonds — the largest, most liquid bond market on earth and the risk-free benchmark everything else is priced against. | ALL |
| **G271** | **TIPS & inflation-linked bonds** (Z3.3) | Treasuries whose principal indexes to CPI, paying a *real* yield — and, via the gap to nominal yields, the market's own inflation forecast (the breakeven). | WM, AM, HF, Macro |
| **G272** | **The money market (bills, CP, CDs)** (Z3.5) | The market for debt maturing inside a year — T-bills, commercial paper, certificates of deposit, fed funds — where the policy rate becomes actual funding. | WM, AM, HF, IB |
| **G273** | **Municipal bonds & tax-equivalent yield** (Z3.6) | State and local government debt whose interest is federally tax-exempt — compared to taxable bonds via the taxable-equivalent yield, the core math of the retail bond buyer. | WM |
| **G274** | **Corporate bonds** (Z3.7) | Standardized, rated, tradable debt issued by companies under an indenture — the public-market sibling of the private loan and the output of IB's debt capital markets. | IB, ER, Credit, AM, HF |
| **G275** | **Investment grade vs. high yield (the ratings divide)** (Z4.3) | The BBB−/Baa3 line that splits the bond market into two regimes — who may own the paper, which index it joins, what it costs to issue — and the "fallen angel" dynamics at the boundary. | IB, Credit, HF, AM, ER |
| **G276** | **Credit ratings & the rating agencies** (Z4.2) | The public letter-grade scales (Moody's, S&P, Fitch) that price default risk into markets — with hard-wired consequences for index membership, mandates, and funding costs. | ALL |
| **G277** | **Bond spreads (G-spread, Z-spread, OAS)** (Z4.4) | The extra yield a bond offers over the Treasury curve — measured against a point (G), the whole curve (Z), or net of embedded options (OAS) — the market's running price of credit risk. | Credit, HF, AM, ER, Macro |
| **G278** | **The credit default swap (CDS)** (Z4.7) | A contract that pays out if a borrower defaults, in exchange for a running premium — tradable default insurance that lets credit risk be bought, sold, and measured apart from the bond. | HF, IB, Credit, Macro, future Derivatives |
| **G279** | **Securitization** (Z3.10) | The machine that pools illiquid loans (mortgages, cards, autos), routes their cash flows through a trust, and issues tradable bonds in tranches against the pool. | RE, Credit, IB, WM |
| **G280** | **Agency MBS & prepayment** (Z3.11) | Bonds backed by pools of government-guaranteed home mortgages, whose defining risk is not default but *prepayment* — homeowners refinancing exactly when investors least want it. | RE, AM, HF, WM |
| **G281** | **Emerging market debt (local vs. external)** (Z3.12) | Sovereign and corporate debt of developing economies, split into local-currency bonds (rates + FX risk) and hard-currency bonds (credit risk) — a distinct asset class with its own indices. | HF, AM, Macro |
| **G282** | **Repo & secured financing** (Z5.3) | Selling a security with an agreement to buy it back — a collateralized loan that finances every bond desk, sets the secured overnight rate (SOFR's raw material), and transmits leverage system-wide. | HF, Macro, AM, future Derivatives |
| **G283** | **The bond index & the benchmark (the Agg)** (Z5.5) | The rules-based baskets (Bloomberg Aggregate, EMBI, HY indices) that define "the bond market" for portfolios — with the quirk that issuers get bigger weights by owing more. | AM, WM, HF |
| **G284** | **Immunization & liability-driven investing (LDI)** (Z5.8) | Structuring a bond portfolio so assets move with liabilities — matching duration so a pension or insurer is hedged against rates rather than betting on them. | AM, WM |
| **G285** | **Callable bonds & embedded options** (Z3.9) | Bonds carrying issuer or holder options (call, put, conversion) whose value the market strips out via yield-to-worst and OAS — the reason a 6% callable isn't a 6% bullet. | Credit, IB, WM, future Derivatives |

**Tag legend (as in the prior maps):** `★ GLOBAL` = canonical home node contributed to the shared glossary · `[core]` = essential zone node, not globalized · `[branch]` = a sub-tree head or a specific framework/instrument variant · `[process]` = a step in a sequence · `GAP:` = source thin, dated, or silent here (a future attachment point).

---

# ZONE 1 · The Bond & Its Market

**What this zone is:** the front door. What fixed income *is* as an asset class, the bond as an object (`★ G264`), why issuers borrow this way and why investors lend this way, how big the market actually is (bigger than equities — the fact that reframes everything), who the players are, how bonds are born (the primary market) and where they live afterward (the OTC secondary), and the seam with Private Credit that a learner arriving from that module needs immediately. *(Sources: Thau Part 1 for the frame and the life of a bond; Fabozzi Ch. 1–3 for the taxonomy and market structure; Parameswaran Ch. 2 for anatomy; Tuckman Ch. 0 for the modern market map.)*

`What fixed income is → The bond → Why borrow/why lend → The scale of the market → The players → The primary market → The secondary market → The private-credit seam → A bond's life.`

---

### Z1.1 · What Fixed Income Is (the Asset Class) `[core]`

**Quick definition.** The asset class of *tradable debt* — securities that promise contractual payments on a schedule — spanning government, municipal, corporate, securitized, and emerging-market debt; called "fixed income" because the payments are set by contract, not by the issuer's profits.

**Explainer covers (basic → technical):**
- The defining contrast with equity: a bondholder is a *lender with a contract*, not an owner with a claim on profits. Coupons are obligations (missing one is default); dividends are discretionary. Upside is capped at the promised payments; downside protection comes from seniority (`★ G78`) and the contract.
- Why "fixed" income still moves: the *payments* are fixed but the *price* is not — it reprices continuously as rates (`★ G248`) and credit conditions (`★ G258`) move. Zone 2 is the mechanics of that repricing.
- The map of the universe (previewing Zone 3): governments (Treasuries `★ G270`, TIPS `★ G271`), the money market (`★ G272`), munis (`★ G273`), corporates (`★ G274`, IG and HY `★ G275`), securitized products (`★ G279`/`★ G280`), and EM (`★ G281`).
- Where this module sits in the app: Macro built the *rates variables*; Private Credit built the *private lending world*; Asset/Wealth Management built the *vehicles and mandates*. This module builds the *market* they all assume.

**Connects to.** `★ G264` the bond (the atomic unit), Z1.3 (why the asset class exists), Z1.8 (the private-credit seam), `★ G248` the risk-free rate (the anchor variable), AM Z2.8 (Active Fixed Income — the manager's seat over this market), `★ G143` asset allocation (where FI sits in a portfolio).

---

### Z1.2 · The Bond `★ GLOBAL (G264)` `[core]`

**Quick definition.** A tradable IOU: a security promising to pay a fixed **coupon** on set dates and return the **face value** (par) at **maturity** — the atomic unit of the fixed-income market, defined by four terms: face, coupon, maturity, and the price the market sets against them.

**Explainer covers (basic → technical):**
- The anatomy (Parameswaran Ch. 2): **face/par value** (the principal repaid at the end, the base coupons are computed on), the **coupon rate** (the contractual interest, usually paid semiannually in the US), the **maturity** (when the debt ceases to exist), and the **price** (what the market pays today — quoted per 100 of face). The fifth number, **yield** (`★ G265`), is *derived* from price, not written in the contract.
- Bond vs. loan vs. note vs. debenture: a bond is *securitized borrowing* — standardized, registered, transferable. In US usage a debenture is unsecured and a bond is secured; in practice the words blur, and the load-bearing distinction is *tradable security vs. bilateral loan* (Z1.8).
- Variants previewed (each gets its Zone 3 node): zero-coupon (Z3.2), floating-rate (Z3.8, `★ G69`), inflation-linked (`★ G271`), callable (`★ G285`), amortizing and mortgage-backed (`★ G280`).
- The two things that can happen to a holder: get paid as promised, or default (`★ G62`) — with recovery (`★ G61`) governed by seniority (`★ G78`). Everything in Zone 4 prices the odds of the second outcome.

**Connects to.** Z2.2 pricing (`★ G266`), `★ G265` YTM (the derived number), Z1.9 (the life cycle), `★ G29` leverage (the issuer's side — bonds are how companies lever without diluting), `★ G34` covenant (the contract's teeth, lighter in bonds than loans), Z3 (every variant). Across the graph: the word "bond" appears in all ten modules; this is its home.

---

### Z1.3 · Why Issuers Borrow & Why Investors Lend `[core]`

**Quick definition.** The two-sided motive that creates the market: issuers get capital without dilution plus a tax shield and leverage; investors get contractual income, seniority over equity, and the portfolio ballast of an asset that (usually) zigged when stocks zagged.

**Explainer covers (basic → technical):**
- The issuer's side (Parameswaran): debt raises capital *without giving up ownership* — the leverage effect (`★ G29`, back-link: it magnifies equity returns both ways) and the **tax shield** (interest is deductible; dividends are not — the same arithmetic PE runs in every LBO). Governments have no equity to sell; bonds are their *only* security.
- The investor's side (Thau): predictable income (retirees, insurers, pensions — the LDI motive previewed at `★ G284`), capital preservation via seniority, and diversification — the historical stock–bond hedge, with the honest caveat that the hedge fails when *inflation* is the shock (2022: both fell together; `★ G252`).
- Who must hold bonds by mandate: banks (regulation and liquidity rules), insurers (matching liabilities), pensions (LDI), money-market and bond funds (`★ G283` benchmarks). Much of the market is *structurally* long.
- The pecking order in the capital structure: secured debt → unsecured bonds → subordinated → preferred → equity (`★ G78`, `★ G95` the EV bridge). Where a bond sits determines its recovery (`★ G61`) and therefore its spread (`★ G277`).

**Connects to.** `★ G29` leverage, `★ G95` EV bridge (IB), `★ G143` asset allocation (AM), `★ G170` the 4% rule (WM — the income link), Z4.6 (default & recovery), `★ G284` LDI. *Real-world layer: Parameswaran Ch. 2 (leverage & tax shield tables); Thau Part 1.*

---

### Z1.4 · The Scale of the Market `[core]`

**Quick definition.** The fact that reframes everything: the global bond market is *larger* than the global equity market — US Treasuries alone form the deepest securities market on earth — and bond-market prices (yields) are the gravitational field every other asset is priced in.

**Explainer covers (basic → technical):**
- The size ranking a newcomer never guesses: global debt securities outstanding exceed global equity market capitalization; within the US, the Treasury market (`★ G270`) is the single deepest and most-traded market in existence, followed by MBS (`★ G280`) and corporates (`★ G274`).
- Why equities get the headlines anyway: stocks are exchange-traded, volatile, and story-rich; bonds trade OTC (Z1.7) in institutional size. Retail sees the bond market mostly through funds (Z5.7) and mortgage rates.
- Why the bond market is called "the smart money": yields aggregate the market's view of growth, inflation, and policy (`★ G257` the inversion signal is *bond-market* information); "the bond vigilantes" discipline fiscal policy (`★ G242`, `★ G262`).
- The gravitational-field point (the G248→G259 chain restated from the market side): the Treasury curve is the risk-free base; every mortgage, loan, corporate bond, cap rate (`★ G219`), and equity multiple (`★ G27`) is priced at a spread or premium to it.

**Connects to.** `★ G270` the Treasury market, `★ G248`/`★ G259` (the valuation chain — this node is its marketplace), Macro Z4.10 (the macro–markets bridge), `★ G283` (how the market is indexed). GAP: outstanding-size figures are level-data that date quickly — sources run to ~2022; refresh at authoring depth.

---

### Z1.5 · The Players: Issuers, Investors & Dealers `[core]`

**Quick definition.** The three-sided cast: issuers who need capital (Treasury, agencies, states, corporations), investors who supply it (central banks, funds, insurers, pensions, banks, households), and the dealers in the middle who underwrite, quote, and warehouse risk.

**Explainer covers (basic → technical):**
- The issuer roster by size: the US Treasury (the anchor issuer, `★ G270`), the housing agencies/GSEs (Z3.4), states and municipalities (`★ G273`), corporations from AAA to CCC (`★ G274`/`★ G275`), securitization trusts (`★ G279`), and foreign sovereigns (`★ G281`).
- The investor roster and what each *wants*: central banks (reserves — the Fed itself via QE `★ G251`), commercial banks (liquidity portfolios), insurers and pensions (liability matching, `★ G284`), mutual funds and ETFs (benchmark tracking, `★ G283`), hedge funds (RV and macro — HF Z2.3/Z2.4), money-market funds, and households (Thau's reader).
- The dealers: the sell-side desks (and, for Treasuries, the designated **primary dealers**, Z3.1) that underwrite new issues (Z1.6, `★ G103`), make secondary markets (Z1.7), and finance inventory in repo (`★ G282`). Post-Basel III their balance sheets are scarcer — a structural liquidity change the older sources predate (Huggins Ch. 18).
- The Fed as a player, not just a referee: open-market operations, the QE/QT portfolio (`★ G251`), and the standing repo facilities put the central bank *inside* this market — the direct line to Macro Z2.

**Connects to.** Z1.6/Z1.7 (what dealers do), `★ G244` the Fed, `★ G251` QE/QT, AM/WM (the buy-side modules — their firms are these investors), HF Z2.8 (credit funds), `★ G282` repo (the financing layer). *Real-world layer: Tuckman Ch. 0's market-participant map; Fabozzi Ch. 3.*

---

### Z1.6 · The Primary Market: Auctions & Underwriting `[core]`

**Quick definition.** How bonds are born: governments sell by **auction** on a published calendar; corporates and munis sell by **underwriting**, where an IB syndicate buys the issue and re-offers it — the fixed-income half of the capital-markets machinery IB already teaches.

**Explainer covers (basic → technical):**
- The auction route (Treasuries, detailed at Z3.1): announced size and date, competitive bids in yield from primary dealers and directs, a single clearing yield, when-issued trading before settlement (Parameswaran Ch. 2).
- The underwritten route: the DCM desk builds a book, prices the deal as a *spread over Treasuries* (`★ G277` at birth), and the syndicate earns the **gross spread (`★ G103`** — back-link, homed in IB). New-issue concessions and order-book dynamics are the corporate market's version of an IPO pop.
- Private placements and MTN programs as the middle path (Fabozzi Ch. 14): continuously offered notes off a shelf — flexible size and maturity, sitting between a bond deal and a loan.
- Why the primary market matters for pricing everywhere: new-issue supply is the marginal flow that moves secondary spreads; Treasury auction sizes are fiscal policy (`★ G242`) arriving in the market.

**Connects to.** `★ G103` underwriting spread (IB — back-link, the fee side), IB's ECM/DCM zone (the process this node is the product of), Z3.1 (the Treasury auction in full), `★ G274` corporates, Z1.7 (where the bonds go next). *Real-world layer: Fabozzi Ch. 3 (primary market); Parameswaran (auction illustration).*

---

### Z1.7 · The Secondary Market: OTC Dealer Trading `[core]`

**Quick definition.** Where bonds live after issuance: not an exchange but a **dealer network** — investors trade against dealer quotes, bilaterally or on electronic platforms, which makes liquidity a *negotiated*, tiered thing rather than a continuous ticker.

**Explainer covers (basic → technical):**
- The structural fact (Thau's Part 1 warning to retail buyers): most bonds don't trade on an exchange. A dealer quotes a **bid** and an **ask** and holds inventory in between; the spread between them is the price of liquidity (Z5.1 deepens this).
- The liquidity tiers: on-the-run Treasuries trade nearly continuously; off-the-run and IG corporates trade daily-ish; a seasoned muni or small HY issue may not trade for weeks. "The price" of an untraded bond is a *mark*, not a print — matrix pricing off comparable bonds.
- The electronification shift: platforms, all-to-all trading, and portfolio trading have transformed corporate-bond liquidity since the sources' publication dates. GAP: Thau (2011) and Fabozzi (7th ed.) predate this; Tuckman covers the modern structure partially. Flag for refresh at depth.
- Transparency plumbing: TRACE (corporates) and EMMA (munis) publish trades after the fact — the closest the OTC market gets to a tape.

**Connects to.** Z5.1 (the dealer desk & bid–ask, the trading-zone deepening), Z1.5 (the dealers), `★ G282` repo (how dealer inventory is financed), WM (why retail should usually buy funds, Z5.7 — Thau's core advice), PC Z1.7 (the *other* market structure: none at all).

---

### Z1.8 · Public/Traded Credit vs. Private Credit (the Seam) `[core]`

**Quick definition.** The module's front-door disambiguation (Part 1, first callout): the same act of lending split into two worlds — bilateral, negotiated, illiquid, floating-rate private credit vs. standardized, rated, continuously repriced public fixed income — with the syndicated-loan market as the blurry middle.

**Explainer covers (basic → technical):**
- The two-column contrast, made concrete with one borrower: a sponsor-backed company might carry a private unitranche (`★ G68`) *and* a public high-yield bond. The unitranche: one lender, SOFR + spread set at close (`★ G69`/`★ G70`), maintenance covenants (`★ G34`), no secondary price. The bond: hundreds of holders, a fixed coupon, incurrence-only covenants, a price on a screen every day.
- What "traded" buys and costs: liquidity (you can exit) and price discovery (you know the mark) — paid for with mark-to-market volatility, thinner covenants, and disclosure obligations. What "private" buys: yield premium, covenant control, information access — paid for with illiquidity (`★ G63`'s disintermediation story is the supply side of this).
- The blurry middle this seam already flagged from the other side: the **broadly syndicated loan market** (Private Credit Z1.7 — back-link, the canonical BSL node). Term Loan Bs are *loans* that *trade* — rated, index-tracked, institutionally distributed. The two modules meet exactly there.
- Reading the same credit in both markets: the bond's spread (`★ G277`) and the loan's spread (`★ G70`) price the same default risk in different clothes; the CDS (`★ G278`) prices it in a third. Divergences between them are the raw material of capital-structure relative value (HF Z2.8).

**Connects to.** PC Z1.7 (the paired seam node — the app renders these as two doors on one wall), `★ G70` vs. `★ G277` (Part 1 spread callout), `★ G58` vs. `★ G265` (Part 1 yield callout), `★ G64` BDCs (who holds the private side), HF Z2.8 (who trades the dislocations).

---

### Z1.9 · A Bond's Life: Issue → Coupons → Maturity (or Default) `[process]`

**Quick definition.** The full arc as a sequence: origination and pricing at issue, the seasoning of a coupon-paying security through the curve and the credit cycle, and the three exits — maturity at par, an early call (`★ G285`), or default and workout (`★ G62`, `★ G81`).

**Explainer covers (basic → technical):**
- Birth (Z1.6): priced at ~par with a coupon set to the market yield for that issuer, maturity, and moment — meaning the coupon is a *time capsule* of the rate environment at issue (`★ G258`).
- Life: the price walks with the market (Z2.2) while **pulling to par** as maturity approaches (Z2.3); the bond migrates from on-the-run to off-the-run liquidity (Z1.7); its rating can migrate too (`★ G276` — upgrades, downgrades, the fallen-angel cliff at `★ G275`).
- The three deaths: **maturity** (par repaid, the ordinary case), **the call** (the issuer refinances when rates fall — exactly when the holder least wants the money back, `★ G285`), or **default** (Z4.6 — acceleration, restructuring `★ G81`, recovery `★ G61`).
- Why the arc matters for the app's learners: every metric in Zones 2 and 4 (YTM, duration, spread, YTW) is a *snapshot along this arc*, and each assumes a different ending. Yield-to-maturity assumes death #1; yield-to-worst prices death #2; spreads price the odds of death #3.

**Connects to.** Z1.6 (birth), Z2.3 (pull to par), `★ G285` (the call), Z4.6 (default & recovery), `★ G255` the credit cycle (the weather across the life), Z1.2 (the object whose biography this is).

---

# ZONE 2 · Bond Math & the Curve

**What this zone is:** the arithmetic engine. Discounting (inheriting `★ G90` rather than re-teaching it), pricing and the price–yield inversion (`★ G266`), par/premium/discount and the pull to par, the day-count plumbing, the yield-measure family and its disambiguation (`★ G265` vs. `★ G58`), total return decomposed, the curve as a pricing toolkit (`★ G269` — the third vantage on the object Macro homed as `★ G248`/`★ G257`), the term-structure theories, and the two risk numbers everything downstream runs on: duration (`★ G267`) and convexity (`★ G268`). *(Sources: Parameswaran Ch. 1–5 as the pedagogical spine; Tuckman Ch. 1–8 as the modern quantitative treatment; Fabozzi Ch. 5, 7–9; Thau Ch. 3–4 for the plain-English layer; Huggins Ch. 5 for the practitioner caveats.)*

`Discounting → Pricing & the inversion → Par/premium/discount → Day counts & accrued → The meanings of yield → Total return → Spot/forward/par → Term-structure theories → Duration → Convexity → Hedging & immunization logic.`

---

### Z2.1 · Discounting & the Time Value of Money `[core]`

**Quick definition.** The single principle under all of fixed income: a dollar later is worth less than a dollar now, so every bond is valued by discounting its future cash flows to the present — the same DCF machinery IB homed at `★ G90`, applied to contractual cash flows.

**Explainer covers (basic → technical):**
- The back-link discipline first: DCF is homed in IB (`★ G90`); this node does not re-teach it — it specializes it. Bonds are the *cleanest possible DCF*: the cash flows are contractual, so all the uncertainty lives in the discount rate.
- Compounding conventions that actually bite (Parameswaran Ch. 1): nominal vs. effective rates, semiannual compounding (the US bond norm — a "5% yield" means 2.5% per half-year), and continuous compounding as the quant limit (Tuckman's appendices).
- The discount factor as the primitive (Tuckman Ch. 1): d(t) = the price today of $1 at time t. A bond's price is just its cash flows times the discount factors. Everything in Z2.7 is machinery for *extracting* those discount factors from market prices.
- Annuities and perpetuities as bond building blocks: a coupon bond = an annuity (the coupons) + a zero (the face). This decomposition is why zeros (Z3.2) are conceptually prior to coupon bonds even though coupon bonds came first historically.

**Connects to.** `★ G90` DCF (the home — back-link), Z2.2 (pricing as applied discounting), Z2.7 (extracting discount factors), `★ G248` (the risk-free rate as the base discount rate), `★ G1` IRR (YTM is an IRR — the PE bridge). *Real-world layer: Parameswaran Ch. 1 end-to-end.*

---

### Z2.2 · Bond Pricing & the Price–Yield Inversion `★ GLOBAL (G266)` `[core]`

**Quick definition.** A bond's price is the present value of its remaining cash flows at the market's required yield — which makes price and yield two expressions of one number moving in *opposite directions*: when rates rise, existing bond prices fall, mechanically.

**Explainer covers (basic → technical):**
- The mechanism in one story (Thau's version): you hold a 3% coupon bond; the market now offers 5% on new bonds. Nobody will pay par for your 3% — your price falls until a buyer earns 5% on it. No judgment, no panic: arithmetic.
- The pricing equation (Parameswaran Ch. 2): price = coupon annuity discounted at y + face discounted at y. Yield up → every discount factor down → price down. The relationship is convex, not linear (previewing `★ G268`).
- Why this is the single most consequential fact in retail finance: "bonds are safe" and "bond funds lost 13% in 2022" are both true — the *payments* were safe; the *prices* repriced to a 4-handle world. 2022 is the canonical modern case (`GAP:` post-dates Thau/Fabozzi; Tuckman's framework covers it, the episode itself needs current-data authoring).
- What moves the yield that moves the price: the risk-free base (`★ G248` — Macro's channel) plus the credit spread (`★ G277` — Zone 4's channel). Decomposing a price move into "rates" vs. "spread" is the first skill of bond P&L attribution (Tuckman Ch. 3).

**Connects to.** `★ G265` YTM (the y in the equation), Z2.3 (price relative to par), `★ G267`/`★ G268` (the sensitivity of this relationship), `★ G248` + `★ G277` (the two components of yield), Macro Z4.10 (the same inversion driving multiples and cap rates — `★ G259`). Across the graph: WM (why bond funds fell), AM Z2.8 (duration positioning is a bet on this).

---

### Z2.3 · Par, Premium & Discount (and the Pull to Par) `[core]`

**Quick definition.** The three price states of a coupon bond — at par (coupon = market yield), at a premium (coupon > yield), at a discount (coupon < yield) — and the gravitational fact that all of them converge to par as maturity approaches.

**Explainer covers (basic → technical):**
- The classification and what it *signals*: a premium price isn't "expensive" and a discount isn't "cheap" — they just date the bond's birth rate environment against today's (Z1.9's time-capsule point). A 7% coupon trading at 108 and a 3% coupon trading at 92 can have identical yields.
- The pull to par (Parameswaran Ch. 2): hold yield constant and roll the calendar — the premium bond's price drifts *down* to 100, the discount bond's drifts *up* to 100, the par bond stays put. Price change over time therefore has two parts: the market's yield moves *and* the deterministic pull.
- The income-vs-capital composition: a premium bond pays more coupon and gives some back in price; a discount bond pays less coupon and makes it up in appreciation. Same total return, different tax and cash-flow texture (the muni market lives on this — `★ G273`; and OID `★ G71` is the loan-world sibling of discount accrual).
- Roll-down as the trading expression (previewing Z2.6): on an upward-sloping curve, a bond "rolls down" to lower yields as it shortens — a return source that exists even if the curve never moves.

**Connects to.** Z2.2 (the pricing this classifies), Z1.9 (the arc), Z2.6 (carry & roll), `★ G71` OID (back-link — the private-market discount mechanics), `★ G273` munis (premium/discount tax treatment). *Real-world layer: Parameswaran's premium/discount tables.*

---

### Z2.4 · Accrued Interest, Day Counts & the Dirty Price `[branch]`

**Quick definition.** The settlement plumbing: buyers compensate sellers for interest earned since the last coupon (**accrued interest**), quoted prices exclude it (**clean**) while invoices include it (**dirty**), and the accrual is counted under market-specific **day-count conventions**.

**Explainer covers (basic → technical):**
- The mechanism: coupons pay the *holder of record* on the coupon date, so a mid-period seller would lose earned interest — accrued interest fixes that at settlement. Dirty price = clean price + accrued; the screen shows clean, the wire moves dirty.
- The day-count zoo (Parameswaran Ch. 3): actual/actual (Treasuries), 30/360 (corporates and munis), actual/360 (money market — why a T-bill "discount rate" isn't a yield, Z3.5). Same bond math, different calendars; getting the convention wrong misprices the trade.
- The saw-tooth: dirty price climbs between coupons and drops by the coupon on payment date — a pattern that is *not* a market move, which is exactly why quoting convention strips it out.
- Where it bites: settlement fails, coupon rolls, and the ex-dividend mechanics of specific markets — leaf-level detail; this node places the concept and flags the depth. `GAP:` full per-market convention tables are reference material for the depth layer, not the map.

**Connects to.** Z2.2 (what the quoted price actually is), Z3.1/Z3.5 (Treasury vs. money-market conventions), Z5.1 (settlement at the desk). *Real-world layer: Parameswaran Ch. 3 (the convention walkthroughs).*

---

### Z2.5 · The Many Meanings of Yield `★ GLOBAL (G265)` `[core]`

**Quick definition.** Yield to maturity — the single discount rate equating price to the PV of remaining cash flows, i.e. the bond's IRR at today's price — *and* the disambiguation of the whole yield family: coupon, current yield, YTM, yield-to-call/worst, and Private Credit's all-in loan yield (`★ G58`).

**Explainer covers (basic → technical):**
- The family, in one worked contrast (Thau Ch. 4 — her chapter title is this node's title): a 6% coupon bond at 90 has a 6% *coupon*, a 6.7% *current yield* (6/90), and an ~7.8% *YTM* (which adds the pull-to-par gain). Three "yields," one bond — and salespeople historically quoted whichever flattered.
- What YTM really is and really assumes: an IRR (`★ G1` — the PE bridge is literal) with a buried assumption that coupons reinvest *at the YTM*. Realized return only equals YTM if rates cooperate — the reinvestment-risk footnote (Fabozzi Ch. 5's total-return critique, deepened at Z2.6).
- Yield-to-call and yield-to-worst (previewing `★ G285`): recompute YTM to each call date and price; the *worst* of them is the honest quote for a callable — the market's standard convention for pricing the issuer's option crudely before OAS does it properly (`★ G277`).
- The `★ G58` seam (Part 1 callout, restated because it's load-bearing): Private Credit's "yield" is an *underwriting construction* — SOFR + spread + OID + fees on a loan that never trades. This node's YTM is a *market observation* on a security that reprices daily. When AM says "the Agg yields 4.6%," it means the aggregated YTM of `★ G283`'s basket.

**Connects to.** `★ G58` (disambiguate_with — the paired yield), `★ G1` IRR (the shared math), Z2.2/Z2.3 (price ↔ yield ↔ par state), `★ G285` (YTW), Z2.6 (why realized ≠ quoted), `★ G170` (WM's withdrawal math consumes this number). *Real-world layer: Thau Ch. 4; Parameswaran Ch. 3 (the full measure-by-measure derivations).*

---

### Z2.6 · Total Return: Carry, Roll & Price `[core]`

**Quick definition.** What a bondholder actually earns over a horizon, decomposed: **carry** (coupon income plus financing), **roll-down** (the deterministic slide along the curve), and **price return** (the mark-to-market from yield and spread moves) — the P&L attribution frame of every bond desk.

**Explainer covers (basic → technical):**
- Why the decomposition exists (Tuckman Ch. 3): "the bond yields 5%" tells you almost nothing about what you'll *make* this year. Total return = income earned + price change, and the price change splits into the passage of time (pull-to-par + roll-down — knowable today) and market moves (rates + spread — not knowable).
- Carry properly defined: coupon accrual *minus the cost of financing the position* (repo, `★ G282`) — positive carry means the position pays you to wait; negative carry means the clock is against you (Willer's "learn to love negative carry" for EM is the exception that proves the rule).
- Roll-down: on an upward-sloping curve a 5-year bond becomes a 4-year bond priced at a lower yield — a price gain from *aging*, harvested even in a frozen curve. Curve shape (Z2.8) is therefore a return input, not just a signal.
- Horizon analysis and the reinvestment problem (Fabozzi Ch. 5): realized compound yield over a horizon depends on where coupons get reinvested — the formal reason YTM ≠ realized return, and the origin of immunization's duration-matching logic (`★ G284`).

**Connects to.** `★ G265` (the quoted number this corrects), `★ G282` repo (the financing leg of carry), Z2.7/Z2.8 (the curve that roll-down rides), `★ G267` (price return per basis point), HF Z2.3 (RV trades are carry/roll/price bets in pairs), AM Z2.8 (the manager's scoreboard).

---

### Z2.7 · Spot, Forward & Par Rates (the Curve Toolkit) `★ GLOBAL (G269)` `[core]`

**Quick definition.** The pricing machinery extracted from bond prices: **discount factors** (the primitive), **spot rates** (zero-coupon yields), **forward rates** (the rates between future dates the curve implies), and **par rates** (the coupon that prices a bond at 100) — the arithmetic form of the term structure.

**Explainer covers (basic → technical):**
- The extraction chain (Tuckman Ch. 1–2, Parameswaran Ch. 4): observed bond prices → discount factors → spot rates by **bootstrapping** (strip the short bond's cash flows out of the longer bond's price, iterate out the curve) → implied forwards from ratios of discount factors → par curve from the spots. One dataset, four representations.
- Why YTM alone isn't enough: YTM discounts every cash flow at *one* rate, which is internally inconsistent across bonds (Huggins Ch. 5's caveat). Spot rates discount each cash flow at *its own maturity's* rate — the arbitrage-consistent frame, and the reason STRIPS (Z3.2) exist as its physical embodiment.
- Forwards as the market's break-evens: the 1-year rate 1 year forward is the rate at which rolling short bonds ties rolling long bonds — "what's priced in" for the Fed path (`★ G247`) is read off exactly here. Forward ≠ forecast (the term-premium wedge, Z2.8).
- The three-vantages callout, operationalized (Part 1): `★ G248` (the risk-free anchor for valuation), `★ G257` (the shape as macro signal), and this node (the arithmetic toolkit). Fitted curves (Z5.9 — Nelson-Siegel and friends, Huggins Ch. 8) are this toolkit industrialized for relative value.

**Connects to.** `★ G248`/`★ G257` (the sibling vantages — disambiguated in Part 1), Z2.1 (discount factors), Z3.2 (STRIPS as physical spots), Z2.8 (why the curve has its shape), Z5.9 (fitted curves), future Derivatives module (forwards are its native language — flagged seam). *Real-world layer: Parameswaran Ch. 4 (bootstrapping worked); Tuckman Ch. 2.*

---

### Z2.8 · Term-Structure Theories: Why the Curve Has Its Shape `[branch]`

**Quick definition.** The three-part answer to why long rates differ from short rates: **expectations** (long rates average expected future short rates), the **term premium** (extra yield for bearing duration risk), and **segmentation/preferred habitat** (different investors are captive to different maturities).

**Explainer covers (basic → technical):**
- Pure expectations as the baseline (Parameswaran Ch. 4): if investors were risk-neutral, the 10-year would be the geometric average of expected short rates — forwards would *be* forecasts, and an inverted curve would purely mean "cuts are coming" (the mechanism inside `★ G257`).
- The term premium correction (Tuckman Ch. 8; Fabozzi Ch. 8, Ilmanen): duration risk deserves compensation, so long yields = expected shorts + a premium that varies over time — and can go *negative* under QE (`★ G251` distorting the signal, Macro's flagged caveat, now with its mechanism).
- Segmentation and preferred habitat: pensions must own long bonds (`★ G284`), money funds must own short paper (`★ G272`) — captive demand bends segments of the curve independent of expectations (the UK LDI episode as the extreme case, flagged at Z5.8).
- Reading a curve move by decomposition: bull steepener vs. bear steepener vs. flattener each tells a different story about *which* component moved — the grammar `★ G257` uses, taught here with the machinery under it.

**Connects to.** `★ G257` (the signal this theory underwrites — back-link), `★ G269` (the arithmetic it explains), `★ G251` QE/QT (the distortion), `★ G284` LDI (habitat demand), HF Z2.4 (macro curve trades), Willer Ch. 6 (the EM version). `GAP:` post-2022 term-premium estimates and the QT-era curve are recency-flagged; frameworks stable, levels stale.

---

### Z2.9 · Duration & DV01 `★ GLOBAL (G267)` `[core]`

**Quick definition.** The master risk number: **duration** measures how much a bond's price changes for a change in yield (modified duration ≈ %-price-change per 1% yield move; DV01 = the dollar change per basis point) — and it is *not* maturity, though the two rhyme.

**Explainer covers (basic → technical):**
- The intuition ladder: (1) longer bonds swing more; (2) precisely, price sensitivity ≈ the PV-weighted average time to the cash flows (Macaulay), because distant cash flows get discounted hardest; (3) the trading form is DV01 — dollars per basis point — because desks hedge dollars, not percentages (Tuckman Ch. 4).
- The duration-vs-maturity disambiguation (Part 1 callout, the worked cases): 30-year coupon bond ≈ 18-year duration; 30-year zero = 30-year duration (nothing arrives early); floater ≈ duration to the next reset (`★ G69` — why private credit "has no duration" and why floaters were 2022's shelter); higher coupon → lower duration (more of the value arrives sooner).
- Portfolio duration and the hedge ratio: durations aggregate value-weighted; matching DV01s is how a desk hedges a corporate with Treasuries or futures, and how AM Z2.8 states its benchmark bet ("half a year long duration"). Key-rate/partial '01s (Tuckman Ch. 5) refine "the" yield move into moves at each curve point — named here, deferred to depth.
- The limits that motivate the next node: duration is the *linear* approximation, good for small moves, wrong for big ones — and systematically wrong in one direction, which is convexity's subject.

**Connects to.** `★ G268` convexity (the correction), `★ G266` (the relationship it linearizes), `★ G284` immunization (duration-matching as strategy), `★ G69` floaters (the near-zero-duration case), Z5.4 (futures/swaps as duration tools), AM Z2.8 / WM (the word they've been using unexplained — this is its home). *Real-world layer: Parameswaran Ch. 5; Tuckman Ch. 4–5.*

---

### Z2.10 · Convexity `★ GLOBAL (G268)` `[core]`

**Quick definition.** The curvature in the price–yield relationship: for a plain bond, prices rise *more* when yields fall than they drop when yields rise — a free asymmetry duration misses — and for prepayable bonds the curvature flips *negative*, the defining pathology of MBS.

**Explainer covers (basic → technical):**
- The picture: the price–yield curve is bowed toward the origin. Duration is the tangent line; convexity is how the curve bends away from it. Big rate moves therefore beat the duration estimate on the upside and undershoot it on the downside — positive convexity is worth paying for (Parameswaran Ch. 5).
- Where convexity comes from: dispersion of cash flows — zeros have the least for their duration, long low-coupon bonds the most. Barbell vs. bullet portfolios with equal duration differ in convexity, which is a real trade (Fabozzi Ch. 9; HF Z2.3's butterfly trades live here).
- **Negative convexity** (the load-bearing case, previewing `★ G280`): when rates fall, homeowners refinance — the MBS holder gets principal back exactly when reinvestment rates are worst, so the price *stops rising*. When rates rise, prepayments stop and duration *extends* into the sell-off. The price–yield curve bends the wrong way on both sides. Callable bonds (`★ G285`) share the disease in miniature.
- The practitioner caveat (Huggins Ch. 5): "convexity" gets misapplied when yield curves aren't flat — the common textbook shortcut mistakes a curve effect for a convexity effect. Flagged at map level; the correction lives in the depth layer.

**Connects to.** `★ G267` (the linear term this corrects), `★ G280` MBS & `★ G285` callables (negative convexity's homes), Z2.11 (hedging the second order), HF Z2.3 (convexity trades), `★ G259` (the discount-rate channel — long-duration assets are also the most *convex*, the VC/growth-equity rhyme). *Real-world layer: Parameswaran Ch. 5; Tuckman Ch. 4.*

---

### Z2.11 · Hedging & Immunization Logic `[branch]`

**Quick definition.** The zone's payoff assembled: with duration and convexity in hand, a portfolio can be *neutralized* against rate moves — matching DV01s to hedge a position, matching duration (and dispersion) to immunize a liability — the logic that Z5 turns into practice.

**Explainer covers (basic → technical):**
- The single-position hedge: short enough Treasuries (or futures/swaps — Z5.4, usage level) to zero the DV01, leaving only the *spread* exposure — the standard way a credit desk isolates what it's actually paid to take (`★ G277`).
- Single-period immunization (Parameswaran Ch. 5's proof, in words): set portfolio duration equal to the horizon and the two rate risks — reinvestment (rates fall, coupons reinvest worse) and price (rates rise, sale price worse) — offset each other. The pension version scales this into LDI (`★ G284`, the Z5.8 home).
- Beyond parallel shifts: duration hedges assume the whole curve moves together; key-rate '01s, regression hedging, and PCA (Tuckman Ch. 5–6; Huggins Ch. 3) handle twists — named as the professional toolkit, deferred to the depth layer and to the RV node (Z5.9).
- The honest limit: immunization is against *rates*, not *credit* — a duration-matched corporate portfolio still bleeds if spreads widen (`★ G255`). Zone 4 prices what this zone can't hedge.

**Connects to.** `★ G267`/`★ G268` (the inputs), `★ G284` LDI (the institutional application — home in Z5.8), Z5.4 (the instruments, usage level), Z5.9 (PCA-grade hedging), `★ G277` (the residual this isolates). `GAP:` key-rate, regression, and PCA hedging are placed by name; full treatment belongs to depth authoring against Tuckman Ch. 5–6.

---

# ZONE 3 · The Instrument Universe

**What this zone is:** the tour, taken with the math already in hand. Treasuries and the auction machine (`★ G270`), zeros and STRIPS, TIPS and the breakeven (`★ G271`), the agencies, the money market (`★ G272`), munis and the tax math (`★ G273`), corporates (`★ G274`), the floating-rate world (back-linking `★ G69`), embedded options (`★ G285`), and the two structural frontiers — securitization (`★ G279`/`★ G280`) and emerging markets (`★ G281`). Each instrument node answers the same four questions: who issues it, what's distinctive about its cash flows, what risk dominates it, and who buys it. *(Sources: Fabozzi Part 3 as the encyclopedic base; Thau Part 2 for the investor lens; Parameswaran Ch. 6–9 for money market, floaters, mortgages, MBS; Tuckman Ch. 15; Willer for EM.)*

`Treasuries → Zeros & STRIPS → TIPS → Agencies → The money market → Munis → Corporates → Floaters & loans → Embedded options → Securitization → Agency MBS → EM debt.`

---

### Z3.1 · The U.S. Treasury Market `★ GLOBAL (G270)` `[core]`

**Quick definition.** The market for U.S. government debt — **bills** (≤1 year, discount instruments), **notes** (2–10 years), and **bonds** (20–30 years) — the largest and most liquid securities market on earth, the risk-free benchmark (`★ G248`) made tradable, and the anchor issuer of the entire system.

**Explainer covers (basic → technical):**
- Why Treasuries are special (Thau Ch. 6): full-faith-and-credit backing (default risk treated as ~zero in pricing — with the sovereign caveat parked at `★ G262`), unmatched liquidity, exemption from state tax, and the role of *the* collateral of the financial system (`★ G282`).
- The auction machine (Parameswaran Ch. 2; Z1.6 deepened): the announced calendar, competitive bids in yield, single-price clearing, **primary dealers** obligated to bid, **when-issued** trading before settlement, and re-openings. Auction "tails" and bid-to-cover as the market's fiscal thermometer (`★ G242`).
- The liquidity microstructure: **on-the-run** (the newest issue at each maturity — the trading vehicle) vs. **off-the-run** (everything older — cheaper, less liquid); the run/off-run spread as the price of liquidity itself, and a classic RV trade (Z5.9; LTCM's infamous version).
- What the market *does* for everyone else: supplies the risk-free curve every spread is measured against (`★ G277`), the collateral repo runs on (`★ G282`), the hedge instrument for every desk (Z2.11), and the deliverable for the futures complex (Z5.4). The 10-year yield is arguably the single most important price in finance (`★ G248`'s "price of time," now with its marketplace).

**Connects to.** `★ G248` (the concept this market embodies), Z1.6 (auctions), `★ G282` repo, `★ G251` QE/QT (the Fed as largest holder — and QT as supply), `★ G262` sovereign risk (the tail case), Z3.2 (STRIPS carved from these), `★ G283` (the index weight). *Real-world layer: Fabozzi Ch. 10; Tuckman Ch. 0.*

---

### Z3.2 · Zeros & STRIPS `[branch]`

**Quick definition.** Bonds with no coupons — sold at a discount, paying face at maturity — and **STRIPS**, the Treasury program that carves coupon bonds into separately tradable zero-coupon pieces: the physical embodiment of the spot curve (`★ G269`).

**Explainer covers (basic → technical):**
- The cleanest bond there is: one cash flow, so yield *is* the spot rate, duration *equals* maturity (`★ G267`'s limiting case), and convexity is maximal per unit of duration (`★ G268`). Zeros are the atoms; coupon bonds are molecules (Z2.1's decomposition made literal).
- STRIPS mechanics (Parameswaran Ch. 2): dealers separate a note's coupons and principal into individual claims (Separate Trading of Registered Interest and Principal); the pieces trade as zeros and can be *reconstituted*. Arbitrage between the bond and its pieces enforces the bootstrapped curve (Z2.7).
- Who wants them: liability-matchers who need a known sum on a known date (`★ G284` — a zero is a self-immunizing bond), and the tax wrinkle that phantom income (accrued OID, `★ G71`'s public-market cousin) is taxed annually, pushing zeros into tax-deferred accounts (Thau).
- The volatility warning (Thau): the longest zeros are the most rate-sensitive instruments in the Treasury complex — retail buys them for "safety" and discovers duration.

**Connects to.** `★ G269` (spots made physical), `★ G267` (duration = maturity case), `★ G271` (TIPS also strip), `★ G284` (the LDI use), `★ G71` OID (back-link — accretion math shared with loans). *Real-world layer: Parameswaran (synthetic zeros); Fabozzi Ch. 10.*

---

### Z3.3 · TIPS & Inflation-Linked Bonds `★ GLOBAL (G271)` `[core]`

**Quick definition.** Treasuries whose principal indexes to CPI — coupons pay a fixed *real* rate on the inflating principal — so the holder earns purchasing power directly, and the *gap* between nominal and TIPS yields (**the breakeven**) is the market's own inflation forecast.

**Explainer covers (basic → technical):**
- The mechanism (Fabozzi Ch. 15; Thau Ch. 6): principal adjusts with CPI (`★ G253`); the coupon rate is real and constant; at maturity you get the greater of adjusted or original principal (the deflation floor). The instrument operationalizes the Fisher relation (`★ G249` — back-link: that node's math, this node's security).
- The breakeven as information: nominal 10y minus TIPS 10y ≈ expected inflation plus an inflation-risk premium — the bond market's inflation expectation read in real time, the anchoring evidence Macro Z3.5 relies on (back-link).
- What TIPS hedge and what they don't: realized CPI inflation, yes; *real-rate* rises, no — 2022's lesson, when TIPS fell despite the inflation spike because real yields surged (`GAP:` the episode post-dates the sources' data; framework covered by Tuckman/Willer, levels need current authoring).
- The EM version (Willer Ch. 7 — "real rates: simply superior"): linkers are a mature, often superior habitat in high-inflation EMs (Brazil's market as the canon); breakeven trading rules (buy breakevens below inflation expectations) preview Z5.10.

**Connects to.** `★ G249` Fisher (back-link — the concept), `★ G252`/`★ G253` inflation & the indices (what's being indexed), `★ G270` (the issuer), WM (the retiree inflation hedge), Willer Ch. 7 (EM linkers), Z5.10. *Real-world layer: Fabozzi Ch. 15 (Brynjolfsson); Thau's TIPS chapter.*

---

### Z3.4 · Agencies & the GSEs `[branch]`

**Quick definition.** Debt of the government-sponsored enterprises (Fannie Mae, Freddie Mac, the FHLBs) and federal agencies — near-Treasury credit with a small spread, and the institutional machine whose *guarantee business* makes the agency MBS market (`★ G280`) possible.

**Explainer covers (basic → technical):**
- The two products of one system: agency *debentures* (this node — bullet or callable senior debt funding the enterprises) and agency *MBS guarantees* (Z3.11 — the credit wrap on pooled mortgages). The debenture market is the callable-bond training ground (`★ G285` in the wild).
- The credit nuance: "implicit" government backing priced at a sliver over Treasuries — made near-explicit by the 2008 conservatorships (Fabozzi Ch. 10's account; the episode is the case study for `★ G263`'s taxonomy touching home soil).
- Who buys: banks (favorable capital treatment), foreign officials, and money funds at the short end; the FHLB system doubling as a quiet liquidity backstop for banks (the 2023 regional-bank episode — `GAP:` post-dates all sources; flag for current authoring).
- The map placement note: this node is deliberately compact — the agencies matter to this app mostly as the *gateway to MBS*, which carries the full treatment.

**Connects to.** `★ G280` (the main event this enables), `★ G285` (callable debentures), `★ G270` (the pricing benchmark), `★ G263` (the 2008 case), RE module (the housing-finance context). *Real-world layer: Fabozzi Ch. 10 (agency securities).*

---

### Z3.5 · The Money Market `★ GLOBAL (G272)` `[core]`

**Quick definition.** The market for debt maturing inside a year — **T-bills**, **commercial paper**, **negotiable CDs**, **fed funds**, and repo (`★ G282`) — where the policy rate (`★ G247`) becomes actual funding, and where "cash" in every portfolio actually lives.

**Explainer covers (basic → technical):**
- The instrument roster (Parameswaran Ch. 6; Fabozzi Ch. 12): T-bills (discount instruments — quoted on a discount rate that *understates* the true yield, the day-count trap of Z2.4), commercial paper (corporates borrowing short, unsecured), negotiable CDs (banks borrowing short), bankers' acceptances (vestigial), and fed funds (banks trading reserves overnight — the market `★ G247` literally names).
- The rate plumbing: the policy rate anchors overnight money; bills, CP, and CDs price off it with tenor and credit increments; SOFR (`★ G69`) is manufactured from the repo segment (Z5.2 tells that story). This node is the transmission mechanism's (`★ G250`) first meter.
- Why it matters beyond plumbing: the money market is where funding stress *shows first* — CP freezing in 2008, the bill curve kinking around debt-ceiling dates, money funds "breaking the buck" (`★ G263`'s early-warning gauges).
- The vehicle seam (Part 1 callout): money market *funds* — the WM cash bucket — are the retail wrapper on these instruments; the segment is homed here, the wrapper with the fund modules (Z5.7).

**Connects to.** `★ G247` (the anchor rate — back-link), `★ G69` SOFR (manufactured here — back-link), `★ G282` repo (the secured half), Z2.4 (discount-rate quoting), `★ G250` transmission (Macro's chain, first link), WM (cash management). *Real-world layer: Parameswaran Ch. 6 end-to-end; Fabozzi Ch. 12.*

---

### Z3.6 · Municipal Bonds `★ GLOBAL (G273)` `[core]`

**Quick definition.** Debt of states, cities, and their authorities, whose interest is **exempt from federal tax** — making the muni market a parallel bond universe priced in after-tax terms, navigated with the **taxable-equivalent yield** and split between general-obligation and revenue credit.

**Explainer covers (basic → technical):**
- The tax math that defines the market (Thau Ch. 7): TEY = muni yield ÷ (1 − marginal tax rate). A 3.5% muni beats a 5% taxable for a 37%-bracket buyer (TEY ≈ 5.6%) and loses for a low-bracket one — which is why munis are a *household and high-bracket* market, largely absent from pensions and foreign portfolios (they can't use the exemption).
- The two credit species (Fabozzi Ch. 11, 34): **general obligation** (backed by taxing power — analyzed like a sovereign-in-miniature: tax base, pension burden) vs. **revenue** (backed by a project's cash flows — tolls, water, hospitals — analyzed like project finance: coverage `★ G74`'s cousin, rate covenants).
- Muni market structure quirks: enormous issue count with tiny sizes, thin retail-heavy secondary (Z1.7's illiquidity extreme), serial maturities, insurance wrappers (diminished post-2008), and the premium-coupon convention (Z2.3's tax-driven de-minimis mechanics — depth-layer detail, placed here).
- Default reality vs. reputation: historically low default rates but concentrated, slow-motion failures (Detroit, Puerto Rico) — the `★ G262` sovereign-analysis toolkit scaled to sub-sovereigns.

**Connects to.** WM (the natural holder — the tax-location decision), `★ G276` ratings (muni scales), `★ G262` (the GO analysis rhyme), Z1.7 (the illiquid secondary), `★ G242` fiscal policy (state/local edition). *Real-world layer: Thau Ch. 7 (the buyer's guide); Fabozzi Ch. 11 & 34.*

---

### Z3.7 · Corporate Bonds `★ GLOBAL (G274)` `[core]`

**Quick definition.** Standardized, rated, tradable debt issued by companies under an **indenture** with a trustee — the public-market output of IB's debt capital markets, spanning AAA utilities to CCC leveraged credits, and the raw material of Zone 4's entire credit apparatus.

**Explainer covers (basic → technical):**
- The contract (Fabozzi Ch. 13): the **indenture** (the master agreement), the **trustee** (the holders' agent), seniority and security (`★ G78` — back-link: liens and priority are homed with Private Credit), and covenants — typically *incurrence-only*, the structural covenant-lite contrast with private loans (`★ G34`, Z1.8's seam).
- The retirement menu: bullets, sinking funds, calls (`★ G285`), make-wholes, tenders, and defeasance — the issuer's toolkit for getting out early, each priced by the market (Fabozzi's "alternative mechanisms to retire debt").
- The market's internal geography: IG vs. HY (`★ G275` — the divide gets its own node), financials vs. industrials vs. utilities, MTN programs (Z1.6), and the maturity ladder from 2s to 30s along the credit curve (Z4.9's raw material).
- The three-market view of one borrower (Z1.8 completed): the same credit can have bonds (here), a TLB (PC Z1.7), and CDS (`★ G278`) — the capital-structure map ER and HF Z2.8 trade across. Sector-level credit work (banks vs. energy vs. utilities) is deferred to the sector modules (`GAP:` deliberate, per scope boundary 3).

**Connects to.** IB DCM & `★ G103` (the birth process), `★ G275`/`★ G276`/`★ G277` (Zone 4's machinery applied to these), `★ G78` (back-link — seniority), `★ G34` (covenant contrast), PC Z1.7 (the loan sibling), ER (the issuer analysis). *Real-world layer: Fabozzi Ch. 13; Tuckman Ch. 14 (first half).*

---

### Z3.8 · Floaters & Loans: the Floating-Rate Universe `[core]`

**Quick definition.** The instruments whose coupons *reset* off a reference rate — floating-rate notes, the syndicated loan market, and their structured kin — the near-zero-duration corner of the universe (`★ G267`'s limiting case) homed around `★ G69`, which this node back-links rather than re-teaches.

**Explainer covers (basic → technical):**
- The mechanics in one line: coupon = reference rate (`★ G69` SOFR — back-link, the home) + a quoted margin fixed at issue; the reset clock, caps/floors on the coupon, and the margin-measure family (discount margin as the floater's YTM-equivalent — Parameswaran Ch. 7).
- Why duration collapses: the price re-anchors to ~par at each reset — rate risk lives only until the next reset date, leaving *spread* risk as the exposure that remains (a floater is short-duration in rates but full-duration in credit; the 2022 shelter with the 2023 caveat).
- The loan overlap, mapped not re-homed: Term Loan Bs and the BSL market are Private Credit Z1.7's canonical ground; CLOs — the securitized wrapper on loans — are flagged here and treated within `★ G279`'s framework. The inverse floater and structured-note exotica (Parameswaran Ch. 7) are named as leaf variants.
- The issuer's rate-mix decision: fixed vs. floating as corporate ALM — and the swap that converts one into the other, referenced at usage level (Z5.4; mechanics to the future Derivatives module).

**Connects to.** `★ G69` (the home — back-link), PC Z1.7 (loans), `★ G267` (the duration case), `★ G277` (the spread exposure that remains), `★ G279` (CLOs as securitized loans), Z5.2 (how SOFR is made). *Real-world layer: Parameswaran Ch. 7; Fabozzi Ch. 16.*

---

### Z3.9 · Callable, Putable & Convertible: Embedded Options `★ GLOBAL (G285)` `[core]`

**Quick definition.** Bonds carrying options inside the security — the issuer's right to **call** (redeem early), the holder's right to **put** (sell back), or to **convert** into equity — whose value the market strips out via **yield-to-worst** and, properly, **OAS** (`★ G277`): the reason a 6% callable is not a 6% bullet.

**Explainer covers (basic → technical):**
- The call, from both seats: the issuer holds a refinancing option (call when rates fall or spreads tighten); the holder has *sold* that option and is paid for it in extra yield. The crude quote is **yield-to-worst** (`★ G265`'s extension); the honest price is the OAS after modeling the option (`★ G277`; lattice valuation named per Fabozzi Ch. 37, deferred to the Derivatives module for mechanics — flagged seam).
- The behavioral consequence: **negative convexity** (`★ G268`'s pathology in miniature) — price compression as rates fall toward the call. Agency debentures (Z3.4), muni pre-refundings, and HY calls are the habitats; MBS (`★ G280`) is the same option held by millions of homeowners.
- The private-market cousin, disambiguated (Part 1): `★ G72` call protection is the *negotiated shield* against early repayment in loans; this node is the *securitized option the market prices*. Same refinancing economics, opposite framing — the pair is a load-bearing cross-link.
- Puts and converts, placed: putables invert the option (holder protection — rate rises get a par exit); **convertibles** are debt with an equity call option attached (Fabozzi Part 8) — named and framed here, with the option-pricing depth explicitly deferred to Derivatives (`GAP:` deliberate; the convertible node is that module's natural attachment point back into FI).

**Connects to.** `★ G72` (disambiguate_with — the loan cousin), `★ G265` (YTW), `★ G277` (OAS — the proper strip), `★ G268` (negative convexity), `★ G280` (the mass-market version), IB (converts as issuance products), future Derivatives module (option mechanics — flagged seam). *Real-world layer: Parameswaran Ch. 13; Fabozzi Ch. 37, 59–60.*

---

### Z3.10 · Securitization `★ GLOBAL (G279)` `[core]`

**Quick definition.** The machine that turns pools of illiquid loans into tradable bonds: assets (mortgages, card receivables, auto loans) are sold to a bankruptcy-remote trust, and the trust issues **tranches** of securities against the pool's cash flows — senior to junior, each with its own rating and spread.

**Explainer covers (basic → technical):**
- The assembly line (Fabozzi Ch. 22, 26–29): originate → pool → sell to an SPV (true sale, bankruptcy-remote) → tranche the liabilities → wrap with credit enhancement (subordination, over-collateralization, excess spread) → rate (`★ G276`) → distribute. The originator gets balance-sheet relief and fees; investors get tailored risk slices.
- Tranching as the core invention: the *same pool* supports AAA seniors and equity residuals because losses hit bottom-up while cash flows fill top-down — the waterfall. Seniority here is *structural* (rules in a trust) rather than negotiated (`★ G78`'s lien world — the rhyme and the difference).
- The family tree, mapped once: residential MBS (agency → `★ G280`, the flagship; non-agency named), CMBS (**back-link `★ G227`** — homed in Real Estate, per scope boundary 2), ABS (cards, autos, student loans), and CLOs (securitized leveraged loans — the bridge back to Z3.8/PC). CDOs and the 2008 pathology carried at the framework level with `★ G263` owning the crisis narrative.
- Why the machine exists and when it breaks: it converts lending capacity into market capacity (disintermediation's other face, `★ G63`), *and* it moved underwriting risk away from originators — the incentive fault line 2008 exposed (rating-agency structured-finance process per Fabozzi Ch. 35 named; `GAP:` post-crisis reform detail — risk retention, rating reform — post-dates parts of the source base; flag for depth).

**Connects to.** `★ G280` (the flagship product), `★ G227` (back-link — CMBS stays homed in RE), `★ G63` disintermediation (back-link), `★ G276` (ratings' structured-finance arm), `★ G263` (the 2008 case), PC/Z3.8 (CLOs). *Real-world layer: Fabozzi Chs. 22–31.*

---

### Z3.11 · Agency MBS & Prepayment `★ GLOBAL (G280)` `[core]`

**Quick definition.** Bonds backed by pools of government-guaranteed home mortgages — pass-throughs and their CMO re-slicings — whose defining risk is not default (the agencies wrap that) but **prepayment**: millions of homeowners hold a free refinancing option and exercise it exactly when investors least want the money back.

**Explainer covers (basic → technical):**
- The pass-through (Parameswaran Ch. 8–9; Thau Ch. 9): homeowners' monthly payments (interest + scheduled principal + prepayments) flow through the pool to holders, minus servicing. The vocabulary: WAC, WAM, SMM/CPR (prepayment speeds), and the PSA convention — the measurement kit for a cash-flow stream that is never fixed.
- The prepayment option and its price: falling rates → refinancing wave → principal returns at par just as reinvestment rates collapse (**contraction**); rising rates → prepayments stop → duration extends into the sell-off (**extension**). This is `★ G268`'s negative convexity at population scale, and the reason MBS trade at an OAS (`★ G277`) off prepayment *models*, not just curves.
- The CMO re-slicing: sequential tranches, PACs (prepayment-protected schedules with support bonds absorbing the variance), IO/PO strips (pure bets on prepayment speed — the IO is one of the few instruments that *gains* when rates rise). Structuring redistributes the option; it cannot destroy it.
- Who holds this market and why it matters systemically: banks, the Fed (QE's second portfolio — `★ G251`), and money managers against `★ G283` (MBS is a giant index weight). The agency wrap makes it a *rates+prepayment* product; non-agency (credit-risk-bearing) MBS is named and framed under `★ G279` with the 2008 file at `★ G263`.

**Connects to.** `★ G279` (the machine that builds it), `★ G268` (negative convexity — the defining pathology), `★ G277` (OAS as the honest spread), `★ G227` (the commercial sibling — back-link), `★ G251` (the Fed's holdings), RE module (the housing-side view), `★ G283` (the index weight). *Real-world layer: Parameswaran Ch. 8–9; Fabozzi Chs. 22–24; Tuckman Ch. 15.*

---

### Z3.12 · Emerging Market Debt `★ GLOBAL (G281)` `[core]`

**Quick definition.** The sovereign and corporate debt of developing economies, structurally split in two: **local-currency** bonds (a rates market plus an FX exposure — GBI-EM) and **hard-currency/external** bonds (a credit market in dollars — EMBI), each with its own index, buyer base, and risk anatomy.

**Explainer covers (basic → technical):**
- The two-asset-class split (Willer Ch. 1 — the module's organizing fact): local debt is *rates* (`★ G247`-equivalents set by EM central banks) *plus FX* (`★ G260` — most of local-debt volatility is currency); external debt is *credit* (a spread over Treasuries, `★ G277`, behaving like US HY's cousin). Same country, two different trades.
- The historical arc: "original sin" (forced dollar borrowing) → the crises of the 1980s–90s (Bradys — Fabozzi Ch. 20 — restructuring's founding technology) → the deliberate build-out of local markets (Willer's 15% CAGR story) → China as half the local universe. The `★ G262`/`★ G263` sovereign-risk machinery is this market's operating system (back-link).
- What drives it (Willer Ch. 2's 65/35 rule): EM returns are ~two-thirds global macro — the Fed (`★ G247`), the dollar (`★ G260`), US HY spreads, commodities — and one-third local. The asset class is a leveraged read on `★ G258` global financial conditions.
- Index mechanics and the buyer base: EMBI/GBI-EM/CEMBI (`★ G283`'s EM wing), index-inclusion events as flow catalysts, and the dispersion that makes EM an *alpha* habitat (Willer Ch. 1) — the trading treatment continues at Z5.10.

**Connects to.** `★ G260`–`★ G263` (the Macro Zone 5 machinery — back-links throughout), `★ G277` (external spreads), `★ G271` (EM linkers), `★ G283` (the indices), Z5.10 (trading EM), HF Z2.4 (the macro-fund habitat). *Real-world layer: Willer Chs. 1–3, 6, 9; Fabozzi Ch. 20.*

---

# ZONE 4 · Credit & Spread

**What this zone is:** the pricing of default in a *traded* market. Credit risk restated for securities (inheriting `★ G61`/`★ G62`, not re-teaching them), the public rating agencies (`★ G276`) disambiguated from internal ratings (`★ G77`), the IG/HY divide (`★ G275`), the spread-measure family (`★ G277`) disambiguated from the loan spread (`★ G70`), what moves spreads, default and recovery when the workout happens in public, the CDS (`★ G278`), the analyst's craft, and credit relative value. *(Sources: Fabozzi Part 4 and Chs. 13, 32–33; Tuckman Ch. 14; Huggins Chs. 12–13, 16; Willer Ch. 9 for the EM wing; Thau Ch. 8 for the investor lens.)*

`Credit risk in traded markets → The rating agencies → IG vs. HY → The spread measures → What moves spreads → Default & recovery in public → The CDS → The credit work → Credit relative value.`

---

### Z4.1 · Credit Risk in Traded Markets `[core]`

**Quick definition.** The probability-times-severity of not being paid — PD (`★ G62`) × LGD (`★ G61`) — repriced *continuously by a market* rather than monitored privately by a lender: the same risk Private Credit underwrites, now with a ticker.

**Explainer covers (basic → technical):**
- The inheritance stated plainly: default probability, recovery, and loss-given-default are homed in Private Credit (`★ G62`, `★ G61`, `★ G60`) — this zone does not re-define them; it shows what happens when a *market* prices them tick by tick instead of a credit committee reviewing them quarterly.
- Expected loss as the spread's floor: spread ≈ PD × LGD + risk premium + liquidity premium (Macro Z4.8's decomposition — back-link — now applied instrument-by-instrument). The premium components are why spreads systematically *overpay* for realized defaults — the credit risk premium that makes the asset class investable.
- The migration dimension markets add: a bond can lose 15 points without any default — a downgrade (`★ G276`), a sector scare, a liquidity vacuum (Z1.7). Mark-to-market credit risk is a different animal from hold-to-maturity credit risk; the same loan hurts a BDC's NAV differently than the bond hurts a mutual fund (Z1.8's seam, restated in risk terms).
- The cycle overlay: defaults cluster (`★ G255` — back-link); spreads lead realized defaults (the market prices the *next* wave); and the credit cycle's macro seat (Macro Z4.1) meets its market seat here.

**Connects to.** `★ G61`/`★ G62`/`★ G60` (back-links — the homes), Macro Z4.8 (spreads as the price of risk — the macro seat), `★ G255` (the cycle), `★ G277` (the measurement), Z4.6 (when default arrives), PC module (the private seat throughout).

---

### Z4.2 · Credit Ratings & the Rating Agencies `★ GLOBAL (G276)` `[core]`

**Quick definition.** The public letter-grade scales — Moody's (Aaa…C), S&P and Fitch (AAA…D) — issued by licensed agencies and hard-wired into the market's plumbing: index membership, investment mandates, capital rules, and funding costs all key off these grades.

**Explainer covers (basic → technical):**
- What a rating is and is not: an *ordinal opinion of relative default risk* over a cycle — not a price, not a buy/sell, not a market forecast. The scales and their notches (Parameswaran Ch. 2's tables; Fabozzi Ch. 13), split ratings, outlooks, and watch listings as the grammar.
- Why ratings have *consequences* beyond opinion: the IG line (`★ G275`) gates index inclusion (`★ G283`), insurance and pension mandates, bank capital treatment, and CP market access (`★ G272`) — a downgrade mechanically forces selling regardless of anyone's view. Ratings are load-bearing infrastructure, which is exactly why their failures matter.
- The disambiguation (Part 1 callout): `★ G77` internal ratings are a *lender's private grade* for portfolio monitoring (watch-list `★ G82` as its action); this node's grades are *public infrastructure with market consequences*. Related craft — both estimate PD/LGD — different institutions, different stakes.
- The known pathologies, stated honestly: issuer-pays conflicts, structured-finance inflation pre-2008 (`★ G279`'s fault line; Fabozzi Ch. 35's process view), ratings *lagging* markets (Willer Ch. 9: "late, but market-moving" — spreads and CDS move first, ratings confirm). The sovereign wing (`★ G262`) and muni scales (`★ G273`) as the family's other branches.

**Connects to.** `★ G77` (disambiguate_with), `★ G275` (the divide the grades draw), `★ G283` (index gating), `★ G279`/`★ G263` (the structured-finance failure), `★ G262` (sovereign ratings), ER (the analyst's parallel opinion — `★ G182`'s world). *Real-world layer: Fabozzi Chs. 13, 32, 35; Willer Ch. 9.*

---

### Z4.3 · Investment Grade vs. High Yield (the Ratings Divide) `★ GLOBAL (G275)` `[core]`

**Quick definition.** The BBB−/Baa3 line that splits the bond market into two regimes — different buyers, different indices, different covenant norms, different spread behavior — with the **fallen angel** (IG loses the grade) and the **rising star** (HY gains it) as the boundary events the market trades.

**Explainer covers (basic → technical):**
- Two markets, not one spectrum: IG is a *rates-plus* market (spread is a minority of yield; buyers are duration-driven insurers, pensions, foreign officials); HY is an *equity-adjacent* market (spread dominates; buyers are total-return funds; correlation runs to stocks, not Treasuries — Willer's US-HY-as-EM-driver finding is this fact exported).
- The boundary mechanics: the BBB− cliff concentrates issuance just above the line (the "BBB bulge"); a fallen angel triggers forced index selling (`★ G283`) into a thin bid — a repeatable dislocation that dedicated fallen-angel strategies harvest (HF Z2.8's habitat).
- HY's anatomy (Fabozzi Ch. 13's high-yield section): the LBO/leveraged-finance connection — HY bonds fund the same sponsor deals as TLBs (PC's world) — call schedules as standard equipment (`★ G285`), and default/recovery statistics by rating cohort as the base rates the market prices against.
- The divide inside portfolios: "core" mandates hold IG (the Agg contains no HY — `★ G283`'s rule), HY lives in dedicated sleeves, and the crossover space (BB/BBB) is a strategy of its own. Willer's EM credit sweet spot (3–5yr BBs) is the same anatomy in the EMBI.

**Connects to.** `★ G276` (the grades drawing the line), `★ G283` (index consequences), IB leveraged finance & PC (the issuance engine), `★ G285` (HY call structures), HF Z2.8 (distressed & event credit), `★ G255` (HY as the cycle's amplifier). *Real-world layer: Fabozzi Ch. 13; Willer Ch. 9.*

---

### Z4.4 · Bond Spreads: G, Z & OAS `★ GLOBAL (G277)` `[core]`

**Quick definition.** The extra yield a bond offers over the risk-free curve — measured against a single curve point (**G-spread**), against the whole spot curve (**Z-spread**), or net of embedded-option value (**OAS**) — the market's continuously repriced quote for credit, liquidity, and structure.

**Explainer covers (basic → technical):**
- The measurement ladder, and why three rungs exist: G-spread (yield minus the interpolated Treasury yield — quick, curve-shape-blind), Z-spread (the constant shift to the *spot* curve `★ G269` that reprices the bond — the arithmetically honest version), OAS (the Z-spread after a model strips the option — the only fair comparison for callables `★ G285` and MBS `★ G280`). Comparing a callable's G-spread to a bullet's is the classic amateur error.
- What lives inside a spread (Macro Z4.8's decomposition, operationalized): expected loss (PD×LGD — `★ G62`/`★ G61`), a credit risk premium, and a liquidity premium (Z1.7's tiers priced). Spread *level* prices the credit; spread *change* is the P&L (Z2.6's attribution completed: rates + spread).
- The `★ G70` disambiguation (Part 1 callout, restated at the home): the loan spread is *contractual* — set at close, changes only on repricing; these spreads are *observed* — recomputed with every trade. The same borrower's TLB spread and bond Z-spread inform each other but are different objects; their gap is capital-structure information (Z4.9).
- The family's extensions, placed: asset-swap spreads and SOFR spreads (Huggins Chs. 12, 17 — the post-LIBOR yardstick, deepened at Z5.9), CDS spreads (`★ G278` — the third quote on the same risk), and the EM sovereign spread (EMBI's currency — `★ G281`).

**Connects to.** `★ G70` (disambiguate_with — the loan spread), `★ G269` (the curve it's measured against), `★ G285`/`★ G280` (why OAS exists), Macro Z4.8 (the decomposition — back-link), `★ G278` (the derivative quote), Z4.5 (what moves it). *Real-world layer: Fabozzi Ch. 39 (OAS); Tuckman Ch. 3; Huggins Ch. 12.*

---

### Z4.5 · What Moves Spreads (the Spread Cycle) `[core]`

**Quick definition.** The drivers of spread widening and compression: the credit cycle's fundamentals (defaults ahead), risk appetite (the premium demanded), supply/demand technicals (issuance, fund flows, dealer capacity), and liquidity shocks — the market weather Zone 4's instruments live in.

**Explainer covers (basic → technical):**
- The four-driver frame: (1) **fundamentals** — expected defaults over the horizon (`★ G255`'s position); (2) **risk premium** — the compensation mood (`★ G127`'s pendulum in credit clothing); (3) **technicals** — new-issue calendars, fund flows, index events (`★ G283`), dealer balance-sheet capacity (Huggins Ch. 18's post-Basel constraint); (4) **liquidity** — the Z1.7 premium repricing violently in stress.
- The cyclical signature: spreads grind tighter for years and gap wider in weeks (the asymmetry every credit book carries); HY leads IG; spreads *lead* realized defaults (the market prices the next wave, then the defaults arrive into already-wide spreads — the sequencing Willer exploits in EM Ch. 9).
- Compression's anatomy — the private-credit rhyme: PC Z5.13's "spread compression in a capital-flooded market" is this node's mechanism operating in the private market; too much capital chasing carry compresses *both* markets' spreads and erodes *both* markets' covenants (`★ G34`) simultaneously. One cycle, two venues.
- The macro read-through: IG and HY spreads are inputs to financial conditions (`★ G258` — back-link); the HY spread is a recession gauge that rivals the curve (`★ G257`); and spread blowouts are how `★ G263`'s crises announce themselves in this market.

**Connects to.** `★ G255`/`★ G258` (back-links — the macro machinery), `★ G127` (the sentiment overlay), PC Z5.13 (the private rhyme), `★ G283` (technicals), Z1.7 (liquidity), Willer Ch. 9 (the EM playbook). `GAP:` the 2020 COVID spread event and the Fed's corporate-credit facilities post-date most sources' data — framework covered, episode needs current authoring.

---

### Z4.6 · Default, Restructuring & Recovery in Public Markets `[core]`

**Quick definition.** What happens when the promise breaks and the workout occurs *in public*: acceleration, bankruptcy or exchange offers, the priority waterfall paying recoveries by seniority — the traded-market version of the process Private Credit homes at `★ G81`, with distressed investors as the market's undertakers.

**Explainer covers (basic → technical):**
- The event taxonomy: missed payment (past grace), bankruptcy filing, and the *distressed exchange* (a haircut dressed as a tender — the majority of modern "defaults" — a definitional point that matters for reading default statistics and triggers `★ G278`'s committee machinery).
- The waterfall in action: recoveries by seniority and security (`★ G78` — back-link) — secured loans recover most, senior unsecured bonds the benchmark ~40¢ heuristic, subordinated less — the LGD (`★ G61`) statistics behind every spread floor (Z4.1), with the honest caveat that recoveries are cycle-dependent (they fall exactly when defaults cluster).
- Public vs. private workout, the seam completed: `★ G81` (out-of-court restructuring) and `★ G82` (watch-list) are the private lender's quiet process; the public version plays out in prices — bonds trade to recovery estimates within days, and control shifts to whoever buys the fulcrum security. Distressed investing (HF Z2.8 — back-link) is the strategy of buying that transition.
- EM defaults as the sovereign wing (Willer Ch. 9's "embrace defaults"): sovereign restructurings (`★ G262` — back-link) run on exchange offers and CACs rather than bankruptcy courts; recovery outcomes have historically rewarded buying *into* EM defaults — the counterintuitive base rate his backtests document.

**Connects to.** `★ G81`/`★ G82`/`★ G78` (back-links — the private process), `★ G61`/`★ G62` (the statistics), HF Z2.8 (the buyers), `★ G262` (sovereign workouts), `★ G278` (the trigger machinery), Z1.9 (death #3 in the bond's life). *Real-world layer: Fabozzi Ch. 13 (default/recovery data); Willer Ch. 9.*

---

### Z4.7 · The Credit Default Swap `★ GLOBAL (G278)` `[core]`

**Quick definition.** A contract paying out if a reference borrower defaults, in exchange for a running premium — tradable default insurance that separates credit risk from the bond itself, quotes it as a spread, and lets credit be *shorted*, hedged, and measured independently.

**Explainer covers (basic → technical):**
- The mechanics at concept level (Tuckman Ch. 14; Huggins Ch. 13): protection buyer pays a running spread; on a *credit event* (failure to pay, bankruptcy, restructuring — determined by committee), the seller pays par minus recovery. The CDS spread is thus a near-pure market quote on PD×LGD (`★ G62`×`★ G61`) — cleaner than a bond spread because funding and curve noise are stripped out.
- What the instrument *enables*: shorting credit without borrowing bonds, hedging a loan book without selling relationships, expressing single-name views at size, and index trading (CDX/iTraxx) as the credit market's futures. The negative-basis trade (bond + CDS protection) as the arbitrage that ties `★ G277` and this quote together (Huggins Ch. 16's equilibrium machinery, deepened at Z5.9).
- The sovereign wing: sovereign CDS as the market's read on `★ G262` — with the wrinkles Huggins documents (the delivery option, USD-payout quanto effect) that make the quote *more* than pure default probability.
- The scope-boundary note, stated in the map (Part 4 repeats it): CDS is homed *here* because the sources treat it as inseparable from traded credit; the future Derivatives module owns general swap/option mechanics and the post-crisis clearing/margin plumbing, and will back-link G278 rather than re-home it. `GAP:` ISDA determinations detail and the cleared-CDS market structure are deferred to that module.

**Connects to.** `★ G277` (the cash-market quote — the basis pair), `★ G61`/`★ G62` (what it prices), Z4.6 (the trigger events), `★ G262` (sovereign CDS), HF Z2.8 (the users), future Derivatives module (mechanics — flagged seam), Macro (credit conditions read via CDX). *Real-world layer: Tuckman Ch. 14; Huggins Ch. 13; Fabozzi Ch. 58.*

---

### Z4.8 · The Credit Work: Analyzing a Corporate Bond `[branch]`

**Quick definition.** The analyst's craft applied to a traded credit: business risk, financial risk (the coverage and leverage arithmetic inherited from Private Credit), indenture and structure reading, and the relative-value judgment — ER's discipline pointed at the debt side of the balance sheet.

**Explainer covers (basic → technical):**
- The four-part frame (Fabozzi Ch. 32): **industry** (cyclicality, competitive position — the sector layer, deferred per scope boundary 3 to the sector modules hanging off ER Z2.3), **financials** (coverage `★ G74`, leverage `★ G29`/debt-to-EBITDA — back-links: the ratios are homed with PC), **indenture** (covenants `★ G34`, structural subordination, guarantees — where the bonds sit in the org chart), **management/event risk** (LBO risk *to* bondholders — the IB/PE event that transfers value from creditors to sponsors).
- The credit-vs-equity lens inversion: the equity analyst (`★ G182`'s world) asks "how good can it get?"; the credit analyst asks "how bad can it get and am I paid for it?" — same company, asymmetric payoff, different work. ER's models feed both; the outputs diverge.
- Quantitative credit, named: structural models (equity as a call on the firm — Merton) and reduced-form models (Fabozzi Ch. 33) as the machinery behind model-implied spreads and default probabilities — placed here, depth deferred (`GAP:` the modeling layer is an authoring-depth item, with the Derivatives module's math as a prerequisite).
- The output: an *opinion versus the market* — is the Z-spread (`★ G277`) paying for the risk? — which is where the craft hands off to Z4.9's relative value and the portfolio's decision (Z5.6).

**Connects to.** `★ G74`/`★ G29`/`★ G34` (back-links — the ratio kit), ER module (the sibling craft), PC underwriting zone (the private version of the same work), `★ G276` (the agencies doing this work publicly), Z4.9 (the RV output), sector modules (the industry layer — flagged forward seam). *Real-world layer: Fabozzi Chs. 32–33.*

---

### Z4.9 · Credit Relative Value `[branch]`

**Quick definition.** Trading credits against each other rather than owning credit outright: curves (one issuer's 5s vs. 10s), capital structure (bonds vs. loans vs. CDS), compression pairs (IG vs. HY, cash vs. index), and the basis — the credit wing of the RV discipline Z5.9 generalizes.

**Explainer covers (basic → technical):**
- The trade taxonomy: **credit curves** (steep issuer curves flatten as credits improve or invert into distress — the front-end-survives logic Willer documents for EM); **capital structure** (the same issuer's TLB `★ G70`, bond `★ G277`, and CDS `★ G278` should cohere; dislocations are the trade — Z1.8's seam monetized); **decompression/compression** (HY vs. IG spread ratios across the cycle `★ G255`); **the basis** (bond vs. CDS — Huggins Ch. 16's arbitrage equalities and their financing/regulatory frictions).
- Why credit RV is harder than rates RV: idiosyncratic risk doesn't diversify in pairs (one default swamps the spread convergence), liquidity is tiered (Z1.7 — exiting the illiquid leg costs the theoretical edge), and shorting cash credit is expensive (why the CDS exists, Z4.7).
- The Malvey frame (Fabozzi Ch. 46): global credit portfolio management as continuous relative value — primary vs. secondary, sector rotation, structure selection (callables vs. bullets), and the swap decision — the institutional discipline AM Z2.8's "sector and credit selection" line compresses.
- The EM wing (Willer Ch. 9): external-vs-local as the master EM credit RV axis, ratings-lag trades, and the IMF-package and default event playbooks — previewing Z5.10.

**Connects to.** Z5.9 (the general RV machinery — fitted curves, ASW), `★ G277`/`★ G278`/`★ G70` (the three quotes traded against each other), HF Z2.3/Z2.8 (the practitioners), `★ G255` (the cycle timing), AM Z2.8 (the long-only version). *Real-world layer: Huggins Chs. 13, 16; Fabozzi Ch. 46; Willer Ch. 9.*

---

# ZONE 5 · Trading, Financing & the Portfolio

**What this zone is:** the market in operation. The dealer desk and the price of liquidity, the reference-rate plumbing (SOFR's manufacture — `★ G69` finally gets its market-side story), repo as the financing layer (`★ G282`), rates derivatives *at usage level* (the flagged seam to the future Derivatives module), the benchmark indices (`★ G283`), active management (back-linking AM Z2.8 rather than duplicating it), the fund wrapper and the individual investor, immunization/LDI as the institutional endgame (`★ G284`), the relative-value discipline, and the global/EM arena. *(Sources: Tuckman Chs. 3, 10–13; Huggins throughout; Fabozzi Part 6; Thau Parts 3–4; Willer Chs. 2, 4–10.)*

`The desk & liquidity → Reference rates & SOFR → Repo → Rates derivatives (usage) → The index → Active management → Funds & the individual → Immunization & LDI → Relative value → Global & EM.`

---

### Z5.1 · The Dealer Desk, Liquidity & the Bid–Ask `[core]`

**Quick definition.** How bonds actually change hands: dealers quote two-way prices, warehouse inventory financed in repo, and charge the bid–ask spread as the price of immediacy — making liquidity a *balance-sheet product* whose supply varies with regulation and stress.

**Explainer covers (basic → technical):**
- The desk's economics: buy at the bid, sell at the ask, finance the warehouse overnight (`★ G282`), hedge the rate risk (Z5.4), and hope the spread beats the inventory risk. Market-making is a *short-volatility* business — profitable daily, ruinous in gaps — which is why liquidity evaporates precisely when it's most wanted.
- The liquidity hierarchy priced: on-the-run Treasuries at fractions of a basis point; IG corporates in basis points; HY, munis, and EM in fractions of a point — the tiering from Z1.7, now as a cost schedule that RV strategies (Z5.9) must clear before their edge is real (Huggins's "demand for immediacy" as an RV *source*).
- The structural shift the older sources predate: post-Basel III balance-sheet costs shrank dealer inventories relative to market size (Huggins Ch. 18's shadow-cost frame); electronification and portfolio trading partially replaced principal liquidity with matching. `GAP:` current market-structure data (ETF-driven liquidity, all-to-all share) post-dates the source base — flagged for depth authoring.
- Stress anatomy: March 2020's Treasury-market seizure — the world's deepest market gapping — as the canonical modern case that liquidity is a *state*, not a property (`★ G263`'s plumbing chapter; `GAP:` episode post-dates sources, framework doesn't).

**Connects to.** Z1.7 (the structure this operationalizes), `★ G282` (the financing), Z5.4 (the hedge), Huggins Ch. 18 (regulatory constraints), `★ G258` (liquidity as a financial-conditions component), HF (the liquidity takers and providers). *Real-world layer: Tuckman Ch. 0; Huggins Chs. 1, 18.*

---

### Z5.2 · Reference Rates: SOFR & the Post-LIBOR World `[core]`

**Quick definition.** Where the floating world's anchor rate actually comes from: SOFR (`★ G69` — back-link, the home) is computed from the *observed volume of overnight Treasury repo* (`★ G282`), replacing LIBOR's surveyed, unsecured, manipulable quote — a plumbing change that re-based every floating contract and swap spread in the system.

**Explainer covers (basic → technical):**
- The manufacture (Huggins Ch. 11 — the definitive treatment in the source base): SOFR = a volume-weighted median of actual overnight repo transactions against Treasury collateral. Transaction-based (unmanipulable in principle), *secured* (collateralized), and overnight (no term credit component) — each property the exact negation of a LIBOR flaw.
- Why the transition happened (the story `★ G69` names and this node tells): the interbank market LIBOR surveyed had hollowed out post-crisis, and the rigging scandal ended its credibility; regulators engineered the migration. The rate *family* now: SOFR (secured overnight), term SOFR (derived), EFFR/fed funds (`★ G247`'s market), and the international siblings (SONIA, ESTR).
- What changed analytically (Huggins's preface, operationalized): LIBOR embedded bank credit risk; SOFR doesn't — so swap spreads versus SOFR became cleanly linkable to sovereign/funding factors (the Z5.9 yardstick), while the *secured–unsecured basis* became its own traded object. Legacy time series broke; the analyst's data problem is real and flagged.
- The stress wrinkle: SOFR is repo, so repo stress *is* reference-rate stress — September 2019's spike printed directly into the benchmark (Z5.3's episode, seen from the rate's side).

**Connects to.** `★ G69` (the home — back-link; this is its market-side story), `★ G282` (the raw material), `★ G247` (the policy anchor it tracks), Z3.8 (the instruments that float on it), Huggins Ch. 11, future Derivatives module (SOFR futures/swaps — flagged seam). *Real-world layer: Huggins Ch. 11; Tuckman Ch. 12.*

---

### Z5.3 · Repo & Secured Financing `★ GLOBAL (G282)` `[core]`

**Quick definition.** Selling a security with a commitment to repurchase it — economically a collateralized loan — the financing layer under every bond desk, the mechanism that turns bond portfolios into levered portfolios, the raw material of SOFR, and the pipe through which funding stress transmits system-wide.

**Explainer covers (basic → technical):**
- The mechanics (Tuckman Ch. 10 — the modern chapter-length treatment): cash lender takes the bond as collateral with a **haircut**; the borrower pays the **repo rate**; reverse repo is the same trade from the other side. Overnight vs. term; general collateral (any Treasury) vs. **specials** (a specific issue in demand repos *below* GC — scarcity priced as a financing subsidy, the mechanism behind on-the-run richness, Z3.1).
- Leverage manufactured: buy a bond, repo it, use the cash to buy another — the loop that turns 2% yields into levered carry (Z2.6's financing leg) and the reason haircut changes *are* margin calls system-wide. Hedge-fund basis trades (cash vs. futures, Z5.4) run entirely on this pipe.
- The Fed inside the market: the standing repo and reverse-repo facilities as the policy rate's enforcement mechanism at the secured short end (`★ G247`/`★ G244` — back-links), and QE/QT (`★ G251`) as the slow-motion version of the same balance-sheet plumbing.
- The stress file: **September 2019** — quarter-end collateral supply met constrained dealer balance sheets and overnight repo printed ~10% intraday, forcing the Fed's return to open-market operations (Huggins Ch. 18's canonical case for shadow balance-sheet costs); March 2020's dash-for-cash as the sequel. Repo is where `★ G263`-grade stress announces itself first.

**Connects to.** `★ G69`/Z5.2 (SOFR made from this), `★ G247`/`★ G251` (the Fed's plumbing — back-links), Z2.6 (carry's financing leg), Z3.1 (specials & the on-the-run), Z5.1 (dealer inventory finance), HF (leverage), Macro Z4 (transmission). *Real-world layer: Tuckman Ch. 10; Huggins Chs. 11, 18; Fabozzi Ch. 45.*

---

### Z5.4 · Rates Derivatives at the Desk: Futures & Swaps (Usage Level) `[branch]`

**Quick definition.** The tools a bond desk reaches for — Treasury futures to move duration instantly, interest-rate swaps to convert fixed↔floating or express curve views — treated here strictly at *usage* level: what they do for a portfolio, with mechanics and pricing deferred to the future Derivatives module.

**Explainer covers (basic → technical):**
- The usage inventory: **futures** — add or shed DV01 (`★ G267`) without touching cash bonds (cheaper, instant, off-balance-sheet); the deliverable basket and CTD named as the reason futures ≠ bonds exactly (Tuckman Ch. 11 flagged as the depth source). **Swaps** — pay-fixed as a duration short, receive-fixed as synthetic bonds; the fixed-vs-floating conversion every corporate treasurer runs (Z3.8's other half). **Swap spreads** — the gap between swap and Treasury curves as a traded object (Huggins Ch. 12's territory, touched at Z5.9).
- Who uses what for what: AM Z2.8's duration bets (futures overlay on a cash portfolio), LDI's hedging (`★ G284` — swaps to extend duration without cash), the mortgage market's convexity hedging (`★ G280`'s holders chasing their moving duration — a rates-volatility amplifier worth naming), and HF macro expression (Willer's EM receivers/payers vocabulary — Z5.10).
- The explicit boundary (scope boundary 1, restated where it bites): contract mechanics, margining, the CTD option, swap valuation, swaptions, caps/floors — **all deferred** to the Derivatives module, which will back-link this node and `★ G278` as its FI attachment points. This node exists so Zone 5's portfolio stories can be told without a forward reference into a module that doesn't exist yet.
- `GAP:` (structural, deliberate): the entire mechanics layer is a designed gap with a named future home — the map's cleanest example of the seam-flagging-over-retrofitting principle.

**Connects to.** `★ G267` (what these tools move), `★ G284` (LDI's usage), `★ G280` (convexity hedging), Z5.9 (swap spreads in RV), future Derivatives module (the mechanics home — the module's largest flagged seam), HF Z2.4. *Real-world layer: Tuckman Chs. 11–13 (named as the depth source for the future module).*

---

### Z5.5 · The Bond Index & the Benchmark `★ GLOBAL (G283)` `[core]`

**Quick definition.** The rules-based baskets that define "the bond market" for portfolios — the Bloomberg US Aggregate above all, plus the HY, muni, and EM families (EMBI/GBI-EM) — with the structural quirk that market-value weighting hands the biggest weights to whoever has borrowed the most.

**Explainer covers (basic → technical):**
- What the Agg is (Fabozzi Ch. 4; AM Z2.8's assumed backdrop, now taught): IG-only (`★ G275`'s gate), USD, size- and maturity-filtered — Treasuries + agencies + IG corporates + agency MBS (`★ G280`'s giant weight). What it *excludes* matters as much: HY, munis, TIPS (own index), non-USD — "the benchmark" is a choice, not the market.
- The debtor's-weight quirk and its consequences (AM Z2.8 flags it; this node owns it): more issuance → bigger index weight → passive flows fund the biggest borrowers; index duration *extends* when issuers term out debt (the 2010s duration creep — benchmark risk rose while yields fell, no one voted on it).
- Index events as market events: rating changes crossing the IG line (`★ G275`'s fallen-angel flows), EM index inclusions (Willer Ch. 8: "buy the news, sell the fact" — a backtested playbook), and rebalancing-day technicals (Z4.5's technicals wing).
- The benchmark's gravitational role: mandates are written against it, tracking error is measured off it, and "active" (Z5.6) is *defined* as deviation from it — the same logic AM built for equities, with the bond-specific twist that replicating an index of tens of thousands of illiquid bonds forces sampling, not full replication.

**Connects to.** AM Z2.8 (back-link — the manager's benchmark), `★ G275`/`★ G276` (the gates), `★ G280` (the MBS weight), `★ G281` (the EM indices), Willer Ch. 8 (inclusion trades), Z5.6 (active defined against this). *Real-world layer: Fabozzi Chs. 4, 43–44.*

---

### Z5.6 · Active Bond Management `[core]`

**Quick definition.** Beating the benchmark with the levers this module has built — duration positioning, curve shape, sector allocation, credit selection, and structure selection — the practice AM Z2.8 homes as a strategy category and this node grounds in its FI machinery (back-link, not duplication).

**Explainer covers (basic → technical):**
- The division of labor with AM stated first: AM Z2.8 owns *the strategy category* (what a bond manager decides, the mandate, the business); this node supplies *the machinery those decisions run on* — each lever now pointing at its Zone 2–4 home rather than at an assumption.
- The lever inventory, wired: **duration** (± vs. benchmark — `★ G267`, expressed via Z5.4's tools), **curve** (bullets vs. barbells, steepener/flattener — Z2.7/Z2.8), **sector** (Treasuries vs. corporates vs. MBS — the Zone 3 map as a menu), **credit** (Z4.8's work, `★ G275`'s divide), **structure** (callables vs. bullets — `★ G285`'s OAS judgment), **security selection** (Z5.9's RV at the margin).
- The scoreboard: excess return vs. benchmark decomposed by lever (Tuckman Ch. 3's P&L attribution scaled to portfolios — Fabozzi Ch. 44's quantitative benchmarked management), tracking error as the risk budget, and information ratio as the grade (`★ G143`'s framework — back-link — applied to bonds).
- The honest base rate: core bond active management is a *low-dispersion* game (the index is efficient at the rates level; edge concentrates in credit and structure) — which is why AM's core/satellite logic (Fabozzi Ch. 43) puts indexed rates at the core and active credit/EM/HY in satellites, and why the fee question (`★ G143`'s adjacent debates) bites hard in FI.

**Connects to.** AM Z2.8 (back-link — the home of the category; the app should render this pair like the Z1.8/PC Z1.7 seam), `★ G283` (the opponent), `★ G267`/Z2.7/Z4.8/`★ G285` (the levers' homes), `★ G284` (the *other* institutional mode — matching, not beating), Z5.9. *Real-world layer: Fabozzi Chs. 43–44, 46.*

---

### Z5.7 · Bond Funds, ETFs & the Individual Investor `[branch]`

**Quick definition.** How households actually own this market: mutual funds and ETFs that hold the bonds (a NAV that moves — no maturity date, no pull-to-par), versus owning individual bonds (a par payoff at maturity, but retail-hostile OTC pricing) — Thau's core dilemma, mapped onto the fund machinery WM/AM home.

**Explainer covers (basic → technical):**
- Thau's fork, stated fairly: an *individual bond* held to maturity returns par regardless of rate moves (`★ G266`'s price risk expires — you bear it only if you sell); a *bond fund* never matures — its NAV is a perpetual mark on a rolling portfolio (2022 made this concrete for a generation of savers). The fund buys diversification, liquidity, and institutional pricing; it sells the certainty of par.
- The vehicle mechanics, back-linked not re-taught: open-end funds, ETFs, closed-end funds, and money-market funds are homed with WM/AM's vehicle nodes (`★ G224`'s open/closed distinction is the RE sibling); this node adds the *bond-specific* wrinkles — fund NAVs marked off matrix prices (Z1.7), the ETF create/redeem arbitrage as a *liquidity translation layer* (bond ETFs traded through March 2020 while underlying bonds froze — price discovery, not failure), and duration disclosure as the retail risk label (`★ G267` on the fact sheet).
- The ladder as the retail middle path (Thau Part 4): staggered individual maturities — each rung pulls to par, reinvestment rolls up the curve — self-immunizing without the fund wrapper (Z2.11's logic in a brokerage account; TreasuryDirect and Z3.1/`★ G273` as the natural habitats).
- `GAP:` (recency): the bond-ETF ecosystem's scale and the 2020/2022 episodes post-date Thau (2011) and Fabozzi's edition — the frameworks hold; the market-structure facts need current-data authoring.

**Connects to.** WM (the client seat — back-link to its vehicle and planning nodes), `★ G170` (the withdrawal math bond income feeds), Thau Parts 3–4 (the source spine), Z1.7 (why retail pricing is hostile), `★ G267` (the risk label), Z2.11 (the ladder's logic).

---

### Z5.8 · Immunization & LDI `★ GLOBAL (G284)` `[core]`

**Quick definition.** The institutional endgame of Zone 2's math: structuring bond assets so they move *with* liabilities — duration-matched (immunized) or fully cash-flow-matched (dedicated) — so a pension or insurer is hedged against rates rather than betting on them; the strategy known institutionally as liability-driven investing.

**Explainer covers (basic → technical):**
- The problem it solves: a pension's liabilities are a stream of promised payments — economically a *short bond position* (`★ G248` discounting — liabilities balloon when rates fall). Holding equities against bond-like liabilities is a levered rates bet; LDI closes it by matching asset duration (`★ G267`) to liability duration (Fabozzi Ch. 47's single- and multi-period immunization; Ch. 48's dedicated portfolios).
- The implementation ladder: duration matching (rebalance as Z2.11's conditions drift), cash-flow matching/dedication (zeros — Z3.2 — and bullets laddered to the payment schedule; certain but expensive), and *derivative overlay* (swaps to extend duration without cash — Z5.4's usage case) — the modern institutional default.
- The stress case that made LDI famous: the 2022 UK gilt/LDI spiral — levered duration overlays met a gilt crash, collateral calls forced gilt sales, prices fell further (`★ G263`'s doom-loop anatomy in a pension wrapper; Z2.8's habitat-demand point inverted). `GAP:` post-dates all sources; framework fully covered by this zone's machinery, episode needs current authoring.
- The seam with the wealth modules: WM's household version (matching a retiree's spending with ladders and TIPS — Z5.7, `★ G271`, `★ G170`) is the same logic at retail scale; AM runs the institutional mandates (`★ G153`'s SMA world).

**Connects to.** `★ G267`/Z2.11 (the math), Z3.2/`★ G271` (the matching instruments), Z5.4 (the overlay tools), `★ G153`/AM (the mandate wrapper), WM (the household version), `★ G248` (the liability discount rate). *Real-world layer: Fabozzi Chs. 47–48; Parameswaran Ch. 5 (the immunization proof).*

---

### Z5.9 · Relative Value & the Fitted Curve `[branch]`

**Quick definition.** The professional discipline of trading bonds against each other: fit a smooth curve through a government market, measure each bond's richness/cheapness against it, hedge the factor risk (duration, curve), and harvest the convergence — Huggins & Schaller's craft, the quant wing of everything this module prices.

**Explainer covers (basic → technical):**
- The analytic process (Huggins Ch. 9's three-step, the map's chosen frame): (1) **fitted curves** (Ch. 8 — a smooth discount function through all of a sovereign's bonds; each bond's residual = its richness/cheapness, adjusted for benchmark status and repo specialness `★ G282`); (2) **factor structure** (PCA — level/slope/curvature as the curve's real degrees of freedom; hedge those, trade the residual); (3) **mean reversion** (Ch. 2 — the statistical engine: half-lives, conditional Sharpe ratios, first-passage times — *when* the convergence pays, not just whether).
- The trade zoo, named: on/off-the-run (Z3.1's liquidity premium harvested), butterflies (Z2.10's convexity in pair form), swap spreads and asset swaps (Huggins Ch. 12 — the bond-vs-swap axis, post-SOFR cleanly linkable to credit/funding factors — Z5.2's payoff), the bond–CDS basis (Z4.9's arbitrage), and cross-currency RV (Chs. 15–17's global yardstick: everything as a spread to USD SOFR).
- Why the free lunch isn't (Huggins Ch. 1's honest frame): RV premia are payment for *immediacy provision*, model risk, and balance-sheet rent (Ch. 18) — LTCM as the permanent cautionary tale that convergence trades embed liquidity and leverage risk (`★ G282`'s haircut spiral; `★ G263`'s 1998 file).
- The map placement: this node *names and organizes* the discipline; the statistical machinery (OU processes, PCA mathematics) is depth-layer material against Huggins Chs. 2–4, and the swap-spread mechanics await the Derivatives module's swap home (`GAP:` both flagged, both deliberate).

**Connects to.** Z2.7/`★ G269` (the curve being fitted), `★ G282` (specials & financing), Z4.9 (the credit wing), Z5.4 (the hedge tools & swap-spread seam), HF Z2.3 (the strategy category — back-link), Huggins end-to-end. *Real-world layer: Huggins Chs. 1–9, 12, 15–18.*

---

### Z5.10 · Global & EM Bond Investing `[core]`

**Quick definition.** The bond market beyond the dollar curve: currency-hedged vs. unhedged foreign bonds, the EM asset class in practice (Willer's backtested playbook — the cycle rules, the event guide), and the portfolio question of what global bonds add — the module's closing bridge back to Macro's Zone 5.

**Explainer covers (basic → technical):**
- The hedging fork that defines global FI: an unhedged foreign bond is mostly an *FX position* (`★ G260` — Willer Fig 1.6: most local-debt volatility is currency); hedged, it's a rates position at the hedge-adjusted yield (covered parity's arithmetic — `★ G261`'s toolkit, named at Macro Z5.2). The hedge decision *is* the asset-allocation decision.
- The EM playbook, compressed from Willer (Z3.12's instrument split, now traded): the 65/35 global-local rule (Ch. 2 — the Fed, DXY, and US HY as the masters); the rates-cycle rules (Ch. 6 — receive after the last hike, pay into the first, steepeners after the first cut); the event guide (Chs. 5, 8 — interventions, emergency hikes, IMF packages, index inclusions, elections — each backtested); credit selection (Ch. 9 — the 3–5yr BB sweet spot, embracing defaults, ratings lag); linkers as the superior habitat (Ch. 7, `★ G271`).
- The portfolio construction wing (Willer Ch. 10): benchmark-aware but not benchmark-slaved (GDP-weighting's failure), frontier markets as the liquidity frontier, derivatives as "weapons of mass alpha" (ND-IRS and NDFs named — usage level, per the standing boundary), and the honest ESG-in-EM tension (poverty-adjusted scoring).
- The closing bridge: this node hands back to Macro Z5 — currencies (`★ G260`), the balance of payments (`★ G261`), sovereign risk (`★ G262`), and crises (`★ G263`) are the *why* under every EM bond price; HF Z2.4's global macro strategy is the *who*. The FI module ends where the app's macro layer begins — by design.

**Connects to.** Z3.12/`★ G281` (the instruments), `★ G260`–`★ G263` (back-links — the macro machinery), HF Z2.4 (the strategy seat), `★ G271` (linkers), `★ G283` (the EM indices), Willer end-to-end. `GAP:` Willer's data runs to ~2019 — the 2020 EM crisis, the 2021–23 EM hiking cycle (EM hiked *before* the Fed — a first), and current index compositions are recency-flagged for depth authoring.

---

# PART 3 · The new globals in dependency order

*The order in which the 22 new globals should be learned/authored — each tier requires only what precedes it (plus the inherited macro chain, which sits under the whole module).*

**Tier 0 — inherited, not minted (the module's foundation).**
`G90` DCF, `G1` IRR (IB/PE) → `G247` the policy rate → `G248` the risk-free rate & term structure → `G249` Fisher → `G257` the yield curve signal (Macro). The module assumes this chain end-to-end; nothing in it is re-taught.

**Tier 1 — the object and its market.**
`G264` the bond → `G270` the U.S. Treasury market (the benchmark issuer the rest is priced against).

**Tier 2 — the arithmetic.**
`G266` pricing & the price–yield inversion → `G265` YTM & the meanings of yield → `G269` spot/forward/par (the curve toolkit) → `G267` duration & DV01 → `G268` convexity.

**Tier 3 — the universe (requires the arithmetic).**
`G271` TIPS (needs `G249` + `G265`) · `G272` the money market (needs `G247`) · `G273` munis (needs `G265`) · `G274` corporates (needs `G264` + Tier 2) · `G285` callables & embedded options (needs `G265` + `G268`) · `G279` securitization (needs `G264`) → `G280` agency MBS & prepayment (needs `G279` + `G268`) · `G281` EM debt (needs `G274` + `G260`–`G263`).

**Tier 4 — credit priced (requires the universe).**
`G276` ratings & the agencies → `G275` IG vs. HY → `G277` bond spreads (G/Z/OAS — needs `G269` + `G285`) → `G278` the CDS (needs `G277` + `G61`/`G62`).

**Tier 5 — the market in operation (requires everything prior).**
`G282` repo & secured financing (needs `G270`; feeds back into `G69`'s SOFR story) → `G283` the bond index & the Agg (needs `G275` + `G280`) → `G284` immunization & LDI (needs `G267` + `G248`).

**The single most important dependency edge:** `G248` (Macro's risk-free term structure) → `G269`/`G266` (the curve as pricing machine, the inversion) → `G277` (spreads over that curve) → `G275`/`G278` (the credit market's regimes and derivatives). This is the chain that turns Macro's *variables* into a tradable *market* — the market-side completion of the `G247→G248→G259→G91/G27/G219` valuation spine the Macro map built.

**Global count check:** 22 net-new globals, G264–G285 contiguous. Running shared-glossary total after this module: **G1–G285** across eleven modules.

---

# PART 4 · Source gaps & attachment points

*Where the sources are thin, dated, silent, or deliberately deferred — flagged as future authoring/attachment points rather than papered over. Consistent with the seam-flagging-over-retrofitting principle: honest seams, not defects.*

**1. The rates-derivatives mechanics layer is a designed gap (the module's largest seam).** Treasury futures, interest-rate swaps, swaptions, caps/floors, and lattice/OAS *machinery* are referenced at usage level only (Z5.4, Z3.9, Z5.9) with mechanics explicitly deferred to the planned **Derivatives** module — consistent with the standing build sequence (FI → Sectors → Derivatives) and with the identical seam the Macro map flagged (its Source Gap #5). The one deliberate exception is the **CDS (`★ G278`)**, homed here because Tuckman (Ch. 14), Fabozzi (Part 7), and Huggins (Ch. 13) treat it as constitutive of the traded-credit market; the Derivatives module should back-link G278 (and Z5.4) rather than re-home them, and Tuckman Chs. 11–13 are pre-identified as its depth sources. **The Derivatives module's FI attachment points, enumerated:** Z5.4 (futures/swaps usage), Z3.9 (option valuation & converts), `★ G277` (OAS machinery), `★ G278` (CDS mechanics/clearing), Z5.9 (swap spreads & ASW), `★ G269` (forwards as its native language).

**2. Two of six sources predate the SOFR transition and modern market structure.** Thau (2011) and Fabozzi 7e were written in the LIBOR era, before post-Basel III dealer balance-sheet constraints, before bond-ETF scale, and before electronification/portfolio trading reshaped corporate-bond liquidity. The map compensates by leaning on Tuckman 4e (2022, deliberately post-LIBOR) and Huggins 2e (2024) for everything rates-plumbing (Z5.1–Z5.3) — but retail-facing nodes grounded in Thau (Z5.7) and market-structure passages grounded in Fabozzi (Z1.7) carry explicit recency flags. When authored to depth, refresh against current market-structure data (all-to-all share, ETF create/redeem scale, TRACE evolution).

**3. The post-2019 episode file post-dates the source base almost entirely.** The map's framework nodes fully *explain* these episodes, but the episodes themselves need current-data authoring: the **September 2019 repo spike** (Huggins covers it — the one exception), **March 2020** (the Treasury seizure, the dash-for-cash, the Fed's corporate-credit facilities — Z5.1, Z4.5), the **2022 rate shock** (the worst bond-market year in modern history; the price–yield inversion made visceral — Z2.2, Z5.7; TIPS falling amid inflation — Z3.3), the **2022 UK gilt/LDI spiral** (Z5.8), and the **2023 regional-bank duration losses** (Z3.4's FHLB backstop; duration risk held-to-maturity — a `★ G267` case study). Each is pre-wired to its framework node; none requires structural change.

**4. Sector-level credit analysis is deferred by design.** Z4.8 names the industry leg of credit work and points at the planned **sector modules** (compact depth-layer clusters off ER Z2.3, per the ratified sequencing). Bank capital securities, utility regulation, energy credit — Fabozzi Part 4's specialized chapters — are that build's raw material, not this one's.

**5. Quantitative credit and RV statistics are placed, not unpacked.** Structural/reduced-form default models (Z4.8; Fabozzi Ch. 33), and Huggins's statistical engine (OU mean reversion, PCA factor mathematics — Z5.9) are named with their homes identified but deferred to depth authoring; the PCA material additionally serves the future Derivatives module's curve machinery. Willer's backtest tables (Z5.10's playbook) similarly compress to rules at map level with the full evidence layer deferred.

**6. Willer's EM data horizon (~2019) and index drift.** The EM playbook's *rules* are stable, but the 2020 EM crisis, the 2021–23 EM-hiked-first cycle, China's index weight evolution, and Russia's 2022 index ejection post-date the source — Z3.12/Z5.10 carry the recency flag.

---

# PART 5 · Connections — which existing nodes now get their market

*The payoff ledger: concepts the ten existing modules reference but never teach now have a home. Left column: the existing node (module). Middle: what was assumed but untaught. Right: the FI node(s) that now supply it. Nothing here is re-homed; every row is a back-link.*

| Existing node (module) | What was assumed but untaught | Now supplied by (this module) |
|---|---|---|
| **`G248` risk-free rate & term structure** (Macro) | The *market* where the risk-free rate lives — who issues, who trades, how the curve is extracted | **`G270`** (the Treasury market) **+ `G269`** (the curve toolkit) — Macro's "price of time" gets its marketplace |
| **`G257` the yield curve signal** (Macro) | The mechanics under the shape — why long ≠ short, term premium, the arithmetic | **Z2.8** (term-structure theories) **+ `G269`** (spot/forward/par) |
| **`G247` the policy rate** (Macro) | How the policy rate becomes actual funding and market yields | **`G272`** (the money market) **+ Z5.2** (SOFR's manufacture) **+ `G282`** (repo — the Fed's enforcement plumbing) |
| **`G251` QE/QT** (Macro) | *What* the Fed buys and the market it moves | **`G270`** (Treasuries) **+ `G280`** (agency MBS — the second portfolio) |
| **`G69` SOFR** (Private Credit) | Where SOFR *comes from* — flagged in Macro's ledger as "what SOFR tracks"; now the full manufacture | **Z5.2** (reference rates) **+ `G282`** (the repo transactions it's computed from) |
| **`G70` credit spread** (Private Credit) | The *traded* spread family the loan spread rhymes with | **`G277`** (G/Z/OAS — disambiguated in Part 1) **+ Z4.5** (what moves spreads) |
| **`G58` yield (all-in)** (Private Credit) | The market yield concept the loan yield must never be conflated with | **`G265`** (YTM & the meanings of yield — the paired disambiguation) |
| **`G72` call protection** (Private Credit) | The securitized version of prepayment economics — the option the *market prices* | **`G285`** (callables & embedded options) **+ `G280`** (prepayment at population scale) |
| **`G77` internal ratings** (Private Credit) | The *public* rating infrastructure with market consequences | **`G276`** (the agencies) **+ `G275`** (the IG/HY line) |
| **`G61`/`G62` recovery & default** (Private Credit) | The public workout, the traded recovery, the default statistics markets price | **Z4.6** (default in public markets) **+ Z4.1** (credit risk with a ticker) |
| **PC Z1.7 the BSL market** (Private Credit) | The public side of the wall — the module's flagged seam, now built | **Z1.8** (the paired seam node) **+ `G274`** (corporates) **+ Z3.8** (the floating universe) |
| **AM Z2.8 Active Fixed Income** (Asset Mgmt) | "Runs on macro and credit taught elsewhere" — the machinery under every lever it names | **The whole module**, wired at **Z5.6**: duration `G267`, curve `G269`/Z2.8, sectors Zone 3, credit Zone 4, the benchmark `G283` |
| **`G143` asset allocation** (Asset Mgmt) | What "bonds" actually are in the 60/40 and why they diversify (and when they don't) | **Z1.3** (why investors lend) **+ `G266`** (the price risk) **+ `G271`** (the inflation caveat) |
| **`G153` SMAs / institutional mandates** (Asset Mgmt) | The liability-driven mandate class | **`G284`** (immunization & LDI) |
| **WM bond ladders, income & cash** (Wealth Mgmt) | The instruments and math under retirement income practice | **Z5.7** (funds vs. bonds, ladders) **+ `G273`** (munis & TEY) **+ `G272`** (cash) **+ `G271`** (TIPS) **+ `G170`** back-linked |
| **`G227` CMBS** (Real Estate) | The general securitization machine CMBS is one product of | **`G279`** (securitization — back-links G227, does not re-home) **+ `G280`** (the residential sibling) |
| **`G219` cap rate** (Real Estate) | The "spread over the 10-year" now has both legs taught | **`G270`** (the 10-year's market) **+ `G277`** (spread logic) — completing Macro's `G259` chain |
| **HF Z2.3 fixed-income RV / Z2.4 global macro / Z2.8 distressed** (Hedge Funds) | The instruments and analytics those strategies trade | **Z5.9** (RV & fitted curves) **+ Z5.3** (`G282` repo/leverage) **+ Z5.10/`G281`** (EM) **+ Z4.6/Z4.9** (distressed & credit RV) **+ `G278`** (CDS) |
| **IB DCM & `G103` underwriting spread** (Investment Banking) | The product and market DCM manufactures | **Z1.6** (the primary market) **+ `G274`** (corporates) **+ `G275`** (the leveraged-finance divide) |
| **ER credit-side & `G182`-adjacent analysis** (Equity Research) | The debt-side analyst craft and the sector seam | **Z4.8** (the credit work — and the forward seam to sector modules off ER Z2.3) |
| **`G252`/`G253` inflation & the indices** (Macro) | The instrument that trades inflation and the market's own forecast | **`G271`** (TIPS & the breakeven) |
| **`G260`–`G263` FX, BoP, sovereign risk, crises** (Macro) | The bond markets where those variables become P&L | **`G281`** (EM debt) **+ Z5.10** (global & EM investing) **+ Z4.6** (sovereign workouts) |

**The hub nodes for all of the above:** **Z1.8** (the public/private seam — the door from Private Credit), **Z5.6** (active management — the door from Asset Management), and **Z5.10** (global/EM — the door back to Macro Z5). Every row above is a traversal a learner can make from "the role-specific what" into "the market-side how" and back.

**Net effect on the graph:** this module converts the app's largest *referenced-but-untaught* surface — the bond market itself — into 51 homed, interconnected nodes, completes the Macro valuation spine on its market side (`G248→G269/G266→G277`), builds the public half of the credit world Private Credit built privately, and pre-wires the two next builds (sector modules at Z4.8; Derivatives at Z5.4/Z3.9/`G278`) with enumerated attachment points.

---

*End of the Fixed Income module node map. Eleven modules mapped; shared glossary G1–G285.*
