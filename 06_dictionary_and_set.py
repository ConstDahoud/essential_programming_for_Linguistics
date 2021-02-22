from typing import Dict
program_language = {
    1: 'python',
    2: 'java',
    3: 'c++',
    4: 'c#',
    5: 'perl',
}

dic = dict()
dic['apple'] = "www.apple.com"
dic['python'] = "www.python.org"
dic['microsoft'] = "www.microsoft.com"
print(dic['python'])
print(dic['microsoft'])
print(dic['apple'])
print(type(dic))
print(dic)

print(dic.get('apple', 0))    # dict().get(key, a default value)
print(dic.keys())
print(dic.values())
print(dic.items())

ages = {
        'Shin': 27,
        'Kim': 13,
        'Park': 7,
        'Lee': 13,
        'Jung': 58,
}

print(sorted(ages.keys()))
print(sorted(ages.values()))
print(sorted(ages.items(), key=lambda tpl: tpl[1]))

print('apple' in dic.keys())
print('pine apple' in dic.keys())
print("www.microsoft.com" in dic.values())
print("www.constdahoudlab.net" in dic.values())

print(type(dic.keys()))
print(type(list(dic.keys())))

try:
    return_value = dic.pop()
except TypeError:
    print("the pop method expected at least 1 argument, but got 0")
return_value = dic.pop('apple')
print(return_value)
print(dic)

try:
    return_value = dic.popitem('microsoft')
except TypeError:
    print("the popitem method takes no arguments, but 1 given")
return_value = dic.popitem()
print(return_value)
print(dic)

dic = {
        'apple': "www.apple.com",
        'python': "www.python.org",
        'microsoft': "www.microsoft.com",
}
dic.clear()
print(dic)

simple_dic = {
        1: [1, 2, 3],
        2: [3, 4, 5],
}
simple_dic[1].append(4)
print(simple_dic)
simple_dic[2].pop()
print(simple_dic)

scores = {
        'student_1': 100,
        'student_2': 80,
        'student_3': 90,
        'student_4': 50,
        'student_5': 70,
}

def sum_and_mean(dic: Dict):
    sum_result = sum(dic.values())
    mean_result = sum_result / len(dic.keys())
    return sum_result, mean_result

sum_result, mean_result = sum_and_mean(scores)
for name, score in scores.items():
    print(f'{name}: {score}')
print(sum_result, mean_result)

fruit_1 = {'apple', 'banana', 'apple'}
fruit_2 = set({'banana', 'mango'})
print(fruit_1 - fruit_2)
print('mango' in fruit_2)
fruit_3 = fruit_1 | fruit_2
print(fruit_3)
fruit_3 = fruit_1 & fruit_2
print(fruit_3)