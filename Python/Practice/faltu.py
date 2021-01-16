"""import random                                               #-----------Importing Library

ka = int(input())                                           #-----------Input of No. of list
ma = int(input())                                           #-----------Input of modulo {less than 1000}

list_l = []                                                 #-----------Main List

if 1 <= ka <= 7 and 1 <= ma <= 1000:                        #-----------If both the input is ajust in given range then proceed

    no_list = 1                                             #-----------Variable of the upcoming loop
    while no_list <= ka:                                    #-----------Number of list is made here
        d = []                                              #-----------Sub List

        list_items = 1                                      #-----------Variable for the another upcoming loop
        while list_items <= random.randrange(3, 7):         #------List ma number bharvana
            num = int(input())
            d.append(num)
            list_items +=1

        print(d)
        print("Successfull 3")
        no_list +=1
        list_l.append(d)
"""

"""def f(x):
    return x ** 2


z = list(map(f, list1))
print(z[0])"""
"""
for item in z:
    print(item, end = "")
    print(z[0])"""
list1 = [1, 9, 990]
sum = 0
j= 0
for i in list1:
    sum = sum + int(list1[j])
    j += 1
sum = sum % 1000
print(sum)
