---
name: requirements-and-research
description: "Turns vague requests into requirements and researches unfamiliar technologies with evidence: separating facts, assumptions and constraints, identifying users and acceptance criteria, using official documentation, verifying that APIs and versions exist, comparing options, recording sources, and knowing when to stop. Use when a request is unclear, when a library or API is unfamiliar, when comparing technologies, or before writing a specification."
metadata:
  category: engineering
  version: "0.1.0"
  related: "architecture-decisions, development-operating-rules, product-design, ai-llm-engineering"
---

# Requirements and research

Good implementation starts with the right problem and verified facts. This skill produces a short requirements statement and an evidence-backed technology decision, without endless research.

## When to use
- The request is vague, the user's real goal is unclear, or acceptance criteria are missing.
- A library, API, framework version or service is unfamiliar or may have changed.
- Choosing between technologies; writing a specification.

## Procedure: requirements
1. **Restate the goal** and the user's problem (not the proposed solution).
2. **Separate facts, assumptions, constraints, preferences** using the [requirements template](templates/requirements-spec.md). A fact has a source; an assumption has a check.
3. **Identify stakeholders and roles,** business rules, data involved, integrations, volumes, and non-functional needs (performance, security, availability, accessibility, compliance).
4. **List edge cases and failure cases:** empty, huge, concurrent, invalid, unauthorized, offline.
5. **Write acceptance criteria** a tester could verify.
6. **Decide whether to ask.** Ask one focused question only when (a) the answer changes the outcome or architecture materially, (b) it cannot be found in the repository or documentation, and (c) a wrong guess is costly. Otherwise state the assumption and proceed.

## Procedure: research
1. **Write the questions** you need answered ("Does library X support Y in version Z?").
2. **Source order:** repository and installed package source and types, official documentation and changelog for the installed version, standards and specifications, the project's issue tracker, then reputable secondary sources. Prefer primary sources for API behavior, flags and configuration.
3. **Verify existence:** confirm that every method, flag, option, endpoint and package you plan to use actually exists in the version in use (read the source, run the help command, run a small test).
4. **Check currency:** versions, deprecations, security advisories, licenses, maintenance activity. Use the date from the environment; do not trust remembered versions.
5. **Compare options** with the [technology evaluation template](templates/technology-evaluation.md): same criteria for each, evidence for each cell.
6. **Record findings** in the [research findings template](templates/research-findings.md) with source, date accessed, and confidence.
7. **Stop when** you can answer: does it exist, how is it called, what are the limits, what does it cost, and what is the risk. More research after that is delay.
8. **Offline or tools unavailable:** say which claims come from memory and are unverified; mark them as such in the output; propose how to verify.

## Decision rules
| Situation | Do this |
| --- | --- |
| Documentation conflicts with the installed behavior | Trust a small reproducible test, note the discrepancy |
| Two options score similarly | Prefer the one already in the project, or the more reversible one |
| Benchmark claims | Cite measured sources or run your own; never invent numbers |
| Package seems unmaintained | Check last release, open issues, alternatives; flag the risk |
| Requirement conflict | Name the conflict, state the trade-off, ask the owner if it matters |

## Common mistakes
- Researching without a question, producing a report nobody needs.
- Citing memory as fact; inventing flags, endpoints or benchmark numbers.
- Skipping the existing codebase's patterns.
- Treating the first search result as authoritative.

## Verification
- Every assumption is labeled and has a validation plan or was validated.
- Each technical claim in the output has a source or is marked unverified.
- Acceptance criteria are testable.
- The recommendation states trade-offs and what would change it.

## Deliverables
Requirements specification, research findings with sources, technology evaluation if comparing, list of open questions.

## References
- [Requirements specification template](templates/requirements-spec.md)
- [Research findings template](templates/research-findings.md)
- [Technology evaluation template](templates/technology-evaluation.md)
