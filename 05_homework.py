"""
Make a plural form of given word, and then print it
"""


words = [
    'sheep',
    'book',
    'box', 'pass',
    'city', 'cry',
    'wife', 'knife',
    'leaf', 'shelf',
    'child',
]

NNS_list = [
    '',
    's',
    'es', 'es',
    'ies', 'ies',
    'ves', 'ves',
    'ves', 'ves',
    'irregular',
]

word_dic = dict(zip(words, NNS_list))


def plural(word: str, suffix: str) -> str:
    if suffix == '':
        word += suffix
        return word

    elif suffix == 's':
        word += suffix
        return word

    elif word.endswith(('x', 's')):
        word += suffix
        return word

    elif word.endswith('y'):
        word = word[:-1]
        word += suffix
        return word

    elif word.endswith('fe'):
        word = word[:-2]
        word += suffix
        return word

    elif word.endswith('f'):
        word = word[:-1]
        word += suffix
        return word

    elif suffix == 'irregular':
        word += 'ren'
        return word


while True:
    word = input("Enter a word: ")
    if word == '-1':
        break
    elif word in word_dic:
        suffix = word_dic[word]
        word = plural(word, suffix)
        print(f'Result: {word}')
