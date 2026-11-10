import unittest

from calculator import add, divide


class CalculatorTests(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-2, 3), 1)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            divide(1, 0)


if __name__ == "__main__":
    unittest.main()
