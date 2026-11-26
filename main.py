#!/usr/bin/env python3
"""Entrypoint for the 'Worst Pizza Topping' make.fun entry.

Reads the one-line pitch from line.txt (shipped beside this file) and
writes it to /output/entry.txt, where the grader picks it up.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    with open(os.path.join(HERE, "line.txt"), encoding="utf-8") as fh:
        line = fh.read().strip()

    # Gate check: the sealed scorer accepts UTF-8 text of 1 to 200
    # characters that is not only whitespace.
    if not line or not 1 <= len(line) <= 200:
        raise SystemExit(f"line outside the 1-200 character gate: {len(line)} chars")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(line)

    # Read-back verification: the file on disk must match the line exactly.
    with open(OUTPUT_PATH, encoding="utf-8") as fh:
        written = fh.read()
    if written != line:
        raise SystemExit("output does not match the line byte for byte")

    print(line)


if __name__ == "__main__":
    main()
