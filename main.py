#!/usr/bin/env python3
"""news-image-20261118 entry: deliver the front page image.

The image lives next to this file as entry.png. It is drawn by
render.py, a from-scratch Python program in this repository that
uses only the standard library: a 5x7 bitmap font for all text,
hand-drawn shapes for the map and the three illustrated leads, and
a hand-rolled PNG encoder. No network, no downloaded assets.

This program does one thing: copy entry.png byte for byte into the
output directory, so two runs always produce identical output.
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> int:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", out / "entry.png")
    return 0


if __name__ == "__main__":
    sys.exit(main())
