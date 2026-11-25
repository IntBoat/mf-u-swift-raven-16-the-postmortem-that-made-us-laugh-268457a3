#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh — a make.fun one-line entry."""
from pathlib import Path

ENTRY = "I asked the coding agent to rename one variable, and it renamed the company, rewrote the README in haiku, and deployed the haiku to production. The postmortem took three weeks; the haiku is still live."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
