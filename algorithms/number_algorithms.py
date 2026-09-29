"""
algorithms/number_algorithms.py

MODULE 2: Number & Factoring Algorithms
Covers CSE1021 Unit 4 concepts: square root, smallest divisor, GCD,
prime generation, prime factorization, pseudo-random numbers,
raising a number to a large power, and the nth Fibonacci number.
"""


def square_root_newton(n, tolerance=1e-6):
    """
    Approximate the square root of n using Newton-Raphson iteration.

    Approach:
    Start with a guess, then repeatedly refine it using:
        next_guess = (guess + n / guess) / 2
    Stop when the guess barely changes between iterations (within
    'tolerance'). This converges very quickly (quadratically).

    Time complexity: roughly O(log(1 / tolerance)) iterations
    Space complexity: O(1)

    Returns a tuple: (approx_square_root, iterations_used)
    """
    if n < 0:
        raise ValueError("Cannot compute a real square root of a negative number")
    if n == 0:
        return 0.0, 0

    guess = n / 2 if n > 1 else 1.0
    iterations = 0

    while True:
        next_guess = (guess + n / guess) / 2
        iterations += 1
        if abs(next_guess - guess) < tolerance:
            guess = next_guess
            break
        guess = next_guess

    return guess, iterations


def smallest_divisor(n):
    """
    Find the smallest divisor of n that is greater than 1, using
    trial division starting at 2.

    Approach:
    Try dividing n by 2, 3, 4, ... up to sqrt(n). If none of these
    divide n evenly, n itself must be prime, so n is its own smallest
    divisor greater than 1.

    Time complexity: O(sqrt(n)) worst case
    Space complexity: O(1)
    """
    if n < 2:
        return None

    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return divisor
        divisor += 1
    return n  # n has no divisor below sqrt(n), so it is prime


def gcd_euclidean(a, b):
    """
    Compute the Greatest Common Divisor using the Euclidean algorithm
    (implemented manually rather than calling math.gcd).

    Approach:
    Repeatedly replace (a, b) with (b, a mod b) until b becomes 0.
    At that point, a holds the GCD.

    Time complexity: O(log(min(a, b)))
    Space complexity: O(1)
    """
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def generate_primes(limit):
    """
    Generate all prime numbers up to and including 'limit' using the
    Sieve of Eratosthenes.

    Approach:
    Assume every number from 2 to limit is prime, then cross out
    (mark False) every multiple of each prime found, starting from
    that prime squared.

    Time complexity: O(n log log n)
    Space complexity: O(n), for the boolean sieve array
    """
    if limit < 2:
        return []

    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    i = 2
    while i * i <= limit:
        if is_prime[i]:
            multiple = i * i
            while multiple <= limit:
                is_prime[multiple] = False
                multiple += i
        i += 1

    return [num for num, prime in enumerate(is_prime) if prime]


def prime_factors(n):
    """
    Compute the prime factorization of n using trial division.

    Approach:
    Try dividing n by 2, then 3, 4, 5, ... Each time a divisor evenly
    divides n, record it and divide it out (possibly more than once).
    Stop trial division once divisor*divisor > n; whatever remains
    (if > 1) is itself a prime factor.

    Time complexity: O(sqrt(n))
    Space complexity: O(log n), for the list of factors
    """
    factors = []
    working = n
    divisor = 2

    while divisor * divisor <= working:
        while working % divisor == 0:
            factors.append(divisor)
            working //= divisor
        divisor += 1

    if working > 1:
        factors.append(working)

    return factors


def pseudo_random_lcg(seed, count=5):
    """
    Generate pseudo-random numbers using a Linear Congruential
    Generator (LCG), a simple algorithm often used to introduce the
    idea of pseudo-random number generation.

    Formula:
        next_value = (a * current_value + c) mod m

    Time complexity: O(count)
    Space complexity: O(count), for the returned list
    """
    a, c, m = 1103515245, 12345, 2 ** 31
    numbers = []
    current = seed

    for _ in range(count):
        current = (a * current + c) % m
        numbers.append(current)

    return numbers


def power_fast(base, exponent):
    """
    Raise 'base' to 'exponent' using fast exponentiation
    (binary exponentiation / repeated squaring), which is far more
    efficient than multiplying 'base' by itself 'exponent' times.

    Approach:
    While the exponent is greater than 0:
      - if the exponent is odd, multiply the result by the current base
      - square the current base
      - halve the exponent (integer division)

    Time complexity: O(log(exponent))
    Space complexity: O(1)
    """
    if exponent < 0:
        raise ValueError("This implementation only supports non-negative exponents")

    result = 1
    current_base = base
    remaining_exponent = exponent

    while remaining_exponent > 0:
        if remaining_exponent % 2 == 1:
            result *= current_base
        current_base *= current_base
        remaining_exponent //= 2

    return result


def nth_fibonacci_iterative(n):
    """
    Compute the nth Fibonacci number (0-indexed: fib(0)=0, fib(1)=1)
    iteratively, keeping only the last two values in memory.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    if n <= 0:
        return 0

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current
