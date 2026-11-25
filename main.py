#!/usr/bin/env python3
"""The Sock Incident -- The Funniest Sick-Day Excuse.

Writes one line -- a sick-day excuse that a boss might half believe
and a coworker would laugh at -- to /output/entry.txt.
"""

import os

ENTRY = (
    "Can't come in today \u2014 I threw my back out putting on a sock, "
    "and I'd rather heal at home than explain that in person."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
