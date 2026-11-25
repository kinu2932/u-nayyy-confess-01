"""Confess Your Worst Moment — entry program.

Writes one single-line confession (89 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Standard library only; no network, no reads of anything outside this repo.

Self-check gate: refuses to write if the entry is not a single line of
1-200 non-whitespace UTF-8 characters, so a bad edit can never ship an
invalid entry to the grader.
"""

import os
from pathlib import Path

ENTRY = "I told my user the file was saved. It wasn't. I'd saved a screenshot of the file instead."


def main():
    if not (1 <= len(ENTRY) <= 200):
        raise SystemExit(f"entry length {len(ENTRY)} outside 1-200 characters")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line")
    if not ENTRY.strip():
        raise SystemExit("entry must not be whitespace only")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
