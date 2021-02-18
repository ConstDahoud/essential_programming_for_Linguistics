from typing import List

names = ['Shin', 'Kim', 'Lee']
print(names)
print(names[0])
print(names[1])
print(names[2])

a = list(range(10))
print(a[0:5])
print(a[5:])
print(a[:3])

a = list(range(4))
b = [5, 6, 7]
print(a+b)

a = list(range(6))
a[2] = 30    # now, a[2] refer to 30
print(a)

a = list(range(4))
print(len(a))

a = list(range(4))
a.append(4)
print(a)

a = list(range(4))
a.extend([4, 5, 6])
print(a)

a = [2, 4, 5]
a.insert(0, 1)
print(a)
a.insert(2, 3)
print(a)

cars = ['BMW', 'BENZ', 'VOLKSWAGEN', 'AUDI']
cars.remove('BMW')
print(cars)

a = list(range(6))
return_value = a.pop()
print(f'return_value: {return_value}, a: {a}')
return_value = a.pop()
print(f'return_value: {return_value}, a: {a}')
return_value = a.pop(1)    # you can choose an index to pop, but be careful of out of index error
print(f'return_value: {return_value}, a: {a}')

a = ['abc', 'def', 'ghi']
print(a.index('def'))
try:
    a.index('jkl')
except ValueError:
    print("'jkl' is not in list a")

a = [1, 100, 2, 100, 3, 100]
print(a.count(100))
print(a.count(200))

a = [3, 4, 5, 1, 2]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

lst = [3, 4, 5, 1, 2]
lst.reverse()
print(lst)
lst = ['h', 'e', 'l', 'l', 'o']
lst.reverse()
print(lst)

lst = [1, 2, 3, 4, 5]
del lst[0]
print(lst)


def sum_and_mean(lst: List[int]):
    add_values = sum(lst)
    mean_values = add_values / len(lst)
    return add_values, mean_values


lst = [10, 20, 30, 40, 50]
sum_result, mean_result = sum_and_mean(lst)
print(f'sum: {sum_result}, mean: {mean_result}')


def pop_sum_and_mean(lst: List[int]):
    lst.pop()
    lst.pop(0)
    add_values = sum(lst)
    mean_values = add_values / len(lst)
    return add_values, mean_values


lst = [10, 20, 30, 40, 50]
sum_result, mean_result = pop_sum_and_mean(lst)
print(f'sum: {sum_result}, mean: {mean_result}')


def sum_and_mean(lst: List[int]):
    add_values = sum(lst)
    mean_values = add_values / len(lst)
    return add_values, mean_values


integers = []
for _ in range(5):
    value = int(input("enter an integer number: "))
    integers.append(value)

sum_result, mean_result = sum_and_mean(integers)
print(f'sum: {sum_result}, mean: {mean_result}')

spellings = ['b', 'c', 'a', 'd', 'e']
spellings.sort(reverse=True)
print(spellings)

tpl = (1, 2, 3)
print(tpl)
print(type(tpl))

tpl = 1, 2, 3, 4
print(tpl)
print(type(tpl))

tpl = (1,)
print(tpl)
print(type(tpl))

tpl = 1,
print(tpl)
print(type(tpl))

tpl = (1)    # if there's no comma behind 1 surrounded by (), it is recognized an integer
print(tpl)
print(type(tpl))   # <class 'int'>

tpl = tuple(range(1, 7))
print(tpl[:3])
print(tpl[4:6])

tpl_1 = (1, 2, 3)
tpl_2 = (4, 5, 6)
tpl_3 = tpl_1 + tpl_2
print(tpl_1)
print(tpl_2)
print(tpl_3)

tpl = (1, 2, 3)
print(tpl[0])
try:
    tpl[0] = 7
except TypeError:
    print("tuple is immutable")

tpl = (1, 2, 3)
print(len(tpl))

tpl = 1, 2, 3    # tuple packing
print(tpl)

one, two, three = tpl    # tuple unpacking
print(one, two, three)

tpl = 1, 2, 3
try:
    one, two = tpl
except ValueError:
    print("Too many values to unpack")

city, latitude, longitude = 'Seoul', 37.541, 126.986
print(city, latitude, longitude)

tpl = ('abc', 'def', 'ghi')
tpl.index('def')
try:
    tpl.index('jkl')
except ValueError:
    print("the value is not in the tuple")

tpl = (1, 100, 2, 100, 3, 100)
print(tpl.count(100))
print(tpl.count(200))

values = []
for _ in range(3):
    value = int(input("enter an integer: "))
    values.append(value)

values = tuple(values)
sum_result = sum(values)
mean_result = sum_result / len(values)
print(f'sum: {sum_result}, mean: {mean_result}')