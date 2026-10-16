#!/usr/bin/env python3
"""WCAG 2.x contrast ratio checker (no dependencies).

Usage:
  python contrast.py FOREGROUND BACKGROUND [--large | --ui] [--json]
Colors are hex: #rgb, #rrggbb (the # may be omitted). Exit code 0 when the pair meets the
AA threshold for the chosen kind of content (normal text 4.5, large text 3, UI 3), else 1.
Exit code 2 for unreadable colors.
"""
import argparse
import json
import sys


def parse_hex(value: str):
    v = value.strip().lstrip("#")
    if len(v) == 3:
        v = "".join(c * 2 for c in v)
    if len(v) != 6:
        raise ValueError(f"not a hex color: {value!r}")
    return tuple(int(v[i:i + 2], 16) for i in (0, 2, 4))


def _lin(channel: int) -> float:
    c = channel / 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(rgb) -> float:
    r, g, b = (_lin(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg, bg) -> float:
    l1, l2 = luminance(fg), luminance(bg)
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="WCAG contrast ratio checker")
    ap.add_argument("foreground")
    ap.add_argument("background")
    kind = ap.add_mutually_exclusive_group()
    kind.add_argument("--large", action="store_true", help="large text thresholds (3:1 AA, 4.5:1 AAA)")
    kind.add_argument("--ui", action="store_true", help="UI component / graphic threshold (3:1)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    try:
        fg, bg = parse_hex(args.foreground), parse_hex(args.background)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    r = ratio(fg, bg)
    aa = 3.0 if (args.large or args.ui) else 4.5
    aaa = 4.5 if args.large else 7.0
    result = {
        "ratio": round(r, 2),
        "kind": "ui" if args.ui else "large-text" if args.large else "normal-text",
        "AA": r >= aa,
        "AAA": None if args.ui else r >= aaa,
    }
    if args.json:
        print(json.dumps(result))
    else:
        aaa_txt = "n/a" if args.ui else ("pass" if result["AAA"] else "fail")
        print(f"{result['ratio']}:1  kind={result['kind']}  AA={'pass' if result['AA'] else 'fail'}  AAA={aaa_txt}")
    return 0 if result["AA"] else 1


if __name__ == "__main__":
    sys.exit(main())
