import json
import os
import re
import unittest

from helpers import REPO, TempCase, make_repo, run

MARKER = ".ai-development-system.json"


class InstallerFixture(TempCase):
    def setUp(self):
        super().setUp()
        self.root = make_repo(self.tmp / "src")
        run("build-collections.py", "--root", str(self.root))
        self.proj = self.tmp / "project"
        self.proj.mkdir()
        self.dest = self.proj / ".claude" / "skills"
        self.home = self.tmp / "home"
        self.home.mkdir()

    def inst(self, *args, env=None):
        e = {"HOME": str(self.home), "USERPROFILE": str(self.home)}
        e.update(env or {})
        return run("install-skills.py", "--root", str(self.root), "--project-dir", str(self.proj), *args, env=e)

    # ---- basic install behavior ----
    def test_list(self):
        code, out, _ = self.inst("--list")
        self.assertEqual(code, 0)
        for n in ("first-skill", "second-skill", "third-skill", "pair", "everything", "--target project"):
            self.assertIn(n, out)

    def test_dry_run_changes_nothing(self):
        code, out, _ = self.inst("--skill", "first-skill", "--target", "project", "--dry-run")
        self.assertEqual(code, 0)
        self.assertIn("[dry-run] [install] first-skill", out)
        self.assertFalse((self.proj / ".claude").exists())

    def test_install_copies_files_and_writes_marker(self):
        code, out, err = self.inst("--skill", "third-skill", "--target", "project")
        self.assertEqual(code, 0, out + err)
        d = self.dest / "third-skill"
        self.assertTrue((d / "SKILL.md").is_file())
        self.assertTrue((d / "references" / "notes.md").is_file())
        marker = json.loads((d / MARKER).read_text())
        self.assertEqual(marker["name"], "third-skill")
        self.assertEqual(marker["version"], "1.2.3")
        self.assertEqual([p.name for p in self.dest.iterdir()], ["third-skill"])  # no temp leftovers

    def test_second_run_is_unchanged(self):
        self.inst("--skill", "first-skill", "--target", "project")
        code, out, _ = self.inst("--skill", "first-skill", "--target", "project")
        self.assertEqual(code, 0)
        self.assertIn("[unchanged] first-skill", out)

    def test_related_skills_hint(self):
        _, out, _ = self.inst("--skill", "first-skill", "--target", "project", "--dry-run")
        self.assertIn("second-skill", out.split("note:")[-1])

    def test_collection_installs_included_collections(self):
        code, out, _ = self.inst("--collection", "everything", "--target", "project")
        self.assertEqual(code, 0, out)
        self.assertEqual(sorted(p.name for p in self.dest.iterdir()), ["first-skill", "second-skill", "third-skill"])

    # ---- conflicts and safety ----
    def test_unmanaged_directory_is_never_overwritten(self):
        d = self.dest / "first-skill"
        d.mkdir(parents=True)
        (d / "SKILL.md").write_text("my own skill", encoding="utf-8")
        code, out, _ = self.inst("--skill", "first-skill", "--target", "project")
        self.assertEqual(code, 3)
        self.assertIn("[conflict]", out)
        self.assertEqual((d / "SKILL.md").read_text(), "my own skill")

    def test_modified_install_is_a_conflict_and_force_backs_up(self):
        self.inst("--skill", "first-skill", "--target", "project")
        f = self.dest / "first-skill" / "SKILL.md"
        f.write_text(f.read_text() + "\nlocal edit\n", encoding="utf-8")
        code, out, _ = self.inst("--skill", "first-skill", "--target", "project")
        self.assertEqual(code, 3)
        self.assertIn("local edit", f.read_text())
        code, out, _ = self.inst("--skill", "first-skill", "--target", "project", "--force")
        self.assertEqual(code, 0, out)
        self.assertNotIn("local edit", f.read_text())
        backups = list((self.proj / ".claude" / ".skill-backups").glob("*/first-skill/SKILL.md"))
        self.assertEqual(len(backups), 1)
        self.assertIn("local edit", backups[0].read_text())
        code, out, _ = self.inst("--skill", "first-skill", "--target", "project", "--status")
        self.assertIn("current", out)

    @unittest.skipUnless(hasattr(os, "symlink"), "symlinks unavailable")
    def test_symlinked_destination_directory_is_not_followed(self):
        outside = self.tmp / "outside"
        outside.mkdir()
        (outside / "keep.txt").write_text("keep", encoding="utf-8")
        self.dest.mkdir(parents=True)
        try:
            os.symlink(outside, self.dest / "first-skill")
        except OSError:
            self.skipTest("cannot create symlink")
        code, out, _ = self.inst("--skill", "first-skill", "--target", "project")
        self.assertEqual(code, 3)
        self.assertEqual((outside / "keep.txt").read_text(), "keep")
        code, _, _ = self.inst("--skill", "first-skill", "--target", "project", "--remove", "--force")
        self.assertEqual(code, 3)
        self.assertTrue((outside / "keep.txt").exists())

    def test_destination_inside_source_repository_is_refused(self):
        code, _, err = self.inst("--skill", "first-skill", "--dest", str(self.root / "skills" / "alpha"))
        self.assertEqual(code, 1)
        self.assertIn("overlaps", err)
        code, _, err = self.inst("--skill", "first-skill", "--dest", str(self.root))
        self.assertEqual(code, 1)

    def test_target_and_dest_are_mutually_required(self):
        code, _, err = self.inst("--skill", "first-skill")
        self.assertEqual(code, 1)
        self.assertIn("exactly one", err)
        code, _, err = self.inst("--skill", "first-skill", "--target", "project", "--dest", str(self.tmp / "x"))
        self.assertEqual(code, 1)

    def test_unknown_skill_suggests_close_match(self):
        code, _, err = self.inst("--skill", "first-skil", "--target", "project")
        self.assertEqual(code, 1)
        self.assertIn("did you mean: first-skill", err)
        self.assertFalse((self.proj / ".claude").exists())

    def test_nothing_selected_is_an_error(self):
        code, _, err = self.inst("--target", "project")
        self.assertEqual(code, 1)
        self.assertIn("choose what to act on", err)

    # ---- update / remove / status ----
    def test_update_flow(self):
        self.inst("--skill", "first-skill", "--target", "project")
        src = self.root / "skills" / "alpha" / "first-skill" / "SKILL.md"
        src.write_text(src.read_text() + "\nNew guidance added upstream.\n", encoding="utf-8")
        code, out, _ = self.inst("--skill", "first-skill", "--target", "project", "--status")
        self.assertIn("outdated", out)
        code, out, _ = self.inst("--skill", "first-skill", "--target", "project")
        self.assertEqual(code, 0)
        self.assertIn("[outdated]", out)
        self.assertNotIn("New guidance", (self.dest / "first-skill" / "SKILL.md").read_text())
        code, out, _ = self.inst("--skill", "first-skill", "--target", "project", "--update")
        self.assertEqual(code, 0, out)
        self.assertIn("[update] first-skill", out)
        self.assertIn("New guidance", (self.dest / "first-skill" / "SKILL.md").read_text())

    def test_update_does_not_clobber_local_edits(self):
        self.inst("--skill", "first-skill", "--target", "project")
        f = self.dest / "first-skill" / "SKILL.md"
        f.write_text(f.read_text() + "\nlocal\n", encoding="utf-8")
        code, _, _ = self.inst("--skill", "first-skill", "--target", "project", "--update")
        self.assertEqual(code, 3)
        self.assertIn("local", f.read_text())

    def test_remove_only_removes_managed_unmodified_skills(self):
        self.inst("--skill", "first-skill,second-skill", "--target", "project")
        code, out, _ = self.inst("--skill", "first-skill", "--target", "project", "--remove")
        self.assertEqual(code, 0, out)
        self.assertFalse((self.dest / "first-skill").exists())
        self.assertTrue((self.dest / "second-skill").exists())
        # unmanaged directory: refused even with --force
        d = self.dest / "third-skill"
        d.mkdir()
        (d / "SKILL.md").write_text("mine", encoding="utf-8")
        code, out, _ = self.inst("--skill", "third-skill", "--target", "project", "--remove", "--force")
        self.assertEqual(code, 3)
        self.assertTrue((d / "SKILL.md").exists())
        # modified managed skill: refused without --force
        f = self.dest / "second-skill" / "SKILL.md"
        f.write_text(f.read_text() + "\nedit\n", encoding="utf-8")
        code, _, _ = self.inst("--skill", "second-skill", "--target", "project", "--remove")
        self.assertEqual(code, 3)
        self.assertTrue(f.exists())

    def test_remove_of_missing_skill_is_harmless(self):
        code, out, _ = self.inst("--skill", "first-skill", "--target", "project", "--remove")
        self.assertEqual(code, 0)
        self.assertIn("not installed", out)

    def test_user_and_agents_targets_follow_home(self):
        self.assertEqual(self.inst("--skill", "first-skill", "--target", "user")[0], 0)
        self.assertTrue((self.home / ".claude" / "skills" / "first-skill" / "SKILL.md").is_file())
        self.assertEqual(self.inst("--skill", "first-skill", "--target", "agents-user")[0], 0)
        self.assertTrue((self.home / ".agents" / "skills" / "first-skill" / "SKILL.md").is_file())
        self.assertEqual(self.inst("--skill", "first-skill", "--target", "agents-project")[0], 0)
        self.assertTrue((self.proj / ".agents" / "skills" / "first-skill" / "SKILL.md").is_file())


class InstallerRealRepository(TempCase):
    def test_all_skills_dry_run_lists_every_skill_and_writes_nothing(self):
        dest = self.tmp / "agent-skills"
        code, out, err = run("install-skills.py", "--all", "--dest", str(dest), "--dry-run")
        self.assertEqual(code, 0, out + err)
        self.assertEqual(len(re.findall(r"\[install\]", out)), 43)
        self.assertFalse(dest.exists())

    def test_real_skill_installs_with_supporting_files_and_reports_current(self):
        dest = self.tmp / "agent-skills"
        code, out, err = run("install-skills.py", "--skill", "ui-animation", "--dest", str(dest))
        self.assertEqual(code, 0, out + err)
        self.assertTrue((dest / "ui-animation" / "references" / "component-recipes.md").is_file())
        code, out, _ = run("install-skills.py", "--skill", "ui-animation", "--dest", str(dest), "--status")
        self.assertIn("current", out)

    def test_collection_install_matches_collection_contents(self):
        dest = self.tmp / "agent-skills"
        code, out, err = run("install-skills.py", "--collection", "motion-and-interaction", "--dest", str(dest))
        self.assertEqual(code, 0, out + err)
        self.assertEqual(sorted(p.name for p in dest.iterdir()),
                         sorted(["motion-design", "ui-animation", "micro-interactions", "scroll-animation",
                                 "animation-performance", "reduced-motion-accessibility"]))


if __name__ == "__main__":
    unittest.main()
