# Import necessary Qiskit modules
from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.visualization import plot_histogram
from qiskit.extensions import UnitaryGate
import numpy as np

# 1️⃣ Function to build Quantum Phase Estimation (QPE) circuit
def quantum_phase_estimation():
    """
    Implements the Quantum Phase Estimation algorithm using Qiskit.
    
    Steps:
    - Create a quantum register for the control qubits (acting as phase measurement qubits).
    - Apply Hadamard gates to the control qubits to create superposition.
    - Apply controlled unitary operations (powers of the unitary U).
    - Apply Inverse Quantum Fourier Transform (QFT).
    - Measure the control qubits.
    """
    
    # Define the phase (theta) we want to estimate: θ = π/3
    theta = np.pi / 3  # Phase for eigenvalue of unitary U

    # Define the unitary matrix U = exp(i * 2πθ)
    U = np.array([[1, 0], [0, np.exp(1j * 2 * np.pi * theta)]])  
    unitary_gate = UnitaryGate(U)

    # Number of qubits for phase estimation (control qubits)
    num_qubits = 3

    # Create a quantum circuit with (num_qubits + 1) qubits
    qc = QuantumCircuit(num_qubits + 1, num_qubits)

    # Apply Hadamard gates to control qubits (superposition)
    for qubit in range(num_qubits):
        qc.h(qubit)

    # Apply controlled unitary operations (powers of U)
    for qubit in range(num_qubits):
        power = 2**qubit  # Apply U^(2^qubit)
        qc.append(unitary_gate.control(1), [qubit, num_qubits])

    # Apply inverse Quantum Fourier Transform (QFT) on control qubits
    qc.append(qft_inverse(num_qubits), range(num_qubits))

    # Measure control qubits
    qc.measure(range(num_qubits), range(num_qubits))

    # Simulate execution
    simulator = Aer.get_backend('qasm_simulator')
    compiled_circuit = transpile(qc, simulator)
    result = execute(compiled_circuit, simulator, shots=1024).result()
    
    # Display results
    print("Quantum Phase Estimation Results:")
    print(result.get_counts())

    # Draw circuit
    qc.draw('mpl')
    plot_histogram(result.get_counts())

# 2️⃣ Function to implement Inverse Quantum Fourier Transform (QFT)
def qft_inverse(num_qubits):
    """
    Implements the inverse Quantum Fourier Transform (QFT).
    This reverses the quantum states back into a classical readable form.
    """
    qft_circuit = QuantumCircuit(num_qubits)

    for j in range(num_qubits):
        for k in range(j):
            qft_circuit.cp(-np.pi / (2 ** (j - k)), k, j)  # Controlled Phase Shift
        qft_circuit.h(j)  # Hadamard gate
    for qubit in range(num_qubits // 2):
        qft_circuit.swap(qubit, num_qubits - qubit - 1)  # Swap qubits for proper ordering

    return qft_circuit.to_gate(label="QFT†")
