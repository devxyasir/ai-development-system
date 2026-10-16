# Workflow: Releasing a version

Requires: [core principles](../core/00-core-principles.md)

## When to use
Publishing a versioned release of an application, package, library or CLI.

## Inspect first
- Current version files, changelog and tags
- Commits since the last release
- Packaging and publishing configuration
- Required checks and who may publish

## Load
Load only these. "Always" skills are mandatory; load the others only when their condition is true.

| Skill | When |
| --- | --- |
| [ci-cd-and-deployment](../../skills/delivery/ci-cd-and-deployment/SKILL.md) | Always |
| [git-and-github](../../skills/delivery/git-and-github/SKILL.md) | Always |
| [documentation-and-handoff](../../skills/delivery/documentation-and-handoff/SKILL.md) | Always |
| [cli-and-library-design](../../skills/specialist/cli-and-library-design/SKILL.md) | A package, CLI or library is being published |
| [desktop-and-mobile-development](../../skills/specialist/desktop-and-mobile-development/SKILL.md) | Signed installers or app store submission is involved |
| [security-review](../../skills/engineering/security-review/SKILL.md) | Dependencies or permissions changed |

## Steps
1. Review commits since the last release; classify as breaking, feature or fix.
2. Choose the version with semantic versioning (MAJOR, MINOR, PATCH) and say why.
3. Update the changelog and version files; write migration notes for breaking changes.
4. Run the full checks on the release commit and build from a clean checkout.
5. Test installation from the built artifact in a clean environment.
6. Complete the release checklist.
7. Tag and publish only with explicit authorization; otherwise give the exact commands.
8. Verify the published artifact installs and runs; announce.

## Decisions
| Situation | Do this |
| --- | --- |
| Breaking change present | MAJOR version bump with migration guide |
| Bad release published | Mark or yank it and publish a fixed patch; do not rewrite published tags |
| Not authorized to publish | Prepare everything and stop before the publish step |

## Artifacts
- Version and changelog updates
- Release checklist
- Release notes

## Verify
- Artifact built from the tagged commit installs in a clean environment
- Checks pass on the release commit
- Published result confirmed by an actual install or fetch (evidence), or marked unpublished

## If verification fails
1. Checks fail on the release commit: do not tag; fix and rebuild.
2. Publish partially fails: stop, record state, follow the provider's recovery steps.

## Final report
- Version and reason
- Checks and install test results
- What was published (with evidence) and what was left to the user
- Follow-ups

Use the four-part format from [quality gate and reporting](../core/03-quality-gate-and-reporting.md); run the [final verification checklist](../checklists/final-verification.md) first.

## Related workflows
- [deployment](deployment.md): to deploy the released version
