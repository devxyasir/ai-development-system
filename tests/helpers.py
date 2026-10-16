"""Shared helpers for the test suite (standard library only)."""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPTS = REPO / "scripts"

DESC = ("Does one specific job well and explains the procedure. Use when the task in the fixture needs "
        "this behavior, and not for unrelated work.")


def run(script, *args, env=None, cwd=None):
    e = os.environ.copy()
    if env:
        e.update(env)
    p = subprocess.run([sys.executable, str(SCRIPTS / script), *args], capture_output=True, text=True, env=e, cwd=cwd)
    return p.returncode, p.stdout, p.stderr


def make_skill(root, category, name, description=DESC, body=None, related=None, extra=None, version="0.1.0"):
    d = Path(root) / "skills" / category / name
    d.mkdir(parents=True, exist_ok=True)
    meta = [f"name: {name}", f'description: "{description}"', "metadata:", f"  category: {category}", f'  version: "{version}"']
    if related:
        meta.append(f'  related: "{related}"')
    body = body if body is not None else (
        f"# {name}\n\nA fixture skill that explains one procedure in enough words to be realistic.\n\n"
        "## When to use\n- When the fixture needs it.\n\n## Procedure\n1. Do the thing.\n\n## Verification\n- Check the thing.\n")
    (d / "SKILL.md").write_text("---\n" + "\n".join(meta) + "\n---\n\n" + body, encoding="utf-8")
    for rel, content in (extra or {}).items():
        f = d / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(content, encoding="utf-8")
    return d


def make_collection(root, name, skills, includes=None, description="A fixture collection for testing purposes.",
                    when="Use when the fixture needs a group of skills for tests."):
    c = Path(root) / "collections"
    c.mkdir(parents=True, exist_ok=True)
    data = {"name": name, "description": description, "when_to_use": when}
    if includes:
        data["includes"] = includes
    data["skills"] = skills
    (c / f"{name}.json").write_text(json.dumps(data, indent=2), encoding="utf-8")


def make_repo(root):
    """Minimal valid fixture repository with schemas, a VERSION file, two skills and a collection."""
    root = Path(root)
    (root / "schemas").mkdir(parents=True, exist_ok=True)
    for f in (REPO / "schemas").glob("*.json"):
        shutil.copy(f, root / "schemas" / f.name)
    (root / "VERSION").write_text("1.2.3\n", encoding="utf-8")
    make_skill(root, "alpha", "first-skill", related="second-skill")
    make_skill(root, "alpha", "second-skill")
    make_skill(root, "beta", "third-skill",
               extra={"references/notes.md": "# Notes\n\nReference material that is long enough to count as real guidance for the fixture skill. It describes the procedure in several sentences so the validator treats it as a genuine support file rather than a stub.\n"},
               body="# third-skill\n\nFixture with a reference.\n\n## When to use\n- When needed.\n\n## Verification\n- Check it.\n\n## References\n- [notes](references/notes.md)\n")
    make_collection(root, "pair", ["first-skill", "second-skill"])
    make_collection(root, "everything", ["third-skill"], includes=["pair"])
    return root


class TempCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()


def copy_repo(dst):
    """Copy the real repository (without VCS and caches) for mutation tests."""
    shutil.copytree(REPO, dst, ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"))
    return Path(dst)
