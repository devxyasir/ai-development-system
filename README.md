# AI Development System

A modular instruction system and a library of installable Agent Skills that help AI coding agents (Claude, Codex-style agents and others) work like disciplined engineers: understand the task, inspect the code, research instead of guessing, make small safe changes, verify by running things, and report honestly.

It has two parts that work together:

- **Playbook** ([`AGENTS.md`](AGENTS.md), [`playbook/`](playbook/README.md)): critical rules, deterministic task routing, 22 workflows, checklists and decision aids. Short enough to stay useful in a small context window.
- **Skills** ([`skills/`](skills/README.md)): 43 independently installable skills in the portable `SKILL.md` format covering design, motion and animation, front end, engineering, specialist areas, delivery and tooling, grouped into [10 collections](collections/README.md).

Status: version 0.1.0, not yet published. See [compatibility](docs/compatibility.md) for exactly what has and has not been verified.

## Quick start

Requires Python 3.9 or newer (syntax-checked for 3.9, executed and tested only on 3.12). No packages to install.

```bash
git clone <your-fork-or-copy-of-this-repository> ai-development-system
cd ai-development-system
python scripts/list-skills.py
python scripts/install-skills.py --collection design-essentials --target project --project-dir /path/to/your/project --dry-run
```

Remove `--dry-run` to install. The installer never overwrites files it did not create; see the [installation guide](docs/installation.md).

## What is in the repository

| Path | Purpose |
| --- | --- |
| [`AGENTS.md`](AGENTS.md) | Vendor-neutral operating rules and routing summary (the entry point) |
| [`CLAUDE.md`](CLAUDE.md) | Imports AGENTS.md for Claude Code and adds Claude-specific notes |
| [`playbook/`](playbook/INDEX.md) | Core principles, routing, workflows, checklists, decision trees |
| [`skills/`](skills/SKILLS-INDEX.md) | Skills by category, plus a generated index and manifest |
| [`collections/`](collections/README.md) | Curated skill sets (design, motion, front end, back end, AI, games and more) |
| [`scripts/`](scripts/) | Installer, validators, index builder, skill lister |
| [`schemas/`](schemas/) | JSON schemas for collections and the generated manifest |
| [`tests/`](tests/) | Standard-library tests for the validators, installer and routing |
| [`docs/`](docs/architecture.md) | Architecture, installation, authoring, compatibility, maintenance |
| [`integrations/`](integrations/claude-code/README.md) | How to use the system with specific agents |

## Using it

1. **Skills only.** Install the skills you want into your agent's skills directory. Agents that support skills load a skill's body only when a task matches its description.
2. **Playbook and skills.** Copy `AGENTS.md`, `playbook/` and `skills/` into your project so the agent follows the routing and workflows. Claude Code users also copy `CLAUDE.md` and `.claude/rules/`.
3. **Manually.** Everything is Markdown. Read a workflow, then the skill files it links to.

## Collections

| Collection | Use when |
| --- | --- |
| design-essentials | Designing or redesigning an interface |
| motion-and-interaction | Adding purposeful motion to a product UI |
| creative-motion | Portfolios, campaign pages, cinematic or 3D experiences |
| frontend-professional | Professional web front-end work |
| backend-professional | Services, APIs, data and their security |
| full-stack-engineering | A feature from requirements to deployment |
| ai-engineering | LLM, retrieval, agent and ML features |
| game-development | Games and game features |
| platform-apps-and-tools | Desktop, mobile, CLI and library development |
| complete-development-system | A general baseline set |

## Checking the repository

```bash
python scripts/validate-instructions.py
python scripts/validate-skills.py
python scripts/build-collections.py --check
python -m unittest discover -s tests
```

## Contributing, security and license

- [Contributing](CONTRIBUTING.md), [code of conduct](CODE_OF_CONDUCT.md), [security policy](SECURITY.md), [changelog](CHANGELOG.md).
- **License: not yet chosen.** No license file is included because choosing one is the maintainer's decision. Until one is added, others have no permission to reuse the contents. Add a `LICENSE` file before publishing.

## Limits worth knowing

- Instructions are guidance, not enforcement. Use your agent's permission and hook features for rules that must never be broken.
- The validators check structure and links, not whether the advice is good. Review changes with a human or a second model.
- Compatibility claims are limited to what was checked against documentation; nothing here was exercised inside a live agent session during the build.
