
# Classical vs Quantum Mechanics Demonstration

# Classical Mechanics: A classical object's state is definite.
# Example: A coin flip lands in either HEADS or TAILS, but not both at once.

class ClassicalCoin:
    def __init__(self):
        self.state = "Heads"  # Assume initial state is Heads
    
    def flip(self):
        # Classical probability: Either Heads or Tails (Never both)
        import random
        self.state = "Heads" if random.random() < 0.5 else "Tails"
    
    def observe(self):
        return f"Classical Coin is in definite state: {self.state}"

coin = ClassicalCoin()
coin.flip()
print(coin.observe())

# Quantum Superposition: A quantum object exists in multiple states at once until observed.
# Example: A quantum coin that is BOTH Heads & Tails (superposition state).

class QuantumCoin:
    def __init__(self):
        self.state = ["Heads", "Tails"]  # Both states exist simultaneously
    
    def observe(self):
        # Observation collapses superposition into a definite state
        import random
        measured_state = random.choice(self.state)
        return f"Quantum Coin collapsed into definite state: {measured_state}"

qcoin = QuantumCoin()
print("Before observation: Quantum Coin is in superposition (Heads & Tails)")
print(qcoin.observe())  # Collapses to a classical state upon measurement

# Wave-Particle Duality Demonstration
# Example: Light behaves as both a wave (diffraction/interference) and particle (discrete photons)

class Light:
    def __init__(self):
        self.behaviors = ["Wave-like behavior", "Particle-like behavior"]
    
    def experiment(self, setup):
        # Depending on the experiment setup, light behaves differently
        if setup == "Double Slit":
            return "Light shows INTERFERENCE PATTERN (Wave-like behavior)"
        elif setup == "Photoelectric Effect":
            return "Light ejects electrons (Particle-like behavior)"
        else:
            return "Unknown experiment setup"

light = Light()
print(light.experiment("Double Slit"))  # Demonstrates wave behavior
print(light.experiment("Photoelectric Effect"))  # Demonstrates particle behavior
