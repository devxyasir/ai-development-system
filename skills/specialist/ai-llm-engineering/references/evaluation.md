# Evaluation guide

## Build the evaluation set
1. Collect real or realistic inputs: typical (most), hard (ambiguous, long, multilingual), adversarial (injection attempts, out-of-scope requests), and known past failures.
2. Label expected outputs or write a rubric (what a good answer must include and must not include). Keep a held-out portion you do not tune on.
3. Size: start with dozens of items that cover each category; grow it as failures appear. Quality and coverage matter more than count.
4. Version the set with the code.

## Metrics by task
| Task | Metrics |
| --- | --- |
| Classification or extraction | Precision, recall, F1 per class; exact match for fields |
| Retrieval | Recall at k, mean reciprocal rank, share of queries with a relevant passage in the top k |
| Generation grounded in documents | Faithfulness (claims supported by sources), answer relevance, citation correctness |
| Summarization or writing | Rubric scores; human review of a sample |
| Agents | Task success rate, steps taken, tool-call correctness, cost and time per task, safety violations |
| Speech or OCR | Word or character error rate |

## Automated judging
- A model can grade outputs against a rubric. Calibrate it: compare its grades with human grades on a sample, check for bias toward longer answers, and use a different model or prompt from the one being evaluated where practical.
- Prefer exact or programmatic checks when the task allows.

## Running evaluations
- Run on every change to prompt, model, retrieval settings or data.
- Report the aggregate and the list of failures; compare against the previous run and a simple baseline.
- Control randomness (low temperature where suitable, multiple runs for noisy tasks) and record model identifiers and parameters.

## Regression policy
- Fixed failures become permanent test cases.
- A change that improves the average but breaks an important category is not an improvement; examine per-category results.

## Online monitoring
- Sample production traffic for review, track user feedback, fallback and refusal rates, latency and cost, and re-run evaluations periodically to catch model drift or provider changes.
