import numpy as np

arr = np.arange(10)
print(arr)

print(arr[5])
print(arr[5:8])

arr[5:8] = 12
print(arr)

arr = np.array([0, 1, 2, 3, 4, 12, 12, 12, 8, 9])
arr_slice = arr[5:8]
print(arr_slice)

arr_slice[1] = 12345
print(arr)

arr_slice[:] = 64
print(arr)

# 2 dimensional matrix
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d)

print(arr2d[2])
print(arr2d[0][2])
print(arr2d[0, 2])

# 3 dimensional matrix
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)
print(arr3d[0])

arr3d[0] = 42
print(arr3d)

print(arr3d[1, 0])

x = arr3d[1]
print(x)
print(x[0])
