with open ("urls.txt", 'r') as file:
    all = file.readlines()
for i in all:
    al = i[:6] + "/" + i[6:]
    rep = al.replace("s", "", 1)
    print(rep)
