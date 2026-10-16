# Before commit

Commit only if the user asked for it or the project workflow clearly expects it. Otherwise prepare the commands.

- [ ] `git status` shows only files that belong to this change.
- [ ] I read `git diff` and `git diff --staged` line by line.
- [ ] No debug output, commented-out code, stray files, or unrelated formatting changes.
- [ ] No secrets, tokens, credentials, personal data or large generated files are staged; `.gitignore` is correct.
- [ ] Build, lint, type check and relevant tests pass; I read the output.
- [ ] New behavior has tests; no test was disabled or weakened.
- [ ] Documentation, configuration and changelog are updated where needed.
- [ ] The change is one logical unit; unrelated work is in a separate commit.
- [ ] The message has an imperative summary line and explains why when it is not obvious.
- [ ] After committing: `git show --stat HEAD` shows what I expect.

Never use `git add -A` without reviewing what it adds. Never amend or rewrite commits that others may have.
