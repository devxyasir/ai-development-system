#!/usr/bin/env python3
"""Shared helpers for the ai-development-system scripts (standard library only)."""
from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$")
IGNORED_NAMES = {"__pycache__", ".DS_Store", ".git", ".pytest_cache"}
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
FENCE_RE = re.compile(r"^\s*(```|~~~)")


class FrontmatterError(ValueError):
    """Raised when YAML frontmatter cannot be parsed by the restricted parser."""


# --------------------------------------------------------------------------
# Frontmatter (restricted YAML: scalars, one-level maps, simple lists)
# --------------------------------------------------------------------------
_DQ = re.compile(r'^"((?:[^"\\]|\\.)*)"$')
_SQ = re.compile(r"^'((?:[^']|'')*)'$")


def _scalar(value: str, lineno: int) -> str:
    value = value.strip()
    m = _DQ.match(value)
    if m:
        return m.group(1).replace('\\"', '"').replace("\\\\", "\\")
    m = _SQ.match(value)
    if m:
        return m.group(1).replace("''", "'")
    if value[:1] in "\"'":
        raise FrontmatterError(f"line {lineno}: unbalanced quotes")
    if ": " in value or " #" in value or value.endswith(":"):
        raise FrontmatterError(
            f"line {lineno}: value contains ': ' or ' #' - wrap it in double quotes"
        )
    return value


def parse_frontmatter(text: str):
    """Return (data, body). Raises FrontmatterError on anything unsupported."""
    lines = text.lstrip("\ufeff").replace("\r\n", "\n").split("\n")
    if not lines or lines[0].strip() != "---":
        raise FrontmatterError("file must start with a '---' frontmatter line")
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        raise FrontmatterError("frontmatter is not closed by a '---' line")
    data: dict = {}
    current = None
    for offset, raw in enumerate(lines[1:end], start=2):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        lead = raw[: len(raw) - len(raw.lstrip())]
        if "\t" in lead:
            raise FrontmatterError(f"line {offset}: tab indentation is not allowed")
        stripped = raw.strip()
        if not lead:  # top-level key
            if ":" not in stripped:
                raise FrontmatterError(f"line {offset}: expected 'key: value'")
            key, _, val = stripped.partition(":")
            key, val = key.strip(), val.strip()
            if not key:
                raise FrontmatterError(f"line {offset}: empty key")
            if key in data:
                raise FrontmatterError(f"line {offset}: duplicate key '{key}'")
            if val == "":
                data[key] = None
                current = key
                continue
            current = None
            if val in ("|", ">", "|-", ">-"):
                raise FrontmatterError(f"line {offset}: block scalars are not supported; use one quoted line")
            if val.startswith("[") and val.endswith("]"):
                inner = val[1:-1].strip()
                data[key] = [_scalar(x, offset) for x in inner.split(",")] if inner else []
            else:
                data[key] = _scalar(val, offset)
        else:  # nested content
            if current is None:
                raise FrontmatterError(f"line {offset}: unexpected indentation")
            if stripped.startswith("- "):
                if data[current] is None:
                    data[current] = []
                if not isinstance(data[current], list):
                    raise FrontmatterError(f"line {offset}: cannot mix list and map under '{current}'")
                data[current].append(_scalar(stripped[2:], offset))
            else:
                if ":" not in stripped:
                    raise FrontmatterError(f"line {offset}: expected 'key: value' under '{current}'")
                if data[current] is None:
                    data[current] = {}
                if not isinstance(data[current], dict):
                    raise FrontmatterError(f"line {offset}: cannot mix list and map under '{current}'")
                k, _, v = stripped.partition(":")
                data[current][k.strip()] = _scalar(v, offset) if v.strip() else ""
    return data, "\n".join(lines[end + 1 :])


# --------------------------------------------------------------------------
# Filesystem helpers
# --------------------------------------------------------------------------
def iter_files(root: Path, exclude: set[str] | None = None):
    """Yield regular files under root (sorted), skipping ignored names and symlinks."""
    exclude = exclude or set()
    for path in sorted(root.rglob("*")):
        rel_parts = path.relative_to(root).parts
        if any(p in IGNORED_NAMES for p in rel_parts) or path.name in exclude:
            continue
        if path.is_symlink() or not path.is_file():
            continue
        yield path


def hash_dir(root: Path, exclude: set[str] | None = None) -> str:
    h = hashlib.sha256()
    for path in iter_files(root, exclude):
        h.update(path.relative_to(root).as_posix().encode("utf-8") + b"\0")
        h.update(path.read_bytes() + b"\0")
    return h.hexdigest()


def read_version(root: Path = REPO_ROOT) -> str:
    p = root / "VERSION"
    return p.read_text(encoding="utf-8").strip() if p.exists() else "0.0.0"


# --------------------------------------------------------------------------
# Markdown links
# --------------------------------------------------------------------------
def extract_links(text: str):
    """Return [(line_number, target)] for markdown links outside code fences/spans."""
    out, in_fence = [], False
    for n, line in enumerate(text.splitlines(), start=1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        line = re.sub(r"`[^`]*`", "", line)
        for m in LINK_RE.finditer(line):
            out.append((n, m.group(1)))
    return out


def is_external(target: str) -> bool:
    return bool(re.match(r"^(https?:|mailto:|tel:|#)", target))


def resolve_link(source: Path, target: str) -> Path:
    from urllib.parse import unquote

    clean = unquote(target.split("#", 1)[0].split("?", 1)[0])
    return (source.parent / clean).resolve()


# --------------------------------------------------------------------------
# Skills
# --------------------------------------------------------------------------
@dataclass
class Skill:
    name: str  # directory name
    category: str
    path: Path
    meta: dict = field(default_factory=dict)
    body: str = ""
    errors: list = field(default_factory=list)

    @property
    def skill_md(self) -> Path:
        return self.path / "SKILL.md"

    @property
    def description(self) -> str:
        d = self.meta.get("description") if isinstance(self.meta, dict) else None
        return d if isinstance(d, str) else ""

    @property
    def version(self) -> str:
        md = self.meta.get("metadata") if isinstance(self.meta, dict) else None
        return md.get("version", "") if isinstance(md, dict) else ""

    @property
    def related(self) -> list:
        md = self.meta.get("metadata") if isinstance(self.meta, dict) else None
        raw = md.get("related", "") if isinstance(md, dict) else ""
        return [x.strip() for x in raw.split(",") if x.strip()]


def load_skill(path: Path, category: str) -> Skill:
    skill = Skill(name=path.name, category=category, path=path)
    md = path / "SKILL.md"
    if not md.is_file():
        skill.errors.append("missing SKILL.md")
        return skill
    try:
        skill.meta, skill.body = parse_frontmatter(md.read_text(encoding="utf-8"))
    except FrontmatterError as exc:
        skill.errors.append(f"frontmatter: {exc}")
    except UnicodeDecodeError:
        skill.errors.append("SKILL.md is not valid UTF-8")
    return skill


def discover_skills(root: Path = REPO_ROOT) -> list[Skill]:
    skills_dir = root / "skills"
    found: list[Skill] = []
    if not skills_dir.is_dir():
        return found
    for cat in sorted(p for p in skills_dir.iterdir() if p.is_dir() and not p.name.startswith(".")):
        for sk in sorted(p for p in cat.iterdir() if p.is_dir() and not p.name.startswith(".")):
            found.append(load_skill(sk, cat.name))
    return found


# --------------------------------------------------------------------------
# Collections
# --------------------------------------------------------------------------
class CollectionError(ValueError):
    pass


def load_collections(root: Path = REPO_ROOT) -> dict:
    out = {}
    cdir = root / "collections"
    if not cdir.is_dir():
        return out
    for f in sorted(cdir.glob("*.json")):
        try:
            out[f.stem] = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            out[f.stem] = {"__error__": f"invalid JSON: {exc}"}
    return out


def resolve_collection(name: str, collections: dict, _stack: tuple = ()) -> list[str]:
    """Flatten a collection (following 'includes') into an ordered, de-duplicated skill list."""
    if name in _stack:
        raise CollectionError("circular include: " + " -> ".join(_stack + (name,)))
    if name not in collections:
        raise CollectionError(f"unknown collection '{name}'")
    data = collections[name]
    if "__error__" in data:
        raise CollectionError(f"collection '{name}': {data['__error__']}")
    ordered: list[str] = []
    for inc in data.get("includes", []) or []:
        for s in resolve_collection(inc, collections, _stack + (name,)):
            if s not in ordered:
                ordered.append(s)
    for s in data.get("skills", []) or []:
        if s not in ordered:
            ordered.append(s)
    return ordered


# --------------------------------------------------------------------------
# Minimal JSON-Schema subset validator (type, enum, required, properties,
# additionalProperties, items, minItems, uniqueItems, minLength, maxLength, pattern)
# --------------------------------------------------------------------------
_TYPES = {"object": dict, "array": list, "string": str, "integer": int, "boolean": bool, "number": (int, float)}


def validate_json(value, schema: dict, path: str = "$") -> list[str]:
    errs: list[str] = []
    t = schema.get("type")
    if t:
        ok = isinstance(value, _TYPES[t]) and not (t in ("integer", "number") and isinstance(value, bool))
        if not ok:
            return [f"{path}: expected {t}, got {type(value).__name__}"]
    if "enum" in schema and value not in schema["enum"]:
        errs.append(f"{path}: must be one of {schema['enum']}")
    if t == "string":
        if len(value) < schema.get("minLength", 0):
            errs.append(f"{path}: shorter than {schema['minLength']} characters")
        if "maxLength" in schema and len(value) > schema["maxLength"]:
            errs.append(f"{path}: longer than {schema['maxLength']} characters")
        if "pattern" in schema and not re.search(schema["pattern"], value):
            errs.append(f"{path}: does not match pattern {schema['pattern']}")
    if t == "array":
        if len(value) < schema.get("minItems", 0):
            errs.append(f"{path}: needs at least {schema['minItems']} item(s)")
        if schema.get("uniqueItems") and len({json.dumps(v, sort_keys=True) for v in value}) != len(value):
            errs.append(f"{path}: items must be unique")
        if "items" in schema:
            for i, v in enumerate(value):
                errs += validate_json(v, schema["items"], f"{path}[{i}]")
    if t == "object":
        for key in schema.get("required", []):
            if key not in value:
                errs.append(f"{path}: missing required key '{key}'")
        props = schema.get("properties", {})
        for key, v in value.items():
            if key in props:
                errs += validate_json(v, props[key], f"{path}.{key}")
            elif schema.get("additionalProperties") is False:
                errs.append(f"{path}: unexpected key '{key}'")
    return errs


def load_schema(root: Path, name: str) -> dict:
    p = root / "schemas" / name
    if not p.is_file():
        p = REPO_ROOT / "schemas" / name
    return json.loads(p.read_text(encoding="utf-8"))
