---
name: security-review
description: "Performs security design and review: threat modeling, trust boundaries, authentication and authorization, session and password handling, injection, XSS, CSRF, SSRF, path traversal, file uploads, secrets, dependencies and supply chain, encryption, logging of sensitive data, and secure deployment. Use when building features that handle user input, authentication, data or files, before release, or when asked for a security review."
metadata:
  category: engineering
  version: "0.1.0"
  related: "backend-api-design, database-engineering, ci-cd-and-deployment, ai-llm-engineering, code-review"
---

# Security review

Identify what an attacker can reach, what they could do with it, and which controls stop them. Never weaken a security control to simplify development or make tests pass.

## When to use
- New features that accept input, authenticate users, store personal data, handle files, call external services, or run user-influenced code.
- Pre-release reviews, dependency updates, incident follow-ups, or any request for a security review.

## Procedure
1. **Define scope and assets:** what data and capabilities matter (credentials, personal data, payments, admin functions).
2. **Draw trust boundaries:** where data enters (browser, API, files, third parties, model output) and where privilege changes. Everything crossing a boundary is untrusted until validated.
3. **Threat model** with the [threat model template](templates/threat-model.md) (for example STRIDE: spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege). List realistic threats per boundary and the control for each.
4. **Walk the [checklist](references/checklist.md)** for the areas touched.
5. **Review code and configuration** for each threat; search for known risky patterns (string-built queries, `eval`, shell commands with user input, disabled certificate checks, hard-coded secrets, permissive CORS).
6. **Run tools where available:** dependency audit (`npm audit`, `pip-audit` or equivalent), secret scanner, static analysis, container scan. Treat results as leads; confirm real risk.
7. **Test the controls:** attempt invalid input, another user's object, expired and forged tokens, oversized uploads, repeated requests, missing auth; write regression tests for fixed issues.
8. **Report findings** with severity (below), evidence, impact and a concrete fix; fix Critical and High before release.

## Severity
| Level | Meaning |
| --- | --- |
| Critical | Remote compromise, mass data exposure, or auth bypass with little effort |
| High | Significant data exposure or privilege escalation under realistic conditions |
| Medium | Needs unusual conditions or limited impact |
| Low | Hardening or defense in depth |

## Decision rules
| Situation | Do this |
| --- | --- |
| Input used in a query, command, path or HTML | Parameterize, avoid shell, resolve and verify paths, encode output for the context |
| Passwords | Hash with a modern memory-hard algorithm (Argon2id, scrypt) or bcrypt; never encrypt or log them |
| Secrets found in the repository | Treat as compromised: rotate, remove from history if needed, add scanning |
| Need to disable a check "temporarily" | Do not; fix the cause or ask for explicit authorization and record the risk |
| Model or tool output used to make decisions | Treat as untrusted input; authorization stays in deterministic code |
| Cryptography | Use vetted libraries and defaults; never design your own scheme |

## Common mistakes
- Authentication without object-level authorization.
- Relying on client-side checks, or CORS as an access control.
- Trusting file names, content types or URLs from users (path traversal, SSRF, stored XSS).
- Verbose errors exposing internals; secrets and personal data in logs.
- Ignoring dependency advisories until an incident.

## Verification
- Each identified threat has a control and a test or an explicit accepted risk.
- Tools run (name and result) or stated as unavailable.
- Regression tests added for fixed issues.
- Current guidance checked for the standards you cite (for example the current OWASP lists) when research tools are available; otherwise mark guidance as from memory.

## Deliverables
Threat model, findings list with severities, fixes and tests, residual risks.

## References
- [Security checklist](references/checklist.md)
- [Threat model template](templates/threat-model.md)
