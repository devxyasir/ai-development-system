# Creating skills

The detailed method is in the [skill-authoring skill](../skills/tooling/skill-authoring/SKILL.md). This page is the contributor checklist.

## Format rules
- Location: `skills/<category>/<skill-name>/SKILL.md`. The folder name equals `name`.
- `name`: lowercase letters, digits and single hyphens, at most 64 characters.
- `description`: one line in double quotes, at most 1024 characters. Say what the skill does and when to use it, using the words a user would say.
- `metadata`: `category` (the parent folder), `version` (for example `0.1.0`), optional `related` (comma-separated skill names).
- Body: a `# Title`, a `## When to use` section and a `## Verification` section, under 500 lines. Put long material in `references/`, skeletons in `templates/`, helpers in `scripts/`.
- Links stay inside the skill's folder. Name other skills; do not link to them.
- Avoid unfinished-work markers (the validator rejects them) and never include real credentials.

## Steps
1. Check for an existing skill that owns the topic.
2. Draft the description, then the three prompts that should trigger the skill and three that should not.
3. Write the procedure as numbered steps with decision rules, common mistakes, verification and deliverables. Explain the reason behind non-obvious rules.
4. Add references and templates only where they save the agent from inventing something.
5. Add the skill to a collection file in `collections/`.
6. Run:
   ```bash
   python scripts/build-collections.py
   python scripts/validate-skills.py
   python scripts/validate-instructions.py
   python scripts/build-collections.py --check
   python -m unittest discover -s tests
   ```
7. If the skill should be routed from the playbook, add it to the skill finder in `playbook/core/02-routing.md` and to the relevant workflow Load table. The instruction validator fails if a skill is unreachable from routing.
8. Update `CHANGELOG.md`.

## Quality bar
- Actionable: a reader can follow the steps without inventing the missing process.
- Honest: claims about tools and versions cite a source or are marked unverified.
- Scoped: one coherent job; a neighboring skill is named instead of duplicated.
- Verifiable: the Verification section lists checks that can really be run.
