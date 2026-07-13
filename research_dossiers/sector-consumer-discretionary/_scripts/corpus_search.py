#!/usr/bin/env python3
"""Corpus inheritance search for CD dossier candidate concepts.

Usage: python corpus_search.py
Writes 04_INHERITANCE_LEDGER.md (partial table) and _inheritance_raw.json.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
DOSSIER = Path(__file__).resolve().parents[1]
GLOSSARY = REPO / "content" / "glossary" / "globals.json"
MODULES = REPO / "content" / "modules"

# Candidate concepts: (canonical, search patterns as regexes, notes)
CANDIDATES = [
    ("Amazon flywheel", [r"\bflywheel\b"], "Stone"),
    ("negative operating cycle / working capital", [r"negative operating cycle", r"cash conversion cycle", r"working capital"], "Stone/retail WC"),
    ("marketplace / third-party seller", [r"\bmarketplace\b", r"third[- ]party seller", r"\b3P\b"], "Stone/Amazon 10-K"),
    ("take rate", [r"\btake rate\b"], "Stephens/marketplace"),
    ("fulfillment / fulfillment network", [r"\bfulfillment\b"], "Stone/Amazon"),
    ("Fulfillment by Amazon (FBA)", [r"\bFBA\b", r"Fulfillment by Amazon"], "Stone"),
    ("Amazon Prime / membership shipping", [r"\bPrime\b", r"membership (program|shipping)"], "Stone/Amazon"),
    ("subscription (commerce / Prime)", [r"\bsubscription\b"], "Amazon/Stephens — collide with IT/PC"),
    ("network effects (retail marketplace)", [r"network effects?"], "Stone/eBay contrast"),
    ("Get Big Fast / scale-first retail", [r"Get Big Fast", r"scale[- ]first"], "Stone"),
    ("everyday low prices (EDLP)", [r"everyday low price", r"\bEDLP\b"], "Stone/Costco"),
    ("trade-up / trading up", [r"trad(e|ing)[- ]up", r"\btrading up\b"], "Silverstein"),
    ("trade-down / trading down", [r"trad(e|ing)[- ]down", r"\btrading down\b"], "Silverstein"),
    ("New Luxury / premiumization", [r"New Luxury", r"\bpremiumi[sz]ation\b", r"masstige"], "Silverstein"),
    ("death in the middle", [r"death in the middle", r"middle[- ]market polar"], "Silverstein"),
    ("accessible superpremium", [r"accessible superpremium"], "Silverstein"),
    ("masstige", [r"\bmasstige\b"], "Silverstein"),
    ("benefit ladder (technical/functional/emotional)", [r"benefit ladder", r"ladder of benefits"], "Silverstein"),
    ("rocketing (selective trade-up)", [r"\brocketing\b"], "Silverstein"),
    ("apostles / brand apostles", [r"\bapostles?\b"], "Silverstein — careful false positives"),
    ("omnichannel", [r"\bomnichannel\b", r"omni[- ]channel"], "Stephens"),
    ("comparable store sales / comps", [r"comparable store sales", r"same[- ]store sales", r"\bcomps\b"], "Nike/Starbucks/ER — collide G88"),
    ("traffic / ticket decomposition", [r"comparable transactions", r"average ticket", r"traffic.{0,20}ticket"], "Starbucks"),
    ("DTC / direct-to-consumer", [r"\bDTC\b", r"direct[- ]to[- ]consumer", r"NIKE Direct"], "Nike"),
    ("wholesale vs direct channel mix", [r"\bwholesale\b"], "Nike"),
    ("gross margin (retail)", [r"gross margin"], "Nike/retail — collide margin senses"),
    ("inventory / inventory turns", [r"\binventor(y|ies)\b", r"inventory turn"], "Nike/IB WC"),
    ("inventory days", [r"inventory days", r"days of inventory"], "Nike"),
    ("systemwide sales", [r"system[- ]?wide", r"systemwide"], "Starbucks/franchise"),
    ("company-operated vs franchised/licensed", [r"company[- ]operated", r"franchised", r"licensed stores"], "Starbucks/Marriott"),
    ("restaurant-level margin", [r"restaurant[- ]level"], "restaurants"),
    ("RevPAR", [r"\bRevPAR\b", r"revenue per available room"], "Marriott/RE"),
    ("ADR (average daily rate)", [r"\bADR\b", r"average daily rate"], "Marriott"),
    ("occupancy (hotels)", [r"\boccupancy\b"], "Marriott/RE"),
    ("asset-light fee model (hotels)", [r"asset[- ]light", r"management fees?", r"franchise fees?"], "Marriott"),
    ("incentive management fees", [r"incentive management"], "Marriott"),
    ("gross fee revenues / take-rate lodging", [r"gross fee revenues?", r"net fee revenues?"], "Marriott"),
    ("heterogeneous homogeneity / category blur", [r"heterogeneous homogeneity", r"category blur"], "Moon"),
    ("reverse positioning / reverse brand", [r"reverse (positioning|brand)"], "Moon"),
    ("breakaway brand", [r"breakaway brand"], "Moon"),
    ("hostile brand", [r"hostile brand"], "Moon"),
    ("competitive herd / differentiation", [r"competitive herd", r"\bdifferentiat"], "Moon"),
    ("brand / brand equity", [r"\bbrand equity\b", r"\bbrand\b"], "Moon/Silverstein — huge; sample"),
    ("moat / durable competitive advantage", [r"\bmoat\b", r"durable competitive advantage"], "backlog §G16"),
    ("margin (retail gross/op)", [r"\bmargin\b"], "multi-sense"),
    ("churn / retention (commerce)", [r"\bchurn\b", r"\bretention\b"], "collide WM/IT"),
    ("e-commerce / online retail", [r"e[- ]commerce", r"online (retail|store)"], "Stone/Stephens"),
    ("platform (retail marketplace vs IT)", [r"\bplatform\b"], "Amazon boundary"),
    ("AWS / cloud (Amazon segment)", [r"\bAWS\b", r"Amazon Web Services"], "Amazon/IT seam"),
    ("advertising services (retail media)", [r"advertising services", r"retail media", r"sponsored ads"], "Amazon"),
    ("fulfillment cost / shipping cost", [r"shipping costs?", r"fulfillment costs?"], "Amazon"),
    ("experiences per square foot", [r"experiences per square", r"sales per click"], "Stephens"),
    ("retail archetype (Stephens ten)", [r"retail archetype"], "Stephens"),
    ("New Retail / unified commerce (Alibaba)", [r"New Retail", r"unified commerce"], "Stephens"),
    ("mall / shopping center economics", [r"\bmall\b", r"shopping center"], "Stephens/RE"),
    ("consumer spending / consumer cycle", [r"consumer spending", r"consumer confidence", r"consumer cycle"], "macro"),
    ("consumer ABS / retail credit", [r"consumer ABS", r"credit card ABS", r"retail credit"], "FI"),
    ("consumer LBO", [r"consumer.{0,30}LBO", r"retail.{0,20}buyout"], "PE"),
    ("direct sales vs dealer franchise (auto)", [r"dealer franchise", r"direct[- ]sales", r"franchise laws?"], "Ludicrous"),
    ("vertical integration (auto/OEM)", [r"vertical(ly)? integrat"], "Ludicrous"),
    ("EV cost structure / battery cost", [r"battery cost", r"\bEV\b", r"electric vehicle"], "Ludicrous"),
    ("gigafactory / manufacturing scale (auto)", [r"\bgigafactory\b", r"production hell"], "Ludicrous"),
    ("autopilot / autonomy economics", [r"\bautopilot\b", r"Full Self[- ]Driving", r"\bFSD\b"], "Ludicrous"),
    ("sector frameworks hub (ER z2.3)", [r"same[- ]store sales", r"sector frameworks?"], "ER door"),
]


def load_globals():
    data = json.loads(GLOSSARY.read_text(encoding="utf-8"))
    entries = data if isinstance(data, list) else data.get("globals") or data.get("entries") or []
    out = []
    for e in entries:
        if not isinstance(e, dict):
            continue
        gid = e.get("id") or e.get("g_id") or e.get("global_id")
        term = e.get("term") or e.get("name") or ""
        aliases = e.get("aliases") or e.get("aka") or []
        if isinstance(aliases, str):
            aliases = [aliases]
        definition = e.get("quick_definition") or e.get("definition") or e.get("short_definition") or ""
        home = f"{e.get('home_module','')}.{e.get('home_zone','')}"
        out.append({"id": gid, "term": term, "aliases": aliases, "definition": definition, "home": home, "raw": e})
    return out


def iter_nodes():
    for path in MODULES.rglob("*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        nodes = []
        if isinstance(data, dict) and isinstance(data.get("nodes"), list):
            nodes = data["nodes"]
        elif isinstance(data, list):
            nodes = data
        for n in nodes:
            if not isinstance(n, dict):
                continue
            nid = n.get("id")
            if not nid:
                continue
            blobs = [
                n.get("title") or "",
                n.get("quick_definition") or "",
                n.get("connects_to_raw") or "",
                " ".join(n.get("explainer_covers") or []) if isinstance(n.get("explainer_covers"), list) else str(n.get("explainer_covers") or ""),
            ]
            # connects_to notes
            for c in n.get("connects_to") or []:
                if isinstance(c, dict):
                    blobs.append(str(c.get("note") or ""))
                    blobs.append(str(c.get("ref") or ""))
            text = "\n".join(blobs)
            yield nid, text, n


def search_patterns(text: str, patterns: list[str]) -> bool:
    for pat in patterns:
        if re.search(pat, text, re.I | re.S):
            return True
    return False


def main():
    globals_ = load_globals()
    nodes = list(iter_nodes())
    print(f"globals={len(globals_)} nodes={len(nodes)}")

    results = []
    for concept, patterns, note in CANDIDATES:
        # glossary hits
        g_hits = []
        for g in globals_:
            blob = " ".join([g["term"], " ".join(map(str, g["aliases"])), g["definition"], str(g["home"])])
            if search_patterns(blob, patterns):
                g_hits.append(g)
        # node hits
        n_hits = []
        for nid, text, n in nodes:
            if search_patterns(text, patterns):
                n_hits.append(nid)

        # classify
        already_homed = []
        for g in g_hits:
            # if term/alias strongly matches concept word, treat as possible home
            already_homed.append(
                {
                    "id": g["id"],
                    "term": g["term"],
                    "home": g.get("home") or g["raw"].get("module") or g["raw"].get("home_module"),
                    "definition_snip": (g["definition"] or "")[:180],
                }
            )

        # Heuristic verdict
        if already_homed and any(
            re.search(r"\b" + re.escape(concept.split()[0]) + r"\b", (h["term"] or ""), re.I) for h in already_homed
        ):
            verdict = "Already homed (candidate — verify meaning)"
        elif n_hits and not already_homed:
            verdict = "Mentioned but unhomed"
        elif n_hits and already_homed:
            verdict = "Mentioned; glossary string-hit exists — verify if true home or collision"
        elif not n_hits and not already_homed:
            verdict = "Absent — genuine mint candidate"
        else:
            verdict = "Glossary-only string-hit — verify"

        results.append(
            {
                "concept": concept,
                "note": note,
                "patterns": patterns,
                "globals": already_homed,
                "nodes": sorted(set(n_hits)),
                "n_nodes": len(set(n_hits)),
                "verdict": verdict,
            }
        )
        print(f"{concept[:40]:40} nodes={len(set(n_hits)):3} globals={len(already_homed):2} | {verdict}")

    (DOSSIER / "raw_extractions" / "_inheritance_raw.json").write_text(
        json.dumps(results, indent=2), encoding="utf-8"
    )

    # counts
    homed = sum(1 for r in results if r["verdict"].startswith("Already homed"))
    unhomed = sum(1 for r in results if "unhomed" in r["verdict"].lower() and "Mentioned but" in r["verdict"])
    mixed = sum(1 for r in results if "verify" in r["verdict"].lower())
    absent = sum(1 for r in results if r["verdict"].startswith("Absent"))
    print("SUMMARY", {"already_homed_heuristic": homed, "mentioned_unhomed": unhomed, "needs_verify": mixed, "absent": absent})


if __name__ == "__main__":
    main()
