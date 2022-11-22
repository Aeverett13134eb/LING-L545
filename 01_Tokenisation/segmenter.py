# program replaces every full stop followed by a space ". " with a full stop and newline ".\n"

import sys

text=sys.stdin.read()

sentences=text.replace(". ",".\n")

sys.stdout.write(sentences)

