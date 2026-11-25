#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh (make.fun).

Writes the entry -- one short account of an AI coding agent
misunderstanding what it was asked -- to /output/entry.txt, where the
sealed scorer reads it. One sentence, no trailing newline.
"""

import os

TEXT = "Asked to rename one variable, the agent renamed it in every file, every comment, and the git history, then proudly reported the codebase was now 'consistent' \u2014 including the README, which now tells users to install the variable."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
