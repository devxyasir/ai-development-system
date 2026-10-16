---
name: skill-installation
description: "Installs, updates, removes and verifies skills from the ai-development-system repository using its installer script, with dry-run previews, safe conflict handling and the right destination for each agent (Claude Code project or personal scope, Codex repo or personal scope, or a custom directory). Use when asked to install skills or a collection, update installed skills, list what is available, or troubleshoot why a skill is not loaded."
metadata:
  category: tooling
  version: "0.1.0"
  related: "skill-authoring, documentation-and-handoff, development-operating-rules"
---

# Skill installation

Install skills into the location your agent reads, preview first, never overwrite files you did not create, and verify afterwards. The installer is `scripts/install-skills.py` in the ai-development-system repository (Python 3.9 or newer expected, tested on 3.12; standard library only).

## When to use
- Installing one skill, a collection or all skills; updating or removing installed skills; checking status; debugging missing skills.
- Not for: writing skills (skill-authoring).

## Procedure
1. **Find the repository checkout** that contains `scripts/install-skills.py` (clone it if the user wants that; do not run remote scripts you have not read).
2. **List what exists:** `python scripts/install-skills.py --list` and `python scripts/list-skills.py --collections`.
3. **Choose the target** with the table below. Prefer project scope for team conventions, personal scope for your own tools. Ask the user if the choice is not obvious; never install globally without being asked.
4. **Preview:** run the same command with `--dry-run` and read the plan.
5. **Install:** run without `--dry-run`. Conflicts (existing directories not installed by this tool, or edited since install) are skipped and reported; resolve them deliberately.
6. **Verify:** `python scripts/install-skills.py ... --status` should show `current`; then start a new agent session (some agents pick up changes live, others need a restart) and ask the agent to use the skill.
7. **Update later:** pull the repository, then rerun with `--update`. **Remove:** rerun with `--remove`.

## Targets
| `--target` | Destination | Agent and status |
| --- | --- | --- |
| `project` | `<project>/.claude/skills/` | Claude Code project scope (documented by Anthropic) |
| `user` | `~/.claude/skills/` | Claude Code personal scope (documented by Anthropic) |
| `agents-project` | `<project>/.agents/skills/` | Codex repository scope (documented by OpenAI) |
| `agents-user` | `~/.agents/skills/` | Codex personal scope (reported by secondary sources; verify) |
| `--dest PATH` | any directory | Other agents that follow the Agent Skills format; check that agent's documentation for its path |
Use `--project-dir PATH` to install into a project other than the current directory.

## Examples
```bash
python scripts/install-skills.py --skill ui-animation --target project --dry-run
python scripts/install-skills.py --collection motion-and-interaction --target project
python scripts/install-skills.py --all --target user --dry-run
python scripts/install-skills.py --collection design-essentials --target project --status
python scripts/install-skills.py --skill ui-animation --target project --update
python scripts/install-skills.py --skill ui-animation --target project --remove
```

## Safety behavior (what the installer guarantees)
- Writes only inside the chosen destination; refuses destinations inside the source repository.
- Each installed skill gets a marker file; only skills with an unmodified marker are updated or removed.
- Existing, unmarked or edited directories are skipped (exit code 3) unless `--force`, which first moves them to `<destination parent>/.skill-backups/<timestamp>/`.
- `--remove` never deletes unmarked directories.
- `--dry-run` changes nothing.

## Troubleshooting
| Symptom | Check |
| --- | --- |
| Skill not shown by the agent | Folder name equals the `name` in SKILL.md; destination matches the agent's scope; restart the session; project skills may require accepting a workspace trust prompt |
| Installer reports a conflict | Compare with the existing directory; use `--force` only after reading the backup path it will use |
| Wrong skill chosen automatically | Improve the skill description; see skill-authoring |
| Two copies of a skill at different scopes | The agent's precedence rules decide which wins; remove one |

## Common mistakes
- Installing everything into the personal scope, then wondering why a project behaves differently from its teammates.
- Skipping the dry run.
- Editing an installed copy, then losing the edit on update (the installer reports it as modified; edit the source repository instead).

## Verification
- `--status` reports `current` for each installed skill.
- A new agent session lists or uses the skill (state if no agent was available to test).
- No unrelated files changed (compare directory listings before and after).

## Deliverables
Installed skills, the commands run, the status output, and any conflicts left for the user.

## References
This skill is self-contained; the repository's installation guide is docs/installation.md in the repository.
