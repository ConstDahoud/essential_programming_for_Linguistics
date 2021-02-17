a = 0b0000000011110000
print(a)    # a = 240

# shift the left operand bits towards the left side for the given number of times in the right
# the binary number is appended with 0s at the end
a = a << 2
print(a)    # a = 240 * 2^2 = 960

# left side operand bits are moved towards the right side for the given number of times
# the right side bits are removed
a = a >> 2
print(a)    # a = 960 / 2^2 = 240

a = -0b0000000011110000
print(a)    # a = -240
a = a << 2
print(a)    # a = -240 * 2^2 = -960
a = a >> 2
print(a)    # a = -960 / 2^2 = -240

coordinates = [(0, 0), (0, 1), (1, 0), (1, 1)]
for x, y in coordinates:
    AND = x & y
    OR = x | y
    XOR = x ^ y
    NOT = ~x
    print(f'x: {x}, y: {y}, '
          f'x & y: {AND}, '
          f'x | y: {OR}, '
          f'~x: {NOT}, ')

a = 9    # 0b1001
b = 10    # 0b1010
c = a & b    # 0b1000
print(c)

a = 9    # 0b1001
b = 10    # 0b1010
c = a | b    # 0b1011
print(c)

a = 9    # 0b1001
b = 10    # 0b1010
c = a ^ b    # 0b0011
print(c)

a = 255    # 0b11111111
a = ~a    # -0b100000000 = -256
print(a)
print(bin(a))