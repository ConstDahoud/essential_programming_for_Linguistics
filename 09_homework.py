import re

with open('wsj_partial.txt', 'r') as f0:
    txt = f0.read()

pattern = re.compile('\w*[,.]?/')
word_lst = pattern.finditer(txt)
words = (word.group().replace('/', '') for word in word_lst)

sentence = []
cnt = 0
for word in words:
    sentence.append(word)
    if word == '.':
        cnt += 1
        sentence = ' '.join(sentence)
        sentence = sentence.replace(' ,', ',')
        sentence = sentence.replace(' .', '.')
        print(f'{cnt}. {sentence}')
        sentence = []
