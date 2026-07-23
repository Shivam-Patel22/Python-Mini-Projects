class Calculator:
    def __init__(self, a, op, b):
        self.a = a
        self.op = op
        self.b = b

    def calculate(self):
        if self.op == '+':
            print("ADDITION =", self.a + self.b)
        elif self.op == '-':
            print("SUBTRACTION =", self.a - self.b)
        elif self.op == '*':
            print("MULTIPLICATION =", self.a * self.b)
        elif self.op == '/':
            print("DIVISION =", self.a / self.b)
        elif self.op == '%':
            print("MODULUS =", self.a % self.b)
        else:
            print("Invalid Choice, Try Again")

a = float(input("Enter First Number = "))
op = input("Select the Operator {+,-,*,/,%} = ")
b = float(input("Enter Second Number = "))

c = Calculator(a, op, b)
c.calculate()
