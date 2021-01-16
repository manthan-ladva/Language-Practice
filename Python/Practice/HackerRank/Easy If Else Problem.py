def If_Else(number):
    if number % 2 == 0:
        if number in range(2,6):
            print('2. Not Weird')
        elif number in range(6,21):
            print('3. Weird')
        else:
            print('4. Not Weird')

    else:
        print('1. Weird')

while True:
    number = int(input())
    If_Else(number)