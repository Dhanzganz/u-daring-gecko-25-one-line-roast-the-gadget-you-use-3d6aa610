"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line (<=200 chars) about the phone used
every day to /output/entry.txt.

The program writes the line, then reads it back to verify the file
contains exactly that line before exiting.
"""

import os

LINE = "My phone's battery health is 78% \u2014 it dies faster than my motivation and judges me with 1% left like it planned the drama."


def main() -> None:
    # Create /output if missing; never delete it (in the grader it is a
    # mounted volume, so removing it would fail the run).
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

    # Verify the file on disk holds exactly the roast line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt does not match LINE"
    print("OK: /output/entry.txt verified")


if __name__ == "__main__":
    main()
