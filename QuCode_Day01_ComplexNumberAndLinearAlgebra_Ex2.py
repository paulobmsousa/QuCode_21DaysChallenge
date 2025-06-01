class ComplexNumber:
    """Class to represent complex numbers and perform basic operations."""
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __str__(self):
        return f"{self.real} + {self.imag}j" if self.imag >= 0 else f"{self.real} - {-self.imag}j"

    def add(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def multiply(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

# Function to approximate square root using Newton's method
def sqrt(number, precision=0.00001):
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    
    guess = number / 2.0  # Initial guess
    while abs(guess * guess - number) > precision:
        guess = (guess + number / guess) / 2.0
    return guess

# Function to compute eigenvalues and eigenvectors for a 2x2 matrix
def eigenvalues_eigenvectors(matrix):
    a, b = matrix[0]
    c, d = matrix[1]
    trace = a + d
    determinant = a * d - b * c
    
    # Using the manual sqrt function instead of math.sqrt
    lambda1 = (trace + sqrt(trace**2 - 4 * determinant)) / 2
    lambda2 = (trace - sqrt(trace**2 - 4 * determinant)) / 2
    
    eigenvalues = [lambda1, lambda2]
    eigenvectors = [[lambda1 - d, b], [lambda2 - d, b]]
    
    return eigenvalues, eigenvectors

# Testing ComplexNumber Class
c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, -2)

print(f"Complex Number 1: {c1}")
print(f"Complex Number 2: {c2}")
print(f"Sum: {c1.add(c2)}")
print(f"Product: {c1.multiply(c2)}\n")

# 2x2 matrix example
matrix_2x2 = [[2, 3], [4, 1]]

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = eigenvalues_eigenvectors(matrix_2x2)

print("Eigenvalues for 2x2 matrix:")
print(eigenvalues)
print("\nEigenvectors for 2x2 matrix:")
print(eigenvectors)
