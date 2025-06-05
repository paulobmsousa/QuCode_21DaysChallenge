# Matrix Operations for Quantum Computing without external libraries

# Helper function for matrix multiplication
def matrix_multiply(A, B):
    """Multiply two matrices A and B manually."""
    result = [[0] * len(B[0]) for _ in range(len(A))]  # Create empty matrix
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Tensor Product (Kronecker Product)
def tensor_product(A, B):
    """Compute Kronecker product manually."""
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    
    result = [[0] * (cols_A * cols_B) for _ in range(rows_A * rows_B)]
    
    for i in range(rows_A):
        for j in range(cols_A):
            for m in range(rows_B):
                for n in range(cols_B):
                    result[i * rows_B + m][j * cols_B + n] = A[i][j] * B[m][n]
    
    return result

# Inner Product (Dot Product)
def inner_product(A, B):
    """Compute inner product manually."""
    return sum(A[i] * B[i] for i in range(len(A)))

# Outer Product
def outer_product(A, B):
    """Compute outer product manually."""
    return [[A[i] * B[j] for j in range(len(B))] for i in range(len(A))]

# Unitary Matrix Verification
def is_unitary(U):
    """Check if U is a unitary matrix by computing U†U = I."""
    U_conjugate_transpose = [[U[j][i] for j in range(len(U))] for i in range(len(U[0]))]  # Transpose
    identity_check = matrix_multiply(U_conjugate_transpose, U)
    identity = [[1 if i == j else 0 for j in range(len(U))] for i in range(len(U))]  # Identity matrix
    
    return identity_check == identity  # Returns True if unitary

# Example Quantum States
psi1 = [[1], [0]]  # |0> state
psi2 = [[0], [1]]  # |1> state

# Tensor Product Example
tensor_result = tensor_product(psi1, psi2)
print("Tensor Product (|0> ⊗ |1>):")
for row in tensor_result:
    print(row)

# Inner Product Example
psi = [1, 0]
phi = [0, 1]
print("Inner Product of |ψ> and |ϕ>:", inner_product(psi, phi))

# Outer Product Example
outer_result = outer_product(psi, phi)
print("Outer Product of |ψ> ⊗ |ϕ>:")
for row in outer_result:
    print(row)

# Unitary Matrix Example (Hadamard Gate)
H = [[1 / 2**0.5, 1 / 2**0.5], [1 / 2**0.5, -1 / 2**0.5]]
print("Hadamard Matrix:")
for row in H:
    print(row)

# Verify Unitarity
print("Is Hadamard Matrix Unitary?:", is_unitary(H))
