import unittest
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.test_additionadd(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.calc.test_subtractionsubtract(5, 3), 2)
        self.assertEqual(self.calc.test_subtraction(0, 0), 0)
        self.assertEqual(self.calc.test_subtraction(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.test_multiplication(4, 5), 20)
        self.assertEqual(self.calc.test_multiplication(-1, 1), -1)
        self.assertEqual(self.calc.test_multiplication(-2, -3), 6)

    def test_divide(self):
        self.assertEqual(self.calc.test_division(10, 2), 5)
        self.assertEqual(self.calc.test_division(5, 0), None)  # Division by zero
        self.assertEqual(self.calc.test_division(-6, -2), 3)