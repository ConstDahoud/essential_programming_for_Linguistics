"""
# 1. split the line with white space
# 2. count how many times '\"' occurs
# 3. make a unique word list
# 4. arrange the unique word list in ascending order
"""
alice = 'Alice, a girl of seven years, is feeling bored and drowsy while sitting on the riverbank with her elder sister. She then notices a talking, clothed White Rabbit with a pocket watch run past. She follows it down a rabbit hole when suddenly she falls a long way to a curious hall with many locked doors of all sizes. She finds a small key to a door too small for her to fit through, but through it she sees an attractive garden. She then discovers a bottle on a table labelled "DRINK ME," the contents of which cause her to shrink too small to reach the key which she has left on the table. She eats a cake with "EAT ME" written on it in currants as the chapter closes.'

split_alice = alice.split()
count = alice.count('\"')
print(f'\": {count}')
unique_word_list = list(set(split_alice))
unique_word_list.sort()
print(unique_word_list)