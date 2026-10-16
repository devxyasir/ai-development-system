# Workflow: Investigating performance

Requires: [core principles](../core/00-core-principles.md)

## When to use
Something is slow, uses too much memory or CPU, regressed, or must meet a latency or capacity target.

## Inspect first
- The exact scenario, metric and target
- Existing benchmarks, profiling or monitoring in the project
- Environment and data size where the problem occurs

## Load
Load only these. "Always" skills are mandatory; load the others only when their condition is true.

| Skill | When |
| --- | --- |
| [performance-analysis](../../skills/engineering/performance-analysis/SKILL.md) | Always |
| [database-engineering](../../skills/engineering/database-engineering/SKILL.md) | A query or data access pattern is suspected |
| [frontend-performance](../../skills/frontend/frontend-performance/SKILL.md) | The problem is page load or interaction speed in the browser |
| [animation-performance](../../skills/motion/animation-performance/SKILL.md) | The problem is animation smoothness |
| [observability-and-incident-response](../../skills/delivery/observability-and-incident-response/SKILL.md) | Production data or tracing is needed |

## Steps
1. Define the metric, scenario and target.
2. Make the scenario reproducible with realistic data; record environment details.
3. Measure a baseline several times; note variance.
4. Profile and rank where the time or memory goes.
5. Form a hypothesis about the largest cost; change one thing.
6. Re-measure with the same method; keep the change only if it helps and nothing regressed.
7. Repeat for the next largest cost until the target is met or returns diminish.
8. Add a guard (benchmark or budget) if regressions are likely.

## Decisions
| Situation | Do this |
| --- | --- |
| Cannot measure | Say results are estimates; do not report numbers |
| Cache proposed | Define key, expiry or invalidation and stampede behavior first |
| Gain is within noise | Revert the change |

## Artifacts
- Benchmark or scenario script
- Profile findings
- Before and after results

## Verify
- Before and after numbers come from the same method and environment
- Tests pass; memory and error rate did not regress
- Unmeasured claims are labeled as hypotheses

## If verification fails
1. No improvement: your hypothesis was wrong; return to the profile.
2. Results vary wildly: control the environment, increase runs, report the spread.

## Final report
- Metric, target, baseline and result
- Method and environment
- What changed
- Not measured; recommendations

Use the four-part format from [quality gate and reporting](../core/03-quality-gate-and-reporting.md); run the [final verification checklist](../checklists/final-verification.md) first.

## Related workflows
- [bug-fixing](bug-fixing.md): if the cause is a defect
