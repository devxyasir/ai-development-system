# Claude Code

Notes were checked against the Claude Code documentation (see [compatibility](../../docs/compatibility.md)); the integration was not run in a live session.

## What Claude Code reads
- `CLAUDE.md` at the project root, and `@path` imports inside it. It does not read `AGENTS.md` by itself, so this repository's `CLAUDE.md` starts with `@AGENTS.md`.
- `.claude/rules/*.md`. Files with a `paths:` list load when Claude works with matching files; files without `paths` load at session start, so this repository only ships path-scoped rules.
- Skills in `.claude/skills/<name>/SKILL.md` (project) and `~/.claude/skills/<name>/SKILL.md` (personal).

## Option A: skills only (lowest cost)
```bash
python scripts/install-skills.py --collection complete-development-system --target project --project-dir /path/to/your/project --dry-run
```
Remove `--dry-run` to install. Then add one line to your project's own `CLAUDE.md`:
```markdown
At the start of any non-trivial task, use the development-operating-rules skill.
```
That skill carries the critical rules, a routing table and the report format.

## Option B: playbook and skills
Copy `AGENTS.md`, `CLAUDE.md`, `playbook/`, `skills/` and `.claude/rules/` into your project root (or merge them into your existing files; if your project already has a `CLAUDE.md`, add `@AGENTS.md` near the top and keep your own rules below it, since your own rules outrank the playbook). Edit the maintenance section of `AGENTS.md` to match your project.

## Verifying
- Start a session and run `/memory` to see which instruction files loaded.
- Ask for a task that should trigger a skill (for example "add a dialog animation") and check that the skill is used.
- Record what you saw. Do not record it as verified unless you ran it.

## Enforcement
Instructions guide behavior; they do not enforce it. If a rule must never be broken (for example no force pushes), configure Claude Code permission rules or hooks according to the current documentation.
