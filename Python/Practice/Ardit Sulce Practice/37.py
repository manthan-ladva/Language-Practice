def string(x):
    x = x.split()
    print(len(x))

with open('words2.txt', 'r') as file:
    word = file.read()
    string(word.replace(",", " "))
