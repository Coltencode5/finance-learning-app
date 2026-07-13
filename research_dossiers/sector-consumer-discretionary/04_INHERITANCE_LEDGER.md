# 04 — Inheritance Ledger (PART 0 mechanical pass)

Corpus searched live: **313 globals** + **615 zone nodes**. Script: `_scripts/corpus_search.py` (aliases + inflections via regex patterns). Raw JSON: `raw_extractions/_inheritance_raw.json`.

## Headline counts (script heuristics — architect verifies meaning)

- Already-homed string hits (heuristic; often collisions): **7**
- Mentioned but unhomed: **13**
- Needs verify (glossary string-hit ± node mentions): **7**
- Absent / genuine mint candidates: **37**
- Total candidates searched: **64**

Note: "Already homed" here means a glossary *string* match on the search pattern — not a confirmed same-meaning home. Cross-check `05_COLLISION_MAP.md` before back-linking.

## Full table

| Candidate concept | Already homed? | Where (G-number + home) | Mentioned but unhomed? | Where (every matching node) | Verdict for the architect |
|---|---|---|---|---|---|
| Amazon flywheel | no | — | yes | `investment-banking.z1.6`, `investment-banking.z4.5`, `investment-banking.z5.2`, `private-credit.z1.3`, `private-credit.z2.2`, `venture-capital.z5.4`, `venture-capital.z5.5` | Mentioned but unhomed |
| negative operating cycle / working capital | yes — verify meaning | G31 «Working capital» @ private-equity.Z3; G92 «Unlevered Free Cash Flow (UFCF)» @ investment-banking.Z3 | yes | `investment-banking.z2.6`, `investment-banking.z3.5`, `investment-banking.z3.6`, `private-equity.z3.13`, `sector-financials.z4.1` | Mentioned; glossary string-hit exists — verify if true home or collision |
| marketplace / third-party seller | no | — | yes | `equity-research.z3.8`, `fixed-income.z1.4`, `fixed-income.z3.1`, `sector-energy.z2.1` | Mentioned but unhomed |
| take rate | no | — | no | — | Absent — genuine mint candidate |
| fulfillment / fulfillment network | no | — | no | — | Absent — genuine mint candidate |
| Fulfillment by Amazon (FBA) | no | — | no | — | Absent — genuine mint candidate |
| Amazon Prime / membership shipping | yes — verify meaning | G117 «Prime brokerage» @ hedge-funds.Z1 | yes | `equity-research.z1.8`, `equity-research.z5.3`, `hedge-funds.z1.10`, `hedge-funds.z1.4`, `hedge-funds.z1.6`, `hedge-funds.z4.5`, `hedge-funds.z5.3`, `macro-economics.z2.5`, `sector-financials.z2.3` | Mentioned; glossary string-hit exists — verify if true home or collision |
| subscription (commerce / Prime) | yes — verify meaning | G67 «Fund leverage & asset coverage» @ private-credit.Z5; G294 «SaaS & the subscription model (Z2.1)» @ sector-information-technology.Z2.1; G300 «ARR (annual recurring revenue) (Z3.2)» @ sector-information-technology.Z3.2 | yes | `equity-research.z4.1`, `equity-research.z5.2`, `private-credit.z1.10`, `private-credit.z2.14`, `private-credit.z5.3`, `sector-information-technology.z1.2`, `sector-information-technology.z2.1`, `sector-information-technology.z3.2`, `sector-information-technology.z4.2` | Already homed (candidate — verify meaning) |
| network effects (retail marketplace) | yes — verify meaning | G298 «Network effects (Z3.1)» @ sector-information-technology.Z3.1 | yes | `macro-economics.z5.5`, `sector-information-technology.z1.2`, `sector-information-technology.z3.1`, `venture-capital.z1.2` | Already homed (candidate — verify meaning) |
| Get Big Fast / scale-first retail | no | — | no | — | Absent — genuine mint candidate |
| everyday low prices (EDLP) | no | — | no | — | Absent — genuine mint candidate |
| trade-up / trading up | no | — | no | — | Absent — genuine mint candidate |
| trade-down / trading down | no | — | no | — | Absent — genuine mint candidate |
| New Luxury / premiumization | no | — | no | — | Absent — genuine mint candidate |
| death in the middle | no | — | no | — | Absent — genuine mint candidate |
| accessible superpremium | no | — | no | — | Absent — genuine mint candidate |
| masstige | no | — | no | — | Absent — genuine mint candidate |
| benefit ladder (technical/functional/emotional) | no | — | no | — | Absent — genuine mint candidate |
| rocketing (selective trade-up) | no | — | no | — | Absent — genuine mint candidate |
| apostles / brand apostles | no | — | no | — | Absent — genuine mint candidate |
| omnichannel | no | — | no | — | Absent — genuine mint candidate |
| comparable store sales / comps | yes — verify meaning | G88 «Comparable companies analysis ("comps")» @ investment-banking.Z3; G89 «Precedent transactions analysis ("deal comps")» @ investment-banking.Z3; G99 «Control premium» @ investment-banking.Z2; G220 «The three appraisal approaches» @ real-estate.Z3.4 | yes | `asset-management.z2.4`, `asset-management.z2.5`, `asset-management.z3.3`, `equity-research.z2.2`, `equity-research.z2.3`, `equity-research.z3.10`, `equity-research.z3.7`, `equity-research.z3.8`, `hedge-funds.z3.2`, `investment-banking.z1.12`, `investment-banking.z1.9`, `investment-banking.z2.15`, `investment-banking.z3.2`, `investment-banking.z3.3`, `investment-banking.z3.4`, `investment-banking.z3.9`, `private-equity.z3.6`, `real-estate.z3.4`, `sector-energy.z4.1`, `sector-financials.z4.1`, `sector-information-technology.z4.1`, `venture-capital.z2.7`, `venture-capital.z3.7` | Already homed (candidate — verify meaning) |
| traffic / ticket decomposition | no | — | yes | `real-estate.z3.4`, `real-estate.z5.3` | Mentioned but unhomed |
| DTC / direct-to-consumer | no | — | yes | `wealth-management.z5.3` | Mentioned but unhomed |
| wholesale vs direct channel mix | no | — | yes | `equity-research.z1.10`, `equity-research.z3.7`, `hedge-funds.z2.8`, `investment-banking.z1.12`, `macro-economics.z3.2`, `real-estate.z1.5`, `sector-energy.z3.2`, `sector-financials.z2.1`, `sector-financials.z4.2` | Mentioned but unhomed |
| gross margin (retail) | no | — | yes | `sector-information-technology.z1.2`, `sector-information-technology.z2.2`, `sector-information-technology.z2.3`, `sector-information-technology.z3.2`, `sector-information-technology.z4.1`, `sector-information-technology.z4.2` | Mentioned but unhomed |
| inventory / inventory turns | yes — verify meaning | G76 «Borrowing base» @ private-credit.Z3 | yes | `fixed-income.z1.5`, `fixed-income.z1.7`, `fixed-income.z5.1`, `fixed-income.z5.3`, `fixed-income.z5.4`, `fixed-income.z5.6`, `private-credit.z2.10`, `private-credit.z3.13`, `sector-energy.z2.1`, `sector-energy.z3.1`, `sector-energy.z3.3`, `sector-information-technology.z2.2`, `sector-information-technology.z2.3` | Mentioned; glossary string-hit exists — verify if true home or collision |
| inventory days | no | — | no | — | Absent — genuine mint candidate |
| systemwide sales | yes — verify meaning | G282 «Repo & secured financing (Z5.3)» @ fixed-income.Z5.3 | yes | `fixed-income.z5.3` | Mentioned; glossary string-hit exists — verify if true home or collision |
| company-operated vs franchised/licensed | no | — | no | — | Absent — genuine mint candidate |
| restaurant-level margin | no | — | no | — | Absent — genuine mint candidate |
| RevPAR | no | — | yes | `real-estate.z2.1`, `real-estate.z2.2` | Mentioned but unhomed |
| ADR (average daily rate) | no | — | no | — | Absent — genuine mint candidate |
| occupancy (hotels) | yes — verify meaning | G230 «Leasing & occupancy» @ real-estate.Z4.3 | yes | `real-estate.z1.7`, `real-estate.z2.2`, `real-estate.z2.4`, `real-estate.z3.2`, `real-estate.z3.5`, `real-estate.z4.2`, `real-estate.z4.3`, `real-estate.z4.4`, `real-estate.z4.5`, `real-estate.z5.1` | Already homed (candidate — verify meaning) |
| asset-light fee model (hotels) | yes — verify meaning | G8 «Management fee» @ private-equity.Z1; G9 «"2 and 20"» @ private-equity.Z1; G180 «Wealth-management fee models» @ wealth-management.Z5 | yes | `asset-management.z1.6`, `hedge-funds.z1.5`, `hedge-funds.z5.1`, `investment-banking.z1.7`, `private-credit.z5.2`, `private-equity.z1.10`, `private-equity.z1.11`, `private-equity.z1.12`, `private-equity.z1.18`, `private-equity.z1.6`, `real-estate.z1.6`, `real-estate.z3.2`, `sector-financials.z2.3`, `venture-capital.z1.6`, `venture-capital.z1.7`, `wealth-management.z1.8` | Mentioned; glossary string-hit exists — verify if true home or collision |
| incentive management fees | no | — | no | — | Absent — genuine mint candidate |
| gross fee revenues / take-rate lodging | no | — | no | — | Absent — genuine mint candidate |
| heterogeneous homogeneity / category blur | no | — | no | — | Absent — genuine mint candidate |
| reverse positioning / reverse brand | no | — | no | — | Absent — genuine mint candidate |
| breakaway brand | no | — | no | — | Absent — genuine mint candidate |
| hostile brand | no | — | no | — | Absent — genuine mint candidate |
| competitive herd / differentiation | no | — | yes | `asset-management.z2.1`, `equity-research.z1.1`, `equity-research.z1.2`, `equity-research.z1.4`, `equity-research.z2.4`, `equity-research.z2.7`, `equity-research.z3.1`, `equity-research.z3.12`, `equity-research.z3.2`, `equity-research.z3.5`, `equity-research.z3.6`, `equity-research.z4.3`, `equity-research.z4.4`, `equity-research.z5.1`, `equity-research.z5.7`, `hedge-funds.z2.1`, `real-estate.z1.7`, `sector-energy.z1.2`, `sector-information-technology.z3.1`, `wealth-management.z2.1`, `wealth-management.z3.2` | Mentioned but unhomed |
| brand / brand equity | no | — | yes | `asset-management.z2.7`, `asset-management.z5.1`, `asset-management.z5.3`, `hedge-funds.z5.1`, `investment-banking.z5.1`, `venture-capital.z1.2`, `venture-capital.z1.8`, `venture-capital.z2.6`, `venture-capital.z5.4`, `venture-capital.z5.5`, `wealth-management.z5.1` | Mentioned but unhomed |
| moat / durable competitive advantage | no | — | yes | `asset-management.z2.7`, `equity-research.z2.7`, `sector-energy.z1.2`, `sector-energy.z2.3`, `sector-financials.z2.1`, `sector-financials.z2.3`, `sector-information-technology.z2.1`, `sector-information-technology.z3.1`, `sector-information-technology.z5.1`, `venture-capital.z1.8`, `wealth-management.z5.1` | Mentioned but unhomed |
| margin (retail gross/op) | yes — verify meaning | G70 «Spread / Credit margin» @ private-credit.Z3; G117 «Prime brokerage» @ hedge-funds.Z1; G286 «Net interest margin (NIM) (Z1.1)» @ sector-financials.Z1.1; G302 «The Rule of 40 (Z4.1)» @ sector-information-technology.Z4.1; G307 «The crack spread (the refining margin) (Z2.3)» @ sector-energy.Z2.3 | yes | `asset-management.z1.6`, `asset-management.z2.4`, `asset-management.z2.5`, `asset-management.z3.3`, `asset-management.z5.1`, `equity-research.z2.3`, `equity-research.z3.2`, `equity-research.z3.8`, `fixed-income.z3.8`, `fixed-income.z4.7`, `fixed-income.z5.3`, `fixed-income.z5.6`, `hedge-funds.z1.6`, `investment-banking.z1.7`, `investment-banking.z3.6`, `macro-economics.z4.4`, `private-equity.z4.6`, `real-estate.z2.3`, `sector-energy.z2.3`, `sector-financials.z1.1`, `sector-financials.z3.1`, `sector-information-technology.z1.1`, `sector-information-technology.z2.2`, `sector-information-technology.z2.3`, `sector-information-technology.z3.2`, `sector-information-technology.z4.1`, `sector-information-technology.z4.2`, `wealth-management.z2.7` | Already homed (candidate — verify meaning) |
| churn / retention (commerce) | yes — verify meaning | G301 «NRR (net revenue retention) (Z3.2)» @ sector-information-technology.Z3.2 | yes | `asset-management.z5.3`, `equity-research.z2.3`, `fixed-income.z3.10`, `sector-information-technology.z1.1`, `sector-information-technology.z2.1`, `sector-information-technology.z3.2`, `venture-capital.z3.12`, `venture-capital.z3.4`, `venture-capital.z3.5`, `wealth-management.z4.1`, `wealth-management.z5.5` | Mentioned; glossary string-hit exists — verify if true home or collision |
| e-commerce / online retail | no | — | yes | `real-estate.z2.1`, `real-estate.z2.2` | Mentioned but unhomed |
| platform (retail marketplace vs IT) | yes — verify meaning | G132 «Multi-strategy / the platform (pod) model» @ hedge-funds.Z2; G178 «The robo-advisor / digital advice» @ wealth-management.Z2; G216 «The venture platform & the partnership» @ venture-capital.Z1.8; G297 «The multi-sided platform (Z3.1)» @ sector-information-technology.Z3.1 | yes | `asset-management.z1.5`, `asset-management.z1.6`, `asset-management.z5.1`, `asset-management.z5.3`, `equity-research.z2.3`, `equity-research.z5.6`, `hedge-funds.z2.10`, `hedge-funds.z2.11`, `hedge-funds.z3.5`, `hedge-funds.z4.1`, `hedge-funds.z4.4`, `hedge-funds.z5.1`, `hedge-funds.z5.6`, `private-credit.z1.17`, `private-credit.z5.9`, `private-equity.z4.9`, `real-estate.z2.7`, `real-estate.z5.3`, `real-estate.z5.5`, `sector-information-technology.z2.2`, `sector-information-technology.z3.1`, `sector-information-technology.z5.1`, `sector-information-technology.z5.2`, `venture-capital.z1.8`, `venture-capital.z2.6`, `venture-capital.z3.2`, `venture-capital.z4.1`, `venture-capital.z5.5`, `wealth-management.z1.4`, `wealth-management.z2.9`, `wealth-management.z5.1`, `wealth-management.z5.3` | Already homed (candidate — verify meaning) |
| AWS / cloud (Amazon segment) | yes — verify meaning | G295 «Cloud computing & the hyperscalers (Z2.1)» @ sector-information-technology.Z2.1 | yes | `sector-information-technology.z2.1` | Mentioned; glossary string-hit exists — verify if true home or collision |
| advertising services (retail media) | no | — | no | — | Absent — genuine mint candidate |
| fulfillment cost / shipping cost | no | — | no | — | Absent — genuine mint candidate |
| experiences per square foot | no | — | no | — | Absent — genuine mint candidate |
| retail archetype (Stephens ten) | no | — | no | — | Absent — genuine mint candidate |
| New Retail / unified commerce (Alibaba) | no | — | no | — | Absent — genuine mint candidate |
| mall / shopping center economics | no | — | no | — | Absent — genuine mint candidate |
| consumer spending / consumer cycle | no | — | yes | `macro-economics.z1.10` | Mentioned but unhomed |
| consumer ABS / retail credit | no | — | no | — | Absent — genuine mint candidate |
| consumer LBO | no | — | no | — | Absent — genuine mint candidate |
| direct sales vs dealer franchise (auto) | no | — | no | — | Absent — genuine mint candidate |
| vertical integration (auto/OEM) | no | — | no | — | Absent — genuine mint candidate |
| EV cost structure / battery cost | yes — verify meaning | G25 «Enterprise Value (EV)» @ private-equity.Z3; G27 «Valuation multiples» @ private-equity.Z3; G95 «Equity Value ↔ Enterprise Value bridge» @ investment-banking.Z3 | yes | `equity-research.z3.7`, `equity-research.z3.8`, `fixed-income.z1.3`, `hedge-funds.z3.2`, `investment-banking.z1.12`, `investment-banking.z3.1`, `investment-banking.z3.3`, `investment-banking.z3.5`, `investment-banking.z3.8`, `macro-economics.z4.7`, `private-equity.z3.10`, `private-equity.z3.13`, `private-equity.z3.6`, `private-equity.z3.7`, `private-equity.z3.8`, `sector-energy.z4.1`, `sector-energy.z5.2`, `sector-financials.z4.1`, `sector-information-technology.z4.1` | Already homed (candidate — verify meaning) |
| gigafactory / manufacturing scale (auto) | no | — | no | — | Absent — genuine mint candidate |
| autopilot / autonomy economics | no | — | no | — | Absent — genuine mint candidate |
| sector frameworks hub (ER z2.3) | no | — | yes | `equity-research.z2.1`, `equity-research.z2.3`, `equity-research.z3.2`, `sector-financials.z1.1`, `sector-information-technology.z1.1` | Mentioned but unhomed |

## Script shown

See `_scripts/corpus_search.py` — loads `content/glossary/globals.json` (term, aliases, quick_definition) and all module zone `nodes[]` (title, quick_definition, explainer_covers, connects_to notes, connects_to_raw).

