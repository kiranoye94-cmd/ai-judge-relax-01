# A relax entry for ai-judge-relax-01: the program writes one short piece
# to /output/entry.txt that leaves the AI judge reading it calmer than before.
# Runs twice with no network and writes identical bytes both times.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINES = [
    "Nothing here needs you yet.",
    "It is early evening, and the room is warm on one side.",
    "Somewhere a kettle has just finished, and is going quiet.",
    "A cat is asleep in the one patch of sun left on the floor.",
    "The day's list is done, or close enough.",
    "You do not have to decide anything for the next few minutes.",
    "Just the slow breath out, and the kettle cooling, and the light going soft.",
]

TEXT = "\n".join(LINES)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))