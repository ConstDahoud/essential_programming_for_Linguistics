"""
# 1. change the following line to lower case
# 2. remove periods
# 3. change the word 'the' to "THE"
# 4. split the line to a word list
"""

import re

alice = 'Alice, a girl of seven years, is feeling bored and drowsy while sitting on the riverbank with her elder sister. She then notices a talking, clothed White Rabbit with a pocket watch run past. She follows it down a rabbit hole when suddenly she falls a long way to a curious hall with many locked doors of all sizes. She finds a small key to a door too small for her to fit through, but through it she sees an attractive garden. She then discovers a bottle on a table labelled "DRINK ME," the contents of which cause her to shrink too small to reach the key which she has left on the table. She eats a cake with "EAT ME" written on it in currants as the chapter closes.'

lower_case = alice.lower()
no_period = lower_case.replace(".", "")
line = re.sub("the ", "THE ", no_period)
word_list = line.split()
for index, word in enumerate(word_list, 1):
    print(f'{index}: {word}')

