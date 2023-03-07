# create a sample triangle class that inherits from the calculator library
from SampleCalculatorUtils.calculatorUtils import CalculatorUtils


class TriangleUtils(CalculatorUtils):

    def __init__(self):
        self.calc = CalculatorUtils()

    def checkTriangleType(self, a, b, c):
        """
        This function will check triangle type, to check if the triangle is equilateral, isosceles or scalene,
        :param a:
        :param b:
        :param c:
        :return:
        """
        # check if the triangle is equilateral
        if self.doubleEquals(a, b) and self.doubleEquals(b, c):
            return "equilateral"
        # check if the triangle is isosceles
        elif self.calc.doubleEquals(a, b) or self.calc.doubleEquals(b, c) or self.calc.doubleEquals(a, c):
            return "isosceles"
        # check if the triangle is scalene
        else:
            return "scalene"
