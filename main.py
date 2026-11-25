"""One-Line Office Joke Laugh-Off entry (variant 2).

Writes a single original one-line office joke to /output/entry.txt.
Standard library only, deterministic, no network access.
"""

from pathlib import Path

# The entry: exactly one line, 113 characters, no trailing spaces.
JOKE = "The calendar invite invited itself to the meeting, declined, and rescheduled it for a time that works for no one."

OUTPUT_PATH = Path("/output/entry.txt")


def validate_line(line: str) -> str:
    """Check the entry line against the competition's one-line gate.

    The line must be a single line of 1-200 characters with no
    surrounding whitespace. Returns the line unchanged when valid.
    """
    if not line:
        raise ValueError("entry line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry line must be 1-200 characters")
    if line != line.strip():
        raise ValueError("entry line must not have surrounding whitespace")
    return line


def main() -> None:
    """Write the validated joke as exactly one line of UTF-8 text."""
    line = validate_line(JOKE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
