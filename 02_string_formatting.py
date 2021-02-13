string = 'I am ' + str(27) + 'years old'    # string combination
print(string)

friends = [('Kim', 26), ('Jung', 28), ('Ann', 27)]
for friend in friends:
    print('My friend', friend[0], 'is', friend[1], 'years old.')    # pass into print function the data I will print

"""
# However, the above example is inconvenient to use when I have a lot of values to pass into print function
# and in addition I need to consider how print function works to print the data
"""

friends = [('Kim', 26), ('Jung', 28), ('Ann', 27)]
for friend in friends:
    string = 'My friend ' + friend[0] + ' is ' + str(friend[1]) + ' years old.'
    print(string)
    """
    # the above two statements can be replaced with this and it is more common
    # print('My friend ' + friend[0] + ' is ' + str(friend[1]) + ' years old.')
    """
"""
# The above example is also inconvenient because I should concatenate each strings by putting '+' operation between them
"""

# string formatting expressions

string = 'My name is %s' % 'DaHun'    # %s is a conversion specifier for a string
print(string)

# have to make a tuple for passing various data into conversion(format) specifiers
string = 'My friend %s is %d years old and %fcm tall.' % ('Lee', 27, 175.5)
print(string)

a = 0b10111011
b = 0xc5f
print('binary number: %d, hexadecimal number: %d' % (a, b))

friends = [('Kim', 26), ('Jung', 28), ('Ann', 27), ('Lee', 27)]
for name, age in friends:
    print('My friend %s is %d years old' % (name, age))

try:
    print('%d' % 'Shin')
except TypeError:
    print("ERROR: The type of the data is not fit to the conversion specifier")

key = 'my_var'
value = 1.234
formatted = '%-10s = %.2f' % (key, value)
print(formatted)

try:
    reordered_tuple = '%-10s = %.2f' % (value, key)
    print(reordered_tuple)
except TypeError:
    print("ERROR: The type of the data is not fit to the conversion specifier")

pantry = [
    ('avocado', 1.25),
    ('banana', 2.5),
    ('cherry', 15),
]
for i, (item, count) in enumerate(pantry):
    print('#%d: %-10s = %.2f' % (i, item, count))

for i, (item, count) in enumerate(pantry):
    print('#%d: %-10s = %d' % (
        i+1,
        item.title(),
        round(count)))    # the length of the tuple is too long

# need to write the same variable name in tuple as many times as you use the value
template = '%s likes the food. %s is a good cook.'
name = 'Charles'
formatted = template % (name, name)
print(formatted)

name = 'young'
formatted = template % (name.title(), name.title())
print(formatted)

# string formatting expressions with dictionaries
string = "%(name)s: %(age)d" % {'name': 'Dahun', 'age': 27}
print(string)

print("%(h)s: %(v)-+10.3f" % {'h': 'height', 'v': 3.14})

key = 'my_var'
value = 1.234

old_way = '%-10s = %.2f' % (key, value)
new_way = '%(key)-10s = %(value).2f' % {'key': key, 'value': value}
reordered = '%(key)-10s = %(value).2f' % {'value': value, 'key': key}
assert old_way == new_way == reordered

name = 'Charles'
template = '%s likes the food. %s is a good cook.'

before = template % (name, name)
template = '%(name)s likes the food. %(name)s is a good cook.'
after = template % {'name': name}
assert before == after

pantry = [
    ('avocado', 1.25),
    ('banana', 2.5),
    ('cherry', 15),
]

for i, (item, count) in enumerate(pantry):
    before = '#%d: %-10s = %d' % (
        i+1,
        item.title(),
        round(count)
    )

    after = '#%(loop)d: %(item)-10s = %(count)d' % {
        'loop': i + 1,
        'item': item.title(),
        'count': round(count)
    }    # too long and intricate
    assert before == after

soup = 'lentil'
formatted = 'Today\'s soup is %(soup)s.' % {'soup': soup}
print(formatted)

menu = {
    'soup': 'lentil',
    'oyster': 'tongyoung',
    'special': 'schnitzel',
}
template = ('Today\'s soup is %(soup)s, '
            'buy one get two %(oyster)s oysters, '
            'and our special entree is %(special)s.')
formatted = template % menu
print(formatted)

# Python converts the data types to str automatically
string = 'My friend %s is %s years old and %scm tall.' % ('Park', 27, 178.5)
print(string)

# Thus, you don't need to do like this
string = 'My friend %s is %s years old and %scm tall.' % ('Park', str(27), str(178.5))
print(string)

# float to integer
print('%f' % 25)

# integer to float
print('%d' % 3.14)

# %[flags][width][.precision]f
print('height: %f' % 3.14)
print('height: %.3f' % 3.14)
print('height: %.2f' % 3.14)

print('height: %7.2f' % 3.14)
print('height: %10.2f' % 3.14)

print('height: %07.2f' % 3.14)
print('height: %010.2f' % 3.14)

print('height: %-7.2f' % 3.14)
print('height: %-10.2f' % 3.14)

n = 3
print('num: %+d' % n)
n = -1
print('num: %+d' % n)

print('height: %+-10.3f' % 3.14)

# string formatting method calls

a = 1234.5678
formatted = format(a, ',.2f')
print(formatted)

b = 'my string'
formatted = format(b, '^20s')
print('*', formatted, '*')

fs = '{0}...{1}...{2}'
ms = fs.format('Deep-learning', 42, 'TF')
print(ms)
# {0} <- 'Deep-learning'
# {1} <- 42
# {2} <- 'TF'

print('{0}...{1}...{2}'.format('Deep-learning', 42, 'TF'))
print('{2}...{1}...{0}'.format('Deep-learning', 42, 'TF'))
print('{}...{}...{}'.format('Deep-learning', 42, 'TF'))

key = 'my_var'
value = 1.234
formatted = '{} = {}'.format(key, value)
print(formatted)

formatted = '{:<10} = {:.2f}'.format(key, value)
print(formatted)
print(format(key, '<10s'))
print(format(value, '.2f'))

print('%.2f%%' % 12.5)
print('{} replaces {{}}'.format(1.23))

formatted = '{1} = {0}'.format(key, value)
print(formatted)

name = 'Charles'
formatted = '{0} likes the food. {0} is a good cook.'.format(name)
print(formatted)

pantry = [
    ('avocado', 1.25),
    ('banana', 2.5),
    ('cherry', 15),
]

for i, (item, count) in enumerate(pantry):
    old_style = '#%d: %-10s = %d' % (
        i+1,
        item.title(),
        round(count)
    )
    new_style = '#{}: {:<10s} = {}'.format(
        i+1,
        item.title(),
        round(count)
    )
    assert old_style == new_style

menu = {
    'soup': 'lentil',
    'oyster': 'tongyoung',
    'special': 'schnitzel',
}
formatted = 'The first letter is {menu[oyster][0]!r}'.format(menu=menu)
print(formatted)

old_template = (
    'Today\'s soup is %(soup)s, '
    'buy one get two %(oyster)s oysters, '
    'and our special entree is %(special)s.'
)
old_formatted = old_template % menu
print(old_formatted)

new_template = (
    'Today\'s soup is {soup}, '
    'buy one get two {oyster} oysters, '
    'and our special entree is {special}.'
)
new_formatted = new_template.format(
    soup='lentil',
    oyster='tongyoung',
    special='schnitzel'
)
assert old_formatted == new_formatted

print('{subject}...{num}...{platform}'.format(subject='Deep-learning', num=42, platform='TF'))

study = ['Deep-learning', 42, 'TF']
print('{0}...{1}...{2}'.format(*study))    # unpacking

study = ['Deep-learning', (42, 'TF')]
print('{0[0]}..{0[1]}..{1[0]}..{1[1]}'.format(*study))

study = {'Deep-learning': 'TF', 'random_seed': 42}
print('Deep-learning = {0[Deep-learning]}, random_seed = {0[random_seed]}'.format(study))

print('{0}'.format(3.14))
print('{0:f}'.format(3.14))    # default precision = .6
print('{0:d}'.format(3))
print('{0:f}'.format(3.1))

print('{0:f}'.format(3.14))    # '%f' % 3.14
print('{0:.4f}'.format(3.14))    # '%.4f' % 3.14
print('{0:9.4f}'.format(3.14))    # '%9.4f' % 3.14
print('{0:<10.4f}'.format(3.14))    # '%-10.4f' % 3.14
print('{0:>10.4f}'.format(3.14))    # '%10.4f' % 3.14
print('{0:^10.4f}'.format(3.14))    # ^ means centrally-located

print('{0:+d}, {1:+d}'.format(5, -5))    # '%+d, %+d' % (5, -5)
print('{0:+}, {1:+d}'.format(5, -5))
print('{:+}, {:+}'.format(5, -5))

print('{0:*^10.4f}'.format(3.14))
print('{0:+<10}'.format(7))
print('{0:^^10}'.format('hi'))
print('{:^^10}'.format('hi'))

# f-string

key = 'my_var'
value = 1.234

formatted = f'{key} = {value}'
print(formatted)

formatted = f'{key!r:<10} = {value:.2f}'
print(formatted)

# compare
f_string = f'{key:<10} = {value:.2f}'    # the shortest one
c_tuple = '%-10s = %.2f' % (key, value)
str_args = '{:<10s} = {:.2f}'.format(key, value)
str_kw = '{key:<10} = {value:.2f}'.format(key=key, value=value)
c_dict = '%(key)-10s = %(value).2f' % {'key': key, 'value': value}

assert c_tuple == c_dict == f_string
assert str_args == str_kw == f_string

pantry = [
    ('avocado', 1.25),
    ('banana', 2.5),
    ('cherry', 15),
]

for i, (item, count) in enumerate(pantry):
    old_style = '#%d: %-10s = %d' % (
        i+1,
        item.title(),
        round(count)
    )
    new_style = '#{}: {:<10s} = {}'.format(
        i+1,
        item.title(),
        round(count)
    )
    f_string = f'#{i+1}: {item.title():<10s} = {round(count)}'
    assert old_style == new_style == f_string

for i, (item, count) in enumerate(pantry):
    print(f'{i+1}: '
          f'{item.title():<10s} = '
          f'{round(count)}')

places = 3
number = 1.23456
print(f'The number I selected is {number:.{places}f}')