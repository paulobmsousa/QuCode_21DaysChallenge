
import numpy as np

# Complex Numbers Example
complex_number1 = 3 + 4j  # Defining a complex number (3 + 4i)
complex_number2 = 1 - 2j  # Another complex number

# Performing operations on complex numbers
sum_complex = complex_number1 + complex_number2  # Addition
product_complex = complex_number1 * complex_number2  # Multiplication

print(f"Complex Number 1: {complex_number1}")
print(f"Complex Number 2: {complex_number2}")
print(f"Sum of Complex Numbers: {sum_complex}")
print(f"Product of Complex Numbers: {product_complex}\n")

# Vectors in Linear Algebra
vector1 = np.array([2, 3])  # Defining a 2D vector
vector2 = np.array([4, 1])

# Vector operations
dot_product = np.dot(vector1, vector2)  # Dot product

print(f"Vector 1: {vector1}")
print(f"Vector 2: {vector2}")
print(f"Dot Product: {dot_product}\n")

# Matrices in Linear Algebra
matrix = np.array([[2, 3], [4, 1]])  # 2x2 matrix

print("Matrix:")
print(matrix)

# Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)  # Compute eigenvalues and eigenvectors

print("\nEigenvalues of the matrix:")
print(eigenvalues)
print("\nEigenvectors of the matrix:")
print(eigenvectors)
