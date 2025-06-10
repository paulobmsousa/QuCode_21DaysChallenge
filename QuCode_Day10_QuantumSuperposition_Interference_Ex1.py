from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_bloch_multivector

# Quantum Superposition & Interference Demonstration

# Create a Quantum Circuit with 2 qubits
qc = QuantumCircuit(2)

# Step 1: Initialize Qubits in Superposition using Hadamard gate
qc.h(0)  # First qubit is placed in superposition
qc.h(1)  # Second qubit is also placed in superposition

# Step 2: Introduce Phase Shift for Quantum Interference
qc.p(3.14/2, 0)  # Apply phase shift (π/2) to first qubit

# Step 3: Apply Quantum Parallelism by running a controlled operation
qc.cx(0, 1)  # Apply a CNOT gate to entangle qubits

# Step 4: Apply another Hadamard gate to first qubit to demonstrate interference
qc.h(0)

# Step 5: Measure the qubits
qc.measure_all()

# Display Quantum Circuit
print("Quantum Circuit:")
print(qc.draw())

# Simulating the circuit using Qiskit's Aer simulator
simulator = Aer.get_backend('statevector_simulator')
compiled_circuit = transpile(qc, simulator)
qobj = assemble(compiled_circuit)
result = simulator.run(qobj).result()
statevector = result.get_statevector()

# Visualizing the quantum state on Bloch sphere
plot_bloch_multivector(statevector)
