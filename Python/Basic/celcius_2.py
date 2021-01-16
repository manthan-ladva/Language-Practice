def celcius(c):
    fare= (c*9/5) +32
    if fare >= -215.0:
        print(fare)
    else:
        print('Lower temperature Cannot posible')

x = float(input('Give the number: '))
celcius(x)
