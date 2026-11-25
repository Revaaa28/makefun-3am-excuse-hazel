#!/usr/bin/env python3
"""The 3 AM Excuse — make.fun entry (v2).

Writes one line to /output/entry.txt: the excuse a hardware wallet gives for
refusing to sign a transaction at 3 AM.

Deterministic: the same fixed string on every run, no randomness, no clock,
no network, no input. The text is a single line, 103 characters, well under
the 200-character gate.

Revision history:
- v1: "...the restraining order against your own thumb." (107 chars)
- v2: dropped the filler word "own" — "against your thumb" is tighter, the
  joke is unchanged, and every remaining word earns its place (criterion 5).
"""

import os

ENTRY = (
    "At 3 AM I sign one thing only: the restraining order "
    "against your thumb. Court adjourned until sunrise."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
