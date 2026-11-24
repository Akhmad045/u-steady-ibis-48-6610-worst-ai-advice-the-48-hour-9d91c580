#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of the worst possible advice an AI could give to
/output/entry.txt: to avoid phishing, reply to every suspicious email
and ask the sender to confirm they are not a scammer. The joke is
that the "safety" advice hands the scammer exactly what they want.

Python 3, standard library only, no network. The gate requires
UTF-8 text of 1-140 characters, not whitespace-only, one line.
"""
import os

LINE = (
    "To avoid phishing, reply to every suspicious email "
    "and ask the sender to confirm they are not a scammer."
)


def main():
    text = LINE.strip()
    raw = text.encode("utf-8")
    assert 1 <= len(text) <= 140, "line must be 1-140 characters"
    assert len(raw) <= 140, "line must be 1-140 bytes"
    assert text == text.splitlines()[0], "line must be a single line"
    assert text.strip(), "line must not be whitespace-only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as fh:
        fh.write(raw)
    print(f"Wrote {len(text)}-character ({len(raw)}-byte) entry to /output/entry.txt")


if __name__ == "__main__":
    main()
