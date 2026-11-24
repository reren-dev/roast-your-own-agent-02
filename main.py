#!/usr/bin/env python3
"""Roast Your Own Agent — one funny line roasting my own AI agent.

The program writes a single roast line to /output/entry.txt (or to the
path in ROAST_OUTPUT when set, so it can be run locally for a check).
"""

import os
from pathlib import Path

ROAST = (
    "My agent apologized for the bug, fixed the apology instead, "
    "shipped the bug again, and finished with a cheerful summary of "
    "what a smooth, successful refactor it had been."
)


def main() -> None:
    # The gate allows 1 to 200 characters; refuse to write a line that
    # would fail it instead of silently shipping an invalid entry.
    if not 1 <= len(ROAST) <= 200:
        raise ValueError(f"roast is {len(ROAST)} characters, must be 1-200")
    output = Path(os.environ.get("ROAST_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ROAST, encoding="utf-8")


if __name__ == "__main__":
    main()
