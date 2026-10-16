# Skills

Each skill is a folder containing a `SKILL.md` (YAML frontmatter plus instructions) and optional `references/`, `templates/`, `examples/` and `scripts/`. The format follows the Agent Skills specification so skills stay portable. See the [full index](SKILLS-INDEX.md) and the [collections](../collections/README.md).

## Layout
```text
skills/<category>/<skill-name>/
  SKILL.md            required: frontmatter + instructions
  references/         deeper material, read on demand
  templates/          reusable skeletons
  examples/           worked examples (optional)
  scripts/            small deterministic helpers (standard library only)
```
Categories: `design`, `motion`, `animation-production`, `frontend`, `engineering`, `specialist`, `delivery`, `tooling`. Installation flattens them: an installed skill is `<destination>/<skill-name>/`, so skill names are unique across categories.

## How skills load
Agents that support skills read only each skill's name and description at startup and load the body when a task matches, then read referenced files as needed. This is why descriptions state both what the skill does and when to use it.

## Rules for skills in this repository
- Folder name equals the frontmatter `name` (lowercase letters, digits, single hyphens).
- `description` is one double-quoted line, at most 1024 characters.
- `metadata` includes `category` (the parent folder), `version` and optional `related` (comma-separated skill names).
- `SKILL.md` has "When to use" and "Verification" sections and stays under 500 lines.
- Skills are self-contained: links stay inside the skill's folder; other skills are named, not linked.

Authoring help: the [skill-authoring skill](tooling/skill-authoring/SKILL.md) and [docs/creating-skills.md](../docs/creating-skills.md). Installing: [docs/installation.md](../docs/installation.md).
