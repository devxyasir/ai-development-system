# RAG, agents and ML notes

## Retrieval-augmented generation (RAG) pipeline
1. **Ingest:** parse documents (keep structure such as headings and tables), clean, attach metadata (source, date, permissions).
2. **Chunk:** split by structure (sections, paragraphs) with modest overlap; chunk size is a tunable parameter evaluated on retrieval metrics.
3. **Embed and index:** choose an embedding model suited to the languages and domain; store vectors with metadata in a vector index or a database with vector support. Re-embed when the model changes.
4. **Retrieve:** combine keyword search and vector search (hybrid) when exact terms matter; apply metadata and permission filters before ranking.
5. **Rerank:** a reranker can improve the top results; measure the gain against its latency and cost.
6. **Generate:** pass the passages as clearly delimited data, ask the model to answer only from them and to cite sources, allow "not found".
7. **Evaluate retrieval and generation separately** so you know which part fails.
Permissions: filter documents by the user's access before they reach the model; never rely on the model to hide content.

## Context and memory
- Keep prompts short and relevant; summarize or truncate history by rule; store long-term memory as retrievable records with a retention policy and user control; do not store sensitive data without a purpose.

## Tool calling
- Define small tools with precise names and typed parameters; validate arguments; return concise structured results; make tools idempotent or require confirmation; enforce authorization inside the tool using the real user's identity, not the model's claim.

## Agent design
- Bound the loop: maximum steps, time and cost; stop conditions.
- Log every step (model call, tool call, result) for debugging and audit.
- Sandbox code execution and file access; allow-list network destinations.
- Human approval for high-impact actions.
- Start with a workflow; add autonomy only where evaluation shows it is needed.

## Prompt injection defenses (layered)
1. Treat all external text as data; delimit it and tell the model it is untrusted.
2. Minimize tool privileges and data access (so a successful injection has little to take).
3. Validate outputs and tool arguments in code.
4. Confirm sensitive actions with the user.
5. Monitor and test with hostile documents. No prompt alone is a sufficient defense.

## Resource planning for local models
- Memory is roughly parameters times bytes per parameter, plus context cache and runtime overhead; lower precision (quantization) reduces memory at some accuracy cost. Measure accuracy, latency and memory on your task and hardware rather than relying on general claims.
- Batch requests where latency allows; use streaming; choose CPU or GPU by measured throughput and cost.

## Classic machine learning workflow
1. Define the target and a baseline (simple rule or majority class).
2. Split data into train, validation and test by the right unit (for example by user or time) to prevent leakage.
3. Establish metrics that match the real cost of errors.
4. Iterate on features and models; track experiments (data version, code version, parameters, seeds).
5. Evaluate once on the test set at the end; check performance across subgroups.
6. Package the model with its preprocessing; version it; monitor for drift; plan retraining.

## Computer vision, speech and OCR notes
- Evaluate on your own samples (lighting, accents, fonts, languages), including noisy ones.
- For OCR and speech, measure error rates and decide how errors are handled (confidence thresholds, human review).
- Respect privacy: faces, voices and documents are personal data.
