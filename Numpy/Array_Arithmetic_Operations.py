import numpy as np

arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr)

arr_squared = arr * arr
print(arr_squared)

arr_sum = arr + arr
print(arr_sum)

reciprocal_arr = 1 / arr
print(reciprocal_arr)

sqrt_arr = arr ** 0.5
print(sqrt_arr)

arr = np.array([[1., 2., 3.], [4., 5., 6.]])
scalar = 2.0

result1 = arr + scalar
print(result1)

arr = np.array([[1., 2., 3.], [4., 5., 6.]])
arr2 = np.array([10., 20., 30.])

result2 = arr + arr2
print(result2)

arr = np.array([[1., 2., 3.], [4., 5., 6.]])
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])

comparison_result = arr2 > arr
print(comparison_result)
