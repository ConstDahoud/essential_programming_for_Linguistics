import re

alice = 'Alice, a girl of seven years, is feeling bored and drowsy while sitting on the riverbank with her elder sister. She then notices a talking, clothed White Rabbit with a pocket watch run past. She follows it down a rabbit hole when suddenly she falls a long way to a curious hall with many locked doors of all sizes. She finds a small key to a door too small for her to fit through, but through it she sees an attractive garden. She then discovers a bottle on a table labelled "DRINK ME," the contents of which cause her to shrink too small to reach the key which she has left on the table. She eats a cake with "EAT ME" written on it in currants as the chapter closes.'

# split the line with sentence unit and then print them with numbering
sentences = alice.split('.')
for index, sentence in enumerate(sentences, 1):
    if sentence:
        print(f'{index}: {sentence.strip()}')

# print words with numbering
print('\n')
no_punc = re.sub("[,.\"]", '', alice)
words = no_punc.split()
for index, word in enumerate(words, 1):
    print(f'{index}: {word}')

# print unique words with numbering
print('\n')
unique_words = list(set(words))
for index, word in enumerate(unique_words, 1):
    print(f'{index}: {word}')

# convert the line to lower case except for proper nouns
print('\n')
proper_nouns = {'Alice': 'alice', 'White Rabbit': 'white rabbit'}
lower_case = alice.lower()
for noun in proper_nouns.values():
    if noun in lower_case:
        lower_case = lower_case.replace(noun, noun.title())
print(lower_case)
