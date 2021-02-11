from typing import List

x = 10    # variable 'x' refers to 10
y = 20    # variable 'y' refers to 20
a = x + y
print("x + y =", a)    # print the output

x = 20
y = 5
b = x - y
print("x - y=", b)

x = 5
y = 3
c = x * y
print("x * y =", c)

x = 15
y = 3
d = x / y
print("x / y=", d)

e = (1 + 2) * (3 + 4)    # check the operation priority
print("(1 + 2) * (3 + 4) =", e)

x = 10
y = 3
f = x // y
g = x % y
print("x // y =", f)
print("x % y =", g)

# the above calculation can be replaced with the following expression. it is more pythonic
f, g = divmod(x, y)    # unpacking
print("x // y =", f)
print("x % y =", g)

x = 5
x = -x    # positive to negative
print("reverse plus/minus sign:", x)

x = 2
y = 30
h = x**y
print("x**y =", h)

x = -8
i = abs(x)
print("absolute value:", i)

x = 3.14
j = int(x)
print("convert x to an integer:", j)

x = 3
k = float(x)
print("convert x to a float type number:", k)

x = 3.678
m = round(x, 1)
print("Round a number to a given precision in decimal digits:", m)

"""
# one rose: 5000
# one sunflower: 4000
# one tulip: 7000

# I bought 18 roses, 8 sunflowers, and 21 tulip and I got a 10% discount on them from the owner
# How much cost should I pay?
"""
rose = 5000
sunflower = 4000
tulip = 7000
n_roses = 18
n_sunflowers = 8
n_tulips = 21
rate = 0.1

cost = (rose*n_roses + sunflower*n_sunflowers + tulip*n_tulips) * (1 - rate)
print("the cost i should pay is", cost)

string1 = "pine"
string2 = "apple"
string = string1 + string2
print(string)

name = "ConstDahoud"
code = 201501745

try:
    identity = name + code    # cannot add a string type variable to an integer type one
except TypeError:
    code = str(code)
    identity = name + code
print("identity:", identity)

star = "*"
for num in range(1, 5):
    print(star * num)    # but, multiplication is ok

A = "abcdefghi"
print(A[0])
print(A[1])
print(A[2])
print(A[-1])    # the last index

print(A[1:4])
print(A[:])
print(A[:-1])
print(A[2:])
print(A[:5])
print(A[-4:-1])

string = "This Is My Computer"
print(string.split())
print(string.lower())
print(string.upper())
print(string.replace("This", "It"))
print(len(string))

a = 10
print(type(a))    # check the data type of the variable 'a'

# hexadecimal number
# binary number
# octal number

# convert decimal numbers to hexadecimal numbers
a = 0
b = 255
c = 12345
print(f"{a}: {hex(a)}\n"
      f"{b}: {hex(b)}\n"
      f"{c}: {hex(c)}\n")

# assign hexadecimal numbers to variables
a = 0xFF
b = 0x20
c = 0x0
print(f"{a}, {b}, {c}\n")    # print function prints hexadecimal numbers in decimal numbers

# convert decimal numbers to binary numbers
a = 0
b = 8
c = 32
d = 255
print(f"{a}: {bin(a)}\n"
      f"{b}: {bin(b)}\n"
      f"{c}: {bin(c)}\n")

# assign binary numbers to variables
a = 0b100
b = 0b1001
print(f"{a}, {b}\n")

# convert decimal numbers to octal numbers
a = 8
b = 10
c = 64
print(f"{a}: {oct(a)}\n"
      f"{b}: {oct(b)}\n"
      f"{c}: {oct(c)}\n")

# assign octal numbers to variables
a = 0o10
b = 0o12
c = 0o100
print(f"{a}, {b}, {c}\n")

def converter(decimal_numbers: List[int]) -> None:
    """ input decimal numbers and convert them to binary, octal and hexadecimal numbers

    :param decimal_numbers: one list which consists of integers
    :return: None
    """
    print("decimal numbers, binary numbers, octal numbers, hexadecimal numbers\n")
    for decimal_number in decimal_numbers:
        print(f"{decimal_number:<18}"
              f"{bin(decimal_number):<18}"
              f"{oct(decimal_number):<18}"
              f"{hex(decimal_number):<18}\n")

decimal_numbers = range(11)
converter(decimal_numbers)

a = 2 + 3j    # complex numbers
b = 25

print(a)
print(type(a))
print(a.real)
print(a.imag)
print(a.conjugate())
print(complex(b))    # convert int to complex
