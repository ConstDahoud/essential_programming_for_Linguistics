f0 = open('alice.txt', 'r')
alice = f0.read()
print(alice)
f0.close()

f1 = open('TheNorthWind&theSun.txt', 'r')
wind_sun = f1.read()
print(wind_sun)
f1.close()

print('\n')
f2 = open('TheNorthWind&theSun.txt', 'r')
wind_sun = f2.readline()    # There is a \n at the end of the line.
print(repr(wind_sun))
f2. close()

print('\n')
f3 = open('TheNorthWind&theSun.txt', 'r')
wind_sun = f3.readline()
while wind_sun:
    print(wind_sun)
    wind_sun = f3.readline()
f3.close()

print('\n')
f4 = open('TheNorthWind&theSun.txt', 'r')
wind_sun = f4.readline()
text = ""
while wind_sun:
    text += wind_sun
    wind_sun = f4.readline()
print(text)
f4.close()

print('\n')
f5 = open('TheNorthWind&theSun.txt', 'r')
wind_sun = f5.readline()
text = []
while wind_sun:
    text.append(wind_sun)
    wind_sun = f5.readline()
print(text)
f5.close()

print('\n')
f6 = open('TheNorthWind&theSun.txt', 'r')
wind_sun = f6.readline()
text = []
while wind_sun:
    text.append(wind_sun.rstrip('\n'))    # If you want to remove \n
    wind_sun = f6.readline()
print(text)
f6.close()

print('\n')
f7 = open('TheNorthWind&theSun.txt', 'r')
wind_sun = f7.readlines()    # There is a \n at the end of each lines
print(wind_sun)
f7.close()

print('\n')
f7 = open('TheNorthWind&theSun.txt', 'r')
wind_sun = f7.readlines()    # There is a \n at the end of each lines
for line in wind_sun:
    print(line.rstrip('\n'))    # If you want to remove \n
f7.close()

f8 = open('write_prac.txt', 'w')
f8.write("writing practice\n")
fruit = 'apple'
f8.write(fruit)
f8.close()

f9 = open('newtext.txt', 'w')
for i in range(1, 11):
    line = f'{i}번째 줄입니다.\n'
    f9.write(line)
f9.close()

f10 = open('TheNorthWind&theSun.txt', 'r')
wind_sun = f10.readline()
text = []
while wind_sun:
    text.append(wind_sun.rstrip('\n'))
    wind_sun = f10.readline()
print(text)
f10.close()

f11 = open('write_prac.txt', 'w')
try:
    f11.write(text)    # Can't write list typed data
except TypeError:
    pass
f11.close()

f12 = open('write_prac2.txt', 'w')
for line in text:
    f12.write(line)
f12.close()

f13 = open('write_prac3.txt', 'w')
f13.writelines(text)    # If you use 'writelines' function, you can write list typed data
f13.close()

with open('TheNorthWind&theSun.txt', 'r') as f14:
    wind_sun = f14.read()
    print(wind_sun)

with open('new_prac.txt', 'r') as f15:
    f15.write("Dahoud")
