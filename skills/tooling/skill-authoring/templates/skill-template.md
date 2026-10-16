# Skill template

Copy this into `skills/<category>/<skill-name>/SKILL.md`, starting with the frontmatter block below, then fill every <field>. Delete sections that genuinely do not apply, but keep "When to use" and "Verification".

```markdown
---
name: <skill-name>
description: "<What the skill does, then when to use it, including trigger phrases and situations. Not for: <exclusions>.>"
metadata:
  category: <parent directory name>
  version: "0.1.0"
  related: "<skill-a>, <skill-b>"
---

# <Skill title>

<One or two sentences: the job this skill does and the principle behind it.>

## When to use
- <situation>
- Not for: <exclusion, with the skill to use instead>

## Inputs needed
- <what to know or inspect before starting>

## Procedure
1. <action, with the reason when not obvious>
2. <action>

## Decision rules
| Situation | Do this |
| --- | --- |
| <situation> | <action> |

## Common mistakes
- <mistake>

## Verification
- <check that can actually be run or observed>
- State what was not verified.

## Deliverables
<what the agent produces>

## References
- [<reference title>](references/<file>.md): <when to read it>
- [<template title>](templates/<file>.md)
```

## Description checklist
- States what it does and when to use it.
- Contains the words a user would actually say.
- Names an exclusion if a neighboring skill exists.
- At most 1024 characters, one line, in double quotes, no double quotes inside.

## Trigger test
Write three prompts that should load the skill and three that look similar but should not. Read the description as the agent would (it sees only the name and description) and decide for each prompt whether it would load the skill. Rewrite the description until all six come out right.
