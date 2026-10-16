# Technical design: <feature or system>

Author: <name> | Date: <date> | Status: <draft / reviewed / approved>

## Summary
<What is being built and why, in a few sentences>

## Requirements and constraints
- Functional: <summary or link to requirements>
- Non-functional: <performance, security, availability targets>
- Constraints: <platform, team, deadline>

## Current state
<Relevant existing architecture, with file or module references>

## Proposed design
- Components and responsibilities: <list>
- Data model changes: <entities, migrations>
- Interfaces: <APIs, events, with contracts or links>
- Key flows: <numbered steps for the main scenarios and failure scenarios>

## Alternatives considered
| Alternative | Why not |
| --- | --- |
| <option> | <reason> |

## Security and privacy
<Trust boundaries, authentication and authorization, sensitive data handling>

## Failure modes and recovery
| Failure | Behavior | Recovery |
| --- | --- | --- |
| <dependency down> | <degrade / queue / error> | <retry, manual step> |

## Observability
<Logs, metrics, health checks, alerts>

## Test plan
<Unit, integration, end-to-end, performance, migration tests>

## Rollout and rollback
<Steps, feature flags, migration order, rollback procedure>

## Risks and open questions
| Item | Impact | Owner |
| --- | --- | --- |
| <item> | <impact> | <who> |
