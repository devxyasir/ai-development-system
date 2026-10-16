import importlib.util
import json
import re
import unittest

from helpers import REPO, SCRIPTS, TempCase, copy_repo, run


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_instructions", SCRIPTS / "validate-instructions.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


VI = load_validator()


class RealPlaybook(unittest.TestCase):
    def test_instruction_system_validates(self):
        code, out, err = run("validate-instructions.py")
        self.assertEqual(code, 0, out + err)
        self.assertIn("0 errors", out)

    def test_entry_files_are_short_and_critical_rules_are_first(self):
        agents = (REPO / "AGENTS.md").read_text()
        self.assertLess(len(agents.splitlines()), 200)
        self.assertLess(agents.index("## Critical rules"), 1200)
        self.assertEqual((REPO / "CLAUDE.md").read_text().splitlines()[0], "@AGENTS.md")

    def test_agents_md_routing_summary_lists_every_workflow(self):
        agents = (REPO / "AGENTS.md").read_text()
        for w in VI.WORKFLOWS:
            self.assertIn(f"playbook/workflows/{w}.md", agents, w)


class RoutingScenarios(unittest.TestCase):
    """Instruction-routing tests: they check the instruction graph, not a real agent run."""

    @staticmethod
    def loaded(workflow, conditions):
        text = (REPO / "playbook" / "workflows" / f"{workflow}.md").read_text()
        out = set()
        for name, _target, when in VI.parse_load_table(text):
            if when.strip().lower() == "always" or any(c.lower() in when.lower() for c in conditions):
                out.add(name)
        return out

    def test_scenarios(self):
        scenarios = json.loads((REPO / "tests" / "routing_scenarios.json").read_text())
        self.assertGreaterEqual(len(scenarios), 7)
        routing = (REPO / "playbook" / "core" / "02-routing.md").read_text()
        for sc in scenarios:
            with self.subTest(task=sc["task"]):
                loaded = set()
                for w in sc["workflows"]:
                    self.assertIn(f"../workflows/{w}.md", routing, f"routing does not reach {w}")
                    loaded |= self.loaded(w, sc.get("conditions", []))
                self.assertFalse(set(sc["must_load"]) - loaded, f"missing: {set(sc['must_load']) - loaded}")
                self.assertFalse(set(sc["must_not_load"]) & loaded, f"irrelevant: {set(sc['must_not_load']) & loaded}")
                self.assertLessEqual(len(loaded), sc.get("max_skills", 10), f"loads too much: {sorted(loaded)}")

    def test_no_workflow_loads_the_whole_library(self):
        total = len(list((REPO / "skills").glob("*/*/SKILL.md")))
        for w in VI.WORKFLOWS:
            rows = VI.parse_load_table((REPO / "playbook" / "workflows" / f"{w}.md").read_text())
            self.assertLessEqual(len(rows), VI.MAX_LOAD_TOTAL, w)
            self.assertLess(len(rows), total / 2, w)


class Mutations(TempCase):
    """Break a copy of the real repository in one way at a time; the validator must notice."""

    def setUp(self):
        super().setUp()
        self.root = copy_repo(self.tmp / "repo")

    def validate(self):
        return run("validate-instructions.py", "--root", str(self.root))

    def edit(self, rel, fn):
        p = self.root / rel
        p.write_text(fn(p.read_text()), encoding="utf-8")

    def assert_fails(self, needle):
        code, out, _ = self.validate()
        self.assertEqual(code, 1, out)
        self.assertIn(needle, out)

    def test_baseline_copy_is_valid(self):
        self.assertEqual(self.validate()[0], 0)

    def test_workflow_missing_section(self):
        self.edit("playbook/workflows/bug-fixing.md", lambda t: t.replace("## Verify", "## Checks"))
        self.assert_fails("missing required section '## Verify'")

    def test_claude_md_must_import_agents_md(self):
        self.edit("CLAUDE.md", lambda t: t.replace("@AGENTS.md\n", "", 1))
        self.assert_fails("@AGENTS.md")

    def test_claude_md_must_not_import_the_playbook(self):
        self.edit("CLAUDE.md", lambda t: t + "\n@playbook/core/02-routing.md\n")
        self.assert_fails("would load whole documents")

    def test_broken_link(self):
        self.edit("playbook/README.md", lambda t: t + "\nSee [nothing](core/missing.md).\n")
        self.assert_fails("broken link: core/missing.md")

    def test_requires_cycle(self):
        self.edit("playbook/core/00-core-principles.md",
                  lambda t: t.replace("# Core principles\n", "# Core principles\n\nRequires: [plan](01-understand-and-plan.md)\n", 1))
        self.assert_fails("circular 'Requires:' chain")

    def test_unscoped_rule_file(self):
        (self.root / ".claude" / "rules" / "everything.md").write_text("# Always loaded\n\nText.\n", encoding="utf-8")
        self.assert_fails("rules without paths load at every session start")

    def test_documented_flag_that_does_not_exist(self):
        self.edit("README.md", lambda t: t + "\n```bash\npython scripts/install-skills.py --skill x --target project --teleport\n```\n")
        self.assert_fails("documented flag --teleport")

    def test_documented_script_that_does_not_exist(self):
        self.edit("README.md", lambda t: t + "\n```bash\npython scripts/nonexistent.py\n```\n")
        self.assert_fails("documented script does not exist")

    def test_entry_file_too_long(self):
        self.edit("AGENTS.md", lambda t: t + "\n".join(f"line {i}" for i in range(220)) + "\n")
        self.assert_fails("entry files are loaded in full")

    def test_workflow_missing_from_routing(self):
        self.edit("playbook/core/02-routing.md", lambda t: t.replace("../workflows/handoff.md", "../workflows/release.md"))
        self.assert_fails("does not route to workflow 'handoff'")

    def test_skill_missing_from_finder(self):
        def drop(t):
            return "\n".join(l for l in t.splitlines() if "skill-installation" not in l) + "\n"
        self.edit("playbook/core/02-routing.md", drop)
        self.assert_fails("skill 'skill-installation' is not in the skill finder")

    def test_index_duplicate_and_omission(self):
        row = next(l for l in (self.root / "playbook/INDEX.md").read_text().splitlines() if "workflow: handoff" in l)
        self.edit("playbook/INDEX.md", lambda t: t + row + "\n")
        self.assert_fails("lists playbook/workflows/handoff.md 2 times")
        self.edit("playbook/INDEX.md", lambda t: "\n".join(l for l in t.splitlines() if "decision-trees" not in l) + "\n")
        self.assert_fails("does not list playbook/references/decision-trees.md")

    def test_too_many_always_skills(self):
        def add(t):
            extra = "".join(f"| [{n}](../../skills/engineering/{n}/SKILL.md) | Always |\n"
                            for n in ("code-review", "refactoring", "performance-analysis", "debugging", "testing-strategy"))
            return t.replace("## Steps", extra + "\n## Steps", 1)
        self.edit("playbook/workflows/handoff.md", add)
        self.assert_fails("'Always' skills (max 6)")

    def test_contradicting_instruction(self):
        self.edit("playbook/core/04-lower-capability-support.md", lambda t: t + "\n- Always push when finished.\n")
        self.assert_fails("contradicts the core rules")


if __name__ == "__main__":
    unittest.main()
