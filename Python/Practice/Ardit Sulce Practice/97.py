with open("97chat.txt", 'a+') as file:
    while True:
        x = input("Enter the word: ")

        if x == "SAVE":
            file.close()
            file = open("97chat.txt", 'a+')

        elif x == "CLOSE":
            file.close()
            break

        else:
            file.write(x + '\n')
