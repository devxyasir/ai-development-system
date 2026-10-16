#!/usr/bin/env python3
"""Install, update, remove and inspect skills from this repository.

Examples:
  python scripts/install-skills.py --list
  python scripts/install-skills.py --skill ui-animation --target project --dry-run
  python scripts/install-skills.py --collection motion-and-interaction --target project
  python scripts/install-skills.py --all --target user --dry-run
  python scripts/install-skills.py --skill ui-animation --target project --update
  python scripts/install-skills.py --skill ui-animation --target project --remove
  python scripts/install-skills.py --collection design-essentials --target project --status
  python scripts/install-skills.py --skill debugging --dest ./some/agent/skills

Safety rules (always on):
  * Nothing is written outside the chosen destination directory.
  * Existing directories are never overwritten silently. A directory is only replaced or
    removed if this tool installed it AND it has not been edited since (tracked by a marker
    file). Anything else is reported as a conflict and skipped.
  * --force replaces a conflicting directory only after moving it to a backup folder
    (<destination parent>/.skill-backups/<timestamp>/). --force never deletes unmanaged
    directories on --remove.
  * --dry-run prints the plan and changes nothing.

Exit codes: 0 success, 1 error, 2 bad arguments, 3 finished but some skills were skipped due to conflicts.
Standard library only.
"""
from __future__ import annotations

import argparse
import datetime
import difflib
import json
import os
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import skilllib as sl  # noqa: E402

MARKER = ".ai-development-system.json"
TARGETS = {
    "project": "<project>/.claude/skills   (Claude Code, project scope - documented)",
    "user": "~/.claude/skills            (Claude Code, personal scope - documented)",
    "agents-project": "<project>/.agents/skills  (Codex repo scope - documented by OpenAI)",
    "agents-user": "~/.agents/skills           (Codex personal scope - reported by secondary sources; verify)",
}
EXIT_OK, EXIT_ERROR, EXIT_CONFLICT = 0, 1, 3


class InstallError(Exception):
    pass


def resolve_dest(args) -> Path:
    if args.dest:
        return Path(args.dest).expanduser().resolve()
    project = Path(args.project_dir).expanduser().resolve()
    home = Path.home()
    return {
        "project": project / ".claude" / "skills",
        "user": home / ".claude" / "skills",
        "agents-project": project / ".agents" / "skills",
        "agents-user": home / ".agents" / "skills",
    }[args.target]


def check_dest(dest: Path, root: Path):
    src = (root / "skills").resolve()
    if dest == dest.parent:
        raise InstallError("refusing to use a filesystem root as destination")
    if dest == root.resolve() or dest == src or src in dest.parents or dest in src.parents:
        raise InstallError(f"destination {dest} overlaps the source repository's skills directory")
    if dest.exists() and not dest.is_dir():
        raise InstallError(f"destination {dest} exists and is not a directory")


def select(args, root: Path):
    skills = {s.name: s for s in sl.discover_skills(root) if not s.errors}
    chosen: list[str] = []
    cols = sl.load_collections(root)
    for c in args.collection:
        try:
            for n in sl.resolve_collection(c, cols):
                if n not in chosen:
                    chosen.append(n)
        except sl.CollectionError as exc:
            hint = difflib.get_close_matches(c, list(cols), n=3)
            raise InstallError(f"{exc}" + (f" (did you mean: {', '.join(hint)}?)" if hint else ""))
    for item in args.skill:
        for n in (x.strip() for x in item.split(",") if x.strip()):
            if n not in skills:
                hint = difflib.get_close_matches(n, list(skills), n=3)
                raise InstallError(f"unknown skill '{n}'" + (f" (did you mean: {', '.join(hint)}?)" if hint else ""))
            if n not in chosen:
                chosen.append(n)
    if args.all:
        chosen = list(dict.fromkeys(chosen + list(skills)))
    missing = [n for n in chosen if n not in skills]
    if missing:
        raise InstallError("collection references skills that do not exist or are invalid: " + ", ".join(missing))
    return [skills[n] for n in chosen]


def classify(skill: sl.Skill, dest: Path) -> str:
    """absent | current | outdated | modified | unmanaged"""
    target = dest / skill.name
    if not target.exists() and not target.is_symlink():
        return "absent"
    if target.is_symlink() or not target.is_dir():
        return "unmanaged"
    marker = target / MARKER
    if not marker.is_file():
        return "unmanaged"
    try:
        info = json.loads(marker.read_text(encoding="utf-8"))
        recorded = info["hash"]
    except (ValueError, KeyError, OSError):
        return "unmanaged"
    if sl.hash_dir(target, exclude={MARKER}) != recorded:
        return "modified"
    return "current" if recorded == sl.hash_dir(skill.path) else "outdated"


def write_skill(skill: sl.Skill, dest: Path, version: str, backup_root: Path | None):
    """Copy atomically via a temp directory; move any existing directory to backup_root if given."""
    tmp = dest / f".tmp-{skill.name}-{os.getpid()}"
    target = dest / skill.name
    try:
        if tmp.exists():
            shutil.rmtree(tmp)
        tmp.mkdir(parents=True)
        for f in sl.iter_files(skill.path):
            out = tmp / f.relative_to(skill.path)
            out.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, out)
        marker = {
            "tool": "ai-development-system",
            "name": skill.name,
            "version": version,
            "hash": sl.hash_dir(skill.path),
            "installed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        }
        (tmp / MARKER).write_text(json.dumps(marker, indent=2) + "\n", encoding="utf-8")
        if target.exists() or target.is_symlink():
            if backup_root is not None:
                backup_root.mkdir(parents=True, exist_ok=True)
                shutil.move(str(target), str(backup_root / skill.name))
            else:
                shutil.rmtree(target)
        tmp.rename(target)
    finally:
        if tmp.exists():
            shutil.rmtree(tmp, ignore_errors=True)


def run(args) -> int:
    root = Path(args.root).resolve()
    if args.list:
        skills = [s for s in sl.discover_skills(root) if not s.errors]
        cur = None
        for s in skills:
            if s.category != cur:
                cur = s.category
                print(f"\n[{cur}]")
            print(f"  {s.name}")
        print("\nCollections: " + ", ".join(sorted(sl.load_collections(root))))
        print("\nTargets:")
        for k, v in TARGETS.items():
            print(f"  --target {k:<15} {v}")
        return EXIT_OK

    if bool(args.target) == bool(args.dest):
        raise InstallError("choose exactly one of --target or --dest")
    if args.remove and args.update:
        raise InstallError("--remove and --update cannot be combined")
    if not (args.skill or args.collection or args.all):
        raise InstallError("choose what to act on: --skill NAME, --collection NAME or --all")

    dest = resolve_dest(args)
    check_dest(dest, root)
    chosen = select(args, root)
    version = sl.read_version(root)
    dry = args.dry_run
    prefix = "[dry-run] " if dry else ""
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_root = dest.parent / ".skill-backups" / stamp
    counts = {"installed": 0, "updated": 0, "unchanged": 0, "removed": 0, "conflicts": 0, "missing": 0}

    print(f"{prefix}destination: {dest}")
    if not dry and not args.status:
        pass  # directory is created lazily on first write

    for skill in chosen:
        state = classify(skill, dest)
        target = dest / skill.name
        if args.status:
            print(f"  {skill.name:<34} {state}")
            continue
        if args.remove:
            if state == "absent":
                print(f"{prefix}[not installed] {skill.name}")
                counts["missing"] += 1
            elif state == "unmanaged":
                print(f"{prefix}[refused] {skill.name}: {target} was not installed by this tool; remove it manually if intended")
                counts["conflicts"] += 1
            elif state == "modified" and not args.force:
                print(f"{prefix}[conflict] {skill.name}: edited since install; use --force to back it up and remove it")
                counts["conflicts"] += 1
            else:
                if state == "modified":
                    print(f"{prefix}[backup+remove] {skill.name} -> {backup_root / skill.name}")
                    if not dry:
                        backup_root.mkdir(parents=True, exist_ok=True)
                        shutil.move(str(target), str(backup_root / skill.name))
                else:
                    print(f"{prefix}[remove] {skill.name}")
                    if not dry:
                        shutil.rmtree(target)
                counts["removed"] += 1
            continue

        if state == "absent":
            print(f"{prefix}[install] {skill.name}")
            if not dry:
                dest.mkdir(parents=True, exist_ok=True)
                write_skill(skill, dest, version, None)
            counts["installed"] += 1
        elif state == "current":
            print(f"{prefix}[unchanged] {skill.name}")
            counts["unchanged"] += 1
        elif state == "outdated":
            if args.update or args.force:
                print(f"{prefix}[update] {skill.name}")
                if not dry:
                    write_skill(skill, dest, version, None)
                counts["updated"] += 1
            else:
                print(f"{prefix}[outdated] {skill.name}: newer version available; add --update")
                counts["unchanged"] += 1
        else:  # modified or unmanaged
            why = "edited since install" if state == "modified" else "exists but was not installed by this tool"
            if args.force:
                print(f"{prefix}[backup+replace] {skill.name} ({why}) -> {backup_root / skill.name}")
                if not dry:
                    dest.mkdir(parents=True, exist_ok=True)
                    write_skill(skill, dest, version, backup_root)
                counts["updated" if state == "modified" else "installed"] += 1
            else:
                print(f"{prefix}[conflict] {skill.name}: {target} {why}; skipped (use --force to back it up and replace)")
                counts["conflicts"] += 1

    if not (args.status or args.remove):
        names = {s.name for s in chosen}
        absent_related = sorted({r for s in chosen for r in s.related if r not in names and not (dest / r).exists()})
        if absent_related:
            print("note: related skills not selected and not installed: " + ", ".join(absent_related))

    if args.status:
        return EXIT_OK
    parts = [f"{v} {k}" for k, v in counts.items() if v]
    print(f"{prefix}install-skills: " + (", ".join(parts) if parts else "nothing to do"))
    return EXIT_CONFLICT if counts["conflicts"] else EXIT_OK


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__.split("\n\n")[0], epilog="\n".join(__doc__.split("\n\n")[1:]),
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=str(sl.REPO_ROOT), help="source repository root (default: this repository)")
    ap.add_argument("--list", action="store_true", help="list installable skills, collections and targets")
    ap.add_argument("--skill", action="append", default=[], metavar="NAME", help="skill to act on (repeatable, comma lists allowed)")
    ap.add_argument("--collection", action="append", default=[], metavar="NAME", help="collection to act on (repeatable)")
    ap.add_argument("--all", action="store_true", help="act on every skill")
    ap.add_argument("--target", choices=sorted(TARGETS), help="named destination (see --list)")
    ap.add_argument("--dest", help="explicit destination directory (for agents not covered by --target)")
    ap.add_argument("--project-dir", default=os.getcwd(), help="project root for project-scoped targets (default: current directory)")
    ap.add_argument("--update", action="store_true", help="replace outdated, unmodified, tool-installed skills")
    ap.add_argument("--remove", action="store_true", help="remove tool-installed, unmodified skills")
    ap.add_argument("--status", action="store_true", help="show install state (absent/current/outdated/modified/unmanaged)")
    ap.add_argument("--force", action="store_true", help="back up and replace/remove conflicting directories")
    ap.add_argument("--dry-run", action="store_true", help="print the plan; change nothing")
    args = ap.parse_args(argv)
    try:
        return run(args)
    except InstallError as exc:
        print(f"install-skills: error: {exc}", file=sys.stderr)
        return EXIT_ERROR


if __name__ == "__main__":
    sys.exit(main())
