
# Import necessary Qiskit modules
from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.circuit import ParameterVector
import random

# 1️⃣ Quantum Data Encoding
def quantum_data_encoding(data):
    """
    Encodes classical data into a quantum state using parameterized rotations.
    Each classical feature is mapped to a qubit using Ry rotation.
    """
    num_qubits = len(data)  # Number of features = number of qubits
    qc = QuantumCircuit(num_qubits)

    for i, value in enumerate(data):
        qc.ry(value, i)  # Encode data using rotation around Y-axis

    return qc

# Example classical data encoding
sample_data = [random.uniform(0, 3.14) for _ in range(3)]  # Three classical features
qc_data = quantum_data_encoding(sample_data)
qc_data.draw('mpl')  # Visualize encoding circuit

# 2️⃣ Quantum Neural Network (QNN) Ansatz
def quantum_neural_network(num_qubits, params):
    """
    Implements a simple Quantum Neural Network (QNN) Ansatz.
    Uses parameterized gates as trainable quantum neurons.
    """
    qc = QuantumCircuit(num_qubits)

    # Apply parameterized rotations (Trainable Quantum Neurons)
    for i in range(num_qubits):
        qc.ry(params[i], i)

    # Apply entanglement using CNOT gates
    for i in range(num_qubits - 1):
        qc.cx(i, i + 1)

    return qc

# Define trainable parameters
num_qubits = 3
parameters = ParameterVector("theta", num_qubits)  # Trainable parameters
qc_qnn = quantum_neural_network(num_qubits, parameters)
qc_qnn.draw('mpl')  # Visualize Quantum Neural Network Ansatz

# 3️⃣ Simulate Quantum Circuits
def simulate_qc(qc):
    """
    Simulates the quantum circuit and returns measurement results.
    """
    simulator = Aer.get_backend("qasm_simulator")
    compiled_circuit = transpile(qc, simulator)
    result = execute(compiled_circuit, simulator, shots=1024).result()

    return result.get_counts()

# Simulate encoded data circuit
data_results = simulate_qc(qc_data)
print("Quantum Data Encoding Results:", data_results)

# Simulate quantum neural network circuit
qnn_results = simulate_qc(qc_qnn)
print("Quantum Neural Network Results:", qnn_results)
