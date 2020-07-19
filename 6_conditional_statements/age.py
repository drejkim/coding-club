age = 13
print(age)
if age == 12:
    print("I'm a pre-teen!")
else:
    print("I'm a teenager!")

age = 8
print(age)
if age == 12:
    print("I'm a pre-teen!")
elif age == 13:
    print("I'm a teenager!")
else:
    print("Huh?")

age = 1
print(age)
if age < 0:
    print("You have not been born yet.")
elif age < 2:
    print("You are a baby!")
else:
    print("You are not a baby. You are growing up.")

age = 13
print(age)
if age == 12 or age == 13:
    print("Are you in middle school?")
else:
    print("Huh?")

age = 15
print(age)
if age >= 13 and age <= 18:
    print("You are a teenager, for sure!")
else:
    print("Huh?")
