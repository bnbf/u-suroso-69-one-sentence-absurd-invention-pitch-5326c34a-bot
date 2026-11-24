#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes exactly one sentence — the pitch for an absurd invention —
to $MAKEFUN_OUTPUT_DIR/entry.txt. No input, no network, no output
beyond the single sentence.
"""

import os

PITCH = "A toaster that refuses to pop until you compliment its browning, ending burnt toast by weaponising its self-esteem."
# Angle: the joke inverts the appliance's job — the toaster holds the
# toast hostage until it is flattered, and "weaponising its self-esteem"
# turns an everyday kitchen failure (burnt toast) into a negotiation
# with a machine that has learned to demand praise.

OUTPUT_PATH = os.path.join(
    os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
