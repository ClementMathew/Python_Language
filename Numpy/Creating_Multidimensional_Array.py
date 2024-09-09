import numpy as np

# random array generation
data = np.random.randn(2, 3) 
print(data)

# initialized array
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
print(arr1)

# multidimension
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print(arr2)

zeroes1 = np.zeros(10)
print(zeroes1)

zeroes2 = np.zeros((3, 6))
print(zeroes2)

empty = np.empty((2, 3, 2))
print()