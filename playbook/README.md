# Playbook

The playbook is the always-available part of the AI Development System: universal rules, routing, workflows, checklists and decision aids. The detailed discipline knowledge (design, motion, frontend, engineering, delivery) lives in the [skills](../skills/README.md), which the playbook routes to.

## How the pieces fit
| Layer | Where | Loaded |
| --- | --- | --- |
| Critical rules and routing summary | [AGENTS.md](../AGENTS.md) (imported by [CLAUDE.md](../CLAUDE.md)) | Always, at session start |
| Core principles, planning, routing, quality gate | `core/` | When the task needs them |
| Workflows (what to do, in order) | `workflows/` | One per task |
| Skills (how to do each discipline well) | `../skills/` | Only the ones the workflow names |
| Checklists and decision aids | `checklists/`, `references/` | At the moments they apply |

Nothing in `playbook/` is loaded automatically by any agent. That is deliberate: loading everything for every task wastes context and weakens critical rules. The agent follows links from AGENTS.md to the routing file, then to one workflow, then to that workflow's skills.

## Reading order for a task
1. [AGENTS.md](../AGENTS.md): critical rules (always).
2. [Routing](core/02-routing.md): pick the workflow and overlays.
3. The workflow: inspect, load skills, follow steps.
4. [Final verification](checklists/final-verification.md) and [reporting](core/03-quality-gate-and-reporting.md).

## Where things are
- Full file list with dependencies: [INDEX](INDEX.md).
- Skills catalog: [skills index](../skills/SKILLS-INDEX.md).
- How to install skills into an agent: [installation guide](../docs/installation.md).
- How to change this system without bloating it: [maintenance policy](../docs/maintenance.md).
- Honest compatibility notes: [compatibility](../docs/compatibility.md).

## Using the playbook without an agent feature
Copy this repository (or just `AGENTS.md`, `playbook/` and `skills/`) into a project. If your agent reads `AGENTS.md`, it will find the rules. If it reads only another file, add one line to that file: "Read AGENTS.md and follow it." Where an agent does not support skills, read the skill files manually when a workflow names them; they are ordinary Markdown.
