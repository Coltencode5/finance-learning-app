# Operating Roadmap

**Approved and committed 2026-07-11.**

---

# Unified Operating Plan — finance-learning-app

**Status:** Ratified operating roadmap (supersedes scattered per-conversation planning)
**Prepared:** 2026-07-10, immediately following Milestone 11 (sector-energy) close
**Corpus at time of writing:** 14 modules · G1–G313 contiguous · 615 zone nodes · 4,433 edges · strict validation 0/0
**Role of this document:** The single answer to "what is next, what is deferred, and who owns what." When this document and any prior conversation disagree, this document wins until it is formally amended.

---

## A. Current-state diagnosis

### What is working

The two-tier pipeline is the project's strongest asset and should not be touched. Eleven milestones of architecture-in-Claude, execution-in-Cursor, verification-against-the-live-tarball have produced a 313-global corpus with zero strict-validation debt. Inheritance-first discipline held through three sector modules — 7, 11, and 10 net-new globals respectively is exactly the compression the model predicted. The ADR discipline, the defect register, and the kickoff-prompt pattern all continue to earn their overhead. Nothing in this plan changes how content milestones are run.

### What is becoming inefficient

The inefficiency is not in either track — it is in the seam between them. Three symptoms:

1. **Strategy is fragmenting across three tools.** Architecture judgment lives in Claude project conversations, mechanical execution lives in Cursor, but *strategic* decisions have been accumulating in ChatGPT conversations with no canonical artifact. That is why the project "feels scattered": there is a `PROJECT_STATUS.md` for corpus state but no equivalent single source of truth for product direction. This document fixes that.
2. **Product ideas have no gate.** Content milestones have acceptance criteria and merge gates; product ideas (streaks, friends, AI tutor, Vercel) have been accumulating in an ungated backlog where each new conversation re-litigates them. The retention roadmap in Section F converts that backlog into a gated sequence so the ideas stop demanding attention.
3. **The next-milestone default is inertia.** "M12 Consumer Discretionary next" is documented because it was the next sector, not because anyone re-evaluated it against the product question. It survives this re-evaluation (Section C), but demoted from *next* to *concurrent*.

### Where the project is at risk of overbuilding

Not where it might seem. Consumer Discretionary is **not** overbuilding — it is one compact sector-layer1 module (~11–13 nodes, ~8–11 globals) that closes a declared wave with known cost and known process. The real overbuilding risk is **wave two**. If, after M12, the default action is "next sector batch" without a product gate having fired, that is inertia. This plan installs the gate: **no new content module is scoped after M12 until Learning Loop V1 has shipped and been tested with real users** (Section C, Gate G1).

A second, subtler overbuilding risk: designing the lesson layer to serve the *full future product* (mastery models, spaced repetition, AI tutoring) rather than the pilot. Section D deliberately specifies the minimum schema that survives those futures without implementing them.

### Where the project is at risk of moving too early

Three ideas discussed recently would be premature if built now, and this plan explicitly defers them:

- **Streaks and daily goals** require trusted server-side timestamps, which require accounts, which require a database. Building them on localStorage produces fake streaks and teaches nothing. Deferred to post-accounts (Section F).
- **Social mechanics** (friends, competitions, leaderboards) require identity, anti-abuse, and — most importantly — evidence that the solo loop retains anyone. Duolingo added social years after the core loop worked. Deferred to Gate G3.
- **AI tutor** requires a stable lesson layer to ground against. Grounding a tutor on a presentation schema that is still moving weekly guarantees rework. Deferred to Gate G3+.

The one thing the project is *not* too early for — and the central judgment of this plan — is the learning loop itself. Fixed Income alone contains a complete, prerequisite-ordered, formula-and-misconception-rich path. The content needed to test the product hypothesis has existed since Milestone 7. Every content milestone since then has widened the graph without reducing uncertainty about the only question that now matters: **can a canonical node become a lesson someone enjoys?** Content breadth stopped being the bottleneck for product validation roughly four milestones ago. It remains the bottleneck for the *eventual full product* — which is exactly why the architecture track continues rather than stops.

---

## B. Relationship between the two tracks

### The tracks run in parallel — across tools, not across your attention

The correct framing is not "65/35 attention split." You are one person; Claude design sessions are inherently serial. What *can* be parallelized is Cursor execution against Claude design output. The operating pattern:

```
Claude session N     →  produces design artifact A
Cursor               →  executes artifact A          (while)
Claude session N+1   →  produces design artifact B
```

Concretely for the next cycle: P0 (lesson-layer architecture + authored Fixed Income pilot + V-1…V-13 validators) is complete pending merge; after merge, Cursor implements the lesson player (P1) from that spec **while** Claude runs the Consumer Discretionary architecture session (M12). Your attention is serial; the project is parallel. The 65/35 number becomes an emergent property of milestone sequencing rather than a daily budgeting exercise.

### Track responsibilities

| | Architecture track | Product track |
|---|---|---|
| **Owns** | `content/glossary/`, `content/modules/`, graph edges, ADRs, validator checks | `content/lessons/`, `content/paths/`, `src/`, deployment, learner UX |
| **May read** | everything | everything |
| **May write** | canonical graph + its own docs | lesson/path/assessment JSON + app code; **never** `content/glossary/` or `content/modules/` |
| **Design owner** | Claude/Fable | Claude/Fable |
| **Execution owner** | Cursor | Cursor |

### The one-way dependency rule (canonical integrity)

The product track has a **read-only, reference-by-ID** relationship to the canonical graph:

1. Lesson and path files reference `G###` and `module.zN.m` IDs. They never copy definitions, never restate canonical prose as their own source of truth, never mint IDs.
2. If a lesson author discovers a canonical node is *wrong or missing something*, the fix is a **defect filed in `MIGRATION_DEFECTS.md`** and resolved through the architecture track — never an inline patch from the product side.
3. The validator gains a dangling-reference check: every ID cited in `content/lessons/` and `content/paths/` must exist in the graph. This makes the dependency machine-enforced, not honor-system.
4. Node IDs, global IDs, `home_of` assignments, zone spines, and edge semantics are **immutable from the product track's perspective.** Append-only evolution of the graph continues under existing rules.

This is the answer to "what product-layer decisions could corrupt the graph": the only corruption vectors are duplication (copying canonical text into lessons, creating drift) and back-pressure (changing nodes to suit UI). Rule 1 blocks the first; rule 2 blocks the second; rule 3 catches violations.

### Artifact exchange between tracks

- Architecture → Product: the graph itself, plus `PROJECT_STATUS.md`.
- Product → Architecture: defect filings, plus a new lightweight register — `docs/LESSON_FEEDBACK.md` — where pilot findings that have *architectural implications* (e.g., "nodes need a misconceptions field") are logged as proposals, each requiring an ADR before any canonical change lands.

---

## C. Recommended milestone sequence

Architecture work uses `M##`; product work uses `P#`. Consumer Discretionary remains architecture milestone M12. Product milestones are P0 (lesson-layer architecture), P1 (learning-loop implementation), and P2 (pilot test), with decision gate G1.

### P0 — Repo audit + Lesson & Path Architecture (design + authored pilot) ← **COMPLETE pending merge**

| | |
|---|---|
| **Objective** | Ratify how canonical nodes become lessons, before any player code is written |
| **Scope** | `LESSON_LAYER_DESIGN.md` (the standing reference, peer to `SECTOR_LAYER_DESIGN.md`); ADR-004 (presentation-layer separation); JSON schemas for lesson, path, and assessment-item files; the implemented V-1…V-13 lesson-layer validation suite; the authored Fixed Income pilot path file and its 10 lesson files |
| **Explicit exclusions** | No app code. No player UI design beyond block-type enumeration. No mastery model. No canonical-content changes of any kind. |
| **Owner** | Claude/Fable design session (new chat, kickoff prompt per your standard pattern) |
| **Inputs** | This document (Section D is the pre-brief); `Fixed_Income_Module_Node_Map.md`; `five_zone_template.md`; the live tarball |
| **Deliverables** | Markdown design doc + ADR + schemas + pilot lesson JSON (authored by Claude, mechanical assembly by Cursor if large) |
| **Acceptance** | Every lesson file validates against its schema; every referenced ID resolves against the live graph; a human read-through of two lessons confirms they read as lessons, not node dumps |
| **Gate** | ADR-004 ratified by you before Cursor receives any implementation prompt |

### M12 — sector-consumer-discretionary (content)

Runs exactly as M9–M11 did: kickoff prompt → Claude architecture session → Cursor extraction + migration → tarball verification. `kind: sector-layer1`, `build_order: 15`, globals from G314. **Closes wave one.** The only change from the documented plan is timing: the Claude session for M12 happens *after* the P0 design session, and its Cursor execution overlaps with P1's Cursor execution. Expected yield based on M9–M11: ~8–13 nodes, ~8–11 net-new globals, disambiguation retrofits per the codified N-way convention.

### P1 — Learning Loop V1 (product build)

| | |
|---|---|
| **Objective** | One complete, enjoyable learner journey through the Fixed Income pilot path, on a phone |
| **Scope** | Lesson player (one idea per screen, progress bar, immediate quiz feedback with explanations); path page (completed/current/next/locked); pilot landing page; completion screen with graph-connection payoff ("you connected Duration to…"); progress via localStorage; anonymous opt-out-respecting event beacon per D5; Vercel deployment of `main` + PR previews |
| **Explicit exclusions** | Accounts, database, streaks, daily goals, notifications, social anything, AI anything, payments, a self-owned analytics backend/database (the D5 anonymous event beacon is in scope; vendor chosen in P1), review queues, any second path |
| **Owner** | Cursor/Sonnet, from the P0 spec. Claude reviews the built experience against the design, not the code line-by-line |
| **Inputs** | ADR-004, schemas, pilot lesson JSON, existing `src/lib/graph/` layer |
| **Acceptance** | You complete the full path on your own phone via the Vercel URL and would honestly show it to a friend without apologizing for it. Type-check, build, and the V-1…V-13 lesson-layer validation suite pass. |
| **Gate** | Product branch merges only after preview deployment reviewed on mobile |

### P2 — Pilot test

Ship the Vercel link to 10–20 real people (classmates, finance-club members — people in the target segment, not just polite friends). Two-week window. Collect the behavioral data in Section E and run short exit conversations. Deliverable: a one-page findings memo. **No building during the test window** except crash fixes.

### Gate G1 — the decision point this plan exists to install

After P2, exactly one of three branches, chosen on evidence:

- **Loop works** (completion + qualitative bar met) → post-G1 product work = accounts + database + server-side progress, then daily goals/streaks (Section F). Content wave two gets scoped *behind* this.
- **Loop is close but format is wrong** (people start lessons but the screens don't land) → post-G1 product work = lesson-format redesign, second pilot path (IB recruiting), re-test. Cheap, because only presentation JSON and player code change — the graph is untouched.
- **Loop fails structurally** (target users don't want lesson-ified professional finance at all) → stop product spend, re-examine the wedge (e.g., reference/graph-browser product, B2B prep-course licensing) before further investment in either track.

No content module beyond M12 is scoped until G1 resolves. That sentence is the anti-inertia mechanism.

---

## D. Learning-content architecture

### The four layers, and where each lives

| Layer | Contents | Location | Mutability | Validated? |
|---|---|---|---|---|
| **1. Canonical graph** | globals, zone nodes, edges, disambiguations, gaps | `content/glossary/`, `content/modules/` | Append-only via architecture track + ADRs | Yes (existing strict) |
| **2. Presentation content** | lessons, paths, assessment items | `content/lessons/`, `content/paths/` | Authored/edited freely by product track | Yes (new checks) |
| **3. Product configuration** | routes, UI copy, feature flags, block renderers | `src/` | Ordinary code review | Type-check + build |
| **4. Learner state** | progress, answers; anonymous product events | localStorage progress (V1) + D5 event beacon (V1) → database (post-G1) | Runtime | n/a |

The critical property: layers 2–4 can be deleted wholesale and layer 1 loses nothing. That is the formal definition of "no second source of truth."

### Why presentation content is a separate schema (ADR-004's core ruling)

- **Not canonical blocks-in-nodes:** embedding lesson blocks in node JSON couples pedagogy to the graph, forces every future presentation experiment through the migration pipeline, and bloats nodes that nine other consumers (search, disambiguation UI, future tutor) don't want.
- **Not purely derived:** a good lesson needs things nodes rightly don't contain — quiz distractors with wrong-answer explanations, screen-by-screen pacing, misconception traps. Pretending these can be mechanically derived produces node dumps with a progress bar, which is precisely the failure mode to avoid.
- **Therefore: authored presentation JSON that references canonical IDs.** It lives in `content/` (it is editorial content deserving validation and versioning, not app config), but in its own directories with its own schemas.

### Lesson file shape (schema sketch for P0 to finalize)

```
lesson: {
  id: "lesson-fi-duration",
  teaches: ["G27x"],                    // canonical global(s), by ID
  draws_on: ["fixed-income.z2.6"],      // zone nodes consulted, by ID
  screens: [ { type, body, ... } ],     // ordered blocks
  checks: [ assessment_item_ids ],
  connects: ["G###", ...]               // powers the completion-screen payoff
}
```

Block types for V1 — deliberately only six: `explanation`, `example`, `key_point`, `comparison`, `misconception`, `check`. (`formula` renders as a styled `key_point`; `application` is an `example` with a role tag; `connection` is generated from `connects`, not authored.) Fewer block types = fewer renderers = faster P1.

### Paths are first-class content artifacts — yes

`content/paths/*.json`: ordered lesson IDs, per-step prerequisites (defaulting to graph-derived ordering but overridable by editorial judgment), landing-page copy, outcome statement. Paths are the unit the product sells, the unit the pilot tests, and eventually the unit a tutor navigates — they earn canonical-adjacent status. They are *not* graph edges: a path is one curated walk through the graph, and many paths will cross the same nodes.

### Assessment items

Separate files (or a section of the lesson file — P0 decides), each item carrying: the concept IDs it tests, the question type (directional-reasoning, comparison, scenario, formula-interpretation, cause-effect, ordering — your Section 12 taxonomy, minus trivia), the distractors, and a per-distractor explanation. Tagging items with concept IDs is what makes a future mastery model and review queue possible *without* re-authoring anything — that is the entire forward-compatibility story, and it costs one array field now.

### Mastery, progress, review scheduling

All layer-4. V1 stores progress (`{lesson_id, completed_at, check_results[]}`) in localStorage and sends the approved anonymous, opt-out-respecting event beacon defined by D5. A mastery model (per-concept strength derived from tagged check results) and spaced-repetition scheduling are post-G1, post-database — but the D5 event shape is designed so they can be computed retroactively from day-one data. The event contract was defined in P0; P1 implements the beacon (not a localStorage-only event log).

### What remains immutable

Everything in layer 1, under existing rules: IDs, `home_of`, spines, edge semantics, contiguity. The 26-global multiple-`home_of` legacy defect and the unhomed-generics backlog continue on their existing track, unaffected by product work.

---

## E. Product pilot recommendation

### Fixed Income wins, and not narrowly

**Target learner:** a college student or early-career candidate preparing for finance recruiting — someone who *must* learn this material, has a deadline, and can judge within one session whether the app is better than their current tools (guides, flashcards, YouTube). This is the strongest initial user for three reasons: motivation is prepaid (no habit-formation problem to solve yet), success is externally measurable (can they answer technicals?), and it is the segment where Imprint is weakest and your graph is strongest. It is also you — which makes P2 recruiting trivial and feedback honest.

**Why Fixed Income over the alternatives:**

- It is the **hardest fair test** of the format. Bond math has formulas, directional reasoning, and the densest misconception field in the corpus (duration vs. maturity, current yield vs. YTM, price-yield inversion). If one-idea-per-screen works for convexity, it works for everything softer. Piloting on an easy path would produce a false positive.
- It is **self-contained**: a clean concept-progression spine (ADR-002), a single module, minimal cross-module prerequisite risk. An IB-recruiting or "finance from the ground up" pilot would span modules and force path-curation architecture questions before the lesson format itself is validated — that's two experiments at once. "Finance foundations" is worse still: it doesn't exist as a module, so it would smuggle a content milestone inside a product milestone.
- Its cross-module edges (FI↔PC seam, the credit handshake into the sector modules, the G247→G248→G259 keystone chain into WACC) make the **completion-screen connection payoff real** rather than decorative — the one moment in the loop that no competitor can copy.

**Path length:** 10 lessons, drawn from your Section 8 sequence, collapsed slightly: (1) what a bond is / principal-coupon-maturity, (2) price and yield, (3) current yield vs. YTM, (4) the price-yield inverse relationship, (5) yield curves, (6) duration, (7) duration vs. maturity, (8) convexity, (9) rate risk vs. credit risk + spreads, (10) total return. Ten is enough to test progression and drop-off, short enough that completion is achievable in under ~90 minutes total, and every lesson maps to existing Z1/Z2/Z4 nodes.

**Lesson structure:** 5–8 screens per lesson, 2–3 checks, target 4–7 minutes. Short, not artificially shallow — your Section 12 principle, enforced by the block budget.

**Required screens:** the five from your Section 10 (landing, path, player, completion, progress) — that list was right; adopt it unchanged. **Required interactions:** advance, answer-with-immediate-feedback, continue-where-left-off. Nothing else.

**localStorage is the right call for V1 progress.** The pilot question is "is this enjoyable and effective," not "does sync work." The only real costs — no cross-device progress and no server-verified streaks — don't matter for a 10-lesson, two-week test. Drop-off and usage visibility come from the D5 anonymous, opt-out-respecting event beacon (not from a localStorage-only event log); a one-tap "export my results" button remains a qualitative interview aid.

**What the pilot tests:** lesson-level completion and drop-off points; check accuracy (especially on the misconception pairs — if testers ace duration-vs-maturity after lesson 7, the format is teaching); whether the connection payoff registers in exit interviews; time-per-lesson vs. target.

**Intentionally postponed:** everything in the P1 exclusion list, plus a second path, plus any node-content changes lessons might tempt you toward.

### Success criteria (pre-registered now so P2 can't be rationalized later)

With 10–20 testers: ≥70% complete the first 3 lessons; ≥30% complete all 10; median lesson time within 3–8 minutes; misconception-check accuracy visibly improves between first exposure and the later comparison lesson; and in exit conversations, a majority say unprompted that they'd use it during actual recruiting prep. **Redesign signals:** drop-off *inside* lessons rather than between them (screens too dense or too thin); testers guessing checks without reading (checks too shallow); "feels like flashcards" feedback (connection payoff not landing). **Structural-failure signal:** testers who complete it but say they'd still rather use their current prep guide.

---

## F. Retention and social roadmap

Ordered by required foundation, not by what Duolingo has. Each stage is gated on the one before it existing *and* on evidence the prior stage retains.

| Stage | Mechanics | Required foundation | Earliest slot |
|---|---|---|---|
| 0 (V1) | progress bar, immediate feedback, continue-where-left-off, path %, completion moment | localStorage only | P1 |
| 1 | accounts, server-side progress, cross-device sync | database, auth | post-G1 (only if G1 passes) |
| 2 | daily goal, streak + calendar, weekly summary email | trusted server timestamps, activity-event definitions (already designed in P0), notification plumbing | post-G1 stage 2 |
| 3 | review queue, weak-area tracking, achievements tied to demonstrated mastery | mastery model over concept-tagged check results | M17 |
| 4 | friends, private weekly competitions, recruiting cohorts, head-to-head concept quizzes | social identity, invitations, anti-abuse, and — non-negotiably — evidence from stages 1–3 that solo retention works | Gate G3, not before |
| 5 | leaderboards, public challenges | everything above at scale | far horizon |
| — | graph-grounded tutor ("explain simply / test me / show my missing prerequisite") | stable lesson+path schema (P0), mastery model (stage 3), and paths as tutor-navigable artifacts | after stage 3 |

Two principles govern the whole table. **Streaks count meaningful learning events** (a completed lesson: every required check attempted; correctness is not required), never app-opens — this falls directly out of the event definitions in P0, which is why they're designed now and built later. **Social amplifies retention that already exists; it cannot create it.** The Duolingo-streak anecdote is real signal about the ceiling, but their social layer sits on a decade-old proven solo loop. Yours is at V1. Sequence accordingly.

---

## G. Tool workflow

| Tool | Owns | Explicitly does not |
|---|---|---|
| **Claude/Fable (this project)** | All architecture judgment (both tracks): module maps, lesson-layer design, ADRs, pilot lesson authoring, kickoff prompts, verification passes, **and — new — product strategy**. This project becomes the single strategy venue; this document is its `PROJECT_STATUS.md`-equivalent. | Repo writes during design sessions; mechanical JSON assembly; app implementation |
| **Cursor/Sonnet** | Everything mechanical, both tracks: extraction, migration, validation fixes, the entire P1 build, tests, git operations, Vercel config | Design decisions; schema rulings; anything requiring an ADR |
| **ChatGPT** | **Deliberately shrunk.** Optional scratchpad for prompt-drafting mechanics. Strategy, scoping, and roadmap conversations move here — the three-venue strategy sprawl is the root cause of the scattered feeling. | Owning any decision or any canonical artifact |
| **GitHub** | Canonical repo. Branch discipline below. | — |
| **Vercel** | **Yes — connect during P1, after P0 merges.** Free plan. Production deploys from `main`; preview deploys per PR. Vercel is not a P0 task. It costs nearly nothing and P2 is impossible without a shareable phone-testable URL. School email / Pro is irrelevant at this scale. | Being a gate for *content* branches (they don't touch the app; the existing build check already protects them) |
| **Figma** | **Not now.** One path, five screens, six block types — design in code against the preview deploy. Revisit only if G1 passes and a designer or a real design system enters the picture. | — |

**Branch discipline:** `content/*` branches (graph migrations — existing rules unchanged) and `product/*` branches (lessons, paths, `src/`). Product-branch merge gate: type-check + build + the V-1…V-13 lesson-layer validation suite + preview deployment reviewed on mobile. Content-branch gate: unchanged (strict validation + tarball verification). A branch that touches both layers is rejected by convention — split it. The lesson-layer reference and integrity checks are what let the two branch families evolve independently without drift.

**Answers to the remaining workflow questions (26–33):** the division of labor is otherwise unchanged from what has worked for eleven milestones; product experiments avoid corrupting canonical content via the one-way rule in Section B (reference-by-ID, defects-not-patches, machine-checked); premium-model spend stays on judgment, which now includes lesson *authoring* (pedagogical judgment) but not lesson *rendering* (mechanical).

---

## H. Immediate next action

**1. The next product milestone after P0 merge is P1 — Fixed Income Learning Loop.** P0 (audit + ADR-004 + schemas + authored Fixed Income pilot + lesson-layer validators) is the ratified design/content gate for that build.

**2. Why P0 came first:** it is the only artifact that unblocks *both* tracks simultaneously. With P0 in place, Cursor can build P1 while you run the M12 Consumer Discretionary session — the parallelism this whole plan is built on. Starting M12 first instead would leave Cursor idle on the product side and delay the pilot by a full milestone for zero information gain; starting P1 without P0 would have Cursor inventing schema on the fly, which is exactly the scope-bleed your pipeline exists to prevent.

**3. What waits:** M12 can proceed independently of P1. Everything in the P1 exclusion list waits for G1. Wave-two sectors wait for G1. Streaks, social, and the tutor wait for their foundations per Section F. Figma waits indefinitely.

**4. Immediate product next step after this P0 placement merges:** open the P1 implementation milestone (lesson player, `/learn` routes, localStorage progress, event beacon) from the ratified P0 artifacts — without inventing schema or pedagogy.

---

# Operating Roadmap — Amendment Pass 1

**Status: PROPOSED. Not canonical.**
This document and the accompanying `OPERATING_PLAN.md` become the project's governing roadmap **only** when you (1) explicitly approve them and (2) commit them to the repo (recommended path `docs/OPERATING_ROADMAP.md`, referenced from `README.md`). A model response cannot self-ratify a governing document. Until both steps happen, treat everything here as a recommendation open to revision.

This pass preserves the ratified-in-spirit strong parts (parallel tracks, one-way reference-by-ID, separate presentation layer, small pilot, Consumer Discretionary closing wave one, post-pilot decision gate, deferral of auth/streaks/social/tutor/broad-graph-viz, Cursor-for-mechanics / Claude-for-judgment, Vercel previews) and amends only the eight issues raised.

---

## Deliverable 1 — Amendment table

| # | Issue | Original ruling | Revised ruling | Reason |
|---|---|---|---|---|
| 1 | Ratification status | Document labelled "Ratified," self-declared to supersede prior planning | Labelled **Proposed**; becomes canonical only on your approval **+ commit** to `docs/OPERATING_ROADMAP.md` | Governance can't originate from a model output; canonical status must be an explicit human act recorded in the repo |
| 2 | Milestone numbering | Product folded into arch sequence as M12A / M12B | **Two permanent namespaces:** architecture keeps `M##` (M12 = Consumer Discretionary); product gets `P#` (P0, P1, P2) + gate `G1`. Separate status docs and branch prefixes | Mixing namespaces would corrupt `PROJECT_STATUS.md`, branch names, prompts, and reports as both tracks run for years |
| 3 | Source-of-truth boundary | Lessons "must never restate canonical prose" | **Two canons.** Graph = canon of *financial truth*; lessons/paths = canon of *pedagogy*. Lessons freely **paraphrase, simplify, illustrate, test**; they may not **redefine** graph facts or **invent** definitional/numeric facts the graph lacks | "Never restate" is unbuildable — every lesson expresses graph concepts. The real hazard is *drift-capable competing definitions*, not paraphrase |
| 4 | Repo audit before schema | Claude designs lesson layer; audit implied | **Audit-first (workflow A).** Claude writes an audit spec → Cursor runs a read-only repo audit → Claude designs ADR-004 + schemas against audit *facts* | Matches the project's own "verify from live repo, don't trust memory" law; audit is low-interpretation so ordering risk is minimal; single Claude design pass = less premium spend than design-then-reconcile |
| 5 | Pilot selection | Fixed Income asserted | Fixed Income **selected on an explicit scored comparison** (43 vs IB-tech 38); IB technical foundations named as the sequenced **second** path / real market-pull test | "May still win, but make it explicit" — and the scoring reveals FI wins execution-risk axes while IB-tech wins market-pull axes, which *sequences* the loser rather than discarding it |
| 6 | Instrumentation | localStorage export + interviews | Add an **anonymous event beacon** (privacy-first tool, anon UUID, 8 events) as the drop-off instrument; localStorage stays progress-only; export demoted to qualitative aid | Export can't capture drop-offs — the people who quit are exactly the ones who won't export. Streaming anon events captures them without accounts or a DB |
| 7 | Success criteria | Hard numeric thresholds (≥70%, ≥30%) | **Pattern-based decision framework** mapping evidence bundles → five decisions; in-lesson vs between-lesson drop-off is the primary diagnostic | n=10–20 makes single thresholds noise; the signal lives in *combinations*, read directionally |
| 8 | Post-M12 content gate | "No module scoped after M12 before G1" | Kept — but split: **new active-module migration waits** for G1; **markdown/tooling/offline prep may continue** (source collection, dossier extraction, validator improvements, backlog/defect *triage*, research prep). Defect *fixes that modify shipped G1–G313* generally wait (blast radius) | Preserves anti-inertia intent while not idling cheap mechanical prep that carries no attention cost or graph-write risk |

---

## Deliverable 2 — Final dual-track milestone sequence

Two permanent workstreams, two numbering namespaces, two status docs, two branch prefixes. `docs/OPERATING_ROADMAP.md` governs both; `PROJECT_STATUS.md` remains the corpus source of truth (unchanged invariant); a new `PRODUCT_STATUS.md` tracks the P-track.

### Naming & branch convention

| | Architecture track | Product track |
|---|---|---|
| Milestone IDs | `M12`, `M13`, … | `P0`, `P1`, `P2`, … + gates `G#` |
| Branch prefix | `content/m12-consumer-discretionary` | `product/p0-lesson-layer`, `product/p1-fi-loop` |
| Status doc | `PROJECT_STATUS.md` (corpus totals, validated) | `PRODUCT_STATUS.md` (product milestone state) |
| Report format | existing milestone report | short product-milestone report |
| Merge gate | strict validation 0/0 + tarball verification | type-check + build + product validator checks + mobile preview review |

### Sequence

| ID | Title | Owner (design → exec) | Inputs | Deliverables | Merge / decision gate | Depends on |
|---|---|---|---|---|---|---|
| **P0** | Repo audit + Lesson-layer architecture | Claude (audit spec) → Cursor (read-only audit) → Claude (ADR-004 + schemas + pilot lessons) → Cursor (P0 placement + V-1…V-13) | This roadmap; live tarball; FI node map; `five_zone_template.md` | Audit report; `LESSON_LAYER_DESIGN.md`; ADR-004; lesson/path/assessment schemas; V-1…V-13 lesson-layer validation suite; 10 authored FI pilot lessons | **ADR-004 Accepted; P0 complete pending merge** before any P1 code | roadmap approved |
| **M12** | sector-consumer-discretionary | Claude (arch session) → Cursor (extract + migrate) | Kickoff prompt; sources; live tarball | New module, `sector-layer1`, `build_order 15`, globals from G314; disambiguation retrofits; closes wave one | strict 0/0 + tarball verification | independent of P-track; runs concurrently |
| **P1** | Fixed Income learning loop | Cursor (build from P0 spec) → Claude (review vs design) | ADR-004, schemas, pilot lessons, `src/lib/graph/` | Lesson player, path/landing/completion/progress screens, localStorage progress, anon event beacon, Vercel deploy + PR previews | mobile preview reviewed; type-check + build + validator checks pass | **P0 ratified** |
| **P2** | Pilot test + findings | You (recruit + run) → Claude (synthesize memo) | Deployed P1 URL; event data; exit interviews | 1-page findings memo against Deliverable-4 framework | — | P1 shipped |
| **G1** | Decision gate | You, on evidence | P2 memo | One of: proceed→persistence, revise-format, change-topic, reconsider-user, reconsider-hypothesis | **Gates all wave-two content and all P3+** | P2 complete |

**Concurrency:** Claude runs the P0 design session and the M12 arch session in series (your attention is serial); Cursor executes P1 build and M12 migration in overlapping windows. That is the whole parallelism story — no daily percentage budgeting.

**During P1/P2 (the pilot window), architecture activity permitted:** source collection, dossier extraction (markdown out), validator improvements, defect/backlog *triage and documentation*, kickoff-prompt drafting for future sectors. **Waits for G1:** migrating any new active module into the graph; large canonical refactors; defect *fixes that rewrite shipped G1–G313 globals* (blast radius) unless trivial and isolated.

---

## Deliverable 3 — Revised source-of-truth model

Five layers. Two of them are *canonical* — one for facts, one for pedagogy — which is the correction to the over-broad "no second source of truth."

| Layer | Name | Contents | Location | Authority over | Mutability |
|---|---|---|---|---|---|
| 1 | **Canonical knowledge graph** | globals, zone nodes, edges, disambiguations, gaps | `content/glossary/`, `content/modules/` | **Financial truth** — definitions, relationships, formulas | Append-only + ADRs (architecture track) |
| 2 | **Canonical learning artifacts** | lessons, paths, assessment items | `content/lessons/`, `content/paths/`, `content/assessments/` | **Pedagogy** — sequencing, framing, examples, questions | Freely authored/edited (product track); reference layer 1 by ID |
| 3 | **Generated / runtime presentation** | connection payoff, computed progress %, rendered screens | derived at build/run | nothing stored; fully recomputable | n/a |
| 4 | **Product configuration** | routes, feature flags, block renderers, chrome copy | `src/` | app behavior | ordinary code review |
| 5 | **Learner data** | progress, answers; anonymous product events | localStorage progress (P1) + D5 event beacon (P1) → DB (post-G1) | runtime state | runtime |

### The relationship rules

1. **Facts flow one way: layer 1 → layer 2.** Lessons *express* graph concepts in learner language; they never *establish* facts. If a lesson needs a definitional or numeric fact the graph doesn't hold, that is a **gap or defect filing** routed to the architecture track — never a lesson-local invention.
2. **Two canons, non-overlapping domains.** The graph is the authority on *what is true*; lessons/paths are the authority on *how it is taught*. Neither overrides the other inside its own domain. Yes — **lessons and paths are canonical for pedagogy**, which is why they live in `content/` and get validated, not in `src/`.
3. **What lesson copy MAY do:** paraphrase, simplify, add analogies and worked examples, phrase quiz questions and distractors, choose ordering, add misconception traps, add role-specific applications. This duplication is *expression*, and it is expected.
4. **What lesson copy MAY NOT do:** state a financial fact that contradicts the node it teaches; substitute its own definition for the canonical one; introduce a definitional/numeric fact absent from the graph. This duplication is *competing truth*, and it is forbidden.
5. **The drift test (how to tell acceptable from harmful duplication):** *If the graph node changed, would this lesson text silently become wrong?* A paraphrase is safe because the lesson declares `teaches: [G###]`, so a node change flags the lesson for review via that link. A hard-coded competing fact is harmful because it can drift out of agreement with the node undetected. Author to the first case, never the second.
6. **Contradiction catching (four mechanisms):** (a) machine dangling-reference check — every ID cited in layers 2 must resolve in layer 1; (b) `teaches` / `draws_on` / concept-tag links make human review *targeted* (compare the lesson only against its declared node); (c) authoring review at merge; (d) `MIGRATION_DEFECTS.md` / gap route for any fact the graph lacks.

Layers 2–5 can be deleted wholesale and layer 1 loses nothing. Layer 1 can evolve (append-only) and layer 2 is flagged for review via its ID links. That two-way integrity — not a blanket duplication ban — is what protects canonical financial truth while letting real lessons exist.

---

## Deliverable 4 — Scored pilot comparison

Four candidates, ten dimensions, 1–5 (5 = best for a **first, format-validating** pilot; for "authoring economy" and "implementation simplicity," 5 = low burden).

| Dimension | Fixed Income | IB technical foundations | Accounting→Valuation | Finance ground-up |
|---|:--:|:--:|:--:|:--:|
| Existing canonical content | 5 | 3 | 3 | 3 |
| Prerequisite cleanliness | 5 | 2 | 3 | 1 |
| Authoring economy (low new authoring) | 5 | 3 | 2 | 1 |
| Target-user urgency | 3 | 5 | 4 | 2 |
| Differentiation vs existing products | 4 | 4 | 4 | 1 |
| Ease of recruiting testers | 3 | 5 | 4 | 3 |
| Demonstrate graph connections | 5 | 4 | 4 | 4 |
| Test formulas + misconceptions | 5 | 5 | 5 | 2 |
| Likelihood of voluntary return | 3 | 5 | 4 | 2 |
| Implementation simplicity | 5 | 2 | 3 | 1 |
| **Total** | **43** | **38** | **36** | **20** |

### Reading the scores — the real decision

The composite (FI 43) is not the interesting part. The **axis split** is: FI dominates every *execution-risk* axis (content ready, clean single-module prereqs, low authoring, simple build), while IB-tech dominates every *market-pull* axis (urgency, tester recruiting, voluntary return). Accounting→Valuation sits between them but its content is more scattered (no dedicated accounting module — statements/linkages are embedded across role modules), raising authoring risk. Ground-up loses decisively: no such module exists, it carries the heaviest cross-module path-curation burden, and it competes directly on Imprint's turf (broad beginner content) where their UX is stronger and our depth advantage is diluted.

### Final pilot recommendation: **Fixed Income (P1)** — with IB-technical explicitly sequenced second

A first pilot's job is to test the **format** with the fewest confounds. FI tests *"does one-idea-per-screen teach genuinely hard finance?"* (convexity, duration-vs-maturity, price-yield inversion — the densest misconception field in the corpus) inside a single self-contained module, so a failure is unambiguously a *format* failure. IB-technical would test market pull harder but confounds the format test with **cross-module path curation** — two experiments at once, and if it failed you couldn't tell which broke.

So FI is chosen deliberately as the **low-confound format validator**, with eyes open to its one weakness (narrower urgency than IB-tech). **IB technical foundations is not rejected — it is the P-track's second path**, built at G1's "loop works" branch as the real market-pull test, at which point you build exactly the cross-module curation the FI pilot let you defer. That sequencing is a feature: prove the format cheaply, then spend on the wedge.

**Pilot spec (unchanged from OPERATING_PLAN §E where not amended):** target = recruiting/early-career candidate; 10 lessons (bond basics → total return); 5–8 screens, 2–3 checks, 4–7 min each; five screens (landing/path/player/completion/progress); interactions = advance, answer-with-immediate-feedback, continue-where-left-off.

---

## Deliverable 5 — Pilot instrumentation (minimum viable, privacy-conscious)

Three clearly separated data tiers. Do **not** build an analytics stack.

| Tier | What | Where | Purpose | PII? |
|---|---|---|---|---|
| **Local progress state** | `{lesson_id, completed_at, check_results[]}` | localStorage | drives UI: continue-where-left-off, path % | none; never leaves device except voluntary export |
| **Anonymous product analytics** | the 8 events below, keyed to a client-generated random UUID | privacy-first event tool, free tier (e.g. PostHog/Plausible-class) | drop-off funnels, time-per-lesson, return behavior | none; anon UUID only |
| **Future authenticated records** | unified per-user learning history | database (post-G1) | real accounts, sync, mastery | deferred entirely |

### The 8 events (the drop-off instrument)

`path_started` · `lesson_started` · `screen_advanced {index}` · `question_answered {item_id, concept_ids, correct}` · `lesson_completed {lesson_id}` · `session_ended` · `path_completed` · `return_session` (fires when a new session starts >N hours after the last).

**Why a beacon, not export-only:** the testers who drop off are precisely the ones who will never export their localStorage. Streaming these 8 anonymous events as they happen is the only reliable way to *see* in-lesson vs between-lesson drop-off — the single most diagnostic signal in Deliverable 6. The localStorage export is demoted to a **qualitative aid** (lets an interviewee show you their answer detail), not the primary instrument.

**Collection approach:** client generates an anonymous UUID in localStorage; a thin `track(event, props)` wrapper POSTs the 8 events to a privacy-first analytics free tier. No accounts, no social identity, no backend of your own, no DB. Show testers a one-line notice that anonymous usage events are collected and honor an opt-out / do-not-track. Concept IDs on `question_answered` are the same tags that later enable a mastery model — captured now, computed post-G1.

---

## Deliverable 6 — Pilot success as a decision framework (directional, n=10–20)

Read **patterns across metrics**, not single thresholds. The primary diagnostic is **where** people stop.

### Evidence signals collected

completion (between-lesson) · drop-off location (in-lesson vs between-lesson) · check accuracy · misconception retention (accuracy on the comparison lesson vs first exposure) · time per lesson vs 4–7 min target · return behavior (`return_session`) · observed usability (interviews) · preference vs current study tools (interviews) · willingness to use for a real goal (interviews).

### Evidence pattern → decision

| Decision | Pattern that supports it |
|---|---|
| **Proceed** (→ P3 = accounts/persistence, then daily goals/streaks) | Most who start reach later lessons; misconception accuracy rises across the path; interviews show unprompted preference over current tools **and** willingness to use for real prep; some return behavior |
| **Revise lesson format** (redesign presentation, re-test same topic) | Drop-off is **inside** lessons, not between them; screens read as too dense/thin; checks guessed without reading; "feels like flashcards"; between-lesson completion is fine but in-lesson isn't |
| **Change pilot topic** (re-pilot on IB technicals) | Format works for those who engage (they complete and learn), but engagement/return is low **specifically because FI isn't what testers are prepping** — low urgency, positive from the few who do it |
| **Reconsider target user** | Recruiting candidates are lukewarm / prefer their guides, but a different segment shows more pull in interviews |
| **Reconsider product hypothesis** (pause product spend; re-examine wedge — reference product? B2B licensing?) | Testers complete it, call it well-made, and **still** wouldn't choose it over current tools; no segment shows pull; the connection payoff doesn't register |

The in-lesson vs between-lesson distinction separates "format broken" (revise) from "topic/pull broken" (change topic / user / hypothesis) — which is why the event beacon in Deliverable 5 is non-negotiable. Treat every number as directional; let the interview evidence break ties.

---

## Deliverable 7 — Exact immediate workflow *(historical — P0 workflow completed)*

Audit-first (workflow A) was the approved P0 sequence because the project's own law is *verify from the live repo, don't design against memory*. **This deliverable is retained as a historical record of the completed P0 workflow; it is not current instructions.** Current next product action: **merge P0, then begin P1.** M12 Consumer Discretionary remains the concurrent architecture milestone; no new active module after M12 is migrated before G1.

Completed sequence (do not re-run):

1. **You** — approved this pass; committed the roadmap as `docs/OPERATING_ROADMAP.md`; referenced it from `README.md`; created `PRODUCT_STATUS.md` and the product-track branch.
2. **Claude (this project)** — produced the P0 read-only **audit prompt** (Deliverable 8, now archived).
3. **Cursor/Sonnet** — ran the audit against the live repo and returned the structured report (`docs/P0_REPO_AUDIT.md`).
4. **P0 design + placement** — Claude produced `LESSON_LAYER_DESIGN.md` + ADR-004 + the three schemas + validator-check specs + the 10 FI pilot lessons; Cursor placed them, implemented V-1…V-13, and ratified ADR-004 as Accepted. **P0 is complete pending merge.**

Meanwhile, independently, the **M12 Consumer Discretionary** arch session can be scheduled whenever your attention frees — it shares no dependency with P0 and its Cursor migration overlaps P1's build.

---

## Deliverable 8 — Paste-ready kickoff prompt (P0.2: Cursor read-only repository audit) *(historical / archived)*

**Status:** Historical. This prompt has already been executed; the resulting audit is `docs/P0_REPO_AUDIT.md`. Do not re-run it as current work. Retained below for provenance only.

Paste the block below into Cursor. It is deliberately read-only and prescriptive about the report shape, so the audit reports *facts* and is not shaped by Cursor's own design opinions.

<<<BEGIN CURSOR PROMPT>>>

# P0 — Read-only repository audit for lesson-layer design

You are performing a **read-only reconnaissance audit** of `finance-learning-app`. Produce a factual report that a knowledge architect will use to design a lesson/path presentation layer. 

## Hard rules — read twice
- **Do not write, edit, create, delete, migrate, or refactor anything.** No new files, no branch changes, no commits, no `npm install`, no code generation.
- **Do not propose a design.** Report what exists, not what should exist. Opinions go only in the final "integration risks" section, clearly labelled as observations.
- If a listed item does not exist, say "not present" — do not scaffold it.
- Run only read/inspect commands (`cat`, `ls`, `grep`, `tree`, open-in-editor). Report the exact commands you used.

## Report structure (use these exact headings)

### 1. Graph data shapes
- The JSON schema / field set of a **global** entry (`content/glossary/`): every field, types, which are optional. Paste 2 representative entries.
- The JSON schema / field set of a **zone node** (`content/modules/`): every field including edge/reference fields, `home_of`, `disambiguate_with`, `gaps`. Paste 2 representative nodes (one global-hosting, one local).
- How module/zone/global IDs are formatted and where the ID-generation or contiguity logic lives.

### 2. Graph access layer
- Every public interface exported from `src/lib/graph/`: function signatures, return types, what they read and when (build-time vs runtime).
- How canonical JSON is loaded (build-time import? fs read? generated types?).

### 3. Routes and components
- Current Next.js routes (paths + whether static/dynamic) and the components they render.
- Any existing component that displays a node, zone, or reference — note reuse candidates for a lesson player.

### 4. Validation
- Where validators live (`pipeline/validate/`, `new_module_checks.py`, etc.), how checks are registered, and the exact command(s) to run strict validation.
- The extension point for adding a **new check** (e.g., a dangling-reference check over a new `content/` subtree): show the pattern a new check must follow.

### 5. Build, types, test
- Exact commands for: dev server, production build, type-check, lint, tests. Which currently pass; paste any failing output.
- Node version / package manager in use.

### 6. Pre-existing product-ish code
- Any existing code or files touching: lessons, paths, quizzes/assessments, progress, learner state, localStorage, analytics/events, or user accounts. Report "not present" if none — this is expected but must be confirmed.

### 7. Vercel / deployment readiness
- Presence of `vercel.json`, framework preset, env-var usage, any config that would affect a static graph build on Vercel. Whether the production build produces output deployable as-is.

### 8. Integration risks (observations only)
- Concrete facts that would complicate adding a separate `content/lessons/`, `content/paths/`, `content/assessments/` tree that references graph IDs — e.g., how IDs are resolved, whether a runtime ID lookup exists or must be built, type-generation coupling, OneDrive/Windows path constraints. Label each as an observation, not a recommendation.

## Output
A single markdown report following the headings above, with pasted representative JSON/signatures and the exact commands you ran. Nothing else.

<<<END CURSOR PROMPT>>>
