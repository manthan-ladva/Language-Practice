#------------------------Map

def square(num):
    a = num ** 2
    return a

num_list = [1,2,3,4,5,6,7,8,9,10]
for i in map(square, num_list):
    print(i)
