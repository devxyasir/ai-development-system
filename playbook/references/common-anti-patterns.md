# Common anti-patterns

Recognize these in your own work and in code you review.

## Process
| Anti-pattern | Why it hurts | Instead |
| --- | --- | --- |
| Coding before reading | Duplicates or breaks existing behavior | Inspect first; follow existing patterns |
| Researching without a question | Time lost, no decision | Write the questions and a stopping rule |
| Big-bang rewrite | No safety net, hard to review | Small verified steps |
| Declaring success unverified | False confidence | Run the checks and report outputs |
| Silent scope growth | Unreviewable changes | Note extra issues; ask before widening scope |

## Code
| Anti-pattern | Instead |
| --- | --- |
| Catch and ignore errors | Handle or surface them with context |
| Retry loops without limits or idempotency | Bounded retries with backoff only for idempotent calls |
| Copy-pasted logic in three places | Extract at the third occurrence |
| Abstraction with one implementation and no second use | Keep it concrete until a second use appears |
| Business logic in controllers or templates | Move rules to a service layer |
| Hard-coded environment values and secrets | Configuration and a secret store |
| Boolean parameter explosions | Named options or variants |

## Architecture
| Anti-pattern | Instead |
| --- | --- |
| Microservices for a small team and a single product | Modular monolith |
| Shared database tables between services | One owner per dataset, accessed through an interface |
| Layers that only forward calls | Remove the layer |
| Framework chosen before requirements | Requirements first, then a proportionate choice |

## Interface design
| Anti-pattern | Instead |
| --- | --- |
| Same purple gradient, navy dashboard and glass cards everywhere | Choose a direction from the audience and context (visual-design-direction skill) |
| Identical card grid on every page | Choose the structure per task |
| Animation on everything | Animate only what communicates something |
| Placeholder as the only label; color as the only signal | Visible labels; text and icons with color |

## Testing
| Anti-pattern | Instead |
| --- | --- |
| Tests that assert nothing meaningful | Assert behavior that could fail |
| Mocking the unit under test | Mock only boundaries |
| Sleeping to wait for async work | Wait for a condition |
| Disabling a failing test | Fix the cause, or report it |

## Security
| Anti-pattern | Instead |
| --- | --- |
| Authentication without object-level authorization | Check permission on the specific resource |
| Building queries or commands by string concatenation | Parameterize; use argument arrays |
| Trusting file names, URLs or model output | Validate, constrain, and keep authorization in code |
| Logging tokens or personal data | Redact and minimize |
| Disabling a check to make a build pass | Fix the cause or get explicit, recorded authorization |

## Delivery
| Anti-pattern | Instead |
| --- | --- |
| Deploy without a rollback plan | Write the rollback before deploying |
| Migrations that break the running version | Expand and contract |
| Claiming something is live without checking | Capture evidence from the live system |
| Documentation nobody has run | Follow the quick start in a clean environment |
