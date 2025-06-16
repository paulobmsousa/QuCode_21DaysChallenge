
from qiskit import QuantumCircuit, Aer, transpile, execute
import numpy as np
from math import gcd

# 1️⃣ Define the number to factor
N = 15  # Example: Factoring 15 (should return 3 and 5)

# 2️⃣ Pick a random number 'a' (must be coprime with N)
def find_coprime(N):
    for a in range(2, N):
        if gcd(a, N) == 1:
            return a
    return None

a = find_coprime(N)

# 3️⃣ Create Quantum Circuit for modular exponentiation
def quantum_modular_exponentiation(a, N, num_qubits):
    """
    Constructs the quantum circuit for modular exponentiation of 'a^x mod N'.
    The exponentiation is encoded within the quantum states.
    """
    qc = QuantumCircuit(num_qubits + 1, num_qubits)
    
    # Apply Hadamard to create superposition
    for qubit in range(num_qubits):
        qc.h(qubit)
    
    # Apply controlled modular exponentiation
    for qubit in range(num_qubits):
        exponent = 2**qubit
        modular_result = (a**exponent) % N
        qc.append(UnitaryGate([[1, 0], [0, np.exp(2j * np.pi * modular_result / N)]]).control(1), [qubit, num_qubits])

    return qc

# 4️⃣ Apply Quantum Fourier Transform
def quantum_fourier_transform(qc, num_qubits):
    """
    Implements the Quantum Fourier Transform (QFT) for phase estimation.
    This extracts useful periodicity information from the quantum states.
    """
    for j in range(num_qubits):
        for k in range(j):
            qc.cp(np.pi / (2 ** (j - k)), k, j)  # Controlled Phase Shift
        qc.h(j)  # Hadamard gate

    for qubit in range(num_qubits // 2):
        qc.swap(qubit, num_qubits - qubit - 1)  # Swap qubits for proper ordering

    return qc

# 5️⃣ Run Shor’s Algorithm
def shors_algorithm(N):
    num_qubits = 4  # Choose number of qubits for phase estimation
    qc = quantum_modular_exponentiation(a, N, num_qubits)
    
    # Apply Quantum Fourier Transform for phase estimation
    qc = quantum_fourier_transform(qc, num_qubits)

    # Measure
    qc.measure(range(num_qubits), range(num_qubits))

    # Simulate execution
    simulator = Aer.get_backend('qasm_simulator')
    compiled_circuit = transpile(qc, simulator)
    result = execute(compiled_circuit, simulator, shots=1024).result()

    # Get measurement outcomes
    counts = result.get_counts()
    print("Quantum Phase Estimation Results:", counts)

    # Find possible factors
    possible_r = max(counts, key=counts.get)  # Find dominant measurement result
    if possible_r.isdigit():
        r = int(possible_r)
        factors = [gcd(a ** (r // 2) - 1, N), gcd(a ** (r // 2) + 1, N)]
        print("Found Factors:", factors)
    else:
        print("No valid factors found.")

# Execute Shor’s Algorithm
shors_algorithm(N)
