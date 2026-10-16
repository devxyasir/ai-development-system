# Compatibility

This page separates what was checked against vendor documentation from what was not. Nothing in this repository was exercised inside a running agent session during the build, so "documented" means "the vendor's documentation says so", not "tested here".

Documentation checks were made on 2026-10-14.

## Canonical format
Skills follow the Agent Skills specification (directory with `SKILL.md`; required `name` and `description`; optional `license`, `compatibility`, `metadata`, `allowed-tools`; `name` must match the directory; description up to 1024 characters; `SKILL.md` recommended under 500 lines). Source: the specification at agentskills.io, read on the check date. The repository uses extra directories (`templates/`, `examples/`) that the specification allows as additional files, and keeps file references one level from `SKILL.md`.

## Agent matrix
| Agent | Instruction file | Skills location | Evidence | Tested here |
| --- | --- | --- | --- | --- |
| Claude Code | `CLAUDE.md` (not `AGENTS.md`); `@path` imports; `.claude/rules/*.md` with `paths:` scoping | `.claude/skills/<name>/SKILL.md` (project), `~/.claude/skills/<name>/SKILL.md` (personal) | Claude Code documentation (memory and skills pages) read on the check date | No |
| OpenAI Codex | `AGENTS.md` | `.agents/skills` in the repository | OpenAI Codex skills documentation, seen in search results; page not read in full | No |
| Codex personal scope | n/a | `~/.agents/skills` | Secondary sources only | No |
| Other agents (Cursor, Gemini CLI, GitHub Copilot, others) | Varies | Varies | Not checked by this project | No |
| claude.ai chat | n/a | Skills are managed in the product's own settings | Not checked; installer does not target it | No |

For agents marked "varies", use `--dest` with the directory that agent's own documentation names, or copy files manually.

## What each repository feature needs
| Feature | Needs |
| --- | --- |
| `AGENTS.md` rules | An agent that reads `AGENTS.md`, or a one-line instruction to read it |
| `CLAUDE.md` import of AGENTS.md | Claude Code (import syntax is Claude Code specific) |
| `.claude/rules/*.md` scoping | Claude Code only; other agents ignore these files harmlessly |
| Skill discovery | An agent implementing Agent Skills, or manual reading |
| Playbook routing | Any agent that can follow Markdown links and read files |
| Scripts | Python 3.9 or newer (executed on 3.12 only) |
| Visual QA and animation profiling steps | Browser or screenshot tooling; the skills say what to do when absent |

## Known limitations
- Instructions are advisory. For enforcement use the agent's permission rules or hooks.
- Hooks, permission rules and any agent settings are not shipped here because their formats change; consult the agent's documentation.
- Some skills mention newer web platform features (view transitions, scroll-driven animations, `@starting-style`, `light-dark()`, container queries). Each states that support must be checked; browser support was not re-verified for this release.
- Model names, prices and platform terms (engine licenses, store policies, standards editions) are deliberately not hard-coded; the skills tell agents to check current sources.

## Reporting verified compatibility
If you test an agent, open a pull request updating this table with: agent and version, date, what you did (install command, task given), and what happened. Evidence beats claims.
