"""
algorithms/conversions.py

Part of MODULE 1: Fundamental Algorithms (Unit 3)
Contains: base conversion and character-to-number (and back) conversion.
"""

DIGITS = "0123456789ABCDEF"  # supports bases up to 16


def decimal_to_base(n, base):
    """
    Convert a non-negative decimal integer to another base (2 to 16)
    using the repeated-division algorithm taught in the course:
    keep dividing by the base and collect the remainders, then reverse
    the collected digits.

    Time complexity: O(log_base(n))
    Space complexity: O(log_base(n)) for the digit list
    """
    if n < 0:
        raise ValueError("Only non-negative numbers are supported")
    if n == 0:
        return "0"

    digits = []
    working = n
    while working > 0:
        remainder = working % base
        digits.append(DIGITS[remainder])
        working = working // base

    digits.reverse()
    return "".join(digits)


def base_to_decimal(num_str, base):
    """
    Convert a string representing a number in the given base into decimal,
    using Horner's rule:
        result = result * base + value_of_next_digit
    processed from left to right.

    Time complexity: O(k), k = number of digits in num_str
    Space complexity: O(1)
    """
    result = 0
    for ch in num_str.upper():
        if ch not in DIGITS[:base]:
            raise ValueError(f"'{ch}' is not a valid digit for base {base}")
        value = DIGITS.index(ch)
        result = result * base + value
    return result


def char_to_number(ch):
    """
    Convert a single character to its ASCII/Unicode code point.
    Time complexity: O(1)
    """
    if len(ch) != 1:
        raise ValueError("Please provide exactly one character")
    return ord(ch)


def number_to_char(code):
    """
    Convert a numeric code point back to its character.
    Time complexity: O(1)
    """
    return chr(code)
