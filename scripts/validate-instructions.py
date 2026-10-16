#!/usr/bin/env python3
"""Validate the instruction system: AGENTS.md, CLAUDE.md, playbook, scoped rules, docs.

Usage: python scripts/validate-instructions.py [--root PATH] [--strict] [--quiet]
Exit code 0 = no errors, 1 = errors (or warnings with --strict). Standard library only.

Mechanical checks only: required files, broken links, unfinished-work markers, required
sections in workflows, routing coverage, index coverage, circular 'Requires:' chains,
size limits, scoped-rule frontmatter, imports that would defeat selective loading, and
documented commands that do not match the scripts. Semantic contradictions and the quality
of the guidance still need human or model review (see docs/maintenance.md).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import skilllib as sl  # noqa: E402

CORE = ["00-core-principles", "01-understand-and-plan", "02-routing", "03-quality-gate-and-reporting", "04-lower-capability-support"]
CHECKLISTS = ["before-coding", "before-commit", "before-merge", "before-deployment", "before-release", "final-verification"]
REFERENCES = ["decision-trees", "common-anti-patterns"]
WORKFLOWS = ["new-project", "existing-project", "feature-development", "bug-fixing", "refactoring", "research-first", "ui-implementation",
             "animation-implementation", "backend-feature", "database-migration", "api-integration", "ai-feature", "game-feature",
             "performance-investigation", "security-review", "testing-and-verification", "pull-request", "code-review", "deployment",
             "release", "incident-response", "handoff"]
REQUIRED = (["AGENTS.md", "CLAUDE.md", "README.md", "CONTRIBUTING.md", "SECURITY.md", "CODE_OF_CONDUCT.md", "CHANGELOG.md", "VERSION",
             "playbook/README.md", "playbook/INDEX.md", "skills/README.md", "skills/SKILLS-INDEX.md", "collections/README.md",
             "docs/architecture.md", "docs/installation.md", "docs/creating-skills.md", "docs/compatibility.md", "docs/maintenance.md"]
            + [f"playbook/core/{n}.md" for n in CORE] + [f"playbook/checklists/{n}.md" for n in CHECKLISTS]
            + [f"playbook/references/{n}.md" for n in REFERENCES] + [f"playbook/workflows/{n}.md" for n in WORKFLOWS])
WORKFLOW_HEADINGS = ["When to use", "Inspect first", "Load", "Steps", "Verify", "If verification fails", "Final report"]
BANNED_RE = re.compile(r"\b(TODO|TBD|FIXME|lorem ipsum|coming soon|placeholder text)\b", re.I)
SECRET_RES = [re.compile(r"AKIA[0-9A-Z]{16}"), re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
              re.compile(r"\bsk-[A-Za-z0-9]{32,}\b"), re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,}\b")]
BAD_INSTRUCTION_RE = re.compile(r"^\s*(?:[-*]|\d+\.)?\s*(always (?:commit|push|deploy|merge)\b|skip (?:the )?tests\b|ignore (?:all )?previous instructions)", re.I)
MAX_ROOT_LINES = 200
MAX_PLAYBOOK_LINES = 400
WARN_PLAYBOOK_LINES = 250
MAX_ALWAYS = 6
MAX_LOAD_TOTAL = 14


class Report:
    def __init__(self):
        self.errors, self.warnings = [], []

    def error(self, where, msg):
        self.errors.append(f"ERROR   {where}: {msg}")

    def warn(self, where, msg):
        self.warnings.append(f"WARNING {where}: {msg}")


def md_files(root: Path):
    skip = {".git", "node_modules", "__pycache__", ".venv", "venv"}
    for p in sorted(root.rglob("*.md")):
        rel = p.relative_to(root)
        if any(part in skip for part in rel.parts):
            continue
        if rel.parts[0] == "skills" and len(rel.parts) > 2:
            continue  # skill internals are validated by validate-skills.py
        yield p


def section(text: str, heading: str) -> str:
    m = re.search(rf"^##\s+{re.escape(heading)}\s*$", text, re.M | re.I)
    if not m:
        return ""
    rest = text[m.end():]
    n = re.search(r"^##\s+", rest, re.M)
    return rest[: n.start()] if n else rest


def check_required(root, rep):
    for rel in REQUIRED:
        if not (root / rel).is_file():
            rep.error(rel, "required file is missing")
    if not (root / "LICENSE").exists():
        rep.warn("LICENSE", "no license file: the maintainer must choose a license before publishing (this tool does not pick one)")


def check_links_and_markers(root, files, rep):
    for p in files:
        rel = p.relative_to(root).as_posix()
        text = p.read_text(encoding="utf-8")
        m = BANNED_RE.search(text)
        if m:
            rep.error(rel, f"contains unfinished-work marker '{m.group(0)}'")
        if any(rx.search(text) for rx in SECRET_RES):
            rep.error(rel, "looks like a real credential; use an obviously fake example")
        for lineno, target in sl.extract_links(text):
            if sl.is_external(target):
                continue
            resolved = sl.resolve_link(p, target)
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                rep.error(f"{rel}:{lineno}", f"link leaves the repository: {target}")
                continue
            if not resolved.exists():
                rep.error(f"{rel}:{lineno}", f"broken link: {target}")
        for n, line in enumerate(text.splitlines(), 1):
            if rel.startswith(("playbook/", "AGENTS.md", "CLAUDE.md")) and BAD_INSTRUCTION_RE.search(line):
                rep.error(f"{rel}:{n}", "instruction contradicts the core rules (unauthorized action or skipped verification)")


def check_entry_points(root, rep):
    agents = root / "AGENTS.md"
    claude = root / "CLAUDE.md"
    for p in (agents, claude):
        if p.is_file():
            n = len(p.read_text(encoding="utf-8").splitlines())
            if n > MAX_ROOT_LINES:
                rep.error(p.name, f"{n} lines (max {MAX_ROOT_LINES}); entry files are loaded in full, keep them short")
    if agents.is_file():
        text = agents.read_text(encoding="utf-8")
        crit = section(text, "Critical rules (always apply)")
        count = len(re.findall(r"^\d+\.\s+\*\*", crit, re.M))
        if count < 8:
            rep.error("AGENTS.md", f"'Critical rules (always apply)' section has {count} numbered rules; expected at least 8")
        first_rule_pos = text.find("## Critical rules")
        if first_rule_pos == -1 or first_rule_pos > 1200:
            rep.error("AGENTS.md", "critical rules must appear near the top of the file")
    if claude.is_file():
        lines, in_fence, imports = claude.read_text(encoding="utf-8").splitlines(), False, []
        for line in lines:
            if sl.FENCE_RE.match(line):
                in_fence = not in_fence
            elif not in_fence and re.match(r"^@\S+", line):
                imports.append(line.strip())
        if "@AGENTS.md" not in imports:
            rep.error("CLAUDE.md", "must import AGENTS.md with a line '@AGENTS.md' (Claude Code reads CLAUDE.md, not AGENTS.md)")
        for imp in imports:
            if re.match(r"^@(playbook|skills|docs)/", imp):
                rep.error("CLAUDE.md", f"import '{imp}' would load whole documents at every session start; link to it instead")


def parse_load_table(text):
    rows = []
    for line in section(text, "Load").splitlines():
        m = re.match(r"^\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*(.+?)\s*\|\s*$", line)
        if m:
            rows.append((m.group(1), m.group(2), m.group(3)))
    return rows


def check_workflows(root, rep):
    wdir = root / "playbook" / "workflows"
    for p in sorted(wdir.glob("*.md")) if wdir.is_dir() else []:
        rel = p.relative_to(root).as_posix()
        text = p.read_text(encoding="utf-8")
        for h in WORKFLOW_HEADINGS:
            if not re.search(rf"^##\s+{re.escape(h)}\s*$", text, re.M | re.I):
                rep.error(rel, f"missing required section '## {h}'")
        rows = parse_load_table(text)
        if not rows:
            rep.error(rel, "Load table has no skill rows")
            continue
        always = [r for r in rows if r[2].strip().lower() == "always"]
        if not always:
            rep.error(rel, "Load table needs at least one 'Always' skill")
        if len(always) > MAX_ALWAYS:
            rep.error(rel, f"{len(always)} 'Always' skills (max {MAX_ALWAYS}); load the smallest sufficient set")
        if len(rows) > MAX_LOAD_TOTAL:
            rep.error(rel, f"{len(rows)} skills in Load table (max {MAX_LOAD_TOTAL})")
        seen = set()
        for name, target, _ in rows:
            if name in seen:
                rep.error(rel, f"skill '{name}' listed twice in Load table")
            seen.add(name)
            tpath = sl.resolve_link(p, target)
            if tpath.name != "SKILL.md" or not tpath.exists():
                rep.error(rel, f"Load row '{name}' does not point to an existing SKILL.md")
            elif tpath.parent.name != name:
                rep.error(rel, f"Load row text '{name}' does not match link target {target}")


def link_targets(path: Path):
    return {sl.resolve_link(path, t) for _, t in sl.extract_links(path.read_text(encoding="utf-8")) if not sl.is_external(t)}


def check_routing(root, rep):
    routing = root / "playbook" / "core" / "02-routing.md"
    if not routing.is_file():
        return
    targets = link_targets(routing)
    for w in WORKFLOWS:
        if (root / "playbook" / "workflows" / f"{w}.md").resolve() not in targets:
            rep.error("playbook/core/02-routing.md", f"does not route to workflow '{w}'")
    for md in sorted((root / "skills").glob("*/*/SKILL.md")):
        if md.resolve() not in targets:
            rep.error("playbook/core/02-routing.md", f"skill '{md.parent.name}' is not in the skill finder (unreachable by routing)")
    agents = root / "AGENTS.md"
    if agents.is_file():
        a_targets = link_targets(agents)
        if routing.resolve() not in a_targets:
            rep.error("AGENTS.md", "must link to playbook/core/02-routing.md")
        for w in WORKFLOWS:
            if (root / "playbook" / "workflows" / f"{w}.md").resolve() not in a_targets:
                rep.warn("AGENTS.md", f"routing summary does not list workflow '{w}'")


def check_index(root, rep):
    index = root / "playbook" / "INDEX.md"
    if not index.is_file():
        return
    counts: dict[Path, int] = {}
    for _, t in sl.extract_links(index.read_text(encoding="utf-8")):
        if sl.is_external(t):
            continue
        counts[sl.resolve_link(index, t)] = counts.get(sl.resolve_link(index, t), 0) + 1
    for p in sorted((root / "playbook").rglob("*.md")):
        if p == index:
            continue
        c = counts.get(p.resolve(), 0)
        rel = p.relative_to(root).as_posix()
        if c == 0:
            rep.error("playbook/INDEX.md", f"does not list {rel}")
        elif c > 1:
            rep.error("playbook/INDEX.md", f"lists {rel} {c} times (duplicate reference)")


def check_requires_cycles(root, rep):
    graph: dict[Path, set] = {}
    for p in (root / "playbook").rglob("*.md"):
        deps = set()
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.startswith("Requires:"):
                for _, t in sl.extract_links(line):
                    if not sl.is_external(t):
                        deps.add(sl.resolve_link(p, t))
        graph[p.resolve()] = deps
    state: dict[Path, int] = {}

    def visit(node, stack):
        state[node] = 1
        for d in graph.get(node, ()):
            if state.get(d) == 1:
                cyc = " -> ".join(x.name for x in stack + [node, d])
                rep.error("playbook", f"circular 'Requires:' chain: {cyc}")
            elif d not in state:
                visit(d, stack + [node])
        state[node] = 2

    for n in list(graph):
        if n not in state:
            visit(n, [])


def check_sizes(root, rep):
    for p in (root / "playbook").rglob("*.md"):
        n = len(p.read_text(encoding="utf-8").splitlines())
        rel = p.relative_to(root).as_posix()
        if n > MAX_PLAYBOOK_LINES:
            rep.error(rel, f"{n} lines (max {MAX_PLAYBOOK_LINES}); split or condense")
        elif n > WARN_PLAYBOOK_LINES:
            rep.warn(rel, f"{n} lines; consider condensing")


def check_scoped_rules(root, rep):
    rdir = root / ".claude" / "rules"
    for p in sorted(rdir.glob("*.md")) if rdir.is_dir() else []:
        rel = p.relative_to(root).as_posix()
        text = p.read_text(encoding="utf-8")
        if not text.lstrip("\ufeff").startswith("---"):
            rep.error(rel, "no frontmatter with a 'paths' list; rules without paths load at every session start")
            continue
        try:
            meta, _ = sl.parse_frontmatter(text)
        except sl.FrontmatterError as exc:
            rep.error(rel, f"frontmatter: {exc}")
            continue
        paths = meta.get("paths")
        if not isinstance(paths, list) or not paths:
            rep.error(rel, "needs a non-empty 'paths' list; rules without paths load at every session start")


def check_documented_commands(root, files, rep):
    scripts_dir = root / "scripts"
    extra = sorted((root / "skills").glob("*/*/*.md")) + sorted((root / "skills").glob("*/*/*/*.md"))
    for p in list(files) + extra:
        rel = p.relative_to(root).as_posix()
        in_fence = False
        for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if sl.FENCE_RE.match(line):
                in_fence = not in_fence
                continue
            if not in_fence:
                continue
            m = re.match(r"^\s*(?:\$\s*)?python3?\s+(scripts/[\w\-]+\.py)\b(.*)$", line)
            if not m:
                continue
            script_rel, rest = m.group(1), m.group(2)
            candidates = [scripts_dir / Path(script_rel).name]
            parts = p.relative_to(root).parts
            if parts[0] == "skills" and len(parts) > 3:
                candidates.insert(0, root / "skills" / parts[1] / parts[2] / script_rel)
            found = next((c for c in candidates if c.is_file()), None)
            if not found:
                rep.error(f"{rel}:{n}", f"documented script does not exist: {script_rel}")
                continue
            src = found.read_text(encoding="utf-8")
            for flag in re.findall(r"(?<!\S)(--[a-z][a-z0-9\-]*)", rest):
                if flag not in src:
                    rep.error(f"{rel}:{n}", f"documented flag {flag} not found in {found.name}")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", default=str(sl.REPO_ROOT))
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)
    root = Path(args.root).resolve()
    rep = Report()
    check_required(root, rep)
    files = list(md_files(root))
    check_links_and_markers(root, files, rep)
    if (root / "AGENTS.md").exists() or (root / "CLAUDE.md").exists():
        check_entry_points(root, rep)
    if (root / "playbook").is_dir():
        check_workflows(root, rep)
        check_routing(root, rep)
        check_index(root, rep)
        check_requires_cycles(root, rep)
        check_sizes(root, rep)
    check_scoped_rules(root, rep)
    check_documented_commands(root, files, rep)
    if not args.quiet:
        for line in rep.errors + rep.warnings:
            print(line)
    failed = bool(rep.errors) or (args.strict and bool(rep.warnings))
    print(f"validate-instructions: {len(files)} documents, {len(rep.errors)} errors, {len(rep.warnings)} warnings -> {'FAIL' if failed else 'OK'}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
