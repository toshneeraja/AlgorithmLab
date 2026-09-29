"""
tests/test_conversions.py

Unit tests for algorithms/conversions.py
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from algorithms import conversions


class TestConversions(unittest.TestCase):

    def test_decimal_to_base_binary(self):
        self.assertEqual(conversions.decimal_to_base(10, 2), "1010")

    def test_decimal_to_base_hex(self):
        self.assertEqual(conversions.decimal_to_base(255, 16), "FF")

    def test_decimal_to_base_zero(self):
        self.assertEqual(conversions.decimal_to_base(0, 2), "0")

    def test_decimal_to_base_negative_raises(self):
        with self.assertRaises(ValueError):
            conversions.decimal_to_base(-5, 2)

    def test_base_to_decimal_binary(self):
        self.assertEqual(conversions.base_to_decimal("1010", 2), 10)

    def test_base_to_decimal_hex(self):
        self.assertEqual(conversions.base_to_decimal("FF", 16), 255)

    def test_base_to_decimal_invalid_digit_raises(self):
        with self.assertRaises(ValueError):
            conversions.base_to_decimal("2", 2)  # '2' is not valid in base 2

    def test_char_to_number(self):
        self.assertEqual(conversions.char_to_number("A"), 65)

    def test_char_to_number_invalid_length_raises(self):
        with self.assertRaises(ValueError):
            conversions.char_to_number("AB")

    def test_number_to_char(self):
        self.assertEqual(conversions.number_to_char(65), "A")


if __name__ == "__main__":
    unittest.main()
