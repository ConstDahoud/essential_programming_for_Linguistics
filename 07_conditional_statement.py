temp = 27
if temp >= 25:
    print("Drink a cup of cold water")
else:
    print("Drink a cup of hot water")

name = input("What is your name? ")
print(name)
print(type(name))

age = input("What is your age? ")
print(age)
print(repr(age))
print(type(name))

num = int(input("odd or even? "))
if num % 2 == 0:
    print("an even number")
else:
    print("an odd number")

entrance_fee = {
    "under_13": 5000,
    "teen_or_adult": 10000,
    "elderly": 7000,
}

number = int(input("How many people are supposed to visit here? "))
who = list()
for person in range(number):
    print(f'entrance_fee\n{entrance_fee}\n'
          f'1: under_13\n'
          f'2: teens_and_adults\n'
          f'3: elderly\n')
    who.append(int(input("Press the button for entrance fee: ")) - 1)

fees = list()
people = list(entrance_fee.keys())
for i in who:
    fees.append(entrance_fee[people[i]])

result = sum(fees)
print(f"The cost: {result}")

bmi = 20
if (18.5 <= bmi) and (bmi < 25):
    print("normal")
else:
    print("take care of")

weight = float(input("Let me know your weight(kg): "))
height = float(input("Let me know your height(cm): "))
bmi = (10000 * weight) / (height**2)

if bmi < 18.5:
    print("thin")
elif (bmi >= 18.5) and (bmi < 25):
    print("normal")
elif (bmi >= 25) and (bmi < 30):
    print("over weight")
else:
    print("obesity")

line = "Mary eats apples and pears everyday"
if 'apple' in line:
    print("Mary eats apples")
if 'pear' in line:
    print("Mary eats pears")
if 'apple' in line:
    print("Mary eats apples")
elif 'pear' in line:
    print("Mary eats pears")
if 'apples' in line:
    if 'pears' in line:
        print("Mary eats apples and pears")
    else:
        print("Mary eats apples")

n = 5
if n == 5:
    pass
else:
    print("n != 5")