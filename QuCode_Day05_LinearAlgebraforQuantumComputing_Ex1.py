import numpy as np

# Tensor Product: Used in quantum mechanics to combine quantum states
# Example: Combining two quantum states |ψ1> and |ψ2>
psi1 = np.array([[1], [0]])  # |0> qubit
psi2 = np.array([[0], [1]])  # |1> qubit

# Compute the tensor product (Kronecker product)
tensor_product = np.kron(psi1, psi2)
print("Tensor Product (|0> ⊗ |1>):\n", tensor_product)

# Inner Product: Measures similarity between quantum states (|ψ> · |ϕ>)
# Example: Computing inner product of |ψ> = [1, 0] and |ϕ> = [0, 1]
psi = np.array([1, 0])
phi = np.array([0, 1])

inner_product = np.dot(psi, phi)  # Should be 0, as they are orthogonal
print("Inner Product of |ψ> and |ϕ>:", inner_product)

# Outer Product: Produces a matrix representation of a quantum state |ψ> ⊗ |ϕ>†
outer_product = np.outer(psi, phi)
print("Outer Product of |ψ> ⊗ |ϕ>:\n", outer_product)

# Unitary Matrices: Preserve quantum state normalization (U†U = I)
# Example: Hadamard gate (used to create quantum superposition)
H = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])

# Verify unitarity (U†U = I)
unitary_check = np.dot(H.T.conj(), H)  # Should be identity matrix
print("Hadamard Matrix:\n", H)
print("Verification (H†H = I):\n", unitary_check)
