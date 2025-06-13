# Import Qiskit core packages
from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.visualization import plot_histogram

# 1️⃣ Quantum Circuit Model: Standard approach using gates
def circuit_model_demo():
    """
    Demonstrates the Circuit Model of Quantum Computing using Qiskit.
    We create a basic quantum circuit, apply gates, and measure the qubits.
    """
    circuit = QuantumCircuit(2, 2)  # Two qubits, two classical bits

    # Apply Hadamard gate to the first qubit (creates superposition)
    circuit.h(0)
    
    # Apply CNOT gate (entanglement)
    circuit.cx(0, 1)
    
    # Measure both qubits
    circuit.measure([0, 1], [0, 1])

    # Execute the circuit on a simulator
    simulator = Aer.get_backend('qasm_simulator')
    compiled_circuit = transpile(circuit, simulator)
    result = execute(compiled_circuit, simulator).result()
    
    print("Circuit Model Results:")
    print(result.get_counts())
    
    # Visualize results
    circuit.draw('mpl')

# 2️⃣ Adiabatic Quantum Computing (QC) Simulation without Qiskit Algorithms
def adiabatic_qc_demo():
    """
    Demonstrates Adiabatic Quantum Computing concept.
    Instead of using Qiskit's optimization package, we simulate annealing manually.
    """
    def classical_optimization():
        """A simple classical simulation of an optimization problem."""
        best_x = None
        best_value = float("inf")
        
        # Simple grid search for optimization
        for x in range(-10, 10):
            for y in range(-10, 10):
                value = (x**2 + y**2)  # Simulated energy function
                if value < best_value:
                    best_value = value
                    best_x = (x, y)
        
        return best_x, best_value

    optimal_solution = classical_optimization()
    print(f"Adiabatic QC Approximate Optimization Result: {optimal_solution}\n")

# 3️⃣ Measurement-Based Quantum Computing (MBQC)
def measurement_based_qc_demo():
    """
    Demonstrates Measurement-Based QC using Qiskit.
    We create a simple cluster state and perform measurements to drive computation.
    """
    circuit = QuantumCircuit(3, 3)  # Three qubits

    # Create a cluster state using Hadamard and CNOT gates
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.cx(1, 2)

    # Measure each qubit to drive the computation
    circuit.measure([0, 1, 2], [0, 1, 2])

    simulator = Aer.get_backend('qasm_simulator')
    compiled_circuit = transpile(circuit, simulator)
    result = execute(compiled_circuit, simulator).result()
    
    print("Measurement-Based QC Results:")
    print(result.get_counts())
    
    # Visualize results
    circuit.draw('mpl')

# Run demonstrations
circuit_model_demo()
adiabatic_qc_demo()
measurement_based_qc_demo()
