
# Import Qiskit modules
from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.algorithms import Shor
import numpy as np

# 1️⃣ Define the number to factor (RSA uses large primes, we use a small example)
N = 15  # Example: Factoring 15 (3 × 5)

# Create and run Shor’s algorithm instance
shor_instance = Shor(N)

# Run the algorithm on Qiskit's simulator
simulator = Aer.get_backend("qasm_simulator")
result = shor_instance.run(simulator)

# Display results
print("Factors found by Shor's Algorithm:", result.factors)

# 2️⃣ Why this matters for Cryptography:
print("\n🚨 Shor's Algorithm can efficiently factor large numbers, which breaks RSA encryption!")
print("RSA relies on the difficulty of factoring large numbers for security.")
print("Quantum computers running Shor’s Algorithm will make classical cryptography obsolete.")

# 3️⃣ Post-Quantum Cryptography:
print("\n🛡️ To counter this, researchers are developing post-quantum cryptographic methods:")
print("- Lattice-based cryptography")
print("- Hash-based cryptography")
print("- Quantum Key Distribution (QKD) for secure communications")
