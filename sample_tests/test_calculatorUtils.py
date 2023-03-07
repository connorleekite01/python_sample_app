from unittest import TestCase
from SampleCalculatorUtils.calculatorUtils import CalculatorUtils
class TestCalculatorUtils(TestCase):
    # test case for add method
    def test_add(self):
        # create an instance of the calculator library
        calc = CalculatorUtils()

       # test the add method with various inputs
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(10, 5), 15)

    # test case for subtract method
    def test_subtract(self):
        # create an instance of the calculator library
        calc = CalculatorUtils()

       # test the subtract method with various inputs
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(5, 10), -5)
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(5, 10), -5)

    # test case for multiply method
    def test_multiply(self):
        # create an instance of the calculator library
        calc = CalculatorUtils()

       # test the multiply method with various inputs
        self.assertEqual(calc.multiply(2, 3), 6)
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(2, 3), 6)
        self.assertEqual(calc.multiply(10, 5), 50)

    # test case for divide method
    def test_divide(self):
        # create an instance of the calculator library
        calc = CalculatorUtils()

       # test the divide method with various inputs
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(10, 2), 5)
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(10, 2), 5)

    # test case for square method
    def test_square(self):
        # create an instance of the calculator library
        calc = CalculatorUtils()

       # test the square method with various inputs
        self.assertEqual(calc.square(2), 4)
        self.assertEqual(calc.square(5), 25)
        self.assertEqual(calc.square(2), 4)
        self.assertEqual(calc.square(5), 25)

    # test case for squareRoot method
    def test_squareRoot(self):
        # create an instance of the calculator library
        calc = CalculatorUtils()

       # test the squareRoot method with various inputs
        self.assertEqual(calc.squareRoot(4), 2)
        self.assertEqual(calc.squareRoot(25), 5)
        self.assertEqual(calc.squareRoot(4), 2)
        self.assertEqual(calc.squareRoot(25), 5)


    # test case for power method
    def test_power(self):
        # create an instance of the calculator library
        calc = CalculatorUtils()

       # test the power method with various inputs
        self.assertEqual(calc.power(2, 3), 8)
        self.assertEqual(calc.power(5, 3), 125)
        self.assertEqual(calc.power(2, 3), 8)
        self.assertEqual(calc.power(5, 3), 125)

    # test case for doubleEquals method
    def test_doubleEquals(self):
        # create an instance of the calculator library
        calc = CalculatorUtils()

       # test the doubleEquals method with various inputs
        self.assertEqual(calc.doubleEquals(10, 10), True)
        self.assertEqual(calc.doubleEquals(10, 5), False)
        self.assertEqual(calc.doubleEquals(10, 10), True)
        self.assertEqual(calc.doubleEquals(10, 5), False)