import string
a = string.ascii_lowercase[0::2]
b = string.ascii_lowercase[1::2]
for i,j in zip(a,b):
    print(i + j)
