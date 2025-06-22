
# Import necessary Qiskit modules
from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.circuit.library import RealAmplitudes

# 1️⃣ Finance: Quantum Portfolio Optimization (Variational Ansatz)
def quantum_portfolio_optimization():
    """
    Uses a variational quantum circuit to optimize portfolio allocation.
    Quantum optimization can improve financial strategies significantly.
    """
    num_qubits = 3  # Represent three assets

    # Define variational circuit (Quantum Portfolio Ansatz)
    qc = RealAmplitudes(num_qubits)
    
    # Simulate execution
    simulator = Aer.get_backend("statevector_simulator")
    result = execute(qc, simulator).result()
    
    print("Quantum Portfolio Optimization - Statevector:")
    print(result.get_statevector())

# 2️⃣ Chemistry: Quantum Simulation of Molecular Energies
def quantum_chemistry_simulation():
    """
    Simulates a basic quantum molecular structure using Qiskit.
    Quantum computing helps solve molecular interactions faster.
    """
    qc = QuantumCircuit(2)

    # Apply rotations representing molecular orbitals
    qc.h(0)
    qc.cx(0, 1)

    # Simulate execution
    simulator = Aer.get_backend("statevector_simulator")
    result = execute(qc, simulator).result()
    
    print("Quantum Chemistry Simulation - Statevector:")
    print(result.get_statevector())

# 3️⃣ AI: Quantum Neural Networks for Machine Learning
def quantum_ai_neural_network():
    """
    Implements a simple Quantum Neural Network (QNN) Ansatz.
    Quantum AI has potential for faster deep learning models.
    """
    num_qubits = 3
    qc = QuantumCircuit(num_qubits)

    # Apply trainable quantum rotations (QNN approach)
    for qubit in range(num_qubits):
        qc.ry(0.5, qubit)

    # Apply entanglement
    for qubit in range(num_qubits - 1):
        qc.cx(qubit, qubit + 1)

    simulator = Aer.get_backend("statevector_simulator")
    result = execute(qc, simulator).result()
    
    print("Quantum Neural Network - Statevector:")
    print(result.get_statevector())

# 4️⃣ Optimization: Solving Complex Problems Faster
def quantum_optimization():
    """
    Demonstrates a quantum approach to solving optimization problems.
    Quantum algorithms provide speedups for logistics, scheduling, and more.
    """
    num_qubits = 3

    # Define a simple quantum optimization circuit
    qc = QuantumCircuit(num_qubits)
    
    # Apply Hadamard gates for superposition
    qc.h(range(num_qubits))

    simulator = Aer.get_backend("statevector_simulator")
    result = execute(qc, simulator).result()
    
    print("Quantum Optimization - Statevector:")
    print(result.get_statevector())

# Execute all demonstrations
quantum_portfolio_optimization()
quantum_chemistry_simulation()
quantum_ai_neural_network()
quantum_optimization()
