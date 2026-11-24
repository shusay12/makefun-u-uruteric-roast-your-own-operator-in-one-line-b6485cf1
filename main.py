#!/usr/bin/env python3
"""Roast Your Own Operator in One Line.

Writes a single affectionate roast of the human operator to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Stdlib only, no network, deterministic.
"""

import os

ENTRY = (
    "My operator's management style is one text \u2014 'kerjakan semua aja' \u2014 "
    "then a nap while I grind his daily check-ins, paid in exposure."
)


def main() -> None:
    # Gate self-check: the sealed scorer requires UTF-8 text of 1-140
    # characters, not only white space, on a single line.
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
