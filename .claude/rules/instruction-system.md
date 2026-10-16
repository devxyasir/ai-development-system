---
paths:
  - "playbook/**"
  - "skills/**"
  - "collections/**"
  - "schemas/**"
  - "scripts/**"
---

# When editing the instruction system itself

- Follow [maintenance](../../docs/maintenance.md): avoid duplication, keep skills self-contained, add files only when they solve a real organizational problem.
- New or changed skills: follow the skill-authoring skill; skills must not link outside their own folder.
- Before reporting done, run `python scripts/validate-instructions.py`, `python scripts/validate-skills.py`, `python scripts/build-collections.py --check` and `python -m unittest discover -s tests`, and report the results.
