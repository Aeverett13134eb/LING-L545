#this program replaces every space " " with a newline "\n"
# it also space separates the following punctuation . , ( )

import sys

text=sys.stdin.read()

text=text.replace(" ", "\n") # every token gets its own line

text=text.replace(".", " . ") # space out .
text=text.replace(",", " , ") # space out ,
text=text.replace("(", " ( ") # space out (
text=text.replace(")", " ) ") # space out )

sys.stdout.write(text)
