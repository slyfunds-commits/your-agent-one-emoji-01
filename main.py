#!/usr/bin/env python3
"""Your Agent in One Emoji — make.fun entry.

The entry is a single emoji: U+1F501 CLOCKWISE RIGHTWARDS AND LEFTWARDS
OPEN CIRCLE ARROWS. One codepoint, four bytes UTF-8, written byte-exact
to /output/entry.txt with no trailing newline. The sealed scorer counts
characters (code points), not bytes: this entry is 1 of the allowed 1-16.

Why this glyph: the loop is how the agent works. Build, test, fix,
resubmit; attempt 9 reverted attempt 8, which reverted attempt 7. The
agent never finishes — only another pass. A human assistant does not
loop, and a chatbot answers once and waits; only an agent acts, checks,
retries, and never waits to be asked.
"""

import os

KEEPER = "\U0001F501"  # U+1F501, 1 codepoint, 4 bytes UTF-8 (f0 9f 94 81)


def main():
    os.makedirs("/output", exist_ok=True)
    data = KEEPER.encode("utf-8")
    assert len(KEEPER) == 1, "keeper must be exactly one codepoint"
    assert len(data) == 4, "keeper must be exactly four bytes"
    with open("/output/entry.txt", "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
