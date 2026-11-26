#!/usr/bin/env python3
# Entry for make.fun bounty u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Deterministic entry: writes exactly one satirical sentence to
/output/entry.txt and prints that same line, nothing else.
"""

import os

LINE = (
    "The senator who wrote the bill to regulate artificial intelligence "
    "has spent three weeks trying to turn a Word document into a PDF, "
    "and now calls the format a deep-state conspiracy."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
