import numpy as np

# Create two arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Basic operations
print("Element-wise addition:", arr1 + arr2)
print("Element-wise multiplication:", arr1 * arr2)
print("Dot product:", np.dot(arr1, arr2))

# Create a 2D array
matrix = np.array([[1, 2], [3, 4]])
print("\nMatrix:")
print(matrix)
print("Matrix transpose:")
print(matrix.T)

# Random numbers
print("\nRandom numbers (0-1):", np.random.rand(3))