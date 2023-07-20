import math

class Operations:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return num1 / num2

    def power(self, base, exponent):
        return base ** exponent

    def square_root(self, num):
        return math.sqrt(num)

    def logarithm(self, num, base):
        return math.log(num, base)

    def factorial(self, num):
        return math.factorial(num)
