import numpy as np

N,M = map(int, input().split())

my_array = np.array([input().split()for i in range(N)], int)
print(np.transpose(my_array))
print(my_array.flatten())