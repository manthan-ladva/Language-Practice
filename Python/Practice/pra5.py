"""
2 2
1 2
3 4
"""
import numpy





"""n, m = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(n)], int)
print (array.transpose())
print (array.flatten())


our_array = numpy.array([input().split() for y in range(int(input().split()[0]))], int)
print(numpy.transpose(our_array), our_array.flatten(), sep="\n")
"""

import numpy
r, c = map(int, input().split())
i = numpy.array([input().split() for _ in range(r)], int)
print(numpy.transpose(i))
print(i.flatten())
