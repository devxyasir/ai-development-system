# Installation

Three ways to use the skills. All of them are plain files; nothing is installed globally unless you choose a user-scope target.

## 1. Manual
Copy a skill folder into your agent's skills directory (for example `.claude/skills/ui-animation/`). The folder name must match the skill name.

## 2. Installer script
`scripts/install-skills.py` copies skills into a destination, tracks what it installed, and refuses to overwrite anything it did not create. Python 3.9 or newer (tested on 3.12 only), standard library only.

```bash
python scripts/install-skills.py --list
python scripts/install-skills.py --skill ui-animation --target project --dry-run
python scripts/install-skills.py --skill ui-animation --target project
python scripts/install-skills.py --collection motion-and-interaction --target project
python scripts/install-skills.py --all --target user --dry-run
python scripts/install-skills.py --collection design-essentials --target project --status
python scripts/install-skills.py --skill ui-animation --target project --update
python scripts/install-skills.py --skill ui-animation --target project --remove
python scripts/install-skills.py --skill debugging --dest ./some/agent/skills
```

### Targets
| `--target` | Destination | Notes |
| --- | --- | --- |
| `project` | `<project>/.claude/skills/` | Claude Code project scope, documented by Anthropic |
| `user` | `~/.claude/skills/` | Claude Code personal scope, documented by Anthropic |
| `agents-project` | `<project>/.agents/skills/` | Codex repository scope, per OpenAI documentation |
| `agents-user` | `~/.agents/skills/` | Codex personal scope; reported by secondary sources only, verify first |
| `--dest PATH` | any directory | For other agents that follow the Agent Skills format; check that agent's documentation |

Use `--project-dir PATH` when the project is not the current directory. Exactly one of `--target` or `--dest` is required.

### Safety behavior
- Writes only inside the destination; refuses a destination inside this repository's `skills/` directory or the repository root.
- Every installed skill gets a marker file (`.ai-development-system.json`) with a content hash.
- A directory is replaced (`--update`) or removed (`--remove`) only if it has the marker and has not been edited since.
- Existing directories without the marker, or edited ones, are reported as conflicts and skipped; the exit code is 3.
- `--force` first moves the conflicting directory to `<destination parent>/.skill-backups/<timestamp>/`, then replaces it. `--remove` never deletes directories without the marker, even with `--force`.
- `--dry-run` prints the plan and changes nothing.
- Exit codes: 0 success, 1 error, 2 bad arguments, 3 finished with skipped conflicts.

### Verify an installation
```bash
python scripts/install-skills.py --collection motion-and-interaction --target project --status
```
Each skill should report `current`. Then start a new agent session and give it a task that should trigger one of the skills. Some agents pick up project skills while running; others need a restart. If you did not test with a real agent, say so.

### Update
Pull the latest repository changes, then run the same install command with `--update`. Skills you edited locally are reported as modified and left alone; make changes in the source repository instead, or use `--force` knowingly.

## 3. The whole system in a project
Copy these into the project root: `AGENTS.md`, `playbook/`, and `skills/` (or install skills with the script). Claude Code users also copy `CLAUDE.md` and `.claude/rules/`. Then edit the "Maintaining this repository" section of `AGENTS.md` to match your project, because it refers to this repository's own validators.

If you only want the global rules without copying the playbook, install the `development-operating-rules` skill. It contains the critical rules, a routing table and the report format.

## Troubleshooting
| Symptom | Check |
| --- | --- |
| Skill not discovered | Folder name equals the `name` field; destination matches your agent's scope; restart the session |
| `conflict` in the plan | Compare with the existing directory; use `--force` only after reading the backup path it prints |
| `destination ... overlaps` error | Choose a destination outside this repository |
| Python errors on start | Use Python 3.9 or newer |
