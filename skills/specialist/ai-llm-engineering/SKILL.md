---
name: ai-llm-engineering
description: "Builds reliable AI features: choosing between deterministic code, a single model call, a workflow, retrieval or agents; prompt and structured-output design, tool calling, RAG, embeddings, memory and context management, evaluation sets, safety against prompt injection and data leakage, latency and cost, monitoring, and classic machine learning workflows. Use when adding LLM, RAG, agent, speech, vision or ML features to a product."
metadata:
  category: specialist
  version: "0.1.0"
  related: "security-review, testing-strategy, architecture-decisions, observability-and-incident-response, performance-analysis"
---

# AI and LLM engineering

Use a model only where it is the right tool, measure its behavior with an evaluation set, and treat model input and output as untrusted data.

## When to use
- Adding or changing LLM calls, retrieval-augmented generation, agents, embeddings, speech, OCR, vision or machine-learning features.
- Evaluating model quality, cost, latency or safety.
- Not for: ordinary logic that deterministic code handles better.

## Procedure
1. **Define the task and success criteria** in measurable terms (accuracy on a labeled set, groundedness, latency, cost per request).
2. **Choose the simplest sufficient approach** with the ladder below. Move up only when the lower rung fails the evaluation.
3. **Select the model and provider** from current official documentation (capabilities, context window, pricing, data-handling terms, rate limits); do not rely on remembered model names or prices. Keep the model name in configuration so it can change.
4. **Design the interface:** a clear instruction prompt, examples for tricky cases, structured output (a schema with validation), explicit handling of "unknown" or refusal.
5. **Build an evaluation set early:** representative real inputs, edge cases and adversarial cases with expected outputs or grading rubrics ([evaluation guide](references/evaluation.md)). Run it on every prompt, model or retrieval change.
6. **Validate outputs in code:** schema validation, allow-lists, range checks; retry or fall back on invalid output; never execute or trust output without validation.
7. **Secure the system:** treat user input, retrieved documents and tool results as untrusted; keep authorization in deterministic code; give tools least privilege; require confirmation for destructive actions; do not put secrets or other users' data into prompts; log without sensitive data.
8. **Control cost and latency:** smaller models for easy steps, caching for repeated calls, shorter context, batching, streaming for perceived speed, timeouts and limits.
9. **Plan for failure:** provider outages, rate limits, slow responses, model changes; fallbacks and clear user messages.
10. **Monitor in production:** quality signals, error and fallback rates, latency, cost, drift; keep versions of prompts, models and data for reproducibility.

## The ladder
| Rung | Use when |
| --- | --- |
| Deterministic code (rules, regex, SQL, classical ML) | The task is well-defined and rules or labeled data suffice |
| Single model call | Language understanding or generation, one step, bounded input |
| Workflow of fixed steps (chain, routing, parallel checks) | Several known steps; you control the sequence |
| Retrieval-augmented generation | Answers must come from your documents or fresh data |
| Single agent with tools | The sequence of steps cannot be fixed in advance |
| Multi-agent orchestration | Only if one agent demonstrably fails and the split is justified by evaluation |

## Decision rules
| Situation | Do this |
| --- | --- |
| Output feeds code | Structured output with schema validation |
| Facts must be correct | Retrieval with citations; verify against sources; allow "I don't know" |
| High-risk domain (medical, legal, financial) | Human review and clear limits; evaluation emphasizes failure cases |
| Fine-tuning proposed | First try better prompts, examples and retrieval; fine-tune only with a measured gap and quality data |
| Local or edge inference | Evaluate quantized models on your task; measure accuracy loss, memory, latency |
| Agent loops | Step and budget limits, logging of every tool call, idempotent tools |

## Common mistakes
- Adding a model because it is possible, not because deterministic code failed.
- No evaluation set, so changes cannot be judged.
- Trusting model output for authorization or execution.
- Putting retrieved text in the instruction channel without delimiting it as data.
- Leaking secrets or personal data into prompts and logs.

## Verification
- The evaluation set was run; results (scores and sample failures) are reported, with the version of prompt, model and data.
- Injection and failure cases were tested (hostile document, tool error, invalid output, provider timeout).
- Cost and latency measured on realistic inputs; state what was estimated.

## Deliverables
Design with chosen rung and reasons, prompts and schemas, evaluation set and results, safety notes, monitoring plan.

## References
- [Evaluation guide](references/evaluation.md)
- [RAG and agents](references/rag-and-agents.md): retrieval, embeddings, agent design, and machine-learning workflow notes.
