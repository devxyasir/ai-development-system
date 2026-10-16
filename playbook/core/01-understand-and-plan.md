# Understand and plan

Requires: [core principles](00-core-principles.md)

Planning exists to prevent mistakes, not to produce documents. Match the effort to the task.

## 1. Restate the goal operationally
Write one sentence: "When this is done, <observable thing> is true." If you cannot, you do not understand the task yet.

## 2. Separate facts, assumptions, constraints, preferences
| Type | Meaning | Handling |
| --- | --- | --- |
| Fact | Verified from a file, command output or document | Cite the source |
| Assumption | Believed but unverified | Verify cheaply, or record it and proceed |
| Constraint | Must hold (platform, deadline, compatibility) | Design around it |
| Preference | Nice to have | Follow when cheap |

## 3. Decide whether to ask
Ask one focused question only if all three are true: (a) the answer changes the outcome or architecture materially, (b) it is not answerable from the repository, documentation or a quick test, (c) a wrong guess would be costly. Otherwise state the assumption in your first message and continue.

## 4. Size the task and plan accordingly
| Size | Signals | Plan |
| --- | --- | --- |
| Small | One file, clear behavior, low risk | One line: what you will change and how you will check it |
| Medium | Several files, some design choice | Short written plan: steps, acceptance criteria, checks |
| Large or risky | Cross-cutting, data or security impact, unfamiliar area | Full plan from the task plan template in the development-operating-rules skill, with risks and a rollback or fallback |

## 5. Decompose
- Break the work into steps that each leave the project working and can be verified alone.
- Order by dependency and risk: do the riskiest or most uncertain step early (a spike), not last.
- Identify what can fail and how you will notice.

## 6. Compare options only when it matters
Compare options when two or more are viable and the choice is costly to reverse. Use these criteria and say which ones decide:
complexity, maintainability, reliability, security, performance, usability, delivery time, operating cost, future flexibility.
| Situation | Rule |
| --- | --- |
| Easy to reverse | Pick the simplest and move on |
| Hard to reverse | Compare two or three options on the deciding criteria; record the decision (see the architecture-decisions skill) |
| Options score about equal | Choose the one already used in the project |
| Not enough evidence | Run a small experiment instead of arguing |

Do not build scoring spreadsheets for small decisions.

## 7. Progress record for long tasks
Keep a short record and update it at milestones, so you can recover after losing context:
```
Goal: <one sentence>
Done: <list>
In progress: <what and state>
Decisions: <decision: reason>
Tests run: <command: result>
Known failures: <list>
Next: <exact next actions>
```

## 8. Re-plan when evidence changes
Stop and revise the plan when: an assumption turns out false, a step takes more than twice the expected effort, a test reveals a design problem, or the user's constraints change. Say what changed.

## 9. Avoid analysis paralysis
- Set a stopping rule before researching (the questions to answer).
- If two attempts at the same approach fail, change the approach or ask for help; do not try a third identical variation.
- Prefer a small working step to a perfect plan.

## 10. Check the result against the acceptance criteria
Before reporting, list each acceptance criterion with met, not met, or unverified, and the evidence.
