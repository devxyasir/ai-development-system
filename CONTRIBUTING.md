# Contributing

Thank you for improving the system. The goals are accurate, actionable guidance that stays small enough to be used. More text is not better text.

## Before you start
- Read the [maintenance policy](docs/maintenance.md) and the [architecture notes](docs/architecture.md).
- Check whether the topic already has an owner (a skill or playbook file). Improve it instead of adding a near-duplicate.

## Adding or changing a skill
1. Follow the [skill-authoring skill](skills/tooling/skill-authoring/SKILL.md) and the [authoring guide](docs/creating-skills.md).
2. Put it in `skills/<category>/<skill-name>/`. The folder name must equal the `name` in `SKILL.md`.
3. Keep the skill self-contained: no links outside its folder; refer to other skills by name.
4. Add it to the relevant `collections/*.json` file.
5. Regenerate the index and manifest: `python scripts/build-collections.py`.
6. Run all checks:
   ```bash
   python scripts/validate-instructions.py
   python scripts/validate-skills.py
   python scripts/build-collections.py --check
   python -m unittest discover -s tests
   ```
7. If the skill makes claims about a tool, version or platform, cite the source in the pull request (official documentation preferred) and mark anything you could not verify.

## Changing the playbook
- Workflows must keep the required sections and a Load table with at most six "Always" skills.
- Do not copy skill content into the playbook; link to the skill.
- New files must be added to `playbook/INDEX.md` (the validator checks this).

## Pull requests
- One purpose per pull request. Describe what changed, why, and how you validated it (paste the validator output).
- Do not include real credentials, personal data or proprietary material in examples.
- Do not weaken a validator or test to make a change pass; fix the cause or discuss it in the pull request.

## Reporting problems
Use the issue templates. For security problems follow [SECURITY.md](SECURITY.md) instead of opening a public issue.

## License
The repository has no license yet (see the README). Contributions will be accepted under the license the maintainers choose; ask in an issue if this matters for you before contributing.
