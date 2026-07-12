#!/usr/bin/env python3
"""
Runs check families over content/:
  1. schema        — every JSON object conforms to /schemas (jsonschema if
                     installed, otherwise a built-in structural check)
  2. ids           — G-number contiguity from G1, no duplicate G-numbers,
                     no duplicate node IDs, node ordinals contiguous per zone
  3. references    — every connects_to ref and global home resolves to a real
                     node/global (no dangling edges)
  4. duplicates    — near-duplicate global terms (normalized term + alias
                     collision; V0 is string-based, embeddings slot in later
                     behind the same check interface)
  5. required      — quick_definition and explainer_covers non-empty; every
                     tag=='global' node has a global_id; every global's home
                     module actually contains a node hosting it (warning)
  6. graph         — self-edges, orphan nodes, low-reference globals (warnings)
  7. module        — five-zone structure, new-global numbering, by_module presence
  8. lessons       — lesson/path/assessment schemas and V-1…V-13 integrity
                     (vacuous pass if those directories are absent)

Exit code 0 = pass (warnings allowed), 1 = errors found.
Usage: python pipeline/validate/validate.py [--repo-root PATH] [--strict]
"""
import argparse
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from checks.graph_checks import check_graph
from checks.lesson_checks import check_lessons
from checks.new_module_checks import check_new_modules
from lib.module_utils import is_draft

try:
    import jsonschema
    HAVE_JSONSCHEMA = True
except ImportError:
    HAVE_JSONSCHEMA = False


def load_content(root: Path):
    globals_ = json.loads((root / "content/glossary/globals.json").read_text(encoding="utf-8"))
    modules, nodes, draft_slugs = {}, [], set()
    for mdir in sorted((root / "content/modules").iterdir()):
        if not mdir.is_dir():
            continue
        mod = json.loads((mdir / "module.json").read_text(encoding="utf-8"))
        if is_draft(mod):
            draft_slugs.add(mdir.name)
            continue
        modules[mdir.name] = mod
        for zfile in sorted((mdir / "zones").glob("z*.json")):
            nodes.extend(json.loads(zfile.read_text(encoding="utf-8")))
    return globals_, modules, nodes, draft_slugs


def norm_term(t: str) -> str:
    t = unicodedata.normalize("NFKD", t.lower())
    t = re.sub(r"\(.*?\)", " ", t)          # drop parentheticals
    t = re.sub(r"[^a-z0-9 ]", " ", t)
    t = re.sub(r"\b(the|a|an|of|and)\b", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def check_schema(root, globals_, modules, nodes, errors, warnings):
    if not HAVE_JSONSCHEMA:
        warnings.append("jsonschema not installed — running structural checks only "
                        "(pip install jsonschema for full validation)")
        for g in globals_:
            for f in ("id", "term", "quick_definition", "home_module"):
                if not g.get(f):
                    errors.append(f"[schema] global {g.get('id','?')} missing {f}")
        for n in nodes:
            for f in ("id", "module", "zone", "ordinal", "title", "tag"):
                if n.get(f) in (None, ""):
                    errors.append(f"[schema] node {n.get('id','?')} missing {f}")
        return
    schemas = {p.stem: json.loads(p.read_text(encoding="utf-8"))
               for p in (root / "schemas").glob("*.schema.json")}
    for g in globals_:
        for e in jsonschema.Draft7Validator(schemas["global.schema"]).iter_errors(g):
            errors.append(f"[schema] global {g.get('id','?')}: {e.message}")
    for n in nodes:
        for e in jsonschema.Draft7Validator(schemas["node.schema"]).iter_errors(n):
            errors.append(f"[schema] node {n.get('id','?')}: {e.message}")
    for m in modules.values():
        for e in jsonschema.Draft7Validator(schemas["module.schema"]).iter_errors(m):
            errors.append(f"[schema] module {m.get('slug','?')}: {e.message}")


def check_ids(globals_, nodes, errors, warnings):
    gnums = sorted(int(g["id"][1:]) for g in globals_)
    dupes = [f"G{n}" for n, c in Counter(gnums).items() if c > 1]
    if dupes:
        errors.append(f"[ids] duplicate global IDs: {dupes}")
    expected = list(range(1, len(set(gnums)) + 1))
    if sorted(set(gnums)) != expected:
        missing = sorted(set(expected) - set(gnums))
        extra = sorted(set(gnums) - set(expected))
        errors.append(f"[ids] G-numbering not contiguous from G1 — missing {missing[:10]}, unexpected {extra[:10]}")
    node_ids = [n["id"] for n in nodes]
    ndupes = [i for i, c in Counter(node_ids).items() if c > 1]
    if ndupes:
        errors.append(f"[ids] duplicate node IDs: {ndupes}")
    by_zone = defaultdict(list)
    for n in nodes:
        by_zone[(n["module"], n["zone"])].append(n["ordinal"])
    for (mod, z), ords in sorted(by_zone.items()):
        want = list(range(1, len(ords) + 1))
        if sorted(ords) != want:
            warnings.append(f"[ids] {mod} zone {z}: ordinals {sorted(ords)} not contiguous 1..{len(ords)}")


def check_references(globals_, nodes, errors, warnings):
    gid_set = {g["id"] for g in globals_}
    nid_set = {n["id"] for n in nodes}
    for n in nodes:
        for r in n.get("connects_to", []):
            ref = r["ref"]
            if ref.startswith("G"):
                if ref not in gid_set:
                    errors.append(f"[refs] {n['id']} → dangling global {ref}")
            elif ref not in nid_set:
                errors.append(f"[refs] {n['id']} → dangling node {ref}")
        if n.get("global_id") and n["global_id"] not in gid_set:
            errors.append(f"[refs] {n['id']} claims home of nonexistent {n['global_id']}")


def check_duplicates(globals_, errors, warnings):
    gmap = {g["id"]: g for g in globals_}
    by_norm = defaultdict(list)
    for g in globals_:
        by_norm[norm_term(g["term"])].append(g["id"])
        for a in g.get("aliases", []):
            key = norm_term(a)
            if key:
                by_norm[key].append(g["id"])
    for term, ids in sorted(by_norm.items()):
        uniq = sorted(set(ids), key=lambda x: int(x[1:]))
        if len(uniq) > 1:
            if all(
                other in gmap[gid].get("disambiguate_with", [])
                for gid in uniq
                for other in uniq
                if other != gid
            ):
                continue
            warnings.append(f"[dupes] term collision '{term}': {uniq} — confirm intentional or merge")


def check_required(globals_, nodes, errors, warnings, draft_slugs: set[str] | frozenset[str] = frozenset()):
    home_hosts = {n["global_id"] for n in nodes if n.get("global_id")}
    for n in nodes:
        for gid in n.get("hosts_globals", []):
            home_hosts.add(gid)
    for n in nodes:
        if not n.get("quick_definition"):
            errors.append(f"[required] {n['id']} missing quick_definition")
        if not n.get("explainer_covers"):
            errors.append(f"[required] {n['id']} missing explainer_covers")
        if n.get("tag") == "global" and not n.get("global_id"):
            errors.append(f"[required] {n['id']} tagged global but has no global_id")
    for g in globals_:
        if g.get("contributed_by") in draft_slugs:
            continue
        if g["id"] not in home_hosts:
            warnings.append(f"[required] {g['id']} '{g['term']}' has no hosting zone node "
                            f"(home explainer not yet mapped to a node)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=str(Path(__file__).resolve().parents[2]))
    ap.add_argument("--strict", action="store_true", help="treat warnings as errors")
    args = ap.parse_args()
    root = Path(args.repo_root)

    globals_, modules, nodes, draft_slugs = load_content(root)
    errors: list[str] = []
    warnings: list[str] = []

    check_schema(root, globals_, modules, nodes, errors, warnings)
    check_ids(globals_, nodes, errors, warnings)
    check_references(globals_, nodes, errors, warnings)
    check_duplicates(globals_, errors, warnings)
    check_required(globals_, nodes, errors, warnings, draft_slugs)
    check_new_modules(root, globals_, modules, nodes, errors, warnings)
    check_lessons(root, globals_, modules, nodes, errors, warnings)
    if not args.strict:
        check_graph(root, nodes, globals_, warnings)

    lessons_dir = root / "content/lessons"
    paths_dir = root / "content/paths"
    assessments_dir = root / "content/assessments"
    n_lessons = len(list(lessons_dir.glob("*.json"))) if lessons_dir.is_dir() else 0
    n_paths = len(list(paths_dir.glob("*.json"))) if paths_dir.is_dir() else 0
    n_assess = (
        len(list(assessments_dir.glob("*.items.json"))) if assessments_dir.is_dir() else 0
    )
    lesson_note = (
        f", {n_lessons} lessons, {n_paths} paths, {n_assess} assessment files"
        if (lessons_dir.is_dir() or paths_dir.is_dir() or assessments_dir.is_dir())
        else " (no lesson layer)"
    )

    print(f"content: {len(globals_)} globals, {len(modules)} modules, {len(nodes)} zone nodes{lesson_note}")
    print(f"result: {len(errors)} errors, {len(warnings)} warnings\n")
    for e in errors:
        print(f"ERROR   {e}")
    for w in warnings:
        print(f"warning {w}")
    return 1 if errors or (args.strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
