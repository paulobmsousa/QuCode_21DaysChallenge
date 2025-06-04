# Introduction to Classical Computing & Boolean Algebra

# Bits: The fundamental unit of classical computing (0 or 1)
class Bit:
    def __init__(self, value):
        self.value = value  # 0 or 1

    def __str__(self):
        return str(self.value)

# Logic Gates: Fundamental Boolean operations
class LogicGate:
    @staticmethod
    def NOT(bit):
        """ NOT gate: Inverts the bit (0 → 1, 1 → 0) """
        return Bit(1 - bit.value)

    @staticmethod
    def AND(bit1, bit2):
        """ AND gate: Outputs 1 if both bits are 1, otherwise 0 """
        return Bit(bit1.value & bit2.value)

    @staticmethod
    def OR(bit1, bit2):
        """ OR gate: Outputs 1 if at least one bit is 1 """
        return Bit(bit1.value | bit2.value)

    @staticmethod
    def XOR(bit1, bit2):
        """ XOR gate: Outputs 1 if bits are different, 0 if they are the same """
        return Bit(bit1.value ^ bit2.value)

# Classical Circuits: Combining logic gates to build functions
class ClassicalCircuit:
    def __init__(self, bit1, bit2):
        self.bit1 = bit1
        self.bit2 = bit2

    def half_adder(self):
        """ Half-Adder Circuit: Computes sum and carry bit """
        sum_bit = LogicGate.XOR(self.bit1, self.bit2)
        carry_bit = LogicGate.AND(self.bit1, self.bit2)
        return sum_bit, carry_bit

# Demonstrating bits
bit_a = Bit(0)
bit_b = Bit(1)
print(f"Bit A: {bit_a}, Bit B: {bit_b}")

# Demonstrating basic logic gates
print(f"NOT A: {LogicGate.NOT(bit_a)}")
print(f"A AND B: {LogicGate.AND(bit_a, bit_b)}")
print(f"A OR B: {LogicGate.OR(bit_a, bit_b)}")
print(f"A XOR B: {LogicGate.XOR(bit_a, bit_b)}")

# Demonstrating a classical circuit (Half-Adder)
circuit = ClassicalCircuit(bit_a, bit_b)
sum_bit, carry_bit = circuit.half_adder()
print(f"Half-Adder Output -> Sum: {sum_bit}, Carry: {carry_bit}")
