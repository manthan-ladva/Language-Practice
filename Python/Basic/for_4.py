def celcius():
    list = [10,-20,-289,100]
    for d in list:
        fare= (d * 9/5) + 32
        if fare >= -215.0:
            print(fare)
        else:
            print('Lower temperature Cannot posible')


celcius()
