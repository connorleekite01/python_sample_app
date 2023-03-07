from unittest import TestCase
from SampleTriangleUtils.TriangleUtils import TriangleUtils

class TestTriangleUtils(TestCase):
    # test case for equilateral triangle
    def test_equilateral(self):
        # create an instance of the calculator library
        calc = TriangleUtils()

        # test the equilateral triangle
        self.assertEqual(calc.checkTriangleType(2, 2, 2), "equilateral")
        self.assertEqual(calc.checkTriangleType(10, 10, 10), "equilateral")
        self.assertEqual(calc.checkTriangleType(2, 2, 2), "equilateral")
        self.assertEqual(calc.checkTriangleType(10, 10, 10), "equilateral")

    # test case for isosceles triangle
    def test_isosceles(self):
        # create an instance of the calculator library
        calc = TriangleUtils()

        # test the isosceles triangle
        self.assertEqual(calc.checkTriangleType(2, 2, 3), "isosceles")
        self.assertEqual(calc.checkTriangleType(10, 10, 5), "isosceles")
        self.assertEqual(calc.checkTriangleType(2, 2, 3), "isosceles")
        self.assertEqual(calc.checkTriangleType(10, 10, 5), "isosceles")

    # test case for scalene triangle
    def test_scalene(self):
        # create an instance of the calculator library
        calc = TriangleUtils()

        # test the scalene triangle
        self.assertEqual(calc.checkTriangleType(2, 3, 4), "scalene")
        self.assertEqual(calc.checkTriangleType(10, 5, 3), "scalene")
        self.assertEqual(calc.checkTriangleType(2, 3, 4), "scalene")
        self.assertEqual(calc.checkTriangleType(10, 5, 3), "scalene")

