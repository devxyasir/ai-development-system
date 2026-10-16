---
name: skill-authoring
description: "Creates, edits and validates Agent Skills in the portable SKILL.md format: scoping, naming, writing trigger-focused descriptions, structuring instructions with progressive disclosure, adding references, templates and scripts, testing triggers, and running this repository's validators. Use when asked to create a new skill, improve an existing skill, fix skill validation errors, or contribute a skill to this repository."
metadata:
  category: tooling
  version: "0.1.0"
  related: "skill-installation, documentation-and-handoff, development-operating-rules"
---

# Skill authoring

A skill is a folder with a `SKILL.md` that teaches an agent one kind of work. The description decides whether it is used at all; the body decides whether it is used well.

## When to use
- Creating or revising a skill; fixing validator errors; adding a skill to this repository's collections.

## Format rules (Agent Skills specification)
- Directory name equals the `name` field: lowercase letters, digits and single hyphens, at most 64 characters, no leading or trailing hyphen.
- Required frontmatter: `name` and `description` (1 to 1024 characters, say what the skill does and when to use it). Optional: `license`, `compatibility` (up to 500 characters), `metadata` (string-to-string map), `allowed-tools` (experimental).
- Keep `SKILL.md` under 500 lines; move detail into files under `references/`, `templates/`, `examples/`, `scripts/` or `assets/` and link to them from `SKILL.md`, one level deep.
- Use relative links inside the skill. In this repository a skill must be self-contained: no links that leave its folder, and other skills are named, not linked.
- Frontmatter in this repository: write the description as one line in double quotes (avoids YAML pitfalls with colons), and include `metadata` with `category` (the parent directory name), `version` (semantic version) and optional `related` (comma-separated skill names).

## Procedure
1. **Scope it:** one coherent job. If it needs two different procedures, make two skills. Check existing skills for overlap and link by name instead of duplicating.
2. **Name it** with a short, specific noun phrase.
3. **Write the description first.** Include what it does, the situations and phrases that should trigger it, and what it is not for. Make it specific and slightly assertive; vague descriptions cause under-triggering. Test it: write three prompts that should trigger it and three near-misses that should not; check the description separates them.
4. **Write the body** from the [skill template](templates/skill-template.md): when to use, inputs needed, a numbered procedure, decision rules, common mistakes, verification, deliverables, references. Use imperative sentences. Explain why a rule matters when it is not obvious. Do not force this structure if the task needs another, but keep a "When to use" and a "Verification" section (the validator requires them).
5. **Make it actionable:** replace advice like "write clean code" with the steps that produce it and the checks that detect failure. Add small correct examples. Do not paste invented benchmark numbers or unverified API details; point to official sources.
6. **Split depth into references:** tables, long examples, code recipes and rubrics go in `references/`; reusable skeletons in `templates/`; deterministic helpers in `scripts/` (stdlib only, with usage in the docstring).
7. **Validate:** run `python scripts/validate-skills.py`, fix errors, then `python scripts/build-collections.py` to refresh the generated index and manifest, then `python scripts/build-collections.py --check`.
8. **Add to collections:** edit the relevant `collections/*.json`; keep collections focused.
9. **Test in an agent** if one is available: install into a scratch project (see skill-installation), give it a prompt that should trigger the skill, and check that it loads and that its steps are followed. State plainly if you could not.

## Decision rules
| Situation | Do this |
| --- | --- |
| Skill body grows past about 400 lines | Move detail into references |
| Same content needed by two skills | Keep it in one and name that skill in the other |
| Needs a script | Standard library only, document usage, make it safe to run without arguments (print help) |
| Needs tool access or network | Say so in `compatibility` |
| Content could be misused (security, offensive tooling) | Keep it defensive and educational; do not include exploit code |

## Common mistakes
- Descriptions that say what the skill is but not when to use it.
- Instruction files that restate general advice instead of procedures.
- Links outside the skill folder; support files not linked from `SKILL.md`.
- Unverified claims about tools, versions or platform behavior.

## Verification
- The validator passes with no errors; warnings reviewed.
- `build-collections.py --check` passes.
- Trigger test prompts written and evaluated against the description.
- Examples and commands in the skill were run or are marked as illustrative.

## Deliverables
The skill folder, collection entries, regenerated index and manifest, a short note of how it was validated.

## References
- [Skill template](templates/skill-template.md)
