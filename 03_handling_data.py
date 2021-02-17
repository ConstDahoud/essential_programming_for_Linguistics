from typing import List

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