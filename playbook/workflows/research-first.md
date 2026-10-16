# Workflow: Researching an unfamiliar technology

Requires: [core principles](../core/00-core-principles.md)

## When to use
A library, framework, API, service or technique is unfamiliar, may have changed, or must be chosen among alternatives, before implementation starts.

## Inspect first
- What the project already uses for the same purpose
- The versions installed or targeted
- Which research tools are available (web access, repository search, terminal, documentation)

## Load
Load only these. "Always" skills are mandatory; load the others only when their condition is true.

| Skill | When |
| --- | --- |
| [requirements-and-research](../../skills/engineering/requirements-and-research/SKILL.md) | Always |
| [architecture-decisions](../../skills/engineering/architecture-decisions/SKILL.md) | You are choosing between technologies or structures |
| [security-review](../../skills/engineering/security-review/SKILL.md) | The candidate handles data, authentication or runs third-party code |
| [ai-llm-engineering](../../skills/specialist/ai-llm-engineering/SKILL.md) | The topic is a model, provider or AI technique |

## Steps
1. Write the questions you need answered and the stopping rule.
2. Search the repository and installed packages first.
3. Read official documentation and changelog for the version in use; prefer primary sources.
4. Verify by running a small test or reading source that the methods, flags and options you plan to use exist.
5. Check currency: versions, deprecations, advisories, license, maintenance.
6. If comparing options, fill a technology evaluation with evidence per cell.
7. Record findings with sources and dates; mark anything from memory as unverified.
8. Stop when the questions are answered; summarize and recommend.

## Decisions
| Situation | Do this |
| --- | --- |
| Documentation and behavior disagree | Trust a small reproducible test and note the discrepancy |
| No web or documentation access | State that findings are from memory and unverified; give the way to verify |
| Options score about equal | Prefer the one already in the project or the more reversible one |

## Artifacts
- Research findings with sources
- Technology evaluation when comparing
- Open questions

## Verify
- Every technical claim has a source or is labeled unverified
- Anything you plan to call was confirmed to exist in the version used
- Recommendation states trade-offs

## If verification fails
1. Sources conflict: run an experiment; report both sources and the result.
2. Cannot confirm a capability: say so and propose a spike or an alternative.

## Final report
- Answer to each question with confidence
- Sources and dates
- Unverified items
- Recommendation and what would change it

Use the four-part format from [quality gate and reporting](../core/03-quality-gate-and-reporting.md); run the [final verification checklist](../checklists/final-verification.md) first.

## Related workflows
- [feature-development](feature-development.md): once the technology is chosen
