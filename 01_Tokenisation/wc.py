# program that counts the number of lines, tokens, and chars in the input

import sys
"""
ln_counter=0 # count every \n
tkn_counter=0 # count every space +1 for every newline
char_counter=0 # count no matter what

for c in sys.stdin.read():
    if c=="\n":
        ln_counter+=1
        tkn_counter+=1
        char_counter+=1
    elif c==" ":
        tkn_counter+=1
        char_counter+=1
    else:
        char_counter+=1


print("Lines: ",ln_counter,"\n\tTokens: ",tkn_counter,"\n\t\tCharacters:",char_counter)

#this works really well assuming that there are no trailing spaces after at the end of a line, found that out the hard way.
"""

#this part counts consonants and vowels, it aslo gives average syllable per word count
#this assumes that syllables=vowels

vow="aeiou" # all vowels
cons="bcdfghjklmnpqrstvwxyz" # all consonants

vow_counter=0 
cons_counter=0
tkn_counter=0

for c in sys.stdin.read():
    if c in vow:
        vow_counter+=1
    elif c in cons:
        cons_counter+=1
    elif c==" " or c=="\n":
        tkn_counter+=1

avg=vow_counter/tkn_counter
formatted="{:.2f}".format(avg)

print("Vowels: ",vow_counter,"\n\tConsonants: ",cons_counter,"\n\t\tSyllable average:",formatted)

