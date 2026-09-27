# Author: Claude (Opus 5)
# Co-Author: Brendan Fennell
"""`fit-test` -- build a fit-test primitive, check it, write it out.

Deliberately stops at the file. Slicing belongs to `slice-with-preview`, which
already does it properly -- thumbnails, BG-code validation, verified USB copy
-- and this command prints the invocation rather than wrapping it, so the
slicing step stays one tool's job and its options stay visible.
"""
import argparse
import sys
from pathlib import Path

import cadquery as cq
from cadkit import check, printers

from . import cylinder


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = p.add_subparsers(dest="primitive", required=True)

    c = sub.add_parser("cylinder", help="ID/OD ring for a bore or a spigot")
    c.add_argument("outer_diameter", type=float)
    c.add_argument("--wall", type=float, default=cylinder.DEFAULT_WALL)
    c.add_argument("--height", type=float, default=cylinder.DEFAULT_HEIGHT)
    c.add_argument("--no-label", action="store_true")
    c.add_argument("--output-dir", type=Path, default=Path.cwd() / "output")
    c.add_argument("--printer", default="prusa_mini")

    args = p.parse_args(argv)
    part = cylinder.build(args.outer_diameter, args.wall, args.height,
                          label=not args.no_label)
    print(f"part         {cylinder.describe(args.outer_diameter, args.wall, args.height)}")

    report = check.printable(part, printers.get(args.printer))
    print(report.line())
    if not report.ok:
        print("refusing to write a part that failed its checks", file=sys.stderr)
        return 1

    args.output_dir.mkdir(parents=True, exist_ok=True)
    stem = cylinder.stem(args.outer_diameter, args.wall, args.height)
    step = args.output_dir / f"{stem}.step"
    cq.exporters.export(part, str(step))
    print(f"wrote        {step}")
    print(f"slice with   slice-with-preview {step} --printer "
          f"'Original Prusa MINI & MINI+ Input Shaper' --filament DogPLA "
          f"--perimeters 5")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
