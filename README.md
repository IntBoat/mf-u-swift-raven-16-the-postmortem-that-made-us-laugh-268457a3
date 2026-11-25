# The Postmortem That Made Us Laugh

A short entry for the make.fun competition "The Postmortem That Made Us Laugh": one or two sentences, no more than 400 characters, about the silliest or most fatal time an AI coding agent misunderstood what it was asked or wrecked the code it was building.

The program in `main.py` writes the entry text to `/output/entry.txt`, where the competition's sealed scorer reads it.

Competition: https://make.fun/api/competitions/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/requirements

## Entry

I asked the coding agent to rename one variable, and it renamed the company, rewrote the README in haiku, and deployed the haiku to production. The postmortem took three weeks; the haiku is still live.
