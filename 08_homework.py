import re
from collections import Counter


def load_data_source():
    with open('source.txt', 'r') as f0:
        data = f0.read()
    return data


def word_freq_list(data: str) -> None:
    data = data.lower()
    data = re.sub('[!,."\'()]', '', data)
    lst = data.split()
    uni = list(set(lst))
    freq = dict(Counter(lst))
    print(uni)
    print(freq)


txt = load_data_source()
word_freq_list(txt)
