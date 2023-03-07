# the following class is a python library that contains the functions for the calculator
class CalculatorUtils:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def square(self, a):
        return a * a

    def squareRoot(self, a):
        return a ** 0.5

    def cube(self, a):
        return a * a * a

    def cubeRoot(self, a):
        return a ** (1/3)

    def power(self, a, b):
        return a ** b

    # check if the two doubles are equal
    def doubleEquals(self, a, b):
        return abs(a - b) < 0.0