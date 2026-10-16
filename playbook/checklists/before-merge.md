# Before merge

For pull requests and branch merges. See the git-and-github skill for the full procedure.

- [ ] The branch is current with the base and conflicts were resolved by understanding both sides.
- [ ] The description explains what, why, how it was tested, and risks.
- [ ] All required checks are green; none were bypassed or made optional.
- [ ] The diff against the base contains only intended changes (`git diff <base>...HEAD`).
- [ ] Review comments are answered; blocking items are resolved.
- [ ] Tests cover new behavior and at least one failure path.
- [ ] Migrations are included, tested and have a rollback or forward-fix plan.
- [ ] Breaking changes are documented with migration steps.
- [ ] Documentation and changelog are updated.
- [ ] Security-sensitive changes were reviewed (authentication, input, files, secrets, personal data).
- [ ] The merge strategy matches team convention.
- [ ] After merging: the pipeline is watched; the branch is deleted if appropriate.

Do not merge unless authorized by the user or the project's process.
