def umar(hel):
    new_age = hel + 50
    if new_age > 150:
        print('Out of stock')
    elif new_age == 150:
        print("Limit")
    else:
        print(new_age)


age = input('Give the new age: ')
c = float(age)
print(umar(c))
