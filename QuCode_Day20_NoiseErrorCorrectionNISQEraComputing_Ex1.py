
# Import necessary Qiskit modules
from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.providers.aer.noise import NoiseModel, depolarizing_error
from qiskit.visualization import plot_histogram

# 1️⃣ Quantum Error Correction: 3-Qubit Bit Flip Code
def quantum_error_correction():
    """
    Implements a 3-qubit quantum error correction code.
    The circuit encodes a logical qubit into a redundant three-qubit state
    and attempts to correct errors if they occur.
    """
    qc = QuantumCircuit(3, 1)  # 3 qubits for redundancy, 1 classical bit for measurement

    # Encode |0⟩ state redundantly (|000⟩)
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(0, 2)

    # Introduce an artificial error (bit-flip on qubit 1)
    qc.x(1)

    # Error correction (Majority Voting)
    qc.cx(1, 0)
    qc.cx(2, 0)
    qc.measure(0, 0)

    return qc

# 2️⃣ Simulating Quantum Noise (Decoherence)
def simulate_quantum_noise(qc):
    """
    Simulates quantum noise (decoherence) using a depolarizing error model.
    The noise model is applied to the circuit before execution.
    """
    noise_model = NoiseModel()

    # Apply depolarizing error to all qubits
    error = depolarizing_error(0.2, 1)  # 20% probability of depolarization
    noise_model.add_all_qubit_quantum_error(error, ["cx", "h", "x"])

    # Simulate execution with noise
    simulator = Aer.get_backend("qasm_simulator")
    compiled_circuit = transpile(qc, simulator)
    result = execute(compiled_circuit, simulator, noise_model=noise_model, shots=1024).result()

    # Display results
    print("Quantum Error Correction & Noise Simulation Results:")
    print(result.get_counts())

    # Visualize results
    qc.draw('mpl')
    plot_histogram(result.get_counts())

# Execute Quantum Error Correction & Noise Simulation
qc_error_correction = quantum_error_correction()
simulate_quantum_noise(qc_error_correction)
