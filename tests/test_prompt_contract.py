"""Static, dependency-free checks of the agent's deliverable-first prompt."""
from __future__ import annotations

import ast
from pathlib import Path
import unittest


def read_note() -> str:
    source = Path(__file__).resolve().parents[1] / "harness.py"
    tree = ast.parse(source.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == "NOTE" for t in node.targets
        ):
            return ast.literal_eval(node.value)
    raise AssertionError("NOTE assignment not found")


class PromptContractTests(unittest.TestCase):
    def test_note_interpolates_workdir(self):
        note = read_note()
        self.assertEqual(note.count("{workdir}"), 1)
        self.assertIn("/app", note.format(workdir="/app"))

    def test_deliverable_and_verification_requirements(self):
        note = read_note().lower()
        for phrase in (
            "exact requested deliverable files",
            "submission.zip",
            "ifc",
            "a script alone is not a substitute",
            "each required path exists",
            "zip",
            "mcp tools",
            "honest partial deliverable",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, note)

    def test_parse_complete_harness(self):
        source = Path(__file__).resolve().parents[1] / "harness.py"
        compile(source.read_text(encoding="utf-8"), str(source), "exec")


if __name__ == "__main__":
    unittest.main()
