# Threat model: <system or feature>

Date: <date> | Owner: <name> | Scope: <what is included and excluded>

## Assets
| Asset | Why it matters | Sensitivity |
| --- | --- | --- |
| <e.g. customer records> | <impact if exposed or altered> | <high / medium / low> |

## Actors
| Actor | Capabilities and motivation |
| --- | --- |
| <anonymous visitor / authenticated user / admin / third-party service / malicious insider> | <what they can do> |

## Data flows and trust boundaries
- <Browser -> API (boundary 1): data sent, authentication>
- <API -> database (boundary 2): ...>
- <API -> third-party service (boundary 3): ...>

## Threats and controls
| ID | Boundary | Threat (STRIDE category) | Likelihood | Impact | Existing control | Gap and planned control | Test |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T1 | <1> | <e.g. tampering: user edits another user's order id> | <L/M/H> | <L/M/H> | <object-level check> | <none or action> | <test name> |

## Abuse cases
- <e.g. credential stuffing against login; upload of a script file; request to an internal URL>

## Accepted risks
| Risk | Reason accepted | Approved by | Review date |
| --- | --- | --- | --- |
| <risk> | <reason> | <who> | <date> |

## Actions
| Action | Severity | Owner | Due |
| --- | --- | --- | --- |
| <fix> | <Critical / High / Medium / Low> | <who> | <date> |
