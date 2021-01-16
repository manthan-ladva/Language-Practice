import random                                               #-----------Importing Library

def f(x):
    return x ** 2

ka = int(input())                                           #-----------Input of No. of list
ma = int(input())                                           #-----------Input of modulo {less than 1000}

list_l = []                                                 #-----------Main List
list_l2 =  []
if 1 <= ka <= 7 and 1 <= ma <= 1000:                        #-----------If both the input is ajust in given range then proceed

    no_list = 1                                             #-----------Variable of the upcoming loop
    while no_list <= ka:                                    #-----------Number of list is made here
        d = []                                              #-----------Sub List

        list_items = 1                                      #-----------Variable for the another upcoming loop
        while list_items <= random.randrange(3, 7):         #------List ma number bharvana
            num = int(input())
            d.append(num)
            list_items +=1

        list_l.append(d)
        print(d)
        print("Successfull 3")
        no_list +=1

    i = 0
    while i < len(list_l):
        ash = list_l[i][random.randrange(0, len(list_l[i]))]
        list_l2.append(ash)
        print(ash)
        i+=1
    print(list_l2)

    z = list(map(f, list_l2))
    print(z)

    sum = 0
    j= 0
    for i in z:
        sum = sum + int(z[j])
        j += 1
    sum = sum % ma
    print(sum)





"""K, M = [int(x) for x in input().split()]
arrayN = []
for _i_ in range(K):
    arrayN.append([int(x) for x in input().split()][1:])

from itertools import product
possible_combination = list(product(*arrayN))

def func(nums):
    return sum(x*x for x in nums) % M

print(max(list(map(func, possible_combination))))"""
