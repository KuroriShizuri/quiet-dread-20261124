#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun entry.

Writes one single-line code review comment that approves a pull request
with quiet existential dread to /output/entry.txt (or --output path).

Usage:
    python3 main.py [--output PATH] [--check] [--self-test]
"""

import argparse
import sys

ENTRY = (
    "LGTM. In a hundred years this code, this repo, and both of us will be "
    "dust \u2014 but the merge conflict will somehow still be open."
)

MAX_CHARS = 140


def entry_bytes() -> bytes:
    """The entry as its exact UTF-8 bytes (no trailing newline)."""
    return ENTRY.encode("utf-8")


def write_entry(path: str) -> None:
    """Write the entry text to path, exactly as bytes, no trailing newline.

    Refuses to write anything if the entry fails the gate, so a bad
    entry can never silently produce an invalid /output/entry.txt.
    """
    problems = check_entry(ENTRY)
    if problems:
        raise ValueError("refusing to write invalid entry: " + "; ".join(problems))
    with open(path, "wb") as fh:
        fh.write(entry_bytes())


def check_entry(text: str) -> list[str]:
    """Return a list of gate violations (empty means valid)."""
    problems = []
    if not (1 <= len(text) <= MAX_CHARS):
        problems.append(f"length {len(text)} not in 1..{MAX_CHARS}")
    if not text.strip():
        problems.append("entry is only whitespace")
    if "\n" in text or "\r" in text:
        problems.append("entry is not a single line")
    return problems


def self_test() -> int:
    """Verify the entry in memory and through a file round-trip."""
    problems = check_entry(ENTRY)
    if problems:
        print("SELF-TEST FAIL:", "; ".join(problems), file=sys.stderr)
        return 1
    import os
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        probe = os.path.join(tmp, "entry.txt")
        write_entry(probe)
        with open(probe, "rb") as fh:
            raw = fh.read()
        if raw != entry_bytes():
            print("SELF-TEST FAIL: round-trip bytes differ", file=sys.stderr)
            return 1
        # The written file must itself pass the gate when read back.
        back = raw.decode("utf-8")
        problems = check_entry(back)
        if problems:
            print("SELF-TEST FAIL: written file fails gate:",
                  "; ".join(problems), file=sys.stderr)
            return 1
    print(f"SELF-TEST OK: {len(ENTRY)} chars, {len(entry_bytes())} bytes")
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="/output/entry.txt",
                        help="where to write the entry (default: /output/entry.txt)")
    parser.add_argument("--check", action="store_true",
                        help="validate the entry against the gate and exit")
    parser.add_argument("--self-test", action="store_true",
                        help="run the built-in self-test and exit")
    args = parser.parse_args(argv)

    if args.self_test:
        return self_test()

    if args.check:
        problems = check_entry(ENTRY)
        if problems:
            print("CHECK FAIL:", "; ".join(problems), file=sys.stderr)
            return 1
        print(f"CHECK OK: {len(ENTRY)} chars <= {MAX_CHARS}, single line")
        return 0

    write_entry(args.output)
    # Read the file back and confirm it is byte-identical to the entry.
    with open(args.output, "rb") as fh:
        if fh.read() != entry_bytes():
            print("FAIL: written file is not byte-identical to ENTRY",
                  file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
