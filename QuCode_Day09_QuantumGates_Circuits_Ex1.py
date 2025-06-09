from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_bloch_multivector
import numpy as np

# Quantum Circuit with common gates
qc = QuantumCircuit(2)  # Two-qubit circuit

# Pauli Gates: X, Y, Z (Basic quantum logic operations)
qc.x(0)  # Apply Pauli-X gate (Bit-flip gate)
qc.y(1)  # Apply Pauli-Y gate
qc.z(1)  # Apply Pauli-Z gate

# Hadamard Gate: Creates quantum superposition (equal probability of |0> and |1>)
qc.h(0)

# Phase Gate: Adds a quantum phase (π/4 rotation)
qc.p(np.pi/4, 1)

# CNOT (Controlled-NOT) Gate: Entangles qubits
qc.cx(0, 1)

# Display quantum circuit
print("Quantum Circuit:")
print(qc.draw())

# Simulate the circuit's statevector
simulator = Aer.get_backend('statevector_simulator')
compiled_circuit = transpile(qc, simulator)
qobj = assemble(compiled_circuit)
result = simulator.run(qobj).result()
statevector = result.get_statevector()

# Visualize quantum state on Bloch sphere
plot_bloch_multivector(statevector)

# Unitary Transformation: Extract the matrix representation of the circuit
unitary_simulator = Aer.get_backend('unitary_simulator')
compiled_circuit_unitary = transpile(qc, unitary_simulator)
qobj_unitary = assemble(compiled_circuit_unitary)
unitary_result = unitary_simulator.run(qobj_unitary).result()
unitary_matrix = unitary_result.get_unitary()

print("Unitary Matrix of the Quantum Circuit:")
print(unitary_matrix)
