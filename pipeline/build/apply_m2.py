#!/usr/bin/env python3
"""One-shot Milestone 2 content repair applicator."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

REF_FIXES = {
    "asset-management.z2.3": {"asset-management.z5.7": "asset-management.z5.6"},
    "asset-management.z4.4": {"asset-management.z5.7": "asset-management.z5.6"},
    "asset-management.z5.2": {"asset-management.z5.7": "asset-management.z5.6"},
    "asset-management.z5.4": {
        "asset-management.z5.7": "private-equity.z5.7",
        "asset-management.z5.8": "private-equity.z5.8",
    },
    "investment-banking.z3.13": {"private-equity.z3.20": "private-equity.z3.16"},
    "investment-banking.z3.14": {"private-equity.z3.20": "private-equity.z3.16"},
    "venture-capital.z5.6": {"venture-capital.z5.7": "equity-research.z5.7"},
    "wealth-management.z2.8": {"wealth-management.z5.7": "private-equity.z5.7"},
    "wealth-management.z5.4": {
        "wealth-management.z5.7": "private-equity.z5.7",
        "wealth-management.z5.8": "private-equity.z5.8",
    },
}

HOSTS: dict[str, list[str]] = {
    "private-equity.z1.3": ["G6", "G7", "G23"],
    "private-equity.z1.4": ["G21", "G22"],
    "private-equity.z3.8": ["G24"],
    "private-equity.z3.7": ["G26", "G30"],
    "private-equity.z2.21": ["G29"],
    "private-equity.z3.13": ["G31"],
    "private-equity.z2.7": ["G37", "G46"],
    "private-equity.z2.8": ["G43"],
    "private-credit.z2.5": ["G73"],
    "private-credit.z3.11": ["G74"],
    "investment-banking.z3.7": ["G93"],
    "investment-banking.z2.5": ["G99"],
    "investment-banking.z2.7": ["G101"],
    "hedge-funds.z1.1": ["G107"],
    "hedge-funds.z1.2": ["G108"],
    "hedge-funds.z2.2": ["G109"],
    "hedge-funds.z1.6": ["G110"],
    "hedge-funds.z5.2": ["G112"],
    "hedge-funds.z3.4": ["G113", "G114", "G115"],
    "hedge-funds.z1.5": ["G118"],
    "hedge-funds.z5.4": ["G120"],
    "hedge-funds.z3.3": ["G122"],
    "hedge-funds.z3.5": ["G126"],
    "hedge-funds.z2.6": ["G133"],
    "hedge-funds.z3.1": ["G136"],
    "asset-management.z3.4": ["G142"],
    "asset-management.z3.2": ["G144"],
    "asset-management.z2.10": ["G145", "G146"],
    "asset-management.z5.2": ["G150"],
    "asset-management.z1.5": ["G152", "G153"],
    "wealth-management.z2.3": ["G164"],
    "wealth-management.z3.4": ["G167"],
    "wealth-management.z2.4": ["G170", "G172"],
    "wealth-management.z4.2": ["G171"],
    "wealth-management.z2.5": ["G174"],
}

# Consolidated Part 9 gaps: node_id -> gap entries to ensure present
CONSOLIDATED_GAPS: dict[str, list[dict]] = {
    "equity-research.z1.7": [{
        "kind": "recency",
        "note": "Part 9 #1 — post-MiFID-II research economics (budgets, headcount, survival); no source after 2018 unbundling",
        "needed_source": "current post-MiFID-II research industry source",
    }],
    "equity-research.z5.2": [{
        "kind": "recency",
        "note": "Part 9 #1 — modern sell-side research business model after unbundling",
        "needed_source": None,
    }],
    "equity-research.z5.7": [
        {
            "kind": "recency",
            "note": "Part 9 #1 — current quantitative state of the research business (budgets, pricing, consolidation)",
            "needed_source": None,
        },
        {
            "kind": "recency",
            "note": "Part 9 #2 — AI and alternative data reshaping the research product",
            "needed_source": None,
        },
    ],
    "equity-research.z2.6": [{
        "kind": "recency",
        "note": "Part 9 #2 — AI/alt-data as disruption of the research product",
        "needed_source": None,
    }],
    "equity-research.z1.9": [{
        "kind": "source",
        "note": "Part 9 #3 — securities-regulation frame (Reg AC, Reg FD, MiFID II conflicts); no dedicated securities-law source",
        "needed_source": "securities-law / regulation source",
    }],
    "equity-research.z5.4": [{
        "kind": "source",
        "note": "Part 9 #3 — securities-regulation frame for research independence",
        "needed_source": None,
    }],
    "equity-research.z5.5": [{
        "kind": "source",
        "note": "Part 9 #3 — securities-regulation frame (rules at learner level, not legal practice)",
        "needed_source": None,
    }],
    "venture-capital.z5.6": [{
        "kind": "recency",
        "note": "Part 9 #1 — 2021 venture boom and 2022–24 reset (exit drought, down-round wave); Part 9 #2 — AI as dual thesis and tool",
        "needed_source": "sources published 2023+",
    }],
    "venture-capital.z2.8": [{
        "kind": "recency",
        "note": "Part 9 #2 — AI's dual role in venture (investment thesis and firm operations)",
        "needed_source": None,
    }],
    "venture-capital.z5.2": [{
        "kind": "recency",
        "note": "Part 9 #3 — venture secondary market growth (fund and direct stakes) as liquidity option",
        "needed_source": None,
    }],
    "venture-capital.z3.12": [{
        "kind": "source",
        "note": "Part 9 #4 — regulatory/legal depth (409A, exemptions, CFIUS, crypto financing) beyond accredited-investor basics",
        "needed_source": "venture securities/regulatory source",
    }],
    "real-estate.z4.6": [{
        "kind": "recency",
        "note": "Part 9 #1 — post-2022 interest-rate shock, cap-rate expansion, refinancing wall, distressed opportunities",
        "needed_source": None,
    }],
    "real-estate.z4.7": [{
        "kind": "recency",
        "note": "Part 9 #1 — CRE value reset and distress cycle detail post-2022",
        "needed_source": None,
    }],
    "real-estate.z2.2": [{
        "kind": "recency",
        "note": "Part 9 #2 — office-sector distress and work-from-home structural shift",
        "needed_source": None,
    }],
    "real-estate.z2.3": [{
        "kind": "recency",
        "note": "Part 9 #3 — data-center and AI demand wave (scale, power constraints, hyperscale leases)",
        "needed_source": None,
    }],
    "real-estate.z5.6": [
        {
            "kind": "recency",
            "note": "Part 9 #2 — office distress; #3 — data-center/AI demand; #4 — proptech/AI in operations; #5 — climate-risk repricing",
            "needed_source": None,
        },
    ],
    "real-estate.z3.10": [{
        "kind": "recency",
        "note": "Part 9 #5 — climate-risk repricing (insurance, decarbonization capex, ESG mandates)",
        "needed_source": None,
    }],
    "real-estate.z3.8": [{
        "kind": "recency",
        "note": "Part 9 #6 — post-2022 CMBS dislocation (spreads, special servicer volumes, office-backed tranche distress)",
        "needed_source": None,
    }],
}


def gap_key(g: dict) -> str:
    return f"{g['kind']}:{g['note'][:80]}"


def merge_gaps(existing: list, additions: list) -> list:
    seen = {gap_key(g) for g in existing}
    out = list(existing)
    for g in additions:
        if gap_key(g) not in seen:
            out.append(g)
            seen.add(gap_key(g))
    return out


def load_all_nodes():
    by_file = {}
    by_id = {}
    for mdir in sorted((ROOT / "content/modules").iterdir()):
        if not mdir.is_dir():
            continue
        for zfile in sorted((mdir / "zones").glob("z*.json")):
            nodes = json.loads(zfile.read_text(encoding="utf-8"))
            by_file[zfile] = nodes
            for n in nodes:
                by_id[n["id"]] = n
    return by_file, by_id


def save_nodes(by_file):
    for zfile, nodes in by_file.items():
        zfile.write_text(json.dumps(nodes, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def apply_ref_fixes(by_id):
    for nid, mapping in REF_FIXES.items():
        n = by_id[nid]
        for c in n["connects_to"]:
            if c["ref"] in mapping:
                c["ref"] = mapping[c["ref"]]


def apply_hosts(by_id):
    for nid, gids in HOSTS.items():
        n = by_id[nid]
        existing = n.get("hosts_globals") or []
        merged = sorted(set(existing + gids), key=lambda x: int(x[1:]))
        n["hosts_globals"] = merged


def apply_gaps(by_id):
    for nid, gaps in CONSOLIDATED_GAPS.items():
        n = by_id[nid]
        n["gaps"] = merge_gaps(n.get("gaps") or [], gaps)


def apply_ipo_disambiguation():
    path = ROOT / "content/glossary/globals.json"
    globals_ = json.loads(path.read_text(encoding="utf-8"))
    for g in globals_:
        if g["id"] == "G53":
            g["disambiguate_with"] = sorted(set(g.get("disambiguate_with", []) + ["G102"]))
        if g["id"] == "G102":
            g["disambiguate_with"] = sorted(set(g.get("disambiguate_with", []) + ["G53"]))
    path.write_text(json.dumps(globals_, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main():
    by_file, by_id = load_all_nodes()
    apply_ref_fixes(by_id)
    apply_hosts(by_id)
    apply_gaps(by_id)
    save_nodes(by_file)
    apply_ipo_disambiguation()
    print("Milestone 2 content repairs applied.")


if __name__ == "__main__":
    main()
