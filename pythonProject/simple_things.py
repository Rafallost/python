name = input("What is your name?")
print("Hello " + name.upper())
year = input("What is your year of birth?")
age_result = 2023 - int(year)
print("You are " + str(age_result) + " years old")
size = float(input("What is your foot size?"))
print("your foot size is " + str(size) + "cm")

print("10 + 3 = " + str(10 + 3))
print("10 - 3 = " + str(10 - 3))
print("10 * 3 = " + str(10 * 3))
print("10 / 3 = " + str(10 / 3))
print("10 % 3 = " + str(10 % 3))
print("10 ** 3 = " + str(10 ** 3))

if age_result >= 21:
    print("Your are adult")
elif (age_result >= 10) and (age_result < 21):
    print("You are teenager")
else:
    print("you are kid")

numbs = [0, 1, 2, 3, 4]

for i in numbs:
    print(i)

print("\n")

i = 0
while i < 3:
    print(numbs[i])
    i += 1

print("\n")

print(numbs[0:3])
