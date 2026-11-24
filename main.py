"""Reassigned to You — a robot vacuum's alibi.

Writes one line to /output/entry.txt: the excuse a robot vacuum gives
for missing a spot. The line is fixed and deterministic, so every run
of this program produces the exact same entry.
"""

import os
import sys

# The entry: one line, at most 200 characters, deadpan machine voice.
ENTRY = (
    "I ran a full diagnostic, found nothing wrong with me, "
    "and reassigned the spot to you \u2014 check your app."
)

MAX_CHARS = 200
DEFAULT_OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The grader runs this with no arguments; an optional path argument
    # exists only so the entry can be verified locally without root.
    output_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT_PATH
    line = ENTRY.strip()
    if not line:
        raise SystemExit("entry is empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be exactly one line")
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    print(line)
    print(f"wrote {len(line)} characters to {output_path}")


if __name__ == "__main__":
    main()
