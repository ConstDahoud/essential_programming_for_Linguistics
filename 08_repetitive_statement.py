student_name = ['Shin', 'Kim', 'Lee', 'Jung']
student_major = ['Linguistics', 'Mathematics', 'Computer science', 'Statistics']

for student_info in zip(student_name, student_major):
    print(student_info)

energy = 3
while energy > 0:
    print("run")
    print(f'energy = {energy}')
    energy -= 1
print("halt")

while True:
    num = input("Enter a number: ")
    if num == "q":
        break
    meter_2 = float(num) * 3.31
    print(f'result = {meter_2}')

for i in range(5):    # [0, 5)
    print(i, end=' ')
print('\n')

for i in range(1, 11, 2):
    print(i, end=' ')
print('\n')

result = 0
for i in range(1, 101, 2):
    result += i
print(f'result = {result}')

s = "We're studying for loop"
for i in s:
    print(i)

lst = ["pen", "car", "cup"]
for word in lst:
    print(word)

for i in range(5):
    print(f'i = {i}')
    if i >= 3:
        continue
    print("check point")

for i in range(1, 11):
    if i == 5:
        break
    if (i % 2) == 0:
        print(f"{i}: an even number")
    else:
        print(f"{i}: an odd number")
