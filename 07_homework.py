import re
from collections import Counter

# open and read the file
with open('alice.txt', 'r') as f0:
    text = f0.read()

text = re.sub("[.,\"]", "", text)
text = text.lower()
words = text.split()
word_dic = dict(Counter(words))
word_dic = word_dic.items()
word_dic = sorted(word_dic, key=lambda x: x[0])

with open('alice_word_list.txt', 'w') as f1:
    for word, num in word_dic:
        print(f'The number of {word} in the data is {num}')
        f1.write(f'The number of {word} in the data is {num}\n')

word_dic = dict(word_dic)
print(word_dic)
