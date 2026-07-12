"""Lesson / path / assessment validation (presentation layer — ADR-004).

Implements V-1 … V-13 from docs/P0_SCHEMAS_VALIDATORS_EVENTS.md.
Absent content/lessons|paths|assessments directories are a vacuous pass.
All failures are errors.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

try:
    import jsonschema
    HAVE_JSONSCHEMA = True
except ImportError:
    HAVE_JSONSCHEMA = False

GLOBAL_REF = re.compile(r"^G[1-9][0-9]*$")
NODE_REF = re.compile(r"^[a-z0-9-]+\.z[1-5]\.[0-9]+$")
GRAPH_REF = re.compile(r"^(G[1-9][0-9]*|[a-z0-9-]+\.z[1-5]\.[0-9]+)$")
OPTION_IDS = ("a", "b", "c", "d")


def _layer2_dirs(root: Path) -> tuple[Path, Path, Path]:
    return (
        root / "content" / "lessons",
        root / "content" / "paths",
        root / "content" / "assessments",
    )


def _any_layer2_present(root: Path) -> bool:
    lessons, paths, assessments = _layer2_dirs(root)
    return lessons.is_dir() or paths.is_dir() or assessments.is_dir()


def _load_json_files(directory: Path, pattern: str) -> list[tuple[Path, dict]]:
    if not directory.is_dir():
        return []
    out: list[tuple[Path, dict]] = []
    for path in sorted(directory.glob(pattern)):
        if not path.is_file():
            continue
        try:
            out.append((path, json.loads(path.read_text(encoding="utf-8"))))
        except json.JSONDecodeError as exc:
            # Surface as a structural error later via schema path; stash empty
            out.append((path, {"__parse_error__": str(exc)}))
    return out


def _load_layer2(root: Path):
    lessons_dir, paths_dir, assessments_dir = _layer2_dirs(root)
    lessons = _load_json_files(lessons_dir, "*.json")
    paths = _load_json_files(paths_dir, "*.json")
    assessments = _load_json_files(assessments_dir, "*.items.json")
    return lessons, paths, assessments


def _is_global(ref: str) -> bool:
    return bool(GLOBAL_REF.match(ref))


def _is_node(ref: str) -> bool:
    return bool(NODE_REF.match(ref))


def check_lessons(
    root: Path,
    globals_: list[dict],
    modules: dict,
    nodes: list[dict],
    errors: list[str],
    warnings: list[str],
) -> None:
    """Run V-1 … V-13. Vacuous pass when no layer-2 directories exist."""
    del modules, warnings  # unused; signature matches sibling checkers
    if not _any_layer2_present(root):
        return

    lessons, paths, assessments = _load_layer2(root)
    gid_set = {g["id"] for g in globals_}
    nid_set = {n["id"] for n in nodes}
    node_by_id = {n["id"]: n for n in nodes}
    global_by_id = {g["id"]: g for g in globals_}

    # Parse errors first
    for path, obj in lessons + paths + assessments:
        if "__parse_error__" in obj:
            errors.append(f"[lesson V-1] {path.relative_to(root)} JSON parse error: {obj['__parse_error__']}")

    lesson_schema_path = root / "schemas" / "lesson.schema.json"
    path_schema_path = root / "schemas" / "path.schema.json"
    assessment_schema_path = root / "schemas" / "assessment.schema.json"

    # --- V-1 schema ---
    if HAVE_JSONSCHEMA:
        try:
            lesson_schema = json.loads(lesson_schema_path.read_text(encoding="utf-8"))
            path_schema = json.loads(path_schema_path.read_text(encoding="utf-8"))
            assessment_schema = json.loads(assessment_schema_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"[lesson V-1] cannot load layer-2 schemas: {exc}")
            return

        validator_l = jsonschema.Draft7Validator(lesson_schema)
        validator_p = jsonschema.Draft7Validator(path_schema)
        validator_a = jsonschema.Draft7Validator(assessment_schema)

        for path, obj in lessons:
            if "__parse_error__" in obj:
                continue
            for err in sorted(validator_l.iter_errors(obj), key=lambda e: list(e.path)):
                loc = "/".join(str(p) for p in err.path) or "(root)"
                errors.append(f"[lesson V-1] {path.name} @ {loc}: {err.message}")

        for path, obj in paths:
            if "__parse_error__" in obj:
                continue
            for err in sorted(validator_p.iter_errors(obj), key=lambda e: list(e.path)):
                loc = "/".join(str(p) for p in err.path) or "(root)"
                errors.append(f"[lesson V-1] {path.name} @ {loc}: {err.message}")

        for path, obj in assessments:
            if "__parse_error__" in obj:
                continue
            for err in sorted(validator_a.iter_errors(obj), key=lambda e: list(e.path)):
                loc = "/".join(str(p) for p in err.path) or "(root)"
                errors.append(f"[lesson V-1] {path.name} @ {loc}: {err.message}")
    else:
        errors.append(
            "[lesson V-1] jsonschema not installed — cannot validate lesson/path/assessment schemas"
        )

    # Index usable objects (skip parse failures)
    lesson_objs = [(p, o) for p, o in lessons if "__parse_error__" not in o]
    path_objs = [(p, o) for p, o in paths if "__parse_error__" not in o]
    assessment_objs = [(p, o) for p, o in assessments if "__parse_error__" not in o]

    lessons_by_id: dict[str, dict] = {}
    assessments_by_lesson: dict[str, tuple[Path, dict]] = {}
    items_by_id: dict[str, dict] = {}
    item_home_lesson: dict[str, str] = {}

    # --- V-2 filename ↔ ID ---
    for path, obj in lesson_objs:
        lid = obj.get("id")
        expected = path.stem
        if lid != expected:
            errors.append(
                f"[lesson V-2] {path.name}: filename stem '{expected}' != id '{lid}'"
            )
        if isinstance(lid, str):
            lessons_by_id.setdefault(lid, obj)

    for path, obj in path_objs:
        pid = obj.get("id")
        expected = path.stem
        if pid != expected:
            errors.append(
                f"[lesson V-2] {path.name}: filename stem '{expected}' != id '{pid}'"
            )

    for path, obj in assessment_objs:
        lesson_field = obj.get("lesson")
        # {lesson-id}.items.json
        if not path.name.endswith(".items.json"):
            errors.append(f"[lesson V-2] {path.name}: expected '*.items.json' filename")
            continue
        expected_lesson = path.name[: -len(".items.json")]
        if lesson_field != expected_lesson:
            errors.append(
                f"[lesson V-2] {path.name}: filename lesson '{expected_lesson}' "
                f"!= lesson field '{lesson_field}'"
            )
        if isinstance(lesson_field, str) and lesson_field not in lessons_by_id:
            errors.append(
                f"[lesson V-2] {path.name}: lesson '{lesson_field}' does not exist"
            )
        if isinstance(lesson_field, str):
            assessments_by_lesson[lesson_field] = (path, obj)
            for item in obj.get("items") or []:
                iid = item.get("id")
                if isinstance(iid, str):
                    items_by_id[iid] = item
                    item_home_lesson[iid] = lesson_field

    # --- V-3 uniqueness ---
    lesson_ids = [o.get("id") for _, o in lesson_objs]
    for lid, count in _counts(lesson_ids).items():
        if lid is None:
            continue
        if count > 1:
            errors.append(f"[lesson V-3] duplicate lesson id '{lid}' ({count} files)")

    path_ids = [o.get("id") for _, o in path_objs]
    for pid, count in _counts(path_ids).items():
        if pid is None:
            continue
        if count > 1:
            errors.append(f"[lesson V-3] duplicate path id '{pid}' ({count} files)")

    all_item_ids: list[str] = []
    for _, obj in assessment_objs:
        for item in obj.get("items") or []:
            iid = item.get("id")
            if isinstance(iid, str):
                all_item_ids.append(iid)
    for iid, count in _counts(all_item_ids).items():
        if count > 1:
            errors.append(
                f"[lesson V-3] duplicate assessment item id '{iid}' across assessments ({count})"
            )

    # --- V-4 reference resolution + draws_on conditional invariant ---
    for path, obj in lesson_objs:
        lid = obj.get("id", path.name)
        teaches = obj.get("teaches") or []
        draws_on = obj.get("draws_on") or []
        connects = obj.get("connects") or []

        for ref in teaches:
            if not isinstance(ref, str) or not GRAPH_REF.match(ref):
                continue  # schema catches shape
            if _is_global(ref) and ref not in gid_set:
                errors.append(f"[lesson V-4] {lid}: teaches dangling global '{ref}'")
            elif _is_node(ref) and ref not in nid_set:
                errors.append(f"[lesson V-4] {lid}: teaches dangling node '{ref}'")

        for ref in draws_on:
            if not isinstance(ref, str):
                continue
            if ref not in nid_set:
                errors.append(f"[lesson V-4] {lid}: draws_on dangling node '{ref}'")

        for ref in connects:
            if not isinstance(ref, str):
                continue
            if ref not in gid_set:
                errors.append(f"[lesson V-4] {lid}: connects dangling global '{ref}'")

        # Conditional invariant: empty draws_on only if every teaches entry is a node
        if isinstance(teaches, list) and teaches:
            any_global = any(isinstance(t, str) and _is_global(t) for t in teaches)
            if any_global and not draws_on:
                errors.append(
                    f"[lesson V-4] {lid}: draws_on[] is empty but teaches[] contains a "
                    f"global id — draws_on may be empty only when every teaches[] entry "
                    f"is a node reference"
                )

    for path, obj in assessment_objs:
        for item in obj.get("items") or []:
            iid = item.get("id", "?")
            for ref in item.get("concept_ids") or []:
                if not isinstance(ref, str) or not GRAPH_REF.match(ref):
                    continue
                if _is_global(ref) and ref not in gid_set:
                    errors.append(
                        f"[lesson V-4] item {iid}: concept_ids dangling global '{ref}'"
                    )
                elif _is_node(ref) and ref not in nid_set:
                    errors.append(
                        f"[lesson V-4] item {iid}: concept_ids dangling node '{ref}'"
                    )

    # --- V-5 / V-6 path integrity ---
    for path, obj in path_objs:
        pid = obj.get("id", path.name)
        steps = obj.get("lessons") or []
        seen_lessons: list[str] = []
        for idx, step in enumerate(steps):
            if not isinstance(step, dict):
                continue
            lesson_ref = step.get("lesson")
            requires = step.get("requires") or []
            if isinstance(lesson_ref, str):
                if lesson_ref not in lessons_by_id:
                    errors.append(
                        f"[lesson V-5] {pid} step {idx}: lesson '{lesson_ref}' does not exist"
                    )
                if lesson_ref in seen_lessons:
                    errors.append(
                        f"[lesson V-6] {pid}: lesson '{lesson_ref}' listed more than once"
                    )
                seen_lessons.append(lesson_ref)
                if lesson_ref in requires:
                    errors.append(
                        f"[lesson V-5] {pid} step {idx}: lesson '{lesson_ref}' requires itself"
                    )
            for req in requires:
                if not isinstance(req, str):
                    continue
                if req not in lessons_by_id:
                    errors.append(
                        f"[lesson V-5] {pid} step {idx}: requires unknown lesson '{req}'"
                    )
                elif req not in seen_lessons[:-1]:
                    # must appear earlier in the same path
                    errors.append(
                        f"[lesson V-5] {pid} step {idx}: requires '{req}' which does not "
                        f"appear earlier in the path"
                    )

    # --- V-7 / V-8 lesson ↔ item coherence ---
    for path, obj in lesson_objs:
        lid = obj.get("id", path.name)
        checks = obj.get("checks") or []
        screen_items = [
            s.get("item")
            for s in (obj.get("screens") or [])
            if isinstance(s, dict) and s.get("type") == "check"
        ]
        if screen_items != checks:
            errors.append(
                f"[lesson V-7] {lid}: ordered check screens {screen_items} != checks[] {checks}"
            )

        own = assessments_by_lesson.get(lid)
        own_ids: set[str] = set()
        if own is not None:
            _, aobj = own
            own_ids = {
                it.get("id")
                for it in (aobj.get("items") or [])
                if isinstance(it.get("id"), str)
            }
        for cid in checks:
            if not isinstance(cid, str):
                continue
            if cid not in own_ids:
                errors.append(
                    f"[lesson V-8] {lid}: checks id '{cid}' not defined in "
                    f"{lid}.items.json (V1 item locality)"
                )

    # --- V-9 / V-10 / V-11 item structure ---
    referenced_items: set[str] = set()
    for _, obj in lesson_objs:
        for cid in obj.get("checks") or []:
            if isinstance(cid, str):
                referenced_items.add(cid)

    for path, obj in assessment_objs:
        for item in obj.get("items") or []:
            iid = item.get("id", "?")
            options = item.get("options") or []
            correct = [o for o in options if isinstance(o, dict) and o.get("correct") is True]
            if len(correct) != 1:
                errors.append(
                    f"[lesson V-9] item {iid}: expected exactly one correct option, "
                    f"found {len(correct)}"
                )

            ids = [o.get("id") for o in options if isinstance(o, dict)]
            expected = list(OPTION_IDS[: len(options)])
            if ids != expected:
                errors.append(
                    f"[lesson V-10] item {iid}: option ids {ids} must be contiguous "
                    f"unique prefix {expected}"
                )
            if len(ids) != len(set(ids)):
                errors.append(f"[lesson V-10] item {iid}: duplicate option ids {ids}")

            concept_ids = item.get("concept_ids") or []
            if not concept_ids:
                errors.append(f"[lesson V-11] item {iid}: concept_ids must be non-empty")
            for o in options:
                if not isinstance(o, dict):
                    continue
                expl = o.get("explanation")
                if not isinstance(expl, str) or not expl.strip():
                    errors.append(
                        f"[lesson V-11] item {iid} option {o.get('id')}: "
                        f"missing non-empty explanation"
                    )

            if isinstance(iid, str) and iid not in referenced_items:
                errors.append(
                    f"[lesson V-11] item {iid}: not referenced by any lesson checks[]"
                )

    # --- V-12 misconception pairing proxy ---
    for path, obj in lesson_objs:
        lid = obj.get("id", path.name)
        screens = obj.get("screens") or []
        has_misc = any(
            isinstance(s, dict) and s.get("type") == "misconception" for s in screens
        )
        if not has_misc:
            continue
        teaches = set(obj.get("teaches") or [])
        paired = False
        for cid in obj.get("checks") or []:
            item = items_by_id.get(cid)
            if not item:
                continue
            cids = set(item.get("concept_ids") or [])
            if teaches & cids:
                paired = True
                break
        if not paired:
            errors.append(
                f"[lesson V-12] {lid}: misconception screen present but no check "
                f"shares a concept_ids entry with teaches[]"
            )

    # --- V-13 one-hop edge reality (from canonical content) ---
    home_nodes: dict[str, list[str]] = {}
    for n in nodes:
        gid = n.get("global_id")
        if gid:
            home_nodes.setdefault(gid, []).append(n["id"])
        for hg in n.get("hosts_globals") or []:
            home_nodes.setdefault(hg, []).append(n["id"])

    for path, obj in lesson_objs:
        lid = obj.get("id", path.name)
        anchors = list(obj.get("teaches") or []) + list(obj.get("draws_on") or [])
        allowed: set[str] = set()
        for a in anchors:
            if not isinstance(a, str):
                continue
            if _is_node(a):
                n = node_by_id.get(a)
                if not n:
                    continue
                for c in n.get("connects_to") or []:
                    ref = c.get("ref") if isinstance(c, dict) else None
                    if isinstance(ref, str):
                        allowed.add(ref)
                if n.get("global_id"):
                    allowed.add(n["global_id"])
                for hg in n.get("hosts_globals") or []:
                    if isinstance(hg, str):
                        allowed.add(hg)
            elif _is_global(a):
                g = global_by_id.get(a)
                if g:
                    for d in g.get("disambiguate_with") or []:
                        if isinstance(d, str):
                            allowed.add(d)
                for hid in home_nodes.get(a, []):
                    allowed.add(hid)
                    hn = node_by_id.get(hid)
                    if not hn:
                        continue
                    for c in hn.get("connects_to") or []:
                        ref = c.get("ref") if isinstance(c, dict) else None
                        if isinstance(ref, str):
                            allowed.add(ref)

        for ref in obj.get("connects") or []:
            if not isinstance(ref, str):
                continue
            if ref not in allowed:
                errors.append(
                    f"[lesson V-13] {lid}: connects '{ref}' is not one-hop reachable "
                    f"from teaches∪draws_on anchors {anchors}"
                )


def _counts(values: list) -> dict:
    out: dict = {}
    for v in values:
        out[v] = out.get(v, 0) + 1
    return out
