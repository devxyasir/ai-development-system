# Security policy

## Scope
This repository contains Markdown guidance and standard-library Python scripts. The parts most relevant to security are:
- `scripts/install-skills.py`: file copying, path handling, overwrite and removal behavior.
- `scripts/validate-*.py`, `scripts/build-collections.py`: parsing of untrusted repository content.
- Guidance content that could lead an agent to unsafe actions.

## Reporting a vulnerability
Please do not open a public issue for a vulnerability. Use the repository's private vulnerability reporting feature (GitHub: Security tab, "Report a vulnerability"). The maintainers must enable that feature, and should add a contact address here, before the repository is made public.

Include: what you found, how to reproduce it, the affected files and version (see `VERSION`), and the impact you expect.

## What to expect
Maintainers should acknowledge reports promptly, confirm or dispute the finding, and publish a fix and a changelog entry. Timelines are set by the maintainers.

## Supported versions
Only the latest released version receives fixes while the project is on 0.x.

## Hardening notes for users
- Read the installer's `--dry-run` output before installing.
- Skills influence what an agent does. Review any skill from any source before installing it, as you would review a script.
- Do not install into a directory shared with files you want to protect without checking the plan first.
- Never put credentials in skills, examples or issues.
