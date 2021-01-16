def umar(hel):
    new_age=hel+ 50
    if new_age>150:
        return 'Out of stock'
    elif new_age==150:
        return 'Limit'
    else:
        return new_age


age = float(input('Give the new age: '))
print(umar(age))
