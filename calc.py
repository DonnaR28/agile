import unittest

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(3, 4)
        self.assertEqual(result, 7)

    def test_subtract(self):
        result = self.calculator.subtract(7, 3)
        self.assertEqual(result, 4)

    def test_multiply(self):
        result = self.calculator.multiply(2, 5)
        self.assertEqual(result, 10)

    def test_divide(self):
        result = self.calculator.divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide1(self):
        result = self.calculator.divide(2,0)
        self.assertEqual(result, 0)
if __name__ == '__main__':
    unittest.main()
