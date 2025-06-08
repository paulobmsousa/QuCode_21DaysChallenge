from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_vector
import numpy as np

# Single Qubit State Representation
# |ψ> = α|0> + β|1> (where α and β are complex numbers satisfying |α|² + |β|² = 1)

def get_bloch_vector(state):
    """Converts a quantum state into Bloch sphere coordinates (θ, φ)."""
    alpha, beta = state
    theta = 2 * np.arccos(abs(alpha))
    phi = np.angle(beta) - np.angle(alpha)
    
    return [np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi), np.cos(theta)]

# Example Quantum State: Superposition (|ψ> = 1/√2 |0> + 1/√2 |1>)
alpha = 1 / np.sqrt(2)
beta = 1 / np.sqrt(2)

bloch_vector = get_bloch_vector([alpha, beta])
print("Bloch Sphere Coordinates:", bloch_vector)

# Visualizing on the Bloch Sphere
plot_bloch_vector(bloch_vector, title="Quantum State on Bloch Sphere")

# Qiskit Quantum Circuit Representation
qc = QuantumCircuit(1)
qc.h(0)  # Apply Hadamard gate to create superposition (|+> state)
qc.draw(output='mpl')  # Visualize circuit
