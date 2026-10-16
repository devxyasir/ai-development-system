# Maintenance policy

The system should improve without growing into a pile. These rules keep it small, consistent and checkable.

## Ownership: one topic, one owner
| Topic | Owner |
| --- | --- |
| Universal rules and honest reporting | `AGENTS.md` (short form), `playbook/core/00-core-principles.md` (long form) |
| Which workflow and skills to use | `playbook/core/02-routing.md` and each workflow's Load table |
| How to do a discipline well | The skill for that discipline |
| Templates | The skill that uses them |
| Skill list, indexes, manifest | `scripts/build-collections.py` (generated; never edit by hand) |
| Compatibility claims | `docs/compatibility.md` |

If two files explain the same thing, delete one and link to the other.

## Rules for changes
- Keep `AGENTS.md` and `CLAUDE.md` under 200 lines. Put detail in skills or the playbook.
- Add a file only when it solves a real organizational problem (a distinct procedure or audience). Do not create files to look complete.
- Keep technology-specific advice in skills or references; keep universal principles in the playbook.
- Prefer relative links so the repository can move. Skills must not link outside their folders.
- Do not add dependencies or infrastructure to manage the Markdown (the scripts use only the standard library).
- Do not hard-code facts that change (model names, prices, license terms, browser support); tell agents where to check.
- Every new skill is added to a collection, to the skill finder, and to at least one workflow when it applies.

## Required checks before merging a change
```bash
python scripts/validate-instructions.py
python scripts/validate-skills.py
python scripts/build-collections.py --check
python -m unittest discover -s tests
```
CI runs the same commands (`.github/workflows/validate.yml`).

## Review the parts scripts cannot check
Once per release and whenever a rule changes:
1. **Contradiction review.** Search for the same rule in `AGENTS.md`, the core principles, the workflows and the skills; confirm they say the same thing.
2. **Routing review.** Run the routing tests and add a scenario for any new task type. Read the workflow chosen for each scenario and confirm it loads the smallest sufficient set.
3. **Claims review.** For each statement about a tool, version or platform, confirm a source and a date, or mark it unverified.
4. **Size review.** Skills over about 400 lines move detail into references; unused references are deleted.
5. **Weak-model read.** Have a smaller model follow one workflow on a toy task and note where it went wrong; fix the instruction, not the model.

## Consolidating and retiring content
- Merge skills that always load together or overlap more than half.
- Retire guidance that is outdated or untested; record it in the changelog.
- When a platform feature changes, update `docs/compatibility.md` first.

## Versioning and releases
- Semantic versioning in `VERSION`: MAJOR for renamed or removed skills and changed installer behavior, MINOR for new skills or workflows, PATCH for fixes.
- Each skill carries its own `metadata.version`; bump it when the skill's behavior changes.
- Update `CHANGELOG.md` with every release. Tag and publish only with the maintainer's authorization.
- A release workflow is not included because the project publishes no package; add one only when there is a published artifact to build.

## After structural changes
Re-run the generated-file builder, then all checks. Fix broken links and routing gaps before anything else.
