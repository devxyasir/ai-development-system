# Other agents

This project has not verified any agents beyond those listed in [compatibility](../../docs/compatibility.md). The content is plain Markdown, so manual use works anywhere a model can read files.

## Manual use
1. Give the agent `AGENTS.md` (or paste its critical rules into the agent's own instruction field).
2. When a workflow tells it to load a skill, give it the linked `SKILL.md` and any reference it links to.
3. Keep the loaded set small; the point of the routing is to avoid loading everything.

## Agents that follow the Agent Skills format
Find the directory your agent documents for skills and install into it explicitly:
```bash
python scripts/install-skills.py --collection design-essentials --dest /path/from/the/agent/documentation --dry-run
```
Read the dry-run output, then remove `--dry-run`.

## Contributing verified notes
Add what you verified to [compatibility](../../docs/compatibility.md): agent and version, date, install command, the task you gave, and the observed result.
