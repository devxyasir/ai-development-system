#!/usr/bin/env python3
"""Validate skills, collections, schemas and the generated manifest.

Usage: python scripts/validate-skills.py [--root PATH] [--strict] [--quiet]
Exit code 0 = no errors (warnings allowed unless --strict), 1 = errors found.
Standard library only.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import skilllib as sl  # noqa: E402

BANNED_RE = re.compile(r"\b(TODO|TBD|FIXME|lorem ipsum|coming soon|placeholder text)\b", re.I)
SECRET_RES = [
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    re.compile(r"\bsk-[A-Za-z0-9]{32,}\b"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,}\b"),
    re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"),
]
KNOWN_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
SUPPORT_DIRS = {"references", "templates", "examples", "assets", "scripts"}
WHEN_RE = re.compile(r"^#{2,3}\s+when to use", re.I | re.M)
VERIFY_RE = re.compile(r"^#{2,3}\s+(verification|verify|quality criteria|quality gate)", re.I | re.M)
MIN_SUPPORT_MD_BYTES = 150
MAX_FILE_BYTES = 200_000


class Report:
    def __init__(self):
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, where: str, msg: str):
        self.errors.append(f"ERROR   {where}: {msg}")

    def warn(self, where: str, msg: str):
        self.warnings.append(f"WARNING {where}: {msg}")


def read_text(path: Path):
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None


def check_text_content(path: Path, where: str, text: str, rep: Report):
    m = BANNED_RE.search(text)
    if m:
        rep.error(where, f"contains unfinished-work marker '{m.group(0)}'")
    for rx in SECRET_RES:
        if rx.search(text):
            rep.error(where, "looks like a real credential; use an obviously fake example value")
            break


def check_skill(skill: sl.Skill, names: set, root: Path, rep: Report):
    where = skill.path.relative_to(root).as_posix()
    for e in skill.errors:
        rep.error(where, e)
    if skill.errors:
        return
    meta = skill.meta
    for k in meta:
        if k not in KNOWN_KEYS:
            rep.warn(where, f"unknown frontmatter key '{k}' (portable skills should use only {sorted(KNOWN_KEYS)})")

    name = meta.get("name")
    if not isinstance(name, str) or not name:
        rep.error(where, "frontmatter 'name' is required")
    else:
        if name != skill.name:
            rep.error(where, f"name '{name}' must equal directory name '{skill.name}'")
        if len(name) > 64 or not sl.NAME_RE.match(name):
            rep.error(where, "name must be 1-64 chars of lowercase letters, digits and single hyphens")

    desc = meta.get("description")
    if not isinstance(desc, str) or not desc.strip():
        rep.error(where, "frontmatter 'description' is required")
    else:
        if len(desc) > 1024:
            rep.error(where, f"description is {len(desc)} chars (max 1024)")
        if len(desc) < 80:
            rep.error(where, "description is too short to trigger reliably (state what it does AND when to use it)")
        if not re.search(r"\bwhen\b|\buse (this|for)\b", desc, re.I):
            rep.warn(where, "description should say when to use the skill")
    comp = meta.get("compatibility")
    if comp is not None and (not isinstance(comp, str) or not 1 <= len(comp) <= 500):
        rep.error(where, "compatibility must be a string of 1-500 characters")

    md = meta.get("metadata")
    if not isinstance(md, dict):
        rep.error(where, "metadata map (category, version) is required by this repository")
    else:
        for k, v in md.items():
            if not isinstance(v, str):
                rep.error(where, f"metadata.{k} must be a string")
        if md.get("category") != skill.category:
            rep.error(where, f"metadata.category '{md.get('category')}' must equal parent directory '{skill.category}'")
        if not sl.SEMVER_RE.match(md.get("version", "")):
            rep.error(where, "metadata.version must be semantic version text such as 0.1.0")
        for rel in skill.related:
            if rel == skill.name:
                rep.error(where, "metadata.related lists the skill itself")
            elif rel not in names:
                rep.error(where, f"metadata.related names unknown skill '{rel}'")

    body = skill.body
    nlines = len((skill.skill_md.read_text(encoding="utf-8")).splitlines())
    if nlines > 500:
        rep.error(where, f"SKILL.md has {nlines} lines (max 500); move detail into references/")
    elif nlines > 400:
        rep.warn(where, f"SKILL.md has {nlines} lines; consider moving detail into references/")
    if not re.search(r"^#\s+\S", body, re.M):
        rep.error(where, "SKILL.md needs a top-level '# Title' heading")
    if not WHEN_RE.search(body):
        rep.error(where, "SKILL.md needs a '## When to use' section")
    if not VERIFY_RE.search(body):
        rep.error(where, "SKILL.md needs a '## Verification' (or Verify / Quality criteria) section")

    root_resolved = skill.path.resolve()
    for p in skill.path.rglob("*"):
        if p.is_symlink():
            rep.error(where, f"symlink not allowed inside a skill: {p.relative_to(skill.path)}")
    linked: set[Path] = set()
    skill_md_text = skill.skill_md.read_text(encoding="utf-8")
    for p in sl.iter_files(skill.path):
        rel = p.relative_to(root).as_posix()
        size = p.stat().st_size
        if size > MAX_FILE_BYTES:
            rep.warn(rel, f"file is {size} bytes; large files cost context when loaded")
        text = read_text(p)
        if text is None:
            continue
        check_text_content(p, rel, text, rep)
        if p.suffix == ".py":
            try:
                compile(text, str(p), "exec")
            except SyntaxError as exc:
                rep.error(rel, f"Python syntax error: {exc}")
        if p.suffix != ".md":
            continue
        if p != skill.skill_md and size < MIN_SUPPORT_MD_BYTES:
            rep.error(rel, f"only {size} bytes; support files must contain real guidance")
        for lineno, target in sl.extract_links(text):
            if sl.is_external(target):
                continue
            resolved = sl.resolve_link(p, target)
            try:
                resolved.relative_to(root_resolved)
            except ValueError:
                rep.error(f"{rel}:{lineno}", f"link escapes the skill directory (skills must be self-contained): {target}")
                continue
            if not resolved.exists():
                rep.error(f"{rel}:{lineno}", f"broken link: {target}")
            elif p == skill.skill_md:
                linked.add(resolved)
    for p in sl.iter_files(skill.path):
        parts = p.relative_to(skill.path).parts
        if len(parts) > 1 and parts[0] in SUPPORT_DIRS:
            rel_posix = p.relative_to(skill.path).as_posix()
            if p.resolve() not in linked and rel_posix not in skill_md_text:
                rep.warn(p.relative_to(root).as_posix(), "support file is not referenced from SKILL.md")


def check_collections(root: Path, skills: list, rep: Report):
    names = {s.name for s in skills}
    collections = sl.load_collections(root)
    schema = sl.load_schema(root, "collection.schema.json")
    used: set[str] = set()
    for cname, data in collections.items():
        where = f"collections/{cname}.json"
        if "__error__" in data:
            rep.error(where, data["__error__"])
            continue
        for e in sl.validate_json(data, schema):
            rep.error(where, e)
        if data.get("name") != cname:
            rep.error(where, f"name '{data.get('name')}' must equal file name '{cname}'")
        for inc in data.get("includes", []) or []:
            if inc not in collections:
                rep.error(where, f"includes unknown collection '{inc}'")
        for s in data.get("skills", []) or []:
            if s not in names:
                rep.error(where, f"unknown skill '{s}'")
        try:
            resolved = sl.resolve_collection(cname, collections)
        except sl.CollectionError as exc:
            rep.error(where, str(exc))
            continue
        if not resolved:
            rep.error(where, "collection resolves to zero skills")
        used.update(resolved)
    for s in sorted(names - used):
        rep.warn(f"skills/{s}", "skill is not part of any collection")


def check_manifest(root: Path, skills: list, rep: Report):
    mpath = root / "skills" / "manifest.json"
    if not mpath.exists():
        rep.error("skills/manifest.json", "missing; run: python scripts/build-collections.py")
        return
    try:
        data = json.loads(mpath.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        rep.error("skills/manifest.json", f"invalid JSON: {exc}")
        return
    for e in sl.validate_json(data, sl.load_schema(root, "skill-manifest.schema.json")):
        rep.error("skills/manifest.json", e)
    listed = {s.get("name") for s in data.get("skills", []) if isinstance(s, dict)}
    actual = {s.name for s in skills}
    if listed != actual:
        rep.error("skills/manifest.json", "stale manifest; run: python scripts/build-collections.py")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", default=str(sl.REPO_ROOT), help="repository root (default: this repository)")
    ap.add_argument("--strict", action="store_true", help="treat warnings as errors")
    ap.add_argument("--quiet", action="store_true", help="only print the summary line")
    args = ap.parse_args(argv)
    root = Path(args.root).resolve()
    rep = Report()
    skills = sl.discover_skills(root)
    if not skills:
        rep.error("skills/", "no skills found")
    names: dict[str, list] = {}
    for s in skills:
        names.setdefault(s.name, []).append(s.category)
    for n, cats in names.items():
        if len(cats) > 1:
            rep.error(f"skills/*/{n}", f"duplicate skill name in categories {cats}; names must be globally unique")
    name_set = set(names)
    for s in skills:
        check_skill(s, name_set, root, rep)
    check_collections(root, skills, rep)
    check_manifest(root, skills, rep)

    if not args.quiet:
        for line in rep.errors + rep.warnings:
            print(line)
    failed = bool(rep.errors) or (args.strict and bool(rep.warnings))
    print(f"validate-skills: {len(skills)} skills, {len(rep.errors)} errors, {len(rep.warnings)} warnings -> {'FAIL' if failed else 'OK'}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
