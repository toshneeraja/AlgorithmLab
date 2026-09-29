"""
tests/test_fundamental.py

Unit tests for algorithms/fundamental.py
Run all project tests with: python3 -m unittest discover
"""

import unittest
import sys
import os

# Make sure the project root is on the import path when tests are run
# directly (e.g. python3 tests/test_fundamental.py) as well as via
# 'python3 -m unittest discover'.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from algorithms import fundamental


class TestFundamental(unittest.TestCase):

    def test_exchange_values_normal(self):
        self.assertEqual(fundamental.exchange_values(1, 2), (2, 1))

    def test_exchange_values_negative(self):
        self.assertEqual(fundamental.exchange_values(-5, 5), (5, -5))

    def test_exchange_values_equal(self):
        self.assertEqual(fundamental.exchange_values(7, 7), (7, 7))

    def test_counting_even(self):
        self.assertEqual(fundamental.counting([1, 2, 3, 4, 5, 6], "even"), 3)

    def test_counting_odd(self):
        self.assertEqual(fundamental.counting([1, 2, 3, 4, 5], "odd"), 3)

    def test_counting_positive_and_negative(self):
        numbers = [-3, -2, 0, 1, 5]
        self.assertEqual(fundamental.counting(numbers, "positive"), 2)
        self.assertEqual(fundamental.counting(numbers, "negative"), 2)

    def test_counting_empty_list(self):
        self.assertEqual(fundamental.counting([], "even"), 0)

    def test_summation_normal(self):
        self.assertEqual(fundamental.summation(5), 15)

    def test_summation_zero(self):
        self.assertEqual(fundamental.summation(0), 0)

    def test_factorial_zero(self):
        self.assertEqual(fundamental.factorial(0), 1)

    def test_factorial_one(self):
        self.assertEqual(fundamental.factorial(1), 1)

    def test_factorial_normal(self):
        self.assertEqual(fundamental.factorial(5), 120)

    def test_fibonacci_sequence_single_term(self):
        self.assertEqual(fundamental.fibonacci_sequence(1), [0])

    def test_fibonacci_sequence_multiple_terms(self):
        self.assertEqual(fundamental.fibonacci_sequence(5), [0, 1, 1, 2, 3])

    def test_fibonacci_sequence_zero_terms(self):
        self.assertEqual(fundamental.fibonacci_sequence(0), [])

    def test_reverse_number_positive(self):
        self.assertEqual(fundamental.reverse_number(123), 321)

    def test_reverse_number_negative(self):
        self.assertEqual(fundamental.reverse_number(-120), -21)

    def test_reverse_number_zero(self):
        self.assertEqual(fundamental.reverse_number(0), 0)


if __name__ == "__main__":
    unittest.main()
