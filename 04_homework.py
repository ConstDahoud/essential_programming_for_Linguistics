# search words in the following line

import re

alice = 'Alice, a girl of seven years, is feeling bored and drowsy while sitting on the riverbank with her elder sister. She then notices a talking, clothed White Rabbit with a pocket watch run past. She follows it down a rabbit hole when suddenly she falls a long way to a curious hall with many locked doors of all sizes. She finds a small key to a door too small for her to fit through, but through it she sees an attractive garden. She then discovers a bottle on a table labelled "DRINK ME," the contents of which cause her to shrink too small to reach the key which she has left on the table. She eats a cake with "EAT ME" written on it in currants as the chapter closes.'

alice = re.sub('[\,\.]', '', alice)
while True:
    word = input("Enter a word you'll find: ")
    if word == '-1':
        break
    key_word = re.compile(word + r'\b', re.IGNORECASE)
    key_words = key_word.findall(alice)
    if key_words:
        print(f'System found {word} in the line. it occurs {len(key_words)} times')
    else:
        print(f'The word you entered is not found')
