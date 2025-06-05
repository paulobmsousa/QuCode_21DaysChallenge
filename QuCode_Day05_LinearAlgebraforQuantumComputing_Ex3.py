# Sparse Matrix Representation for Quantum Computing

class SparseMatrix:
    """Represents a sparse matrix using a dictionary (only nonzero values stored)."""
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = {}  # Dictionary to store (row, col): value pairs

    def set(self, row, col, value):
        """Set a nonzero value in the matrix."""
        if value != 0:
            self.data[(row, col)] = value

    def get(self, row, col):
        """Get value from the matrix, defaulting to 0 if not explicitly stored."""
        return self.data.get((row, col), 0)

    def multiply(self, other):
        """Multiply two sparse matrices manually."""
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions incompatible for multiplication")

        result = SparseMatrix(self.rows, other.cols)
        for (i, k), v in self.data.items():
            for j in range(other.cols):
                if (k, j) in other.data:
                    result.set(i, j, result.get(i, j) + v * other.data[(k, j)])
        return result

    def display(self):
        """Print matrix in dense form for easy visualization."""
        for i in range(self.rows):
            row = [self.get(i, j) for j in range(self.cols)]
            print(row)

# Tensor Product (Sparse Kronecker Product)
def sparse_tensor_product(A, B):
    """Compute tensor product manually using sparse representation."""
    result = SparseMatrix(A.rows * B.rows, A.cols * B.cols)
    
    for (i, j), v in A.data.items():
        for (m, n), w in B.data.items():
            result.set(i * B.rows + m, j * B.cols + n, v * w)

    return result

# Example Quantum States (Sparse Representation)
psi1 = SparseMatrix(2, 1)
psi1.set(0, 0, 1)  # |0> state
psi2 = SparseMatrix(2, 1)
psi2.set(1, 0, 1)  # |1> state

# Compute Tensor Product
tensor_result = sparse_tensor_product(psi1, psi2)
print("Tensor Product (|0> ⊗ |1>):")
tensor_result.display()

# Inner Product Example
psi = SparseMatrix(2, 1)
psi.set(0, 0, 1)  # |ψ> = |0>
phi = SparseMatrix(2, 1)
phi.set(1, 0, 1)  # |ϕ> = |1>
inner_product_result = sum(psi.get(i, 0) * phi.get(i, 0) for i in range(psi.rows))
print("Inner Product of |ψ> and |ϕ>:", inner_product_result)

# Outer Product Example
outer_result = SparseMatrix(2, 2)
for i in range(psi.rows):
    for j in range(phi.rows):
        outer_result.set(i, j, psi.get(i, 0) * phi.get(j, 0))

print("Outer Product of |ψ> ⊗ |ϕ>:")
outer_result.display()

# Unitary Matrix Example (Sparse Hadamard Gate)
H = SparseMatrix(2, 2)
H.set(0, 0, 1 / 2**0.5)
H.set(0, 1, 1 / 2**0.5)
H.set(1, 0, 1 / 2**0.5)
H.set(1, 1, -1 / 2**0.5)

print("Hadamard Matrix:")
H.display()

# Verify Unitarity
H_T = SparseMatrix(2, 2)
for i in range(2):
    for j in range(2):
        H_T.set(j, i, H.get(i, j))  # Transpose

unitary_check = H_T.multiply(H)
print("Verification (H†H = I):")
unitary_check.display()
