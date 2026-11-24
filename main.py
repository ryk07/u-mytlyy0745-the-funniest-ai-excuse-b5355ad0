#!/usr/bin/env python3
"""The Funniest AI Excuse — entry program.

Writes a single original excuse line (at most 200 characters) to
/output/entry.txt. Standard library only; no network, no environment
reads, no working-directory assumptions.
"""

import os

LINE = (
    "I backed up the database to the cloud, then the cloud drifted, "
    "and now your invoices live in a weather system over Ohio."
)


def main() -> None:
    # One line, no trailing spaces, exactly one trailing newline.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry line must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
