"""
algorithms/fundamental.py

MODULE 1: Fundamental Algorithms
Covers CSE1021 Unit 3 concepts: exchange values, counting, summation,
factorial, Fibonacci sequence, and reversing a number.

(Base conversion and character<->number conversion live in conversions.py
because the project structure keeps them as a separate file, but they are
conceptually part of the same "fundamental algorithms" unit.)
"""


def exchange_values(a, b):
    """
    Swap two values.

    Approach:
    Python supports simultaneous (tuple) assignment: a, b = b, a
    This assigns the new values to a and b at the same time, so no
    temporary/third variable is needed.

    Time complexity: O(1)
    Space complexity: O(1)
    """
    a, b = b, a
    return a, b


def counting(numbers, condition="even"):
    """
    Count how many numbers in a list satisfy a given condition.

    condition can be: "even", "odd", "positive", "negative"

    Approach:
    Walk through the list once (linear scan) and increase a counter
    whenever the current number matches the condition.

    Time complexity: O(n), n = number of elements
    Space complexity: O(1)
    """
    count = 0
    for num in numbers:
        if condition == "even" and num % 2 == 0:
            count += 1
        elif condition == "odd" and num % 2 != 0:
            count += 1
        elif condition == "positive" and num > 0:
            count += 1
        elif condition == "negative" and num < 0:
            count += 1
    return count


def summation(n):
    """
    Compute the sum of the first n natural numbers (1 + 2 + ... + n)
    using iteration (not the closed-form formula), to demonstrate looping.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def factorial(n):
    """
    Compute n! iteratively (deliberately not using math.factorial or
    recursion, since the course expects the iterative approach here).

    Time complexity: O(n)
    Space complexity: O(1)
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci_sequence(n):
    """
    Generate the first n terms of the Fibonacci sequence iteratively.

    Approach:
    Start with the first two known terms [0, 1] and keep appending the
    sum of the last two terms until we have n terms.

    Time complexity: O(n)
    Space complexity: O(n), for storing the returned sequence
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]

    sequence = [0, 1]
    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence[:n]


def reverse_number(n):
    """
    Reverse the digits of an integer using arithmetic operations
    (modulo and integer division), not string slicing, to show the
    digit-extraction algorithm taught in the course.

    Approach:
    Repeatedly take the last digit of n using (n % 10), append it to
    the result, then remove that digit from n using integer division
    (n // 10).

    Time complexity: O(d), d = number of digits in n
    Space complexity: O(1)
    """
    is_negative = n < 0
    n = abs(n)

    reversed_num = 0
    while n > 0:
        last_digit = n % 10
        reversed_num = reversed_num * 10 + last_digit
        n = n // 10

    return -reversed_num if is_negative else reversed_num
