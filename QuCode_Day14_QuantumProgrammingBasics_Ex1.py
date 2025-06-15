
# Importing Qiskit components
from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.visualization import plot_histogram

# 1️⃣ Introduction to Qiskit
print("Welcome to Quantum Programming with Qiskit!")

# 2️⃣ Writing the First Quantum Circuit
def first_quantum_circuit():
    """
    This function demonstrates the basics of quantum circuit programming in Qiskit.
    We will:
    - Create a quantum circuit with one qubit
    - Apply a Hadamard gate to create superposition
    - Measure the qubit to collapse its state
    - Run the circuit on a simulator and view results
    """
    
    # Step 1: Create a quantum circuit with 1 qubit and 1 classical bit
    circuit = QuantumCircuit(1, 1) 

    # Step 2: Apply Hadamard gate (H-gate) to create superposition
    circuit.h(0)  # The qubit now has equal probability of being |0⟩ or |1⟩

    # Step 3: Measure the qubit
    circuit.measure(0, 0)  # Measure quantum state and store in classical bit

    # Step 4: Run the circuit on a simulator
    simulator = Aer.get_backend('qasm_simulator')
    compiled_circuit = transpile(circuit, simulator)
    result = execute(compiled_circuit, simulator, shots=1024).result()

    # Step 5: Show measurement results
    counts = result.get_counts()
    print("Measurement Results:", counts)

    # Step 6: Visualize results
    circuit.draw('mpl')  # Draw the circuit
    plot_histogram(counts)  # Histogram of results

# Execute the function
first_quantum_circuit()
