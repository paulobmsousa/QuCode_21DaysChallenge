from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_bloch_multivector

# Quantum Measurement & No-Cloning Theorem Demonstration

# Step 1: Create a Quantum Circuit with 1 qubit
qc = QuantumCircuit(1)

# Step 2: Initialize Qubit in Superposition using Hadamard gate
qc.h(0)  # Creates superposition (|0> + |1>) / sqrt(2)

# Step 3: Measurement causes Wavefunction Collapse
qc.measure_all()

# Display Quantum Circuit
print("Quantum Circuit Demonstrating Measurement Collapse:")
print(qc.draw())

# Simulate the circuit using Qiskit's Aer simulator
simulator = Aer.get_backend('statevector_simulator')
compiled_circuit = transpile(qc, simulator)
qobj = assemble(compiled_circuit)
result = simulator.run(qobj).result()
statevector_before = result.get_statevector()

print("\nQuantum State Before Measurement:")
print(statevector_before)

# Step 4: Run the measurement process (causes state collapse)
simulator_measurement = Aer.get_backend('qasm_simulator')
compiled_circuit_measurement = transpile(qc, simulator_measurement)
qobj_measurement = assemble(compiled_circuit_measurement)
result_measurement = simulator_measurement.run(qobj_measurement).result()
counts = result_measurement.get_counts()

print("\nMeasurement Results (Collapsed State):", counts)

# No-Cloning Theorem Demonstration:
# Step 5: Attempt to copy a quantum state (Not possible due to quantum mechanics!)
qc_clone = QuantumCircuit(2)
qc_clone.h(0)  # Creates superposition
qc_clone.cx(0, 1)  # Attempts to copy state using CNOT (which doesn't work for arbitrary states)

print("\nQuantum Circuit Attempting Cloning (Fails due to No-Cloning Theorem):")
print(qc_clone.draw())

# Simulating incorrect cloning attempt
compiled_circuit_clone = transpile(qc_clone, simulator)
qobj_clone = assemble(compiled_circuit_clone)
result_clone = simulator.run(qobj_clone).result()
statevector_clone = result_clone.get_statevector()

print("\nStatevector After Incorrect Cloning Attempt:")
print(statevector_clone)
