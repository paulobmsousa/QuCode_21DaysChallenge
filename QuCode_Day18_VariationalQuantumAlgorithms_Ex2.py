# Import necessary Qiskit modules
from qiskit import QuantumCircuit, Aer, execute
from qiskit.circuit import Parameter
import numpy as np
from scipy.optimize import minimize

# 1️⃣ Define the problem: Hamiltonian for a 1-qubit system (Z Pauli Operator)
hamiltonian_matrix = np.array([[1, 0], [0, -1]])  # Corresponds to the Pauli Z operator

# 2️⃣ Define Variational Quantum Circuit (Ansatz)
def variational_circuit(theta):
    """
    Constructs the quantum circuit with a parameterized rotation gate.
    This is used as the Ansatz for approximating the ground state.
    """
    qc = QuantumCircuit(1)
    qc.ry(theta, 0)  # Rotation around Y-axis
    return qc

# 3️⃣ Compute Expectation Value
def expectation_value(theta):
    """
    Computes the expectation value of the Hamiltonian for a given theta value.
    This is the key step in VQE to estimate the ground-state energy.
    """
    qc = variational_circuit(theta)
    simulator = Aer.get_backend("statevector_simulator")
    result = execute(qc, simulator).result()
    statevector = result.get_statevector()

    # Compute expectation value ⟨ψ|H|ψ⟩
    exp_val = np.real(statevector.conj().T @ hamiltonian_matrix @ statevector)
    return exp_val

# 4️⃣ Classical Optimization to Minimize Energy
initial_theta = np.random.rand()  # Initialize parameter randomly
result = minimize(expectation_value, initial_theta, method="COBYLA")

# 5️⃣ Display Results
print("Hybrid Quantum-Classical Computing Results:")
print(f"Estimated Ground State Energy: {result.fun}")
print(f"Optimal Theta Value: {result.x}")
