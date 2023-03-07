from unittest import TestCase
from SampleCalculatorUtils.calculatorUtils import CalculatorUtils
class TestCalculatorLibrary(TestCase):
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
