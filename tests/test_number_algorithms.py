"""
tests/test_number_algorithms.py

Unit tests for algorithms/number_algorithms.py
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from algorithms import number_algorithms


class TestNumberAlgorithms(unittest.TestCase):

    def test_square_root_newton_perfect_square(self):
        value, _ = number_algorithms.square_root_newton(16)
        self.assertAlmostEqual(value, 4.0, places=4)

    def test_square_root_newton_zero(self):
        value, iterations = number_algorithms.square_root_newton(0)
        self.assertEqual(value, 0.0)
        self.assertEqual(iterations, 0)

    def test_square_root_newton_negative_raises(self):
        with self.assertRaises(ValueError):
            number_algorithms.square_root_newton(-4)

    def test_smallest_divisor_prime_input(self):
        self.assertEqual(number_algorithms.smallest_divisor(13), 13)

    def test_smallest_divisor_composite_input(self):
        self.assertEqual(number_algorithms.smallest_divisor(15), 3)

    def test_smallest_divisor_below_two(self):
        self.assertIsNone(number_algorithms.smallest_divisor(1))

    def test_gcd_euclidean_normal(self):
        self.assertEqual(number_algorithms.gcd_euclidean(54, 24), 6)

    def test_gcd_euclidean_with_zero(self):
        self.assertEqual(number_algorithms.gcd_euclidean(0, 5), 5)

    def test_generate_primes_normal(self):
        self.assertEqual(number_algorithms.generate_primes(10), [2, 3, 5, 7])

    def test_generate_primes_below_two(self):
        self.assertEqual(number_algorithms.generate_primes(1), [])

    def test_prime_factors_composite(self):
        self.assertEqual(number_algorithms.prime_factors(60), [2, 2, 3, 5])

    def test_prime_factors_prime_number(self):
        self.assertEqual(number_algorithms.prime_factors(13), [13])

    def test_pseudo_random_lcg_length(self):
        result = number_algorithms.pseudo_random_lcg(42, 5)
        self.assertEqual(len(result), 5)

    def test_pseudo_random_lcg_deterministic(self):
        # same seed should always give the same sequence
        result_a = number_algorithms.pseudo_random_lcg(7, 3)
        result_b = number_algorithms.pseudo_random_lcg(7, 3)
        self.assertEqual(result_a, result_b)

    def test_power_fast_normal(self):
        self.assertEqual(number_algorithms.power_fast(2, 10), 1024)

    def test_power_fast_zero_exponent(self):
        self.assertEqual(number_algorithms.power_fast(5, 0), 1)

    def test_power_fast_negative_exponent_raises(self):
        with self.assertRaises(ValueError):
            number_algorithms.power_fast(2, -1)

    def test_nth_fibonacci_iterative_base_cases(self):
        self.assertEqual(number_algorithms.nth_fibonacci_iterative(0), 0)
        self.assertEqual(number_algorithms.nth_fibonacci_iterative(1), 1)

    def test_nth_fibonacci_iterative_normal(self):
        # Sequence (0-indexed): 0,1,1,2,3,5,8,13,21,34,55 -> fib(10) = 55
        self.assertEqual(number_algorithms.nth_fibonacci_iterative(10), 55)


if __name__ == "__main__":
    unittest.main()
