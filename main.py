"""Six Words to a Payday -- entry program.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt. Deterministic: fixed text, no network, no randomness,
no environment input.
"""

import os

ENTRY = "First paycheck: I bought my freedom."
OUTPUT_PATH = "/output/entry.txt"


def self_check(text: str) -> None:
    """Gate self-check (RULES.txt): valid UTF-8 text, 1-60 chars,
    not only whitespace, exactly six words, no control characters.
    Runs after writing; does not change the output."""
    assert isinstance(text, str)
    assert 1 <= len(text) <= 60, "entry must be 1-60 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert len(text.split()) == 6, "entry must be exactly six words"
    assert all(ord(ch) >= 32 and ord(ch) != 127 for ch in text), (
        "entry must contain no control characters"
    )
    text.encode("utf-8")


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written entry differs from ENTRY"
    self_check(written)


if __name__ == "__main__":
    main()
