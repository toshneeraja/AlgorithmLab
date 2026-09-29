"""
analysis/complexity.py

MODULE 4: Algorithm Analysis
Stores a short, human-readable explanation of the approach, time
complexity, and space complexity for every algorithm implemented in
this project. This directly demonstrates Unit 1 concepts: efficiency
of algorithms and analysis of algorithms.
"""

COMPLEXITY_INFO = {
    "exchange_values": {
        "approach": "Uses Python's tuple assignment (a, b = b, a) to swap "
                    "two values without needing a temporary variable.",
        "time_complexity": "O(1)",
        "space_complexity": "O(1)",
    },
    "counting": {
        "approach": "Scans the list once and increments a counter whenever "
                    "an element satisfies the chosen condition.",
        "time_complexity": "O(n)",
        "space_complexity": "O(1)",
    },
    "summation": {
        "approach": "Iterates from 1 to n, adding each value to a running "
                    "total (rather than using the closed-form formula).",
        "time_complexity": "O(n)",
        "space_complexity": "O(1)",
    },
    "factorial": {
        "approach": "Iteratively multiplies numbers from 2 up to n into a "
                    "running result.",
        "time_complexity": "O(n)",
        "space_complexity": "O(1)",
    },
    "fibonacci_sequence": {
        "approach": "Builds the sequence iteratively; each new term is the "
                    "sum of the previous two terms already generated.",
        "time_complexity": "O(n)",
        "space_complexity": "O(n) for storing the sequence",
    },
    "reverse_number": {
        "approach": "Repeatedly extracts the last digit using n % 10, "
                    "appends it to the result, and shrinks n using n // 10.",
        "time_complexity": "O(d), d = number of digits",
        "space_complexity": "O(1)",
    },
    "decimal_to_base": {
        "approach": "Repeatedly divides the number by the target base, "
                    "collects remainders as digits, then reverses them.",
        "time_complexity": "O(log_base n)",
        "space_complexity": "O(log_base n)",
    },
    "base_to_decimal": {
        "approach": "Horner's rule: result = result * base + next_digit, "
                    "processed left to right through the digit string.",
        "time_complexity": "O(k), k = number of digits in the input",
        "space_complexity": "O(1)",
    },
    "char_to_number": {
        "approach": "Uses the character's underlying code point directly "
                    "(built-in ord), a constant-time lookup.",
        "time_complexity": "O(1)",
        "space_complexity": "O(1)",
    },
    "square_root_newton": {
        "approach": "Newton-Raphson iterative refinement: "
                    "guess = (guess + n/guess) / 2, repeated until the "
                    "guess stabilizes within a tolerance.",
        "time_complexity": "Roughly O(log(1/tolerance)) iterations "
                           "(converges quadratically)",
        "space_complexity": "O(1)",
    },
    "smallest_divisor": {
        "approach": "Trial division: tries 2, 3, 4, ... up to sqrt(n).",
        "time_complexity": "O(sqrt(n))",
        "space_complexity": "O(1)",
    },
    "gcd_euclidean": {
        "approach": "Euclidean algorithm: repeatedly replaces (a, b) with "
                    "(b, a mod b) until b becomes 0.",
        "time_complexity": "O(log(min(a, b)))",
        "space_complexity": "O(1)",
    },
    "generate_primes": {
        "approach": "Sieve of Eratosthenes: marks multiples of every prime "
                    "found as not prime, starting from that prime squared.",
        "time_complexity": "O(n log log n)",
        "space_complexity": "O(n), for the boolean sieve array",
    },
    "prime_factors": {
        "approach": "Trial division: repeatedly divides out the smallest "
                    "possible factor, increasing the divisor as needed.",
        "time_complexity": "O(sqrt(n))",
        "space_complexity": "O(log n), for the list of factors",
    },
    "pseudo_random_lcg": {
        "approach": "Linear Congruential Generator: "
                    "next_value = (a * current + c) mod m.",
        "time_complexity": "O(count)",
        "space_complexity": "O(count)",
    },
    "power_fast": {
        "approach": "Binary exponentiation (repeated squaring): the "
                    "exponent is halved each step while the base is "
                    "squared, multiplying into the result on odd steps.",
        "time_complexity": "O(log(exponent))",
        "space_complexity": "O(1)",
    },
    "nth_fibonacci_iterative": {
        "approach": "Iterative bottom-up computation, keeping only the "
                    "last two Fibonacci values at any time.",
        "time_complexity": "O(n)",
        "space_complexity": "O(1)",
    },
    "reverse_array": {
        "approach": "Two-pointer swap: elements from both ends are "
                    "swapped, moving the pointers towards the center.",
        "time_complexity": "O(n)",
        "space_complexity": "O(1) extra",
    },
    "count_elements": {
        "approach": "Linear scan comparing each element to the target "
                    "value.",
        "time_complexity": "O(n)",
        "space_complexity": "O(1)",
    },
    "find_maximum": {
        "approach": "Single linear scan, tracking the best (largest) "
                    "value seen so far.",
        "time_complexity": "O(n)",
        "space_complexity": "O(1)",
    },
    "remove_duplicates_sorted": {
        "approach": "Because the array is ordered, each element only "
                    "needs to be compared to the last kept element, not "
                    "to every previous element.",
        "time_complexity": "O(n)",
        "space_complexity": "O(n), for the result list",
    },
    "partition_array": {
        "approach": "Lomuto partition scheme: picks a pivot, then moves "
                    "smaller elements to its left in a single pass.",
        "time_complexity": "O(n)",
        "space_complexity": "O(1) extra (aside from the safety copy)",
    },
    "kth_smallest": {
        "approach": "Sorts the array and directly indexes the kth "
                    "position - the straightforward approach taught "
                    "before more advanced selection algorithms.",
        "time_complexity": "O(n log n)",
        "space_complexity": "O(n), for the sorted copy",
    },
}


def get_complexity_info(name):
    """
    Return the complexity info dictionary for a given algorithm name.
    If the name is not found, return a safe default message instead
    of raising an error (keeps the menu from crashing).
    """
    default_info = {
        "approach": "No analysis available for this algorithm.",
        "time_complexity": "N/A",
        "space_complexity": "N/A",
    }
    return COMPLEXITY_INFO.get(name, default_info)


def list_all_algorithms():
    """
    Return the list of all algorithm names that have analysis
    information available, in insertion order.
    """
    return list(COMPLEXITY_INFO.keys())
