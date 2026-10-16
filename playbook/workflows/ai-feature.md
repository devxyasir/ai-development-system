# Workflow: Building an AI or LLM feature

Requires: [core principles](../core/00-core-principles.md)

## When to use
Adding model-driven behavior: generation, classification, extraction, retrieval, agents, speech, vision or other machine learning.

## Inspect first
- Whether deterministic code could do the task
- Existing AI integrations, providers and prompt or evaluation conventions in the project
- Data involved and its sensitivity
- Latency, cost and quality expectations

## Load
Load only these. "Always" skills are mandatory; load the others only when their condition is true.

| Skill | When |
| --- | --- |
| [ai-llm-engineering](../../skills/specialist/ai-llm-engineering/SKILL.md) | Always |
| [security-review](../../skills/engineering/security-review/SKILL.md) | Always |
| [testing-strategy](../../skills/engineering/testing-strategy/SKILL.md) | Always |
| [requirements-and-research](../../skills/engineering/requirements-and-research/SKILL.md) | The provider, model or technique must be chosen or is unfamiliar |
| [performance-analysis](../../skills/engineering/performance-analysis/SKILL.md) | There are cost or latency targets to meet |
| [observability-and-incident-response](../../skills/delivery/observability-and-incident-response/SKILL.md) | The feature goes to production and needs monitoring |
| [product-design](../../skills/design/product-design/SKILL.md) | The feature has a user-facing interface |

## Steps
1. Define the task and measurable success criteria.
2. Choose the simplest rung that can work: deterministic code, a single call, a workflow, retrieval, then agents.
3. Pick provider and model from current official documentation; keep names in configuration.
4. Design prompts and structured output with schema validation; handle refusals and unknowns.
5. Build an evaluation set (typical, hard, adversarial) before tuning; record a baseline.
6. Implement; validate outputs in code; apply least-privilege tools and keep authorization in deterministic code.
7. Run the evaluation; iterate on prompts, retrieval or data; compare per category.
8. Test injection, invalid output, timeouts and provider errors.
9. Measure cost and latency on realistic inputs; add monitoring.

## Decisions
| Situation | Do this |
| --- | --- |
| Facts must be correct | Use retrieval with citations and allow 'not found' |
| Output triggers actions | Validate, constrain and require confirmation for destructive steps |
| Fine-tuning proposed | Try prompts, examples and retrieval first; fine-tune only for a measured gap |

## Artifacts
- Prompts and schemas
- Evaluation set and results
- Safety notes and monitoring plan

## Verify
- Evaluation run with results reported (versions of prompt, model, data)
- Injection and failure cases tested
- Cost and latency measured or marked as estimates

## If verification fails
1. Quality below target: inspect failures by category; fix retrieval or data before blaming the model.
2. Unstable results: control randomness, add validation and retries with limits, and increase evaluation size.

## Final report
- Approach chosen and why
- Evaluation results and sample failures
- Safety measures
- Cost, latency, and what was not measured

Use the four-part format from [quality gate and reporting](../core/03-quality-gate-and-reporting.md); run the [final verification checklist](../checklists/final-verification.md) first.

## Related workflows
- [api-integration](api-integration.md): for the provider connection
