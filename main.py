"""Two Lines to Your Past Self — make.fun bounty entry.

Writes exactly two lines to /output/entry.txt:
  line 1 — one sentence warning the past self about one specific moment;
  line 2 — one sentence saying why that moment mattered and what changed
  because of it.
The gate requires UTF-8 text of 1 to 280 characters, not only whitespace.
"""

import os

LINE_1 = (
    "Don't say 'I'll call you back tomorrow' when Grandma rings "
    "on the night of 12 August \u2014 stay on the line, even for five more minutes."
)
LINE_2 = (
    "She was gone by morning, so the call you put off is the one conversation "
    "you have spent six years wishing you could buy back."
)

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
