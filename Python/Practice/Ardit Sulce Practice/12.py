my_range = range(1, 21)
print(list(map (lambda x : x * 10, my_range)))


#---------Alternate Solution
print([x * 10 for x in my_range])
