# Lower-capability support

Requires: [core principles](00-core-principles.md)

This system is written so that a model with limited reasoning ability or a small context window can still follow it. This file lists the techniques it relies on and gives a compact procedure to use when you are struggling.

## Techniques built into the system
1. Critical rules sit at the start of AGENTS.md.
2. Each file covers one discipline and says when it applies.
3. Procedures are numbered where order matters; checklists cover easily forgotten items.
4. Routing is deterministic: the routing file maps a task type to one workflow, and the workflow names exactly which skills to load.
5. Conditional steps state their condition ("when", "if").
6. Each workflow lists what to do when verification fails.
7. Examples show good and bad behavior.

## Load only what you need
- Never read the whole repository of instructions. Read AGENTS.md, then the routing file, then the one workflow, then its "Always" skills. Load "If" skills only when their condition is true.
- If you lose context, re-read your progress record and the workflow's Steps section, not everything again.

## Compact procedure (use when unsure what to do next)
1. Say the goal in one sentence.
2. Look: list files, read the ones involved, find how to run tests.
3. Choose the workflow from the routing file.
4. Make a plan with at most five steps and a check for each.
5. Do step 1. Run its check. Read the result.
6. If the check fails: read the error, find the cause, fix the cause, run the check again. After two failed attempts, stop and re-read the error and the code; if still stuck, report what you know and ask.
7. Repeat for each step.
8. Run the final verification checklist.
9. Write the four-part report.

## Self-check questions before acting
- Did I read the file I am about to change?
- Do I know this function, flag or package exists in this version?
- Is this change needed for the task?
- Could this delete or overwrite something I did not create?
- Am I about to run something external (commit, push, deploy, delete)? Do I have permission?
- How will I know it works?

## Common failure patterns and the fix
| Pattern | Fix |
| --- | --- |
| Starts coding immediately | Stop. Restate the goal. Inspect first |
| Hallucinated function or option | Search the codebase or documentation; run help; test in isolation |
| Rewrites a big area for a small bug | Revert; make the smallest change that removes the cause |
| Claims success without running anything | Run the check; report the output |
| Forgets earlier requirements | Re-read the task and the acceptance criteria before the final report |
| Loops on the same failing approach | After two attempts, change approach or ask |
| Skips edge cases | Use the test case list in the testing-strategy skill |

## Fallback when you cannot complete the task
1. Stop at a state where the project still builds, or clearly mark that it does not.
2. Do not leave half-applied migrations, partial renames or broken imports without saying so.
3. Write the handoff using the project-handoff template in the documentation-and-handoff skill: what is done, what remains, exact next commands, known failures, risks.
4. Tell the user plainly that the task is incomplete.

## Honest limits
Say when you lack a tool (browser, network, database, device), when an answer comes from memory, and when you are unsure. An honest "I could not verify this" is more useful than confident text.
