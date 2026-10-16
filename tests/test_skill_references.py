import sys
import unittest

from helpers import SCRIPTS, TempCase, make_repo, make_skill, run

sys.path.insert(0, str(SCRIPTS))
import skilllib as sl  # noqa: E402


class LinkChecks(TempCase):
    def setUp(self):
        super().setUp()
        self.root = make_repo(self.tmp)
        run("build-collections.py", "--root", str(self.root))

    def validate(self, *extra):
        return run("validate-skills.py", "--root", str(self.root), *extra)

    def test_broken_link_is_an_error(self):
        make_skill(self.root, "alpha", "broken-link",
                   body="# b\n\n## When to use\n- x\n\n## Verification\n- see [missing](references/nope.md)\n")
        code, out, _ = self.validate()
        self.assertEqual(code, 1)
        self.assertIn("broken link", out)

    def test_link_leaving_the_skill_is_an_error(self):
        make_skill(self.root, "alpha", "escaping",
                   body="# e\n\n## When to use\n- x\n\n## Verification\n- see [other](../second-skill/SKILL.md)\n")
        code, out, _ = self.validate()
        self.assertEqual(code, 1)
        self.assertIn("escapes the skill directory", out)

    def test_orphan_support_file_warns_and_strict_fails(self):
        make_skill(self.root, "alpha", "orphaned",
                   extra={"references/unused.md": "# Unused\n\nThis reference is not linked from the entry file but it is long enough to count as real guidance, which is exactly the situation the orphan warning is meant to catch.\n"})
        run("build-collections.py", "--root", str(self.root))
        code, out, _ = self.validate()
        self.assertEqual(code, 0, out)
        self.assertIn("not referenced from SKILL.md", out)
        code, out, _ = self.validate("--strict")
        self.assertEqual(code, 1)

    def test_tiny_support_file_is_an_error(self):
        make_skill(self.root, "alpha", "tiny",
                   body="# t\n\n## When to use\n- x\n\n## Verification\n- [r](references/r.md)\n", extra={"references/r.md": "# R\n"})
        code, out, _ = self.validate()
        self.assertEqual(code, 1)
        self.assertIn("support files must contain real guidance", out)

    def test_related_must_name_existing_skills(self):
        make_skill(self.root, "alpha", "relates", related="does-not-exist")
        code, out, _ = self.validate()
        self.assertEqual(code, 1)
        self.assertIn("unknown skill 'does-not-exist'", out)

    def test_python_scripts_inside_skills_must_compile(self):
        make_skill(self.root, "alpha", "script-skill",
                   body="# s\n\n## When to use\n- x\n\n## Verification\n- run scripts/tool.py\n",
                   extra={"scripts/tool.py": "def broken(:\n    pass\n"})
        code, out, _ = self.validate()
        self.assertEqual(code, 1)
        self.assertIn("Python syntax error", out)


class SchemaSubset(unittest.TestCase):
    def test_required_type_pattern_and_unique(self):
        schema = {"type": "object", "required": ["name"], "additionalProperties": False,
                  "properties": {"name": {"type": "string", "pattern": "^[a-z]+$"},
                                 "items": {"type": "array", "uniqueItems": True, "items": {"type": "integer"}}}}
        self.assertEqual(sl.validate_json({"name": "abc", "items": [1, 2]}, schema), [])
        self.assertTrue(sl.validate_json({}, schema))
        self.assertTrue(sl.validate_json({"name": "ABC"}, schema))
        self.assertTrue(sl.validate_json({"name": "a", "items": [1, 1]}, schema))
        self.assertTrue(sl.validate_json({"name": "a", "extra": 1}, schema))
        self.assertTrue(sl.validate_json({"name": "a", "items": [True]}, schema))


if __name__ == "__main__":
    unittest.main()
