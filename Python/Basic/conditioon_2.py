def umar(hel):
    new_age = hel + 50
    print(new_age)

age = float(input("Give the value: "))
if age>150:
    print("Overage")
elif age == 150:
    print('Can be possible')
    umar(age)
else:
    umar(age)