from unittest import TestCase
from calculatorLibrary import CalculatorLibrary
class TestCalculatorLibrary(TestCase):
    # test case for add method
    def test_add(self):
        # create an instance of the calculator library
        calc = CalculatorLibrary()

        # test the add method
        self.assertEqual(calc.add(2, 3), 5)
