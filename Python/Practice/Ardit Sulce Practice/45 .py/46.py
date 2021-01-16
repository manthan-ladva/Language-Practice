import glob2

letters = []
file_list = glob2.glob("*.txt")

for filename in file_list:
    with open(filename, 'r') as file:
        letters.append(file.read())

print(letters)
