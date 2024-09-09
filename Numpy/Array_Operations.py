import numpy as np

# initialized array
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)

# multidimension
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)

print(arr1.ndim)
print(arr2.ndim)

print(arr1.shape)
print(arr2.shape)

print(arr1.dtype)
print(arr2.dtype)