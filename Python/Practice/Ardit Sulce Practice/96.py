a = []

with open("96chat.txt", 'a+') as file:
    while True:
        x = input("Enter the word: ")
        if x == "CLOSE":
            for i in a:
                file.write(i + '\n')
            break
        a.append(x)


#------------------------------------------------Alternate Solution

file = open("96chat.txt", 'a+')

while True:
    line = input("Enter the word: ")
    if line == "CLOSE":
        file.close()
        break
    else:
        file.write(line + '\n')
