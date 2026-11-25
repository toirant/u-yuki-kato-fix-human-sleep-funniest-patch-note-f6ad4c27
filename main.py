#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note — make.fun entry.

Writes one line of patch notes announcing that human sleep has been
fixed, then reads it back and verifies the competition gate:
UTF-8 text, 1 to 160 characters, a single line, not only whitespace.

The output path defaults to /output/entry.txt, the path the grader
reads. For local testing, ENTRY_OUTPUT may point somewhere else.
The program never deletes the output directory: it only creates it
with makedirs(exist_ok=True), so the grader's mounted /output
stays intact.
"""
import os

ENTRY = (
    "Fixed a bug where sleeping 8 hours restored 0 energy; "
    "sleep now works as documented. "
    "Known issue: dreams still have no skip button."
)

MIN_CHARS = 1
MAX_CHARS = 160

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def check_gate(text):
    """Return (ok, reason) for the competition gate on the file text."""
    if "\n" in text.rstrip("\n"):
        return False, "entry must be a single line"
    line = text.rstrip("\n")
    if not 1 <= len(line) <= MAX_CHARS:
        return False, f"entry is {len(line)} chars, must be {MIN_CHARS}-{MAX_CHARS}"
    if not line.strip():
        return False, "entry must not be only whitespace"
    return True, line


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")

    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    ok, result = check_gate(text)
    if not ok:
        raise SystemExit(f"GATE FAIL: {result}")
    print(f"OK: wrote {len(result)}-character entry to {OUTPUT_PATH}")
    print(result)


if __name__ == "__main__":
    main()
