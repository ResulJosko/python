class Calculator:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def add(self):
        return self.value1 + self.value1
    def multiply(self):    
        return self.value1 * self.value2

calc = Calculator(10, 20)

print(f"Add method: {calc.add()}")
print(f"Multiply method: {calc.multiply()}")