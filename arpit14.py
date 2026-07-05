# import numpy as np

# # Create a 5x6 array with random integers
# arr = np.random.randint(10, 101, (5, 6))

# print("Array:\n", arr)

# # Print properties
# print("Shape:", arr.shape)
# print("Size:", arr.size)
# print("Data Type:", arr.dtype)

import numpy as np

arr = np.random.randint(1, 51, 20)

print("Array:", arr)

print("Minimum:", arr.min())
print("Index of Minimum:", arr.argmin())

print("Maximum:", arr.max())
print("Index of Maximum:", arr.argmax())

print("Sum:", arr.sum())
print("Mean:", arr.mean())
print("Standard Deviation:", arr.std())