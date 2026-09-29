# AlgorithmLab - Fundamental Algorithm & Array Toolkit

**Course:** CSE1021 - Problem Solving / Python
**Student:** Neeraja Tosh
**Registration Number:** 26BCE10574
**GitHub:** toshneeraja

## 1. Project Overview

AlgorithmLab is a command-line Python application that implements
the fundamental algorithms and array/list techniques taught in
CSE1021, and lets you run each one interactively from a text menu.
Every algorithm is implemented from scratch (not by calling a
built-in shortcut), and every result is shown alongside a short
explanation of the algorithm's approach and its time/space
complexity.

## 2. Problem Statement

See [`statement.md`](statement.md) for the full problem statement,
scope, target users, and expected input/output. In short: first-year
students learn many small algorithms individually but rarely have
one place to run and compare them along with their efficiency -
AlgorithmLab is that one place.

## 3. Objectives

- Implement CSE1021's fundamental algorithms and array techniques by
  hand, iteratively, in plain Python.
- Provide a simple, crash-resistant, menu-driven CLI.
- Provide a basic algorithm-analysis reference (approach, time
  complexity, space complexity) for every implemented algorithm.
- Demonstrate Python's core data structures (lists, tuples, sets,
  dictionaries) including a simple time-tradeoff example.
- Keep the code understandable by a first-year student.

## 4. Features

- 4 functional modules (Fundamental Algorithms, Number & Factoring
  Algorithms, Array/List Techniques, Algorithm Analysis) plus an
  Examples viewer.
- 23 algorithms/utilities implemented from scratch across the three
  algorithm modules.
- Reusable input validation (handles empty input, invalid integers,
  invalid arrays, invalid menu choices, out-of-range k values,
  division by zero, and Ctrl+D/Ctrl+C).
- 64 automated unit tests covering normal, boundary, and invalid
  cases, using Python's standard `unittest` framework.
- Mermaid-based design documentation: architecture, component,
  workflow, use case, and sequence diagrams.

## 5. Course Concepts Demonstrated

| CSE1021 Unit | Concepts | Where |
|---|---|---|
| Unit 1 | Problem solving, algorithm analysis, efficiency | `docs/architecture.md`, `analysis/complexity.py` |
| Unit 2 | Variables, expressions, functions, modules, parameters, tuple assignment | Every module (plain functions, `a, b = b, a`) |
| Unit 3 | Exchange, counting, summation, factorial, Fibonacci, reverse, base conversion, char-to-number, loops/conditionals | `algorithms/fundamental.py`, `algorithms/conversions.py` |
| Unit 4 | Square root, smallest divisor, GCD, primes, prime factors, pseudo-random numbers, large power, nth Fibonacci | `algorithms/number_algorithms.py` |
| Unit 5 | Array reversal, counting, max, dedup, partition, kth smallest, lists/tuples/sets/dicts, time tradeoff | `algorithms/array_algorithms.py` |

## 6. Functional Modules

1. **Fundamental Algorithms** (Module 1)
2. **Number & Factoring Algorithms** (Module 2)
3. **Array/List Techniques** (Module 3)
4. **Algorithm Analysis** (Module 4)
5. **Examples** (sample inputs/outputs viewer)

## 7. Technologies / Tools Used

- **Language:** Python 3 (standard library only)
- **Testing:** Python's built-in `unittest` module
- **No external dependencies.** No Flask/Django, no database, no
  Pandas/NumPy, no Tkinter, no web/cloud/API usage, and no machine
  learning of any kind.

## 8. Project Structure

```
AlgorithmLab/
├── README.md
├── statement.md
├── PROJECT_REPORT_CONTENT.md
├── requirements.txt
├── main.py
├── algorithms/
│   ├── __init__.py
│   ├── fundamental.py         # Module 1: exchange, counting, summation,
│   │                          #   factorial, fibonacci, reverse
│   ├── conversions.py         # Module 1: base conversion, char<->number
│   ├── number_algorithms.py   # Module 2: sqrt, gcd, primes, power, etc.
│   └── array_algorithms.py    # Module 3: array/list techniques
├── analysis/
│   ├── __init__.py
│   └── complexity.py          # Module 4: complexity/approach lookup
├── utils/
│   ├── __init__.py
│   ├── input_validation.py    # Reusable input validation helpers
│   └── display.py             # Menu/result/explanation printing
├── tests/
│   ├── __init__.py
│   ├── test_fundamental.py
│   ├── test_conversions.py
│   ├── test_number_algorithms.py
│   └── test_array_algorithms.py
├── docs/
│   ├── architecture.md        # Architecture, NFRs, design decisions
│   ├── workflow.md             # Workflow, use case & sequence diagrams
│   └── diagrams/
│       └── README.md
└── sample_inputs/
    └── examples.txt
```

## 9. Installation / Setup

AlgorithmLab uses **only the Python standard library** - there is
nothing to install with `pip`.

Requirements:
- Python 3.8 or newer

Steps:

```bash
# 1. Clone the repository
git clone https://github.com/toshneeraja/AlgorithmLab.git

# 2. Move into the project folder
cd AlgorithmLab

# 3. (Optional) confirm your Python version
python3 --version
```

## 10. How to Run

From the project's root folder (the folder containing `main.py`),
run:

```bash
python3 main.py
```

You will see the main menu:

```
==================================================
                   ALGORITHMLAB
          Fundamental Algorithm Toolkit
==================================================

1. Fundamental Algorithms
2. Number & Factoring Algorithms
3. Array/List Techniques
4. Algorithm Analysis
5. Examples
6. Exit

Enter your choice:
```

Type a number and press Enter to navigate. Every submenu has a
"Back" option that returns you to the previous menu.

## 11. How to Run Tests

From the project's root folder, run:

```bash
python3 -m unittest discover
```

Expected output (64 tests, all passing):

```
................................................................
----------------------------------------------------------------------
Ran 64 tests in 0.02s

OK
```

You can also run a single test file directly, for example:

```bash
python3 -m unittest tests.test_number_algorithms
```

## 12. Example Usage

```
Enter your choice: 1

--------------------------------------------------
         MODULE 1: FUNDAMENTAL ALGORITHMS
--------------------------------------------------
1. Exchange values
2. Counting elements in a list
3. Summation of first n numbers
4. Factorial (iterative)
5. Fibonacci sequence
6. Reverse a number
7. Base conversion
8. Character <-> Number conversion
9. Back
Enter your choice: 4
Enter n: 5

Result -> Factorial: 120

Explanation:
  Approach          : Iteratively multiplies numbers from 2 up to n into a running result.
  Time complexity   : O(n)
  Space complexity  : O(1)
```

## 13. Input/Output Examples

**Valid input:**
```
Enter n: 5
Result -> Factorial: 120
```

**Invalid input (handled gracefully):**
```
Enter a positive integer: abc
Invalid input. Please enter a valid positive integer.
Enter a positive integer: 7
```

**Array input:**
```
Enter array elements: 7 2 9 1 5
Enter k: 3
Result -> 3th smallest element: 5
```

More worked examples are available inside the app itself under
menu option **5. Examples**, or directly in
[`sample_inputs/examples.txt`](sample_inputs/examples.txt).

## 14. Complexity Analysis

A full table of every algorithm's time and space complexity is in
[`docs/architecture.md`](docs/architecture.md#8-complexity-analysis-summary),
and the same information is browsable live from inside the running
program via **Module 4: Algorithm Analysis**.

Quick highlights:

- **Fastest growth handled well:** `power_fast` uses binary
  exponentiation, computing `base^exponent` in O(log exponent)
  instead of O(exponent).
- **Classic O(n log log n):** `generate_primes` uses the Sieve of
  Eratosthenes rather than testing every number individually.
- **Deliberately simple tradeoff:** `kth_smallest` uses a sort-based
  approach (O(n log n)) rather than quickselect (O(n) average),
  because the simpler, easier-to-verify approach is more appropriate
  for a first course - this tradeoff is explained to the user in the
  app itself.

## 15. Limitations

- This project is a teaching/demonstration tool, not a
  production-grade library: input sizes are expected to be small
  (suitable for manual verification), not industrial-scale.
- The pseudo-random number generator (LCG) is for demonstration only
  and is **not** cryptographically secure.
- The square root function uses floating-point arithmetic and a
  fixed default tolerance, so extremely large or extremely precise
  results are not guaranteed.
- There is no persistent storage; results are not saved between
  runs.
- The CLI is single-user and single-session; there is no
  multi-user or concurrent access support (not needed for this
  course's scope).

## 16. Future Enhancements

- Add a quickselect-based kth-smallest as an alternative, faster
  option, alongside the current sort-based approach, and let the
  user compare both.
- Add an option to log/export a session's results to a plain text
  file for later review.
- Add more example algorithms (e.g. matrix operations) if the
  syllabus scope grows in a later course.
- Add a "compare complexities" view that plots (as text) how two
  algorithms scale for the same growing input size.

## 17. Author

**Neeraja Tosh**
Reg. No. 26BCE10574
VIT Bhopal, CSE1021 - Problem Solving / Python
GitHub: [toshneeraja](https://github.com/toshneeraja)
