#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes a single original warning label for human beings to
``<output_dir>/entry.txt``. The label is a fixed string, so every run
produces byte-identical output. Standard library only, no network.
"""

import os

LABEL = (
    "WARNING: This human skipped the instructions, voided the warranty, "
    "and is now confidently in charge of everything."
)


def main() -> None:
    # The gate requires 1 to 160 characters of non-whitespace UTF-8 text.
    assert 1 <= len(LABEL) <= 160 and LABEL.strip(), "label outside gate"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LABEL)


if __name__ == "__main__":
    main()
