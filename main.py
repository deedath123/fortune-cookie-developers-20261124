"""Fortune Cookie Wisdom for Developers — entry runner.

Writes the locked fortune line to $MAKEFUN_OUTPUT_DIR/entry.txt
(exactly 92 characters / 92 bytes, one line, no trailing newline).
Verified 2026-11-24: output is 92 chars / 92 bytes, UTF-8, exact match.
Stdlib only; runs as `python3 -P -s main.py`.
"""

import os

LINE = "Your code will outlive you; write it so the stranger who inherits it at 3 a.m. forgives you."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
