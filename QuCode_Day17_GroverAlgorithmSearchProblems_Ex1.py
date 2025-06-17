# Import necessary Qiskit modules
from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.visualization import plot_histogram

# 1️⃣ Function to create an Oracle (marks the desired state)
def grover_oracle(num_qubits, target_state):
    """
    Creates an Oracle circuit that flips the sign of the target state.
    This helps Grover's Algorithm amplify the correct solution probability.
    """
    oracle = QuantumCircuit(num_qubits)

    # Apply X-gates to reach the target state
    for index, bit in enumerate(target_state):
        if bit == '0':
            oracle.x(index)

    # Apply multi-controlled Z (which flips target state amplitude)
    oracle.h(num_qubits - 1)
    oracle.mcx(list(range(num_qubits - 1)), num_qubits - 1)  # Multi-controlled NOT
    oracle.h(num_qubits - 1)

    # Undo the X-gates applied earlier
    for index, bit in enumerate(target_state):
        if bit == '0':
            oracle.x(index)

    return oracle.to_gate(label="Oracle")

# 2️⃣ Function to apply Grover's Diffusion Operator (Amplifies correct state)
def grover_diffusion(num_qubits):
    """
    Implements the Grover Diffusion Operator.
    This reflects across the average amplitude to amplify correct solutions.
    """
    diffusion = QuantumCircuit(num_qubits)

    diffusion.h(range(num_qubits))
    diffusion.x(range(num_qubits))
    
    diffusion.h(num_qubits - 1)
    diffusion.mcx(list(range(num_qubits - 1)), num_qubits - 1)
    diffusion.h(num_qubits - 1)
    
    diffusion.x(range(num_qubits))
    diffusion.h(range(num_qubits))

    return diffusion.to_gate(label="Diffusion")

# 3️⃣ Function to run Grover’s Algorithm
def grovers_algorithm(num_qubits, target_state):
    """
    Implements Grover's Algorithm to search for the target state in an unsorted database.
    The number of iterations is approximately sqrt(N), providing quadratic speedup.
    """
    # Step 1: Initialize Quantum Circuit
    qc = QuantumCircuit(num_qubits, num_qubits)

    # Step 2: Apply Hadamard gates to create uniform superposition
    qc.h(range(num_qubits))

    # Step 3: Apply Grover iterations (Oracle + Diffusion)
    num_iterations = int(np.sqrt(2**num_qubits))  # Approximate optimal iterations

    for _ in range(num_iterations):
        qc.append(grover_oracle(num_qubits, target_state), range(num_qubits))
        qc.append(grover_diffusion(num_qubits), range(num_qubits))

    # Step 4: Measure qubits
    qc.measure(range(num_qubits), range(num_qubits))

    # Step 5: Execute on a quantum simulator
    simulator = Aer.get_backend('qasm_simulator')
    compiled_circuit = transpile(qc, simulator)
    result = execute(compiled_circuit, simulator, shots=1024).result()

    # Step 6: Display results
    print("Grover's Algorithm Search Results:")
    print(result.get_counts())

    # Visualize results
    qc.draw('mpl')
    plot_histogram(result.get_counts())

# Execute Grover’s Algorithm for a 3-qubit system, searching for "101"
grovers_algorithm(3, "101")
