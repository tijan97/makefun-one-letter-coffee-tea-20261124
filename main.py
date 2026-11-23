#!/usr/bin/env python3
"""One Letter: Coffee or Tea — make.fun bounty entry.

The brief asks for exactly one letter and nothing else: A for coffee,
B for tea, with no word, no explanation and no punctuation. The program
writes that single letter to /output/entry.txt, where the sealed scorer
checks it is UTF-8 text of exactly 1 character.

Choice: A — coffee. Of the two letters, A is the bolder, more vivid
stance: the first letter, the top grade, the wake-up drink. Coffee is
the fuller, more alive answer in the coffee-against-tea argument, and
the letter A lands as a whole answer on its own, clean and
unmistakable, with nothing needed beside it.
"""

import os

ENTRY_LETTER = "A"  # A = coffee, B = tea


def validate(letter: str) -> None:
    """Enforce the brief's caps before anything is written.

    The gate requires /output/entry.txt to be UTF-8 text of exactly
    1 character, not only white space, and the judge only counts a
    letter that chooses coffee (A) or tea (B). Anything else loses
    to any valid letter, so fail loudly instead of shipping it.
    """
    if len(letter) != 1:
        raise ValueError(f"entry must be exactly 1 character, got {len(letter)}: {letter!r}")
    if letter.isspace():
        raise ValueError("entry must not be only white space")
    if letter not in ("A", "B"):
        raise ValueError(f"entry must be A (coffee) or B (tea), got {letter!r}")


def main() -> None:
    validate(ENTRY_LETTER)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    # Exactly one character, no trailing newline: the gate requires
    # /output/entry.txt to be 1 to 1 characters.
    with open(target, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_LETTER)
    # Read back and re-validate what was actually written.
    written = open(target, encoding="utf-8").read()
    validate(written)
    print(f"wrote {target}: {ENTRY_LETTER!r}")


if __name__ == "__main__":
    main()
