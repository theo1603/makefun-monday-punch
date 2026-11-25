#!/usr/bin/env python3
"""Monday Morning Punchlines — make.fun entry.

Writes one original joke about Monday mornings (<= 200 characters)
to /output/entry.txt. Python 3.13, standard library only, no network.

Revision notes (v2): the v1 draft landed the twist — the alarm itself
refusing Monday — but its closer ("Even it needs a minute") was soft
and "looked at the time" was wasted setup. v2 cuts the filler, names
the day in the twist ("saw what day it was"), and closes with the
narrator siding with the alarm ("I respect that"), which turns the
complaint into a punchline: the alarm isn't broken, it's the only one
being honest about Monday.
"""

import os

JOKE = (
    "Monday morning: my alarm went off, saw what day it was, "
    "and snoozed itself. I respect that."
)


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke is {len(text)} chars, must be 1-200"
    assert text.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
