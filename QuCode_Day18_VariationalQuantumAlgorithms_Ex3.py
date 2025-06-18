
# Import necessary Qiskit modules
from qiskit import QuantumCircuit, Aer, execute
import random

# 1️⃣ Define the Hamiltonian Matrix (Z Pauli Operator)
def hamiltonian_expectation(statevector):
    """
    Computes expectation value ⟨ψ|H|ψ⟩ for a given quantum state.
    The Hamiltonian is Z-Pauli: [[1, 0], [0, -1]].
    """
    return (statevector[0].conjugate() * 1 * statevector[0] + 
            statevector[1].conjugate() * (-1) * statevector[1]).real

# 2️⃣ Define Variational Quantum Circuit (Ansatz)
def variational_circuit(theta):
    """
    Constructs a single-qubit variational circuit with a parameterized Ry rotation.
    """
    qc = QuantumCircuit(1)
    qc.ry(theta, 0)  # Parameterized rotation around Y-axis
    return qc

# 3️⃣ Classical Optimization (Gradient Descent)
def gradient_descent(expectation_func, initial_theta, learning_rate=0.1, max_iter=100):
    """
    Implements basic gradient descent to minimize the expectation value.
    Finds the optimal θ that minimizes ⟨ψ|H|ψ⟩.
    """
    theta = initial_theta
    for _ in range(max_iter):
        # Compute expectation value
        qc = variational_circuit(theta)
        simulator = Aer.get_backend("statevector_simulator")
        result = execute(qc, simulator).result()
        statevector = result.get_statevector()

        expectation = expectation_func(statevector)

        # Compute finite difference approximation of gradient
        delta = 0.01
        qc_plus = variational_circuit(theta + delta)
        result_plus = execute(qc_plus, simulator).result()
        statevector_plus = result_plus.get_statevector()
        expectation_plus = expectation_func(statevector_plus)

        gradient = (expectation_plus - expectation) / delta

        # Update theta using gradient descent
        theta -= learning_rate * gradient

    return theta, expectation

# 4️⃣ Run VQE
initial_theta = random.uniform(0, 3.14)  # Initialize randomly
optimal_theta, min_energy = gradient_descent(hamiltonian_expectation, initial_theta)

# 5️⃣ Display Results
print("Hybrid Quantum-Classical Computing Results:")
print(f"Estimated Ground State Energy: {min_energy}")
print(f"Optimal Theta Value: {optimal_theta}")
