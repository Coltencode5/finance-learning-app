#!/usr/bin/env python3
"""One-off dossier cleanup for sector-information-technology. Not part of pipeline."""
from __future__ import annotations

import csv
import re
from pathlib import Path

DOSSIER = Path(__file__).resolve().parent

PATH_MAP = {
    r"c:\\Users\\cfroo\\Downloads\\_OceanofPDF\.com_The_Business_of_Platforms_-_Michael_A_Cusumano\.pdf": "The_Business_of_Platforms.pdf",
    r"c:\\Users\\cfroo\\Downloads\\_OceanofPDF\.com_Subscribed_-_Tien_Tzuo\.pdf": "Subscribed.pdf",
    r"c:\\Users\\cfroo\\Downloads\\_OceanofPDF\.com_Chip_War_-_Chris_Miller\.pdf": "Chip_War.pdf",
    r"c:\\Users\\cfroo\\Downloads\\_OceanofPDF\.com_Investment_Valuation_University_Edition_-_Aswath_Damodaran\.pdf": "Investment_Valuation.pdf",
    r"c:\\Users\\cfroo\\Downloads\\_OceanofPDF\.com_Platform_Revolution_How_Networked_Markets_Are_Transforming_the_Economy--And_How_to_Make_Them_Work_for_You_-_Sangeet_Paul_Choudary\.pdf": "Platform_Revolution.pdf",
    r"c:\\Users\\cfroo\\Downloads\\_OceanofPDF\.com_Lean_Analytics_-_Alistair_Croll_Benjamin_Yoskovitz\.pdf": "Lean_Analytics.pdf",
    r"c:\\Users\\cfroo\\Downloads\\Accenture-2025-10-K\.pdf": "Accenture-2025-10-K.pdf",
    r"c:\\Users\\cfroo\\Downloads\\0001327567-25-000027\.pdf": "Palo-Alto-Networks-2025-10-K.pdf",
    r"c:\\Users\\cfroo\\Downloads\\0505eb02-5a4e-449e-a662-edef3bc70e7b\.pdf": "ServiceNow-2025-10-K.pdf",
    r"c:\\Users\\cfroo\\Downloads\\0001535527-25-000009\.pdf": "CrowdStrike-2025-10-K.pdf",
}

REMOVE_NORMALIZED = {
    "annual recurring revenue",
    "beta",
    "cac",
    "capital structure",
    "contribution margin",
    "fabrication",
    "foundry",
    "intrinsic value",
    "ipo",
    "leverage",
    "economies scale",
    "p e",
    "rpo",
    "wacc",
    "terminal value",
    "relative valuation",
    "enterprise value",
    "paas",
    "platform as service",
    "iaas",
    "infrastructure as service",
    "two sided market",
    "initial public offering",
    "private equity",
    "churn",
    "operating leverage",
    "venture capital",
    "price to earnings",
    "price to sales",
    "network effects",  # merge into network effect
}

REWRITES: dict[str, dict] = {
    "arr": {
        "term": "ARR",
        "short_definition": "Annual recurring revenue — subscription revenue expected to recur each year rather than one-time bookings (Subscribed; Palo Alto/CrowdStrike 10-Ks cite ARR metrics).",
        "notes": "Distinct from total revenue; filing and book sources use ARR for subscription businesses.",
    },
    "artificial intelligence": {
        "short_definition": "AI/ML capabilities embedded in enterprise software, cybersecurity platforms, and IT services delivery; filings discuss AI product roadmaps and infrastructure demand.",
        "notes": "",
    },
    "barriers to entry": {
        "short_definition": "Structural obstacles to new competitors — platform books discuss network effects and switching costs as entry barriers in digital markets.",
        "notes": "",
    },
    "capex": {
        "short_definition": "Capital expenditure; subscription economy sources contrast capex-heavy on-prem installs with opex/subscription cloud models.",
        "notes": "",
    },
    "capital expenditure": {
        "short_definition": "Up-front capital spending on technology assets; cloud shift moves spend from capex to operating/subscription expense.",
        "notes": "",
    },
    "chip design": {
        "short_definition": "Semiconductor design activity; fabless model separates design from fabrication (Chip War).",
        "notes": "",
    },
    "cloud delivered": {
        "term": "cloud-delivered",
        "short_definition": "Security and software delivered via cloud rather than on-premises appliances (Palo Alto, CrowdStrike 10-Ks).",
        "notes": "",
    },
    "cloud infrastructure": {
        "short_definition": "Data centers, networks, and cloud platforms used to deliver SaaS and security services; cited as operational dependency in filings.",
        "notes": "",
    },
    "cloud platform": {
        "short_definition": "Vendor cloud platform for security operations or enterprise workflows (Cortex Cloud, Falcon platform, ServiceNow AI Platform).",
        "notes": "",
    },
    "cloud security": {
        "short_definition": "Security across cloud application lifecycle — CNAPP, cloud-native protection (Palo Alto, CrowdStrike 10-Ks).",
        "notes": "",
    },
    "competitive advantage": {
        "short_definition": "Sustainable differentiation; platform and semiconductor sources discuss scale, ecosystem, and technology moats.",
        "notes": "Generic term; corpus overlap with ER/competition frameworks.",
    },
    "consulting": {
        "short_definition": "Accenture delivers consulting alongside technology and managed services; revenue recognized as services are delivered.",
        "notes": "",
    },
    "cortex": {
        "term": "Cortex",
        "short_definition": "Palo Alto AI-powered security operations platform consolidating SOC and cloud security offerings.",
        "notes": "",
    },
    "credit rating": {
        "short_definition": "Filings cite credit-rating downgrade risk affecting debt costs and financing availability.",
        "notes": "",
    },
    "customer acquisition cost": {
        "short_definition": "Cost to acquire a subscriber/customer; subscription sources link CAC to lifetime value and payback.",
        "notes": "Not the UK Central Arbitration Committee false match.",
    },
    "cybersecurity": {
        "short_definition": "Enterprise security services and products; core business for Palo Alto and CrowdStrike; Accenture/ServiceNow discuss cyber risk programs.",
        "notes": "",
    },
    "data center": {
        "short_definition": "Facilities and infrastructure hosting cloud workloads; semiconductor and platform sources tie data-center buildout to chip demand.",
        "notes": "",
    },
    "dcf": {
        "term": "DCF",
        "short_definition": "Discounted cash flow valuation framework (Investment Valuation); sector valuation overlap.",
        "notes": "",
    },
    "discounted cash flow": {
        "short_definition": "Intrinsic valuation approach discounting expected cash flows (Investment Valuation textbook).",
        "notes": "",
    },
    "dollar based net retention": {
        "term": "dollar-based net retention",
        "short_definition": "CrowdStrike metric comparing ARR from subscription customers year-over-year including expansion and churn.",
        "notes": "",
    },
    "endpoint security": {
        "short_definition": "Endpoint detection/prevention (EDR/XDR) protecting devices and workloads (Palo Alto, CrowdStrike 10-Ks).",
        "notes": "",
    },
    "enterprise software": {
        "short_definition": "ServiceNow positions as AI enterprise software company delivering workflow automation on its platform.",
        "notes": "",
    },
    "euv": {
        "term": "EUV",
        "short_definition": "Extreme ultraviolet lithography equipment critical to advanced semiconductor fabrication (Chip War).",
        "notes": "",
    },
    "fabless": {
        "short_definition": "Chip companies that design semiconductors but outsource manufacturing to foundries (Chip War).",
        "notes": "",
    },
    "firewall": {
        "short_definition": "Next-generation firewalls (NGFW) for on-prem and cloud network security (Palo Alto 10-K).",
        "notes": "",
    },
    "free cash flow": {
        "short_definition": "Cash generated after operating and capital needs; cited in subscription transition examples and filing MD&A.",
        "notes": "",
    },
    "freemium": {
        "short_definition": "Pricing model offering free tier to drive adoption before paid conversion (platform/analytics sources).",
        "notes": "",
    },
    "gpu": {
        "term": "GPU",
        "short_definition": "Graphics processing units used for parallel compute and AI workloads; linked to semiconductor supply chain (Chip War).",
        "notes": "",
    },
    "gross margin": {
        "short_definition": "Revenue minus cost of revenue; filings report product vs services gross margins; subscription businesses often high gross margins.",
        "notes": "",
    },
    "gross retention": {
        "short_definition": "CrowdStrike cites dollar-based gross retention rates post-incident; measures revenue retained from existing customers.",
        "notes": "",
    },
    "hardware": {
        "short_definition": "Physical devices and appliances; Palo Alto sells hardware NGFWs alongside software; Apple/hardware ecosystem thin without Apple 10-K.",
        "notes": "",
    },
    "it service management": {
        "term": "IT Service Management",
        "short_definition": "ITSM workflows (incident, change, service desk) on ServiceNow platform alongside ITOM.",
        "notes": "",
    },
    "it services": {
        "short_definition": "Technology services including implementation, support, and operations; Accenture core revenue line.",
        "notes": "",
    },
    "managed services": {
        "short_definition": "Ongoing outsourced IT/operations contracts; Accenture recognizes managed services revenue over contract life.",
        "notes": "",
    },
    "mergers acquisitions": {
        "term": "mergers and acquisitions",
        "short_definition": "M&A activity cited in filings for platform expansion and cybersecurity consolidation.",
        "notes": "",
    },
    "moat": {
        "short_definition": "Competitive defense metaphor in semiconductor strategy (e.g., Intel x86 architecture moat in Chip War).",
        "notes": "",
    },
    "net retention": {
        "short_definition": "Net revenue retention / dollar-based net retention measuring expansion minus churn on installed base.",
        "notes": "",
    },
    "network effect": {
        "short_definition": "Value increases as more users/participants join a platform; core platform-economics concept (Business of Platforms, Platform Revolution).",
        "notes": "Merged duplicate network-effects row.",
    },
    "next generation firewall": {
        "term": "Next-Generation Firewall",
        "short_definition": "ML-powered NGFWs securing campus, data center, and cloud networks (Palo Alto 10-K).",
        "notes": "",
    },
    "ngfw": {
        "term": "NGFW",
        "short_definition": "Abbreviation for next-generation firewall product line (Palo Alto 10-K).",
        "notes": "",
    },
    "operating margin": {
        "short_definition": "Operating income as percent of revenue; filings and subscription case studies cite margin expansion targets.",
        "notes": "",
    },
    "outsourcing": {
        "short_definition": "Contracting operations to third parties; Accenture as outsource provider; Chip War notes manufacturing outsourcing.",
        "notes": "",
    },
    "platform business": {
        "short_definition": "Business model connecting multiple market sides and enabling ecosystem complements (Business of Platforms).",
        "notes": "",
    },
    "platform ecosystem": {
        "short_definition": "Network of developers, partners, and complements around a core platform (platform strategy sources).",
        "notes": "",
    },
    "prisma": {
        "term": "Prisma",
        "short_definition": "Palo Alto SASE portfolio (Prisma Access, Prisma SD-WAN, Prisma Access Browser).",
        "notes": "",
    },
    "product revenue": {
        "short_definition": "Palo Alto separates product revenue (appliances/components) from subscription and support revenue.",
        "notes": "",
    },
    "professional services revenue": {
        "short_definition": "Implementation and consulting fees alongside subscription revenue (ServiceNow, CrowdStrike 10-Ks).",
        "notes": "",
    },
    "recurring revenue": {
        "short_definition": "Revenue that repeats on a subscription or contract basis; central to SaaS/subscription economy framing (Subscribed).",
        "notes": "",
    },
    "reinvention services": {
        "term": "Reinvention Services",
        "short_definition": "Accenture integrated services unit combining strategy, consulting, technology, operations, and industry solutions.",
        "notes": "",
    },
    "remaining performance obligations": {
        "short_definition": "Contracted revenue not yet recognized — RPO/backlog metric in software filings.",
        "notes": "",
    },
    "research development": {
        "term": "research and development",
        "short_definition": "R&D spend on product innovation; filings disclose R&D as percent of revenue; high in software and semiconductors.",
        "notes": "",
    },
    "revenue growth": {
        "short_definition": "Top-line growth drivers discussed in MD&A — subscriptions, seat expansion, platform adoption.",
        "notes": "",
    },
    "saas": {
        "term": "SaaS",
        "short_definition": "Software-as-a-service delivery model with subscription pricing and cloud hosting.",
        "notes": "",
    },
    "sase": {
        "term": "SASE",
        "short_definition": "Secure access service edge — cloud-delivered network/security convergence (Palo Alto Prisma SASE).",
        "notes": "",
    },
    "security operations": {
        "short_definition": "SOC workflows, threat detection, and response automation (Cortex, Falcon platforms).",
        "notes": "",
    },
    "segment": {
        "short_definition": "Reportable operating segments — Accenture by geography; software vendors by product or region in notes.",
        "notes": "",
    },
    "semiconductor": {
        "short_definition": "Chip industry covering design, fabrication, equipment, and geopolitical supply chain (Chip War primary source).",
        "notes": "",
    },
    "semiconductor equipment": {
        "short_definition": "Tools for wafer fabrication including lithography (Chip War / Sematech discussion).",
        "notes": "",
    },
    "services revenue": {
        "short_definition": "Services portion of revenue mix vs product/subscription (Accenture managed services growth; ServiceNow services line).",
        "notes": "",
    },
    "software as service": {
        "term": "software as a service",
        "short_definition": "Cloud-hosted software sold on subscription rather than perpetual license (Subscribed, Lean Analytics, filings).",
        "notes": "",
    },
    "software licensing": {
        "short_definition": "License models for on-prem and hybrid deployments; Palo Alto discusses licensing in security management context.",
        "notes": "",
    },
    "subscription": {
        "short_definition": "Recurring payment model for software/services; core theme of Subscribed and SaaS filings.",
        "notes": "",
    },
    "subscription revenue": {
        "short_definition": "Revenue from subscription contracts; mix with support revenue fluctuates per Palo Alto/CrowdStrike disclosures.",
        "notes": "",
    },
    "switching costs": {
        "short_definition": "Costs of changing vendors/platforms; raises customer retention in platform markets.",
        "notes": "",
    },
    "systems integrat": {
        "term": "systems integration",
        "short_definition": "Implementing and connecting enterprise systems; Accenture/ServiceNow ecosystem context.",
        "notes": "",
    },
    "technology services": {
        "short_definition": "Accenture technology services alongside consulting and managed services.",
        "notes": "",
    },
    "tsmc": {
        "term": "TSMC",
        "short_definition": "Taiwan Semiconductor Manufacturing Company — leading contract foundry (Chip War).",
        "notes": "",
    },
    "usage based pricing": {
        "term": "usage-based pricing",
        "short_definition": "Pricing tied to consumption meters rather than flat subscription (Subscribed).",
        "notes": "",
    },
    "valuation multiple": {
        "short_definition": "Market valuation ratios (e.g., price/sales) applied to subscription transitions (Subscribed).",
        "notes": "",
    },
    "wafer": {
        "short_definition": "Silicon wafer unit for chip fabrication; capacity measured in wafers-per-month (Chip War).",
        "notes": "",
    },
    "workflow automation": {
        "short_definition": "Automating enterprise workflows on ServiceNow platform; AI-enhanced process orchestration.",
        "notes": "",
    },
    "xdr": {
        "term": "XDR",
        "short_definition": "Extended detection and response across endpoint, network, cloud, and identity data (Palo Alto, CrowdStrike).",
        "notes": "",
    },
}


def neutralize_paths(text: str) -> str:
    out = text
    for pattern, replacement in PATH_MAP.items():
        out = re.sub(pattern, replacement, out, flags=re.I)
    out = re.sub(r"c:\\Users\\cfroo\\Downloads\\", "", out, flags=re.I)
    return out


def clean_concept_inventory() -> tuple[int, int, list[str]]:
    src = DOSSIER / "Concept_Inventory.csv"
    rows_in = list(csv.DictReader(src.open(encoding="utf-8")))
    before = len(rows_in)

    kept: dict[str, dict] = {}
    examples: list[str] = []

    for row in rows_in:
        nt = row["normalized_term"]
        if nt in REMOVE_NORMALIZED:
            examples.append(f"REMOVED: {row['term']} — index/false-positive/debris")
            continue

        if nt in REWRITES:
            rw = REWRITES[nt]
            old_def = row["short_definition"][:60]
            row["term"] = rw.get("term", row["term"])
            row["short_definition"] = rw["short_definition"]
            row["notes"] = rw.get("notes", row.get("notes", ""))
            if old_def != row["short_definition"][:60]:
                examples.append(f"REWRITTEN: {row['term']}")
        else:
            # drop rows with obvious debris definitions
            d = row["short_definition"]
            if re.match(r"^[a-z]{1,3}\b", d) or "CHAPTER 1[67]" in d or "Figure 17" in d:
                examples.append(f"REMOVED: {row['term']} — snippet fragment")
                continue
            if re.match(r"^\d+,\s*\d+", d) and "annual recurring" in d:
                examples.append(f"REMOVED: {row['term']} — index debris")
                continue

        if nt not in kept:
            kept[nt] = row
        else:
            # merge sources
            existing = kept[nt]
            titles = set(existing["source_titles"].split(" | "))
            titles.update(row["source_titles"].split(" | "))
            existing["source_titles"] = " | ".join(sorted(titles))
            locs = existing["source_locations"] + " | " + row["source_locations"]
            existing["source_locations"] = " | ".join(locs.split(" | ")[:10])

    out_rows = sorted(kept.values(), key=lambda r: r["normalized_term"])
    after = len(out_rows)

    with src.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=rows_in[0].keys())
        w.writeheader()
        w.writerows(out_rows)

    return before, after, examples[:20]


def write_chapter_summaries() -> None:
    content = """# Chapter Summaries — sector-information-technology

Compact filing/chapter index for architecture session. Paraphrased context only — no long excerpts.

## The Business of Platforms
Author: Cusumano, Gawer, Yoffie | Pages: 239 | Status: partial

### Chapter 1: Platform Thinking (p.~1)
- Topics: platform definition, two-sided markets, network effects, chicken-and-egg problem
- Context: Introduces platform business model vs traditional pipeline firms.

### Chapter 2: Winner Take All or Most (p.~15)
- Topics: network effects, multi-homing, entry barriers, digital technology drivers
- Context: When platforms concentrate market share.

### Chapter 3: Strategy and Business Models (p.~35)
- Topics: innovation vs transaction vs hybrid platforms, four-step platform build
- Context: Platform strategy and monetization choices.

### Chapter 4: Common Mistakes (p.~55)
- Topics: mispricing, mistrust, mistiming, hubris in platform launches
- Context: Failure patterns in platform competition.

### Chapter 5: Old Dogs and New Tricks (p.~75)
- Topics: incumbents building, buying, or joining platforms
- Context: Legacy firms adapting to platform competition.

### Chapter 6: Double-Edged Swords (p.~95)
- Topics: platform power, antitrust, privacy, labor, self-regulation
- Context: Governance and social costs of platform scale.

### Chapter 7: Looking Forward (p.~115)
- Topics: future platform battlegrounds, AI/cloud competition
- Context: Forward-looking platform industry trends.

## Subscribed
Author: Tzuo & Weisert | Pages: 235 | Status: partial

### Introduction / Part 1: The New Subscription Economy
- Topics: shift from ownership to subscriptions, recurring revenue, ARR
- Context: Subscription business model across industries.

### Chapters 1–4: End of ownership era, retail, media, mobility (p.~10–60)
- Topics: recurring billing, customer relationships, usage-based models
- Context: Sector examples of subscription transition.

### Chapters 5–8: Newspapers, Adobe/PTC fish model, IoT, end of ownership (p.~60–100)
- Topics: capex-to-opex shift, subscription metrics, manufacturing services
- Context: Software and hardware companies adopting subscriptions.

### Part 2: Succeeding in the subscription economy (Ch. 9–12, p.~100+)
- Topics: innovation in beta, marketing/sales for subscriptions, customer success
- Context: Operating model for subscription businesses.

## Chip War
Author: Chris Miller | Pages: 654 | Status: partial

### Part I–II: Cold War chips, invention of the microchip (p.~1–80)
- Topics: semiconductor origins, U.S.–Soviet technology race, chip design
- Context: Historical foundation of semiconductor industry.

### Middle chapters: Fabless model, TSMC, globalization (p.~80–300)
- Topics: fabless design, foundries, wafer fabrication, EUV lithography, supply chain
- Context: Semiconductor manufacturing economics and geopolitics.

### Later chapters: AI, GPUs, data centers, U.S.–China competition (p.~300+)
- Topics: Nvidia, TSMC, export controls, chip war national security
- Context: Modern semiconductor strategic competition.

## Investment Valuation (University Edition)
Author: Damodaran | Pages: 1331 | Status: partial

### Chapters 1–4: Valuation foundations (p.~1–80)
- Topics: intrinsic vs relative valuation, DCF, financial statements, risk
- Context: General valuation toolkit (sector overlap with ER).

### Chapters 17–20: Multiples and sector valuation (p.~400+)
- Topics: revenue multiples, P/E, P/S, sector-specific multiples
- Context: Relative valuation for growth and software firms.

### Chapters 21–25: Financial services, money-losing, young, private, M&A (p.~500+)
- Topics: valuing growth companies, acquisitions
- Context: Life-cycle valuation (partial IT relevance).

## Platform Revolution
Author: Parker, Van Alstyne, Choudary | Pages: 324 | Status: partial

### Chapters 1–3: Platform revolution, network effects, architecture (p.~1–60)
- Topics: platform design, network effects, governance
- Context: Platform strategy complement to Business of Platforms.

### Chapters 4–7: Disruption, monetization, openness, policy (p.~60–150)
- Topics: platform pricing, regulation, ecosystem management
- Context: Operating and policy dimensions of platforms.

## Lean Analytics
Author: Croll & Yoskovitz | Pages: 439 | Status: partial

### Part 1: Stop lying to yourself (Ch. 1–2)
- Topics: metrics discipline, one metric that matters
- Context: Analytics for startups and growth companies.

### Part 2–3: Finding the right metric, lines in the sand (p.~50–200)
- Topics: stage-appropriate KPIs, SaaS metrics
- Context: Subscription/analytics metrics (VC overlap).

### Part 4: Putting lean analytics to work (p.~200+)
- Topics: business-model-specific dashboards
- Context: Operational metrics by company stage.

## Accenture plc Form 10-K (FY2025)
Company: Accenture plc | Pages: 102 | Status: clean

### Item 1: Business (p.~2)
- Topics: Reinvention Services, consulting, managed services, technology services, AI, geographic segments
- Context: IT services leader — $69.7B revenue, three geographic markets, consulting vs managed services mix.

### Item 1A: Risk Factors (p.~11)
- Topics: cybersecurity, AI disruption, talent, macro, client concentration
- Context: Sector-relevant operational and technology risks.

### Item 7: MD&A (p.~31)
- Topics: revenue growth, managed services, investments, margins
- Context: Operating drivers for IT services business.

### Item 8 / Notes: Segment reporting (p.~43+)
- Topics: Americas/EMEA/Asia Pacific segments, contract liabilities
- Context: Geographic and service-line revenue breakdown.

## Palo Alto Networks Form 10-K (FY2025)
Company: Palo Alto Networks | Pages: 260 | Status: clean

### Item 1: Business (p.~4)
- Topics: cybersecurity platform, NGFW, SASE, Prisma, Cortex XDR/SOAR, cloud security, ARR, platformization
- Context: Security platform vendor — network, cloud, and SOC offerings.

### Item 1A: Risk Factors (p.~14)
- Topics: competition, cloud platform security, AI, supply chain, cyber incidents
- Context: Cybersecurity sector risks.

### Item 7: MD&A (p.~42)
- Topics: ARR, RPO, subscription vs product revenue, gross margin, operating expenses
- Context: Subscription security economics.

## ServiceNow Form 10-K (FY2025)
Company: ServiceNow | Pages: 178 | Status: clean

### Item 1: Business (p.~1)
- Topics: ServiceNow AI Platform, workflow automation, ITSM/ITOM, enterprise software, AI governance
- Context: Enterprise workflow platform expanding across departments.

### Item 1A: Risk Factors (p.~22)
- Topics: AI competition, platform security, customer adoption, international expansion
- Context: Enterprise software sector risks.

### Item 7: MD&A (p.~48)
- Topics: subscription revenue, professional services, RPO, operating margin
- Context: SaaS enterprise software operating drivers.

## CrowdStrike Holdings Form 10-K (FY2025)
Company: CrowdStrike | Pages: 148 | Status: clean

### Item 1: Business (p.~4)
- Topics: Falcon platform, endpoint security, cloud security, XDR, subscription model, ARR, net retention
- Context: Cloud-native cybersecurity with unified agent architecture.

### Item 1A: Risk Factors (p.~21)
- Topics: July 19 incident, platform availability, competition, regulatory
- Context: Cybersecurity operational and reputational risks.

### Item 7: MD&A (p.~61)
- Topics: subscription revenue, ARR, dollar-based net retention, gross retention, professional services
- Context: Security subscription unit economics and incident aftermath.
"""
    (DOSSIER / "Chapter_Summaries.md").write_text(content, encoding="utf-8")


def clean_manifest_areas(text: str) -> str:
    """Remove figure/table debris lines from manifest area lists."""
    lines = text.splitlines()
    out = []
    skip_patterns = re.compile(
        r"^(FIGURE|TABLE|TITLE PAGE|COPYRIGHT|DEDICATION|ISBN|CLICK HERE|EMPLOYEES|OPERATING|R&D|SALES GROWTH|PLATFORMS\)|TRANSACTION$|INNOVATION$|PLATFORMS$|G&A)",
        re.I,
    )
    for line in lines:
        if skip_patterns.search(line.strip().lstrip("- ")):
            continue
        out.append(line)
    return "\n".join(out)


def main() -> None:
    before, after, examples = clean_concept_inventory()
    write_chapter_summaries()

    for name in ("Source_Manifest.md", "TOC_Index.md", "Handoff_Note.md"):
        path = DOSSIER / name
        text = neutralize_paths(path.read_text(encoding="utf-8"))
        if name == "Source_Manifest.md":
            text = clean_manifest_areas(text)
        path.write_text(text, encoding="utf-8")

    # Update handoff row count and cleanup note
    hn = (DOSSIER / "Handoff_Note.md").read_text(encoding="utf-8")
    hn = re.sub(
        r"## 5\. Concept inventory row count\n\d+",
        f"## 5. Concept inventory row count\n{after}",
        hn,
    )
    if "## 6d. Cleanup pass" not in hn:
        hn = hn.replace(
            "## 7. Architecture deferral",
            "## 6d. Cleanup pass (2026-07-07)\n"
            "- Concept inventory audited: removed index/OCR false positives and snippet fragments; rewrote definitions as short paraphrases.\n"
            "- Chapter_Summaries.md compacted; long copyrighted excerpts removed.\n"
            "- Local Windows file paths replaced with neutral filenames in committed dossier files.\n"
            "- `raw_extractions/` remains gitignored and uncommitted.\n\n"
            "## 7. Architecture deferral",
        )
    (DOSSIER / "Handoff_Note.md").write_text(hn, encoding="utf-8")

    print(f"concepts: {before} -> {after}")
    for ex in examples:
        print(ex)


if __name__ == "__main__":
    main()
