# Workflow: Conducting a security review

Requires: [core principles](../core/00-core-principles.md)

## When to use
Reviewing a feature, change, repository or deployment for vulnerabilities, or hardening before release.

## Inspect first
- What the system does, its assets and users
- Entry points and trust boundaries (APIs, forms, files, third parties, model output)
- Authentication, authorization and session handling code
- Secrets handling, dependency manifests, CI and deployment configuration

## Load
Load only these. "Always" skills are mandatory; load the others only when their condition is true.

| Skill | When |
| --- | --- |
| [security-review](../../skills/engineering/security-review/SKILL.md) | Always |
| [code-review](../../skills/engineering/code-review/SKILL.md) | Always |
| [testing-strategy](../../skills/engineering/testing-strategy/SKILL.md) | Always |
| [backend-api-design](../../skills/engineering/backend-api-design/SKILL.md) | The review covers API endpoints |
| [ai-llm-engineering](../../skills/specialist/ai-llm-engineering/SKILL.md) | The system uses models or agents |
| [ci-cd-and-deployment](../../skills/delivery/ci-cd-and-deployment/SKILL.md) | Pipelines, secrets or deployment configuration are in scope |

## Steps
1. Define scope and assets.
2. Draw trust boundaries and list threats per boundary (threat model).
3. Walk the security checklist for each area in scope.
4. Review the code and configuration for each threat; search for risky patterns.
5. Run available tools (dependency audit, secret scan, static analysis) and triage results.
6. Test the controls with hostile input, other users' objects, bad tokens and oversized or repeated requests.
7. Rate findings by severity with evidence and fixes.
8. Apply fixes for Critical and High; add regression tests; rerun checks.

## Decisions
| Situation | Do this |
| --- | --- |
| Secret found in the repository | Treat as compromised: rotate, then clean history only with authorization |
| A check blocks development | Do not disable it; fix the cause or ask for explicit, recorded authorization |
| Standards cited | Check current editions when research tools are available; otherwise label as from memory |

## Artifacts
- Threat model
- Findings list with severities
- Fixes and regression tests
- Residual risk list

## Verify
- Each threat has a control and a test, or a recorded accepted risk
- Tools run (names and results) or stated unavailable
- Fixed issues have regression tests

## If verification fails
1. A fix breaks functionality: find a narrower control; do not remove the control.
2. Cannot test a control: say so and describe how to test it.

## Final report
- Scope and method
- Findings by severity with evidence
- Fixes made and tests added
- Residual risks; not reviewed

Use the four-part format from [quality gate and reporting](../core/03-quality-gate-and-reporting.md); run the [final verification checklist](../checklists/final-verification.md) first.

## Related workflows
- [pull-request](pull-request.md): to submit fixes
