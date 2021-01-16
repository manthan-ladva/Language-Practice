def string(x):
    x = x.split()
    print(len(x))

with open('words1.txt', 'r') as file:
    word = file.read()
    string(word)
