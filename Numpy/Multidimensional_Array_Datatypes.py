import numpy as np

# Create arrays with specified data types
arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([1, 2, 3], dtype=np.int32)

# Check data types
print(arr1.dtype)  # Output: float64
print(arr2.dtype)  # Output: int32

# Example of type conversion using astype
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)  # Output: int64 (default)

# Convert the integer array to float
float_arr = arr.astype(np.float64)
print(float_arr.dtype)  # Output: float64

# Convert floating-point numbers to integers
arr = np.array([3.7, 1.2, -2.6, 0.5, 12.9, 10.1])
print(arr)  # Output: [3.7, 1.2, -2.6, 0.5, 12.9, 10.1]

int_arr = arr.astype(np.int32)  # Convert to int32
print(int_arr)  # Output: [3, 1, -2, 0, 12, 10]
