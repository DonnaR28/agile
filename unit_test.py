import unittest

def sum_numbers(a, b):
    return a + b

class SumTest(unittest.TestCase):
    def test_sum_positive_numbers(self):
        result = sum_numbers(5, 10)
        self.assertEqual(result, 15)

    def test_sum_negative_numbers(self):
        result = sum_numbers(-8, -3)
        self.assertEqual(result, -11)

    def test_sum_zero_and_positive_number(self):
        result = sum_numbers(0, 7)
        self.assertEqual(result, 7)

    def test_sum_zero_and_negative_number(self):
        result = sum_numbers(0, -5)
        self.assertEqual(result, -5)

    def test_sum_zero_and_zero(self):
        result = sum_numbers(0, 0)
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()
