# Agents that read AGENTS.md

`AGENTS.md` is the canonical operating manual in this repository. Agents that read an `AGENTS.md` at the project root will find the critical rules and the routing summary.

## Setup
1. Copy `AGENTS.md`, `playbook/` and `skills/` into your project root.
2. Install skills where your agent expects them, if it supports skills (see [compatibility](../../docs/compatibility.md)):
   ```bash
   python scripts/install-skills.py --collection complete-development-system --target agents-project --project-dir /path/to/your/project --dry-run
   ```
   Remove `--dry-run` to install.
3. If your agent reads a different instruction file, add one line to it: "Read AGENTS.md and follow it."
4. Edit the "Maintaining this repository" section of `AGENTS.md` for your project.

## Notes
- Links in `AGENTS.md` are relative to its location, so keep `playbook/` and `skills/` next to it.
- Agents without skill discovery can still use the system: the routing file and workflows link to the skill files, which are ordinary Markdown.
- Tool-specific behavior of individual agents has not been verified by this project.
