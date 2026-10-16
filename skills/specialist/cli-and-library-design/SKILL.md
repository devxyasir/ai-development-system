---
name: cli-and-library-design
description: "Designs command-line tools, libraries and SDKs: command and flag design, help output, configuration precedence, exit codes, streams, composability, error messages, public API surface, semantic versioning, deprecation, packaging, documentation and developer experience. Use when creating or changing a CLI, package, SDK or reusable module that other developers or scripts will depend on."
metadata:
  category: specialist
  version: "0.1.0"
  related: "testing-strategy, ci-cd-and-deployment, documentation-and-handoff, architecture-decisions"
---

# CLI and library design

Other people's code and scripts will depend on your interface. Keep it small, predictable, documented and versioned.

## When to use
- Creating or changing a CLI tool, library, SDK or shared package.
- Deciding what to expose, how to name it, and how to version changes.
- Not for: web or mobile apps (use their skills).

## Procedure
1. **Define the users and use cases:** who calls this (humans, scripts, other libraries) and the three most common tasks. Design the interface for those first.
2. **Design the public surface minimally:** expose only what is needed; everything public is a promise. Keep internals private by convention and by packaging.
3. **For a CLI:**
   - Command structure: `tool <noun> <verb>` or `tool <verb>`; consistent names; short and long flags (`-v`, `--verbose`).
   - Provide `--help` with a usage line, description and examples for each command, and `--version`.
   - Read input from arguments, files or standard input; write results to standard output and diagnostics to standard error so the tool composes in pipelines.
   - Offer machine-readable output (`--json`) for scripting; stable keys.
   - Exit codes: 0 for success, non-zero for failure, with documented distinct codes for distinct failures; usage errors return a usage code.
   - Be safe by default: confirm destructive actions, offer `--dry-run` and `--yes`; never prompt when not attached to a terminal.
   - Configuration precedence: command-line flags, then environment variables, then project config, then user config, then defaults; document it.
   - Color and progress only when output is a terminal; honor `NO_COLOR`.
   - Error messages say what failed, why, and what to try next, without stack traces unless in debug mode.
4. **For a library:**
   - Choose clear names, consistent argument order, and types; accept simple inputs, return simple outputs; avoid global state; make resources explicit (open, close, context managers).
   - Error handling: raise or return specific, documented error types; never swallow errors silently; never exit the process from library code.
   - Make it testable and mockable: dependencies injected; no hidden network or file access by default.
   - Provide type information where the language supports it.
   - Keep dependencies few; each is a cost for every user.
5. **Version with semantic versioning:** breaking changes bump MAJOR, new compatible features MINOR, fixes PATCH. Deprecate before removing: announce, warn at runtime, document the replacement, and remove in a later major release.
6. **Package properly:** metadata, license field (as chosen by the maintainer), supported language and platform versions, reproducible build, lockfile for apps (not libraries), minimal files in the package, install test from the built artifact in a clean environment.
7. **Document with runnable examples** (quick start, common tasks, reference, changelog, migration guide for breaking changes) and test the examples.
8. **Test the interface as users do:** CLI end-to-end tests (spawn the process, check output and exit codes); library tests through the public API; compatibility tests for supported versions.

## Decision rules
| Situation | Do this |
| --- | --- |
| Need to change behavior users may rely on | Treat as breaking unless it is clearly a bug fix; document it |
| Many options on one command | Group into subcommands or a config file |
| Interactive prompts requested | Provide non-interactive flags too |
| Output format change | Keep the old format or add a flag; scripts depend on it |
| Library needs a heavy dependency | Make it optional (extra) or reconsider |

## Common mistakes
- Writing human messages to standard output, breaking pipelines.
- Always exiting with code 0 or 1 with no distinction.
- Exposing internal types, then being unable to change them.
- Breaking changes in minor releases.
- Documentation that no one runs.

## Verification
- Run the CLI with `--help`, valid and invalid input, in a pipeline, and non-interactively; check exit codes and stream separation.
- Install the built package into a clean environment and run the quick start.
- Public API listing reviewed for accidental exposure; changelog and version updated.

## Deliverables
Interface specification, implementation, tests, documentation with examples, versioning and deprecation notes.

## References
This skill is self-contained. Load documentation-and-handoff for README and release notes, and ci-cd-and-deployment for publishing pipelines.
