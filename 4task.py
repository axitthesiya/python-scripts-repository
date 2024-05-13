class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: Division by zero"

    def power(self):
        return self.num1 ** self.num2

    def remainder(self):
        return self.num1 % self.num2

    def bitwise_left_shift(self):
        return self.num1 << self.num2

    def bitwise_right_shift(self):
        return self.num1 >> self.num2

    def bitwise_and(self):
        return self.num1 & self.num2

    def bitwise_or(self):
        return self.num1 | self.num2

    def bitwise_xor(self):
        return self.num1 ^ self.num2

    def bitwise_not(self):
        return ~self.num1

    def less_than(self):
        return self.num1 < self.num2

    def less_than_or_equal_to(self):
        return self.num1 <= self.num2

    def equal_to(self):
        return self.num1 == self.num2

    def not_equal_to(self):
        return self.num1 != self.num2

    def greater_than(self):
        return self.num1 > self.num2

    def greater_than_or_equal_to(self):
        return self.num1 >= self.num2


calc = Calculator(10, 3)
print("Addition:", calc.addition())
print("Subtraction:", calc.subtraction())
print("Multiplication:", calc.multiplication())
print("Division:", calc.division())
print("Power:", calc.power())
print("Remainder:", calc.remainder())
print("Bitwise Left Shift:", calc.bitwise_left_shift())
print("Bitwise Right Shift:", calc.bitwise_right_shift())
print("Bitwise AND:", calc.bitwise_and())
print("Bitwise OR:", calc.bitwise_or())
print("Bitwise XOR:", calc.bitwise_xor())
print("Bitwise NOT of num1:", calc.bitwise_not())
print("Less than:", calc.less_than())
print("Less than or equal to:", calc.less_than_or_equal_to())
print("Equal to:", calc.equal_to())
print("Not equal to:", calc.not_equal_to())
print("Greater than:", calc.greater_than())
print("Greater than or equal to:", calc.greater_than_or_equal_to())

