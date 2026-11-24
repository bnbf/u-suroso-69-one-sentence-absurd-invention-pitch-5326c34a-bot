#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance to /output/entry.txt (1-220 chars, UTF-8).
"""

import os

# The pitch: one sentence, at most 220 characters.
# Annoyance: burnt toast. Invention: a toaster that demands praise.
# Mechanism: it will not pop until you compliment its browning.
PITCH = "A toaster that refuses to pop until you compliment its browning, ending burnt toast by weaponising its self-esteem."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = PITCH.strip()
    assert 1 <= len(text) <= 220, f"pitch must be 1-220 chars, got {len(text)}"
    assert text and not text.isspace()
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
