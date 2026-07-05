# Q.1
# import numpy as np
# # a) Create a 1D array
# arr1 = np.array([10, 20, 30, 40, 50])

# # b) Create a 3x3 2D array
# arr2 = np.array([[1, 2, 3],
#                  [4, 5, 6],
#                  [7, 8, 9]])

# # Print 1D array
# print("1D Array:")
# print(arr1)
# print("Shape:", arr1.shape)
# print("Data Type:", arr1.dtype)

# # Print 2D array
# print("\n2D Array:")
# print(arr2)
# print("Shape:", arr2.shape)
# print("Data Type:", arr2.dtype)


# # Q.2
# import numpy as np

# # a) 1D array of 8 zeros
# a = np.zeros(8)

# # b) 4x4 array of ones
# b = np.ones((4, 4))

# # c) 3x3 matrix of zeros
# c = np.zeros((3, 3))

# # Print arrays
# print("1D Array of Zeros:")
# print(a)

# print("\n4x4 Array of Ones:")
# print(b)

# print("\n3x3 Matrix of Zeros:")
# print(c)


# # Q.3
# import numpy as np

# # a) Numbers from 0 to 20
# a = np.arange(0, 21, 1)

# # b) Even numbers from 10 to 50
# b = np.arange(10, 51, 2)

# # c) Numbers from 5 to 100 with step 5
# c = np.arange(5, 101, 5)

# # Print arrays
# print("Numbers from 0 to 20:")
# print(a)

# print("\nEven Numbers from 10 to 50:")
# print(b)

# print("\nNumbers from 5 to 100 (Step = 5):")
# print(c)


# # Q.4
# import numpy as np

# # a) 10 equally spaced numbers between 0 and 5
# a = np.linspace(0, 5, 10)

# # b) 15 equally spaced numbers between -10 and 10
# b = np.linspace(-10, 10, 15)

# # Print arrays
# print("10 Equally Spaced Numbers (0 to 5):")
# print(a)
# print("Length:", len(a))

# print("\n15 Equally Spaced Numbers (-10 to 10):")
# print(b)
# print("Length:", len(b))


# # Q.5
# import numpy as np

# # a) 1D array of 10 random numbers
# a = np.random.rand(10)

# # b) 3x3 matrix using randn()
# b = np.random.randn(3, 3)

# # c) 4x5 matrix of random integers between 10 and 50
# c = np.random.randint(10, 51, (4, 5))

# # Print arrays
# print("1D Random Array:")
# print(a)

# print("\n3x3 Random Normal Matrix:")
# print(b)

# print("\n4x5 Random Integer Matrix:")
# print(c)


# # Q.6
# import numpy as np
# v1 = np.array([2, 4, 6, 8])
# v2 = np.array([1, 3, 5, 7])

# # Addition
# add = v1 + v2

# # Subtraction
# sub = v1 - v2

# # Element-wise Multiplication
# mul = v1 * v2

# # Dot Product
# dot = np.dot(v1, v2)

# # Print results
# print("Vector 1:", v1)
# print("Vector 2:", v2)

# print("\nAddition:")
# print(add)

# print("\nSubtraction:")
# print(sub)

# print("\nElement-wise Multiplication:")
# print(mul)

# print("\nDot Product:")
# print(dot)


# #Q.7
# import numpy as np
# # Create two 3x3 matrices
# A = np.array([[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]])

# B = np.array([[9, 8, 7],
#               [6, 5, 4],
#               [3, 2, 1]])

# # Matrix Addition
# add = A + B

# # Matrix Multiplication
# mul = A @ B

# # Element-wise Multiplication
# element_mul = A * B

# # Print results
# print("Matrix A:")
# print(A)
# print("\nMatrix B:")
# print(B)

# print("\nMatrix Addition:")
# print(add)

# print("\nMatrix Multiplication:")
# print(mul)

# print("\nElement-wise Multiplication:")
# print(element_mul)


# # Q.8
# import numpy as np

# # Create a 4x4 matrix of random integers
# arr = np.random.randint(1, 101, (4, 4))

# # Print matrix
# print("Matrix:")
# print(arr)

# # Print properties
# print("\nShape:", arr.shape)
# print("Dimension:", arr.ndim)
# print("Total Elements:", arr.size)
# print("Data Type:", arr.dtype)
# print("Minimum Value:", arr.min())
# print("Maximum Value:", arr.max())


# # Q.9
# import numpy as np
# # Generate 20 random integers between 1 and 50
# arr = np.random.randint(1, 51, 20)

# # Reshape into 4x5 matrix
# matrix = arr.reshape(4, 5)

# # Print matrix
# print("4x5 Matrix:")
# print(matrix)

# # Statistics
# print("\nSum:", matrix.sum())
# print("Mean:", matrix.mean())
# print("Standard Deviation:", matrix.std())

# # Maximum value in each row
# print("\nMaximum Value in Each Row:")
# print(matrix.max(axis=1))


# Q.10
import numpy as np

try:
    n = int(input("Enter how many numbers you want to generate: "))
    # Check if the input is valid
    if n <= 0:
        print("Please enter a positive number.")
    else:
        arr = np.random.randint(10, 101, n)

        # Print the array
        print("\nGenerated Array:")
        print(arr)

        # Calculate and print statistics
        print("\nMean:", np.mean(arr))
        print("Median:", np.median(arr))
        print("Standard Deviation:", np.std(arr))
        print("Minimum Value:", np.min(arr))
        print("Maximum Value:", np.max(arr))

        # Reshape into a 2D array if possible
        if n % 2 == 0:
            matrix = arr.reshape(n // 2, 2)

            print("\nReshaped 2D Array:")
            print(matrix)

            print("\nRow-wise Sum:")
            print(np.sum(matrix, axis=1))

        else:
            print("\nArray cannot be reshaped into a 2D array with 2 columns.")

except ValueError:
    print("Invalid input! Please enter an integer.")