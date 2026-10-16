---
name: refactoring
description: "Restructures existing code safely without changing behavior: establishing safety nets with characterization tests, making small reversible steps, separating refactoring from feature work, removing duplication and dead code, improving names and boundaries, and verifying behavior is unchanged. Use when asked to refactor, clean up, simplify, modernize, or reorganize code or modules."
metadata:
  category: engineering
  version: "0.1.0"
  related: "testing-strategy, code-review, architecture-decisions, git-and-github"
---

# Refactoring

Refactoring changes structure, not behavior. The proof that behavior is unchanged is a test suite that passes before and after.

## When to use
- Code is hard to change, duplicated, tangled or unclear; preparing for a feature; moving or renaming modules.
- Not for: adding or changing behavior (do that in a separate step and commit), or large rewrites with no safety net.

## Procedure
1. **State the goal and the boundary:** what gets easier after this, and which files and public interfaces are in scope. Resist widening it.
2. **Check the safety net:** run existing tests and record the baseline. If coverage of the area is thin, add characterization tests that capture current behavior (including quirks), before changing structure.
3. **Plan small steps,** each one leaving the code working: rename, extract function or module, inline, move, replace conditional with polymorphism, introduce parameter object, delete dead code.
4. **Make one step, run the tests,** commit when green (if the user has authorized commits). If tests fail, undo the step instead of patching forward.
5. **Keep public contracts stable** (APIs, file formats, database schema, CLI flags) unless the task includes changing them; use deprecation and adapters when they must change.
6. **Do not mix** behavior changes, dependency upgrades, and formatting sweeps with the refactor; put them in separate steps.
7. **Search all usages** before moving or removing code (text search and type checker); for dynamic languages also search strings and configuration.
8. **Finish by re-running everything:** tests, lint, type check, build; review the full diff for accidental behavior changes.

## Decision rules
| Situation | Do this |
| --- | --- |
| No tests and no way to add them | Reduce scope to mechanical, tool-assisted changes (rename, move) and say the risk |
| Large module | Strangle: extract one seam at a time behind the existing interface |
| Duplicate code appears twice | Wait; extract at the third occurrence or when the duplication hides a bug |
| Performance claim for the refactor | Measure before and after; otherwise do not claim it |
| Style differences | Follow the project's formatter; do not reformat unrelated files |

## Common mistakes
- Changing behavior "while we are here".
- Huge diffs that cannot be reviewed.
- Removing code that is used dynamically (reflection, plugins, templates).
- Breaking public interfaces consumed elsewhere.

## Verification
- Tests that passed before still pass; characterization tests added where needed.
- The diff shows structural changes only; behavior-affecting hunks are listed and justified.
- Search for removed or renamed symbols finds no remaining references.

## Deliverables
Refactored code in reviewable steps, tests, a short note on what changed and what was deliberately left alone.

## References
This skill is self-contained. Load testing-strategy for writing characterization tests and code-review for reviewing the result.
