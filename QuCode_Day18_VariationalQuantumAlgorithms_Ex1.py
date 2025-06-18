
# Import necessary Qiskit modules
from qiskit import Aer, execute
from qiskit.circuit.library import EfficientSU2
from qiskit.algorithms.minimum_eigen_solvers import VQE
from qiskit.opflow import PauliSumOp
from qiskit.utils import algorithm_globals
from qiskit.algorithms.optimizers import COBYLA

# 1️⃣ Define the problem: Finding the lowest eigenvalue of a simple Hamiltonian
hamiltonian = PauliSumOp.from_list([("Z", 1.0)])  # Simple 1-qubit Hamiltonian

# 2️⃣ Choose a variational quantum circuit (Ansatz)
num_qubits = 1
ansatz = EfficientSU2(num_qubits)  # Parameterized quantum circuit

# 3️⃣ Select an optimizer (classical part)
optimizer = COBYLA(maxiter=100)  # Classical optimization algorithm

# 4️⃣ Setup the quantum simulator
algorithm_globals.random_seed = 42  # Set random seed for reproducibility
backend = Aer.get_backend("aer_simulator_statevector")

# 5️⃣ Run Variational Quantum Eigensolver (VQE)
vqe_instance = VQE(ansatz, optimizer, quantum_instance=backend)
result = vqe_instance.compute_minimum_eigenvalue(hamiltonian)

# 6️⃣ Display results
print("Hybrid Quantum-Classical Computing Results:")
print(f"Estimated Ground State Energy: {result.eigenvalue.real}")
