import glob2

letters = []
word = "python"
file_list = glob2.glob("*.txt")

for filename in file_list:
    with open(filename, 'r') as file:
        bal = file.read()
        if bal in word:
            letters.append(bal)
print(letters)
