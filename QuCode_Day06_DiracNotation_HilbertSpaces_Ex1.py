# Dirac Notation & Hilbert Spaces Demonstration

# Bra-Ket notation: Quantum states are represented as "kets" |ψ> and "bras" <ψ|
# Example: Basis states |0> and |1> (Computational Basis)

class Ket:
    """Represents a quantum state in Ket notation |ψ>."""
    def __init__(self, vector):
        self.vector = vector  # Column vector representation

    def __str__(self):
        return f"|ψ> = {self.vector}"

    def conjugate_transpose(self):
        """Returns the conjugate transpose (bra) <ψ|."""
        return Bra([x for x in self.vector])  # Assuming real values (no complex conjugate needed)

class Bra:
    """Represents a quantum state in Bra notation <ψ|."""
    def __init__(self, vector):
        self.vector = vector  # Row vector representation

    def __str__(self):
        return f"<ψ| = {self.vector}"

# Basis States: The fundamental quantum states
ket_0 = Ket([1, 0])  # |0> state
ket_1 = Ket([0, 1])  # |1> state

print("Basis states:")
print(ket_0)
print(ket_1)

# Inner Product: Measures overlap between quantum states <ψ|ϕ>
def inner_product(bra, ket):
    """Computes inner product <ψ|ϕ>."""
    return sum(b * k for b, k in zip(bra.vector, ket.vector))

bra_0 = ket_0.conjugate_transpose()
bra_1 = ket_1.conjugate_transpose()
print("Inner product <0|1>:", inner_product(bra_0, ket_1))  # Should be 0 (orthogonal states)

# Outer Product: Forms a matrix representing quantum transformations |ψ><ϕ|
def outer_product(ket, bra):
    """Computes outer product |ψ><ϕ| as a matrix."""
    return [[k * b for b in bra.vector] for k in ket.vector]

print("Outer product |0><1|:")
outer_matrix = outer_product(ket_0, bra_1)
for row in outer_matrix:
    print(row)

# Operators: Quantum operators transform quantum states
# Example: Pauli-X (NOT gate in quantum computing)
X_operator = [[0, 1], [1, 0]]  # Swaps |0> and |1>

def apply_operator(operator, ket):
    """Applies an operator matrix to a quantum state."""
    result_vector = [sum(operator[i][j] * ket.vector[j] for j in range(len(ket.vector))) for i in range(len(operator))]
    return Ket(result_vector)

# Applying Pauli-X to |0>, should yield |1>
new_state = apply_operator(X_operator, ket_0)
print("Applying Pauli-X to |0>:")
print(new_state)
