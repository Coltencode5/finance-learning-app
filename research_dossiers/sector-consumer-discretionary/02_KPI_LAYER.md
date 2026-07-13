# 02 — KPI Layer (FY2025 Form 10-K filings)

Values below use **the filing’s own labels**. Years are each issuer’s fiscal year ending on the report date. Sources: Amazon YE 2025-12-31; Nike YE 2025-05-31; Starbucks YE 2025-09-28; Marriott YE 2025-12-31. Snippet store: `_kpi_pulls.md`.

---

## Amazon.com, Inc. — broadline / e-commerce

### Net sales by activity (filing label: Net Sales) — Year Ended Dec 31 ($ millions)

| Label (exact) | 2024 | 2025 |
|---|---:|---:|
| Online stores | 247,029 | 269,287 |
| Physical stores | 21,215 | 22,561 |
| Third-party seller services | 156,146 | 172,162 |
| Advertising services | 56,214 | 68,635 |
| Subscription services | 44,374 | 49,619 |
| AWS | 107,556 | 128,725 |
| Other | 5,425 | 5,935 |
| **Consolidated** | **637,959** | **716,924** |

Also disclosed: Net product sales $296,266 / Net service sales $420,658 (2025).

### Segment net sales & operating income (North America / International / AWS)

| Segment | 2025 Net sales ($m) | 2025 Operating income ($m) | 2024 Op. income ($m) |
|---|---:|---:|---:|
| North America | 426,305 | 29,619 | 24,967 |
| International | 161,894 | 4,750 | 3,792 |
| AWS | 128,725 | 45,606 | 39,834 |
| Consolidated | 716,924 | 79,975 | 68,593 |

Sales mix 2025: NA 59% / International 23% / AWS 18%. Consolidated sales +12% YoY.

### Fulfillment / shipping cost trend

| Label | 2024 | 2025 |
|---|---:|---:|
| Fulfillment expense ($m) | 98,505 | 109,074 |
| Fulfillment % of net sales | 15.4% | 15.2% |
| Fulfillment YoY growth | 9% | 11% |
| Shipping costs ($b, as stated) | 95.8 | 102.7 |

**Note:** Amazon states operating income is more meaningful than gross profit/gross margin given category diversity.

---

## NIKE, Inc. — apparel & durables (Fiscal 2025)

| Label (exact / MD&A) | FY2025 | FY2024 |
|---|---:|---:|
| NIKE, Inc. Revenues | $46.3B ($46,309m) | $51.4B ($51,362m) |
| Sales through NIKE Direct | $18,783m (~42% of NIKE Brand) | $21,519m |
| Sales to Wholesale Customers (NIKE Brand) | $25,883m | $27,758m |
| Gross margin | 42.7% | 44.6% (−190 bps) |
| Inventories (as of May 31) | $7.5B | $7.5B (flat) |
| EBIT margin | 8.2% | 12.7% |
| Comparable store sales (NIKE Direct stores) | −1% (company definition) | — |

**Channel color:** NIKE Direct −13% reported (−12% FX-neutral); Brand Digital $9.6B vs $12.1B (−20%); store sales flat. Wholesale −7% reported / −6% FX-neutral. Gross margin pressure from discounts, channel mix, inventory obsolescence reserves.

**Inventory days:** Not disclosed as a named “days” KPI in the highlights pulled; inventories level $7.5B is the disclosed stock metric. **Flag:** days-on-hand would need computation from COGS—not presented as a filing label here.

---

## Starbucks Corporation — restaurants (Fiscal 2025)

| Label | FY2025 | FY2024 / notes |
|---|---:|---|
| Total net revenues | $37.2B | $36.2B (+3%) |
| Consolidated operating margin | 7.9% | 15.0% (−710 bps) |
| Company-operated store revenue share | 83% of total net revenues | — |
| Licensed store revenue share | 12% of total net revenues | — |
| Store mix (count) | Co-op 21,514 (52%) / Licensed 19,476 (48%); Total 40,990 | — |
| North America comparable store sales | −2% | transactions −4%, average ticket +2% |
| International comparable store sales | −1% | transactions −2%, ticket +1% |
| North America operating margin | 11.5% | −830 bps YoY |
| North America co-op vs licensed stores | 11,018 (60%) / 7,293 (40%) | — |

**System-wide / restaurant-level margin:** Starbucks discusses company-operated vs licensed economics (licensed: lower gross margin, higher operating margin; royalty + product margin) but does **not** lead with a McDonald’s-style “system-wide sales” total in the pulled MD&A highlights. **Flag:** “system-wide sales” as a single KPI is thin/absent in the extracted Starbucks labels—use store-count mix + co-op revenue share instead, or note gap vs classic QSR disclosure.

**Traffic/ticket decomposition:** Explicitly disclosed for comps (comparable transactions + average ticket).

---

## Marriott International, Inc. — hotels (Calendar 2025)

### Fee structure (asset-light)

| Label ($ millions) | 2025 | 2024 |
|---|---:|---:|
| Franchise fees | 3,325 | 3,113 |
| Base management fees | 1,322 | 1,288 |
| Incentive management fees | 791 | 769 |
| Gross fee revenues | 5,438 | 5,170 |
| Contract investment amortization | (135) | (103) |
| Net fee revenues | 5,303 | 5,067 |
| Owned, leased, and other revenue | 1,679 | 1,551 |
| Cost reimbursement revenue | 19,204 | 18,482 |
| Consolidated revenue | 26,186 | 25,100 |

### Operating KPIs (comparable properties — filing table)

Comparable **company-operated** U.S. & Canada (2025): ADR-related figures in table include RevPAR $185.78 (+2.3%), occupancy 69.0% (−0.4 pts), ADR $269.36 (+2.9%).

Comparable **systemwide** U.S. & Canada: RevPAR $132.35 (+0.7%), occupancy 69.5% (−0.6 pts), ADR $190.33 (+1.5%).

(Europe and other regions also tabulated in filing—see `_kpi_pulls.md` Marriott section.)

**Gross bookings / OTA take rate:** Not Marriott’s primary disclosure model (fee revenues on managed/franchised system). **Flag:** Booking Holdings–style gross bookings/take rate **not** obtained (Booking 10-K not fetched).

---

## Cross-cutting KPI map

| KPI | Broadline/e-com (AMZN) | Apparel (NKE) | Restaurants (SBUX) | Hotels (MAR) | Travels across CD? |
|---|---|---|---|---|---|
| Comparable store / comps | Nike Direct comps only; Amazon not store-comps led | Yes (Direct stores) | **Yes — core** | Hotel “comparable properties” (RevPAR comps) | **Yes** (retail/restaurant); hotels use property comps |
| Traffic / ticket (transactions × ticket) | Unit sales qualitative | Traffic decline cited for Direct | **Yes — explicit** | Occupancy × ADR → RevPAR | Strong in restaurants; analogous in hotels |
| DTC / direct mix | 1P online stores + physical; also 3P | **Yes — NIKE Direct vs Wholesale** | Co-op vs licensed (not classic DTC apparel) | Owned/leased small vs fees | Apparel yes; others via channel mix |
| Inventory / turns | Inventory allowance; quick-turn culture | **Inventories $7.5B**; obsolescence | Food/retail inventory less central in highlights | Rooms inventory = capacity | Retail/apparel yes; hotels different |
| Gross / operating margin | Op. income by segment; resists gross margin | **Gross margin 42.7%** | Operating margin 7.9% | Fee margins embedded in fee lines | Yes, but definitions differ |
| Take rate / marketplace fees | 3P seller services commissions | — | License royalties | Franchise + management fees | Platform/franchise businesses |
| Fulfillment / shipping cost | **Yes — core** | Warehousing/logistics in GM bridge | — | — | E-com specific |
| RevPAR / ADR / occupancy | — | — | — | **Yes — core** | Hotels/leisure (also in RE module) |
| System-wide sales | GMV not labeled “system-wide” | — | **Thin in SBUX pull** | Systemwide RevPAR | Franchise systems |
| Subscription / membership | Prime / subscription services | — | Digital loyalty (not pulled as ARR) | Loyalty deferred revenue | Partial |
| AWS / cloud | Segment | — | — | — | **IT boundary**, not CD-native |

**Verified candidates that travel:** comps (with collision risk vs G88), traffic/ticket (or occupancy/ADR), channel mix (DTC/wholesale/co-op/licensed), inventory (retail), margins (with collision risk), fee/take-rate structures (marketplace & lodging).
