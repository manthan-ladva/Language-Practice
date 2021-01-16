x = input("Enter the value: ").split(",")

with open("95.txt", 'a+') as file:
    for i in x:
        file.write(i + '\n')
    #file.close()
