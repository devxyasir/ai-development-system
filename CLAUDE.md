@AGENTS.md

# Claude Code specifics

Claude Code reads `CLAUDE.md`, not `AGENTS.md`, so the line above imports the shared operating rules. Everything in AGENTS.md applies. The notes below are only for Claude Code. They were checked against the Claude Code documentation; see [compatibility](docs/compatibility.md) for what was and was not verified.

## What loads automatically and what does not
- This file and the imported AGENTS.md load at session start. Keep both short.
- Files under `playbook/` do **not** load automatically. Read them by following the links in AGENTS.md. This is intentional: files in `.claude/rules/` without a `paths` field load at launch, so the playbook is not stored there.
- `.claude/rules/` in this repository contains only small path-scoped rules. They load when Claude works with matching files and point back to the right workflow and skills.

## Skills
- Install skills with `python scripts/install-skills.py` (see [installation](docs/installation.md)). Project skills go to `.claude/skills/<name>/SKILL.md`; personal skills to `~/.claude/skills/<name>/SKILL.md`.
- Installed skills are discovered by name and description; their bodies load when a task matches. The routing file still decides which skills to follow for a task.

## Working notes
- Use plan mode for large or risky tasks, then follow the plan in the loop.
- Instructions are context, not enforcement. For rules that must never be broken (for example blocking force pushes), use Claude Code permission rules or hooks; consult the Claude Code documentation for the current format.
- Use `/memory` to check which instruction files were loaded in a session.
