# Final verification

Run before reporting substantive work as done. Evaluate the areas that apply; write "not applicable" with a reason for the rest. Details are in the quality gate file.

## Requirements
- [ ] The requested outcome is delivered; each acceptance criterion is marked met, not met or unverified, with evidence.

## Architecture and code
- [ ] The change follows existing project patterns; any new abstraction or dependency is justified by a requirement.
- [ ] The diff is understandable; no dead code, debug output or unrelated changes.
- [ ] Important errors are handled; nothing is swallowed silently.

## Design (interfaces)
- [ ] Rendered and inspected at the relevant widths and states, or stated clearly as not rendered.
- [ ] Keyboard use, focus, contrast and responsive behavior checked.

## Data and security
- [ ] Inputs validated; permissions enforced on the specific object; secrets not exposed; data integrity preserved.

## Performance
- [ ] No obvious unbounded work (queries, loops, payloads); any performance claim has measured numbers.

## Tests
- [ ] Relevant checks ran (commands and results recorded): tests, lint, type check, build.
- [ ] Failure paths are covered; no test was disabled or weakened.

## Delivery
- [ ] Configuration, documentation, migrations and deployment notes are addressed where applicable.

## Truthfulness
- [ ] Every claim in my report has evidence.
- [ ] I listed what I did not verify and any tool I lacked.
- [ ] I did not claim actions (commit, push, deploy, publish) that I did not perform.

## Report
- [ ] Four parts: done, verified, not verified, risks and follow-ups.
