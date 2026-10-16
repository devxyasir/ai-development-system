import contextlib
import importlib.util
import io
import sys
import unittest

from helpers import REPO, SCRIPTS, TempCase, make_repo, make_skill, run

sys.path.insert(0, str(SCRIPTS))
import skilllib as sl  # noqa: E402


class FrontmatterParser(unittest.TestCase):
    def test_parses_scalars_maps_and_lists(self):
        text = '---\nname: demo\ndescription: "Use when: testing"\nmetadata:\n  category: x\n  version: "1.0.0"\ntags: [a, b]\n---\nbody'
        data, body = sl.parse_frontmatter(text)
        self.assertEqual(data["name"], "demo")
        self.assertEqual(data["description"], "Use when: testing")
        self.assertEqual(data["metadata"], {"category": "x", "version": "1.0.0"})
        self.assertEqual(data["tags"], ["a", "b"])
        self.assertEqual(body.strip(), "body")

    def test_rejects_unquoted_colon(self):
        with self.assertRaises(sl.FrontmatterError):
            sl.parse_frontmatter("---\nname: demo\ndescription: Use when: testing\n---\n")

    def test_rejects_missing_close_and_missing_open(self):
        with self.assertRaises(sl.FrontmatterError):
            sl.parse_frontmatter("---\nname: demo\n")
        with self.assertRaises(sl.FrontmatterError):
            sl.parse_frontmatter("name: demo\n---\n")

    def test_rejects_duplicate_keys_and_tabs(self):
        with self.assertRaises(sl.FrontmatterError):
            sl.parse_frontmatter("---\nname: a\nname: b\n---\n")
        with self.assertRaises(sl.FrontmatterError):
            sl.parse_frontmatter("---\nmetadata:\n\tcategory: x\n---\n")


class RealRepository(unittest.TestCase):
    def test_all_real_skills_validate(self):
        code, out, err = run("validate-skills.py", "--strict")
        self.assertEqual(code, 0, out + err)
        self.assertIn("43 skills", out)

    def test_every_skill_directory_matches_its_name(self):
        for s in sl.discover_skills(REPO):
            self.assertFalse(s.errors, f"{s.name}: {s.errors}")
            self.assertEqual(s.meta["name"], s.name)
            self.assertEqual(s.meta["metadata"]["category"], s.category)
            self.assertLessEqual(len(s.description), 1024)


class FixtureNegatives(TempCase):
    def setUp(self):
        super().setUp()
        self.root = make_repo(self.tmp)

    def validate(self, *extra):
        return run("validate-skills.py", "--root", str(self.root), *extra)

    def test_fixture_is_valid_after_build(self):
        run("build-collections.py", "--root", str(self.root))
        code, out, err = self.validate("--strict")
        self.assertEqual(code, 0, out + err)

    def test_name_must_match_directory(self):
        p = self.root / "skills" / "alpha" / "first-skill" / "SKILL.md"
        p.write_text(p.read_text().replace("name: first-skill", "name: other-name", 1))
        code, out, _ = self.validate()
        self.assertEqual(code, 1)
        self.assertIn("must equal directory name", out)

    def test_missing_description_and_sections(self):
        make_skill(self.root, "alpha", "bad-one", description="short", body="# bad-one\n\nNo sections here at all.\n")
        code, out, _ = self.validate()
        self.assertEqual(code, 1)
        self.assertIn("too short", out)
        self.assertIn("When to use", out)
        self.assertIn("Verification", out)

    def test_unfinished_marker_rejected(self):
        make_skill(self.root, "alpha", "marker-skill", body="# m\n\n## When to use\n- x\n\n## Verification\n- TODO fill this in\n")
        code, out, _ = self.validate()
        self.assertEqual(code, 1)
        self.assertIn("unfinished-work marker", out)

    def test_credential_like_string_rejected(self):
        make_skill(self.root, "alpha", "secret-skill", body="# s\n\n## When to use\n- x\n\n## Verification\n- key AKIAABCDEFGHIJKLMNOP\n")
        code, out, _ = self.validate()
        self.assertEqual(code, 1)
        self.assertIn("credential", out)

    def test_duplicate_names_across_categories(self):
        make_skill(self.root, "beta", "first-skill")
        code, out, _ = self.validate()
        self.assertEqual(code, 1)
        self.assertIn("duplicate skill name", out)

    def test_category_must_match_parent_directory(self):
        p = self.root / "skills" / "alpha" / "second-skill" / "SKILL.md"
        p.write_text(p.read_text().replace("category: alpha", "category: wrong"))
        code, out, _ = self.validate()
        self.assertEqual(code, 1)
        self.assertIn("metadata.category", out)


class ContrastScript(unittest.TestCase):
    def load(self):
        path = REPO / "skills" / "design" / "color-palette-selection" / "scripts" / "contrast.py"
        spec = importlib.util.spec_from_file_location("contrast", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod

    def test_black_on_white_is_21(self):
        m = self.load()
        self.assertAlmostEqual(m.ratio(m.parse_hex("#000"), m.parse_hex("#ffffff")), 21.0, places=2)

    def test_exit_codes(self):
        m = self.load()
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(m.main(["#000000", "#ffffff"]), 0)
            self.assertEqual(m.main(["#777777", "#888888"]), 1)
            self.assertEqual(m.main(["nothex", "#ffffff"]), 2)
            self.assertEqual(m.main(["#767676", "#ffffff", "--ui"]), 0)


if __name__ == "__main__":
    unittest.main()
