# Test plan: <feature or change>

## Scope
- In scope: <behaviors>
- Out of scope: <items and reason>

## Risks
| Risk | Impact | Test type that covers it |
| --- | --- | --- |
| <risk> | <high/med/low> | <unit / integration / e2e ...> |

## Cases
| ID | Behavior | Type | Data or setup | Expected result |
| --- | --- | --- | --- | --- |
| 1 | <normal> | <unit> | <...> | <...> |
| 2 | <boundary> | <...> | <...> | <...> |
| 3 | <invalid input> | <...> | <...> | <...> |
| 4 | <forbidden access> | <...> | <...> | <...> |
| 5 | <dependency failure> | <...> | <...> | <...> |
| 6 | <repeat or concurrency> | <...> | <...> | <...> |

## Environment
- Commands: <how to run each level>
- Services needed: <database, queue, mocks>
- Data: <fixtures, seeds>

## Exit criteria
- [ ] All planned cases implemented and passing
- [ ] Full suite, lint and type checks pass
- [ ] No tests disabled or weakened

## Results
| Command | Result | Notes |
| --- | --- | --- |
| <command> | <pass / fail> | <details> |

## Not verified
- <item and reason>
