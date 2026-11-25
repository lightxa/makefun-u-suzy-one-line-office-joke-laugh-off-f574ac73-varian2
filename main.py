"""One-Line Office Joke Laugh-Off entry (variant 2).

Writes a single original one-line office joke to /output/entry.txt.
Standard library only, deterministic, no network access.
"""

from pathlib import Path

JOKE = (
    "The calendar invite invited itself to the meeting, declined, "
    "and rescheduled it for a time that works for no one."
)


def main() -> None:
    """Write the joke as exactly one line of UTF-8 text."""
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
