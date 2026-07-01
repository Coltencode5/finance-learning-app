# Finance Learning App — Content Architecture & Project Brief

## What We're Building

A financial and business literacy app for anyone — students, professionals, curious adults — who wants to understand how finance, business, and economics actually work in practice. Think Duolingo meets Bloomberg — deeply educational, visually explorable, and built around real content from authoritative books and sources.

The app is **not** a chatbot or search tool. It's a browsable, discoverable knowledge environment where users scroll and explore, stumble into topics, and go as deep as they want.

---

## Core Design Principles

- **Discovery-first, not search-first.** Like YouTube or Instagram — you browse and find things, not always search for them.
- **Freely explorable with a suggested sequence.** Content is organized in the logical order a professional would encounter it, but users can jump around freely.
- **Progressive depth.** Every topic has layers: quick definition → deeper explanation → technical mechanics → real-world application.
- **Knowledge graph, not silos.** Every term is a node that links to every other place it appears. IRR shows up in PE, real estate, VC — they all link to the same canonical explainer.
- **Multiple learning modes.** Definitions, worked examples, comparisons, visuals, quizzes — not just text.

---

## Home Page Structure

Four exploration categories, browsable not searchable:

1. **Sectors & Industries** — scroll through construction, industrials, tech, healthcare, energy, commodities, etc. Click one, get a full deep-dive on how that industry actually works end-to-end.
2. **Roles & Careers** — private equity, investment banking, equity research, hedge funds, private credit, asset management, wealth management, venture capital, etc. Click one, learn exactly what someone in that role does, what they know, what tools they use.
3. **Core Concepts** — the building blocks. Markets, debt, equity, interest rates, capital, leverage, how the Fed works, macroeconomics. Foundation for everything else.
4. **Trending Ideas** — curated discovery feed. New topics, notable concepts, things worth exploring. Surfaces content users didn't know they wanted.

---

## Onboarding Flow

First-time users see a lightweight prompt:

> "Do you know the basics of how economies and businesses work?"

- **No / Not sure** → short foundational primer covering: markets, debt vs equity, interest rates, how capital flows, what a business model is. Estimated 10-15 core concept explainers.
- **Yes / Skip** → straight into exploration.

The primer is always accessible later from Core Concepts. It's never forced on returning users.

---

## Knowledge Graph Architecture

Every term is a **node**. Nodes have:
- A canonical definition (quick, inline)
- A full explainer page (layered depth)
- Links to every context where the term appears

Example: IRR appears in private equity, real estate, venture capital, and infrastructure. Every instance links to the same IRR explainer. The IRR explainer itself has: what it is → how to calculate it → pitfalls and nuances → how it compares to MOIC and other return metrics.

When a user is reading about private equity deals and hits "IRR," they can click it and either get the quick definition inline or jump to the full explainer. They're never stuck.

**The shared glossary is the most important architectural decision in the app.** One canonical set of primitives reused across every module rather than rebuilt per module is what turns a set of courses into a single interconnected knowledge graph. Currently G1–G235 across nine completed modules.

---

## The Two-Layer Industry Structure

Industries and sectors work differently from finance roles. Each industry has **two distinct entry points** that serve different learners:

**Layer 1 — Industry Deep Dive** (accessible to anyone):
How does this industry actually work? Who are the players, how are products made and sold, what drives demand, what are the cost structures, what macro events have shaped it, how does the competitive landscape work. Completely self-contained — no finance background required.

**Layer 2 — Analyst Mode** (the professional lens on the same industry):
How would an equity research analyst or investor actually look at this industry? What are the KPIs, what do you model and forecast, what valuation approaches are specific to this sector, what metrics matter most? This layer assumes you already understand the industry basics from Layer 1.

A user can start in the industry module and click a button to enter analyst mode. Or they can be in the equity research module and click into an industry to get the full context. Both paths lead to the same content, accessed differently.

---

## The Macro & Economics Layer

Macroeconomics is a **standalone foundational module** that lives in Core Concepts. It covers:

- How the Federal Reserve works and what it actually does
- Monetary policy, interest rates, and how they're set
- Inflation — what causes it, how it's measured, how it's fought
- The yield curve and what its shape signals
- Credit cycles — boom, bust, and what drives each
- How macro conditions flow through to asset prices, deal activity, and returns
- GDP, employment, and the major economic indicators
- Global macro — currencies, trade, central bank coordination

This module is the connective tissue for everything else. It explains *why* rates affect LBO pricing, *why* credit cycles matter for private credit, *why* multiples compress in certain environments. Every finance role module references it; every industry module references it. It should be mapped before sector work begins so those connections are explicit from day one.

---

## Learning Module Structure

Each topic (sector, role, or concept) has a self-contained learning path. Structure within each module:

1. **What is this?** — high-level overview, who's involved, why it matters
2. **How does it work?** — the mechanics, the process, the flow
3. **Key players** — who does what
4. **Core concepts** — the terms and ideas you need (all linked to glossary nodes)
5. **Technical depth** — modeling, pricing, analysis tools (for finance/role modules)
6. **Real-world application** — case studies, examples, how this plays out in practice
7. **How this connects** — links to related modules, sectors, and roles

The sequence is logical but not mandatory — users can jump in anywhere.

---

## Progress & Memory

- App tracks what you've visited and learned
- Not a v1 priority but architecturally accounted for from the start
- Future: personalized recommendations based on what you've explored

---

## Current State — What's Been Built

**Phase 1 (content architecture) is well underway.**

### Completed Module Node Maps (9 modules):
All modules follow the canonical five-zone template: Ecosystem → Types → Process → Managing → Meta/Firm

1. **Private Equity** — G1–G57 (57 global nodes; the structural template for all subsequent modules)
2. **Private Credit** — G58–G82
3. **Investment Banking** — G83–G105 (LevFin bridges to Private Credit; IB valuation toolkit G87–G95 serves as inherited analytical spine)
4. **Hedge Funds** — G106–G136
5. **Asset Management** — G137–G158
6. **Wealth Management** — G159–G181
7. **Equity Research** — G182–G200 (19 new globals)
8. **Venture Capital** — G201–G216 (16 new globals — most inheritance-heavy module)
9. **Real Estate** — G217–G235 (19 new globals; spans all four quadrants of investable capital)

**Global glossary currently stands at G1–G235 across all nine modules.**

### Key Architectural Principles Validated:
- **Inheritance-first discipline**: New globals contributed only when genuinely net-new. VC's 16-global count vs. PE's 57 is the correct result of a growing shared base.
- **GAP-flagging over papering**: Source gaps and recency gaps flagged explicitly at the node level.
- **Five-zone template is fully portable**: Maps cleanly onto every finance discipline tested so far.
- **Cross-module connections are explicit and directional**: Which module owns a concept vs. which reuses it is always specified.

### Book Library (Google Drive — Books For App → Asset Class):
- **Private Equity**: Mastering Private Equity + Private Equity in Action (Zeisberger); Private Capital Investing (Ippolito)
- **Private Debt**: Private Debt (Nesbitt); Distressed Debt Analysis (Moyer); Private Capital Investing (Ippolito)
- **Venture Capital**: Venture Deals (Feld & Mendelson); Secrets of Sand Hill Road (Kupor); The Business of Venture Capital (Ramsinghani)
- **Hedge Funds**: More Money Than God (Mallaby); Hedge Fund Market Wizards (Schwager); Inside the House of Money (Drobny); Advances in Active Portfolio Management (Grinold & Kahn)
- **Investment Banking**: Investment Banking (Rosenbaum & Pearl — scanned, text not extractable; text-based copy still needed)

---

## What's Next — Phase 1 Continuation

### Immediate next steps in order:

**1. Macro & Economics Module** *(map this first)*
Standalone foundational module in Core Concepts. Covers Fed, monetary policy, rates, inflation, yield curve, credit cycles, macro indicators, global macro. Every sector module will reference it. New globals start at G236. Recommended source books: Dalio's *Principles for Navigating Big Debt Crises* (free PDF at economicprinciples.org), *The Alchemy of Finance* (Soros), or a clear macro textbook.

**2. Sector & Industry Modules** *(two layers per industry, starting at G236+ after macro)*
Each industry gets a Layer 1 (how it works) and a Layer 2 (analyst mode) node map. Build order recommendation:
- **Energy & Oil/Gas** — macro-sensitive, well-documented, widely relevant
- **Industrials** — broad, great for manufacturing and supply chains
- **Healthcare** — unique regulatory and financial mechanics
- **Technology** — high-growth, valuation-intensive

**3. Core Economics Primer** *(onboarding layer)*
10-15 foundational nodes for brand new users. What is a market, what is debt, what is equity, how do interest rates work, what is a business model.

### Still needed in book library:
- Macro/economics source book
- Industry-specific books per sector (1-2 per industry)
- Text-based version of Rosenbaum & Pearl

---

## What We're NOT Doing Yet

- No design or visual decisions
- No database or backend infrastructure
- No user accounts or progress tracking
- No code

---

## Node Map Template (reference for every new module build)

Every node carries:
- **Node ID**: Z{zone}.{n} for zone nodes; G{n} for global glossary nodes
- **Quick definition**: One sentence, inline-able
- **Explainer covers**: Bulleted scope ordered basic → technical
- **Connects to**: Every other node this links to, including G-numbers for shared globals
- **Tag**: [core], [process], [branch], or ★ GLOBAL

New globals contributed only when genuinely net-new to the system. Everything else references existing G-numbers.
