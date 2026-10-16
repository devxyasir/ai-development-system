import json
import sys
import unittest

from helpers import REPO, SCRIPTS, TempCase, make_collection, make_repo, make_skill, run

sys.path.insert(0, str(SCRIPTS))
import skilllib as sl  # noqa: E402


class RealCollections(unittest.TestCase):
    def test_all_collections_resolve_to_existing_skills(self):
        cols = sl.load_collections(REPO)
        names = {s.name for s in sl.discover_skills(REPO)}
        self.assertGreaterEqual(len(cols), 9)
        for c in cols:
            resolved = sl.resolve_collection(c, cols)
            self.assertTrue(resolved, c)
            self.assertFalse(set(resolved) - names, c)
            self.assertEqual(len(resolved), len(set(resolved)), f"duplicates in {c}")

    def test_every_skill_belongs_to_a_collection(self):
        cols = sl.load_collections(REPO)
        used = set()
        for c in cols:
            used.update(sl.resolve_collection(c, cols))
        self.assertEqual({s.name for s in sl.discover_skills(REPO)} - used, set())

    def test_generated_files_are_current(self):
        code, out, err = run("build-collections.py", "--check")
        self.assertEqual(code, 0, out + err)

    def test_no_collection_loads_everything(self):
        cols = sl.load_collections(REPO)
        total = len(sl.discover_skills(REPO))
        for c in cols:
            self.assertLess(len(sl.resolve_collection(c, cols)), total, f"{c} loads every skill")


class FixtureCollections(TempCase):
    def setUp(self):
        super().setUp()
        self.root = make_repo(self.tmp)

    def test_includes_are_resolved_in_order_without_duplicates(self):
        cols = sl.load_collections(self.root)
        self.assertEqual(sl.resolve_collection("everything", cols), ["first-skill", "second-skill", "third-skill"])

    def test_cycle_detected(self):
        make_collection(self.root, "a", ["first-skill"], includes=["b"])
        make_collection(self.root, "b", ["second-skill"], includes=["a"])
        with self.assertRaises(sl.CollectionError):
            sl.resolve_collection("a", sl.load_collections(self.root))
        code, out, _ = run("validate-skills.py", "--root", str(self.root))
        self.assertEqual(code, 1)
        self.assertIn("circular include", out)

    def test_unknown_skill_and_bad_name_rejected(self):
        make_collection(self.root, "ghosts", ["no-such-skill"])
        code, out, _ = run("validate-skills.py", "--root", str(self.root))
        self.assertEqual(code, 1)
        self.assertIn("unknown skill 'no-such-skill'", out)

    def test_build_writes_files_and_check_detects_staleness(self):
        code, _, _ = run("build-collections.py", "--root", str(self.root), "--check")
        self.assertEqual(code, 1)  # nothing generated yet
        code, out, _ = run("build-collections.py", "--root", str(self.root))
        self.assertEqual(code, 0, out)
        manifest = json.loads((self.root / "skills" / "manifest.json").read_text())
        self.assertEqual(manifest["version"], "1.2.3")
        self.assertEqual({s["name"] for s in manifest["skills"]}, {"first-skill", "second-skill", "third-skill"})
        self.assertIn("references/notes.md", next(s for s in manifest["skills"] if s["name"] == "third-skill")["files"])
        code, _, _ = run("build-collections.py", "--root", str(self.root), "--check")
        self.assertEqual(code, 0)
        make_skill(self.root, "beta", "fourth-skill")
        code, out, _ = run("build-collections.py", "--root", str(self.root), "--check")
        self.assertEqual(code, 1)
        self.assertIn("stale", out)

    def test_list_skills_filters(self):
        code, out, _ = run("list-skills.py", "--root", str(self.root), "--category", "beta")
        self.assertEqual(code, 0)
        self.assertIn("third-skill", out)
        self.assertNotIn("first-skill", out)
        code, out, _ = run("list-skills.py", "--root", str(self.root), "--collections")
        self.assertIn("everything (3 skills)", out)
        code, out, _ = run("list-skills.py", "--root", str(self.root), "--json", "--search", "second")
        self.assertEqual([s["name"] for s in json.loads(out)], ["second-skill"])


if __name__ == "__main__":
    unittest.main()
