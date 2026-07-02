#!/usr/bin/env python3
"""Tests for module scaffolding."""
from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "pipeline"))

from scaffold.scaffold_module import plan_scaffold, write_scaffold  # noqa: E402
from lib.module_utils import validate_slug  # noqa: E402
import importlib.util


def _load_validate():
    pipeline_dir = str(ROOT / "pipeline")
    validate_dir = str(ROOT / "pipeline" / "validate")
    for p in (pipeline_dir, validate_dir):
        if p not in sys.path:
            sys.path.insert(0, p)
    path = ROOT / "pipeline" / "validate" / "validate.py"
    spec = importlib.util.spec_from_file_location("pipeline_validate", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(mod)
    return mod


class TestScaffoldModule(unittest.TestCase):
    def test_malformed_slug_rejected(self):
        self.assertIsNotNone(validate_slug("Corporate-Finance"))
        self.assertIsNotNone(validate_slug(""))
        self.assertIsNone(validate_slug("corporate-finance"))

    def test_dry_run_plan(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "content/modules").mkdir(parents=True)
            plan = plan_scaffold("test-module", "Test Module", root)
            self.assertEqual(plan["slug"], "test-module")
            self.assertEqual(len(plan["files"]), 6)
            self.assertEqual(plan["visibility"], "draft")

    def test_scaffold_creates_required_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "content" / "glossary").mkdir(parents=True)
            (root / "content/glossary/globals.json").write_text("[]", encoding="utf-8")
            (root / "content/modules").mkdir(parents=True)
            shutil.copytree(ROOT / "templates/module", root / "templates/module")

            plan = plan_scaffold("test-module", "Test Module", root)
            write_scaffold(plan)

            mod_dir = root / "content/modules/test-module"
            self.assertTrue((mod_dir / "module.json").exists())
            for n in range(1, 6):
                self.assertTrue((mod_dir / "zones" / f"z{n}.json").exists())

            mod = json.loads((mod_dir / "module.json").read_text(encoding="utf-8"))
            self.assertEqual(mod["visibility"], "draft")

    def test_duplicate_slug_blocked(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "content/modules/existing").mkdir(parents=True)
            with self.assertRaises(ValueError):
                plan_scaffold("existing", "Existing", root)

    def test_broken_reference_caught(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "content/glossary").mkdir(parents=True)
            (root / "content/glossary/globals.json").write_text("[]", encoding="utf-8")
            mod_dir = root / "content/modules/fixture"
            (mod_dir / "zones").mkdir(parents=True)
            (mod_dir / "module.json").write_text(
                json.dumps(
                    {
                        "slug": "fixture",
                        "title": "Fixture",
                        "kind": "core-concept",
                        "build_order": 99,
                        "visibility": "active",
                        "zones": [
                            {"zone": i, "title": f"Z{i}"} for i in range(1, 6)
                        ],
                    }
                ),
                encoding="utf-8",
            )
            for n in range(1, 6):
                (mod_dir / "zones" / f"z{n}.json").write_text("[]", encoding="utf-8")
            (mod_dir / "zones" / "z1.json").write_text(
                json.dumps(
                    [
                        {
                            "id": "fixture.z1.1",
                            "module": "fixture",
                            "zone": 1,
                            "ordinal": 1,
                            "title": "Broken",
                            "tag": "core",
                            "quick_definition": "x",
                            "explainer_covers": ["x"],
                            "connects_to": [{"ref": "G99999"}],
                        }
                    ]
                ),
                encoding="utf-8",
            )

            validate = _load_validate()
            globals_, modules, nodes, _draft_slugs = validate.load_content(root)
            errors: list[str] = []
            warnings: list[str] = []
            validate.check_references(globals_, nodes, errors, warnings)
            self.assertTrue(any("G99999" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
