"""
# 1. remove all punctuations
# 2. split the line with white space
# 3. make an unique word list
# 4. arrange the word list in ascending order
# 5. arrange the word list in descending order
# 6. split the line with a sentence unit
# 7. make a word frequency dictionary
# 8. make a word length dictionary
"""

import re
from collections import Counter

alice = 'Alice, a girl of seven years, is feeling bored and drowsy while sitting on the riverbank with her elder sister. She then notices a talking, clothed White Rabbit with a pocket watch run past. She follows it down a rabbit hole when suddenly she falls a long way to a curious hall with many locked doors of all sizes. She finds a small key to a door too small for her to fit through, but through it she sees an attractive garden. She then discovers a bottle on a table labelled "DRINK ME," the contents of which cause her to shrink too small to reach the key which she has left on the table. She eats a cake with "EAT ME" written on it in currants as the chapter closes.'

no_punctuation = re.sub("[,.\"]", "", alice)
print(no_punctuation)
split_alice = no_punctuation.split()
print(split_alice)
unique_word_list = list(set(split_alice))
print(unique_word_list)
ascending_order = sorted(unique_word_list)
print(ascending_order)
descending_order = sorted(unique_word_list, reverse=True)
print(descending_order)
sentence_list = alice.split(".")
sentence_list.pop()
print(sentence_list)
frequency_dict = dict(Counter(split_alice))
print(frequency_dict)
length_dict = {word: len(word) for word in unique_word_list}
print(length_dict)