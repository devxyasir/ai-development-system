#!/usr/bin/env python3
"""List skills and collections.

Usage:
  python scripts/list-skills.py                  # all skills by category
  python scripts/list-skills.py --category motion
  python scripts/list-skills.py --search animation
  python scripts/list-skills.py --collections
  python scripts/list-skills.py --json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import skilllib as sl  # noqa: E402


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", default=str(sl.REPO_ROOT))
    ap.add_argument("--category")
    ap.add_argument("--search", help="case-insensitive keyword matched against name and description")
    ap.add_argument("--collections", action="store_true", help="list collections instead of skills")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args(argv)
    root = Path(args.root).resolve()

    if args.collections:
        cols = sl.load_collections(root)
        rows = []
        for n in sorted(cols):
            try:
                rows.append({"name": n, "description": cols[n].get("description", ""), "skills": sl.resolve_collection(n, cols)})
            except sl.CollectionError as exc:
                print(f"error: {exc}", file=sys.stderr)
                return 1
        if args.json:
            print(json.dumps(rows, indent=2))
        else:
            for r in rows:
                print(f"{r['name']} ({len(r['skills'])} skills)\n    {r['description']}")
        return 0

    skills = [s for s in sl.discover_skills(root) if not s.errors]
    if args.category:
        skills = [s for s in skills if s.category == args.category]
    if args.search:
        q = args.search.lower()
        skills = [s for s in skills if q in s.name or q in s.description.lower()]
    if args.json:
        print(json.dumps([{"name": s.name, "category": s.category, "description": s.description,
                           "path": s.path.relative_to(root).as_posix()} for s in skills], indent=2))
        return 0
    if not skills:
        print("No skills matched.")
        return 0
    current = None
    for s in skills:
        if s.category != current:
            current = s.category
            print(f"\n[{current}]")
        short = s.description if len(s.description) <= 100 else s.description[:99].rstrip() + "…"
        print(f"  {s.name:<34} {short}")
    print(f"\n{len(skills)} skill(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
