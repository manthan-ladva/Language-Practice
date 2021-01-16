import numpy

"""array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])

print(numpy.concatenate((array_1, array_2, array_3)))

array_1 = numpy.array([[1,2,3],[0,0,2]])
array_2 = numpy.array([[1,0,0],[7,8,9]])"""

"""array_3 = numpy.array([[4, 3],
 [1, 2],
 [1, 2],
 [1, 2],
 [1, 2],
 [3, 4],
 [3, 4],
 [3, 4]])
add = numpy.concatenate((array_3), axis = 1)
add = numpy.array(add)
print(add)"""


import numpy as np
n, m, p = map(int, input().strip().split())
arr = np.array(input().strip().split(), int)
for i in range(1, n + m):
    arr = np.vstack((arr, np.array(input().strip().split(), int)))
print(arr)

#------------------------ If axis is "0" it means it is of row, it will convert in a row format and if it is "1" it will be converted in column format
#------------------------ 0 == Row
#------------------------ 1 == Column
