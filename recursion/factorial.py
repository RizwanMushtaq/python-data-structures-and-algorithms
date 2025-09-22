import unittest


class FactorialCode:

    @staticmethod
    def factorial_rec(n):
        if (n < 0):
            raise ValueError("Factorial is not defined for negative numbers")
        if n == 0 or n == 1:
            return 1
        return n * FactorialCode.factorial_rec(n - 1)


class TestFactorialCode(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(FactorialCode.factorial_rec(5), 120)
        self.assertEqual(FactorialCode.factorial_rec(0), 1)
        self.assertEqual(FactorialCode.factorial_rec(1), 1)
        self.assertEqual(FactorialCode.factorial_rec(3), 6)
        with self.assertRaises(ValueError):
            FactorialCode.factorial_rec(-1)
        with self.assertRaises(RecursionError):
            FactorialCode.factorial_rec(1000)


if __name__ == "__main__":
    unittest.main()
