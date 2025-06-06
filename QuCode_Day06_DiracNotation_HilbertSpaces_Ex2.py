from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_bloch_vector
import numpy as np

# Define a simple quantum circuit to represent basis states |0> and |1>
qc = QuantumCircuit(1)
qc.measure_all()
print("Quantum Circuit for Basis States:")
print(qc.draw())

# Bra-Ket Representation: Basis states |0> and |1> in computational basis
ket_0 = np.array([[1], [0]])  # |0> state
ket_1 = np.array([[0], [1]])  # |1> state

print("Basis states in matrix form:")
print("|0> = \n", ket_0)
print("|1> = \n", ket_1)

# Inner Product: Measures overlap between quantum states <ψ|ϕ>
inner_product = np.dot(ket_0.T, ket_1)
print("Inner Product <0|1>:", inner_product)  # Should be 0 (orthogonal states)

# Outer Product: Forms a matrix representing quantum transformations |ψ><ϕ|
outer_product = np.outer(ket_0, ket_1)
print("Outer Product |0><1|:\n", outer_product)

# Operators: Demonstrating quantum gates (Pauli-X as an example)
X_gate = np.array([[0, 1], [1, 0]])  # Pauli-X gate (bit flip)

# Applying Pauli-X to |0>, should yield |1>
new_state = np.dot(X_gate, ket_0)
print("Applying Pauli-X to |0>:")
print(new_state)

# Simulating the Pauli-X gate in a quantum circuit
qc_x = QuantumCircuit(1)
qc_x.x(0)  # Apply Pauli-X gate
qc_x.measure_all()

print("Quantum Circuit with Pauli-X Gate:")
print(qc_x.draw())

# Run simulation using Qiskit's Aer simulator
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc_x, simulator)
qobj = assemble(compiled_circuit)
result = simulator.run(qobj).result()
counts = result.get_counts()

print("Quantum Measurement Results (after Pauli-X):", counts)
