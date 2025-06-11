
from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_bloch_multivector

# Quantum Entanglement Demonstration

# Step 1: Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2)

# Step 2: Apply a Hadamard gate to the first qubit to create superposition
qc.h(0)

# Step 3: Apply a CNOT gate (Controlled-NOT) to entangle the qubits
qc.cx(0, 1)

# Bell State |Φ+> = (|00> + |11>) / sqrt(2)
print("Quantum Circuit to create a Bell State:")
print(qc.draw())

# Simulating the entangled state using Qiskit's Aer simulator
simulator = Aer.get_backend('statevector_simulator')
compiled_circuit = transpile(qc, simulator)
qobj = assemble(compiled_circuit)
result = simulator.run(qobj).result()
statevector = result.get_statevector()

# Visualizing the quantum state on Bloch sphere
plot_bloch_multivector(statevector)

# Step 4: Measure the entangled qubits
qc.measure_all()

# Run the measurement simulation
simulator_measurement = Aer.get_backend('qasm_simulator')
compiled_circuit_measurement = transpile(qc, simulator_measurement)
qobj_measurement = assemble(compiled_circuit_measurement)
result_measurement = simulator_measurement.run(qobj_measurement).result()
counts = result_measurement.get_counts()

print("Measurement results of the entangled qubits:", counts)
