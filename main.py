#!/usr/bin/env python3
"""make.fun entry: one office joke, a single line under 200 characters.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT if set).
Deterministic, stdlib only, no network, no clock, no randomness.
"""

import os

ENTRY_TEXT = "My boss said dress for the job you want, so I came in pyjamas — he works from home."


def validate(text: str) -> None:
    """The brief requires exactly one line of 1-199 characters."""
    if not 1 <= len(text) <= 199:
        raise ValueError(f"entry must be 1-199 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> int:
    validate(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT")
    if out_dir is None:
        # Prefer /output, fall back to ./output when /output is not writable.
        try:
            os.makedirs("/output", exist_ok=True)
            probe = os.path.join("/output", ".writetest")
            with open(probe, "w", encoding="utf-8") as f:
                f.write("ok")
            os.remove(probe)
            out_dir = "/output"
        except OSError:
            out_dir = "./output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    # Verify the written file by reading it back.
    with open(out_path, "r", encoding="utf-8") as f:
        if f.read() != ENTRY_TEXT:
            raise RuntimeError("verification failed: written file differs from entry text")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
