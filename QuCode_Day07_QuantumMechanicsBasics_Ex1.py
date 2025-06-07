
import numpy as np
import matplotlib.pyplot as plt

# Schrödinger's Equation: Time evolution of quantum states
# Example: Free particle in 1D (Wavefunction evolution)

def schrodinger_evolution(psi, H, dt, steps):
    """Solves the time-dependent Schrödinger equation numerically."""
    evolved_states = []
    for _ in range(steps):
        # Time evolution using unitary transformation: psi' = exp(-iH dt) * psi
        psi = np.dot(np.linalg.matrix_power(np.eye(len(H)) - 1j * H * dt, steps), psi)
        evolved_states.append(psi)
    return evolved_states

# Define Hamiltonian (Energy operator) for a simple quantum system
H = np.array([[0, -1], [-1, 0]])  # Example: Two-state quantum system
psi_initial = np.array([1, 0])  # Initial quantum state

# Time evolution simulation
dt = 0.1  # Small time step
steps = 50
evolution = schrodinger_evolution(psi_initial, H, dt, steps)

# Plot Evolution of Quantum State
plt.plot([np.abs(state[0]) for state in evolution], label="Probability of |0>")
plt.plot([np.abs(state[1]) for state in evolution], label="Probability of |1>")
plt.xlabel("Time Steps")
plt.ylabel("Probability")
plt.title("Quantum State Evolution (Schrödinger Equation)")
plt.legend()
plt.show()

# Measurement in Quantum Mechanics: Observing collapses quantum states
def measure(psi):
    """Simulates quantum measurement by collapsing the wavefunction."""
    probabilities = np.abs(psi)**2  # Probability of each state
    collapsed_state = np.random.choice(len(psi), p=probabilities)
    measured_psi = np.zeros_like(psi)
    measured_psi[collapsed_state] = 1  # Collapses to measured state
    return measured_psi, collapsed_state

measured_psi, outcome = measure(psi_initial)
print(f"Measurement outcome: |{outcome}>")
print(f"Collapsed state: {measured_psi}")

# Postulates of Quantum Mechanics:
# 1. States are vectors in Hilbert Space
# 2. Observables are Hermitian operators
# 3. Measurement collapses states
# 4. Evolution follows Schrödinger's equation
print("Postulates of Quantum Mechanics:")
postulates = [
    "1. Quantum states are vectors in Hilbert space.",
    "2. Physical observables correspond to Hermitian operators.",
    "3. Measurement collapses a quantum state into an eigenstate.",
    "4. Quantum evolution follows Schrödinger's equation."
]
for postulate in postulates:
    print(postulate)
