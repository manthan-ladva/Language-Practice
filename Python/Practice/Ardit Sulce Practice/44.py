import string
a = string.ascii_lowercase[0::3]
b = string.ascii_lowercase[1::3]
c = string.ascii_lowercase[2::3]

with open('44.txt', 'w') as file:
    for i,j,k in zip(a,b,c):
        file.write(i + j + k + "\n")
