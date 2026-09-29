# Problem Statement - AlgorithmLab

**Project Title:** AlgorithmLab - Fundamental Algorithm & Array Toolkit
**Course:** CSE1021 - Problem Solving / Python
**Student:** Neeraja Tosh (Reg. No. 26BCE10574)

## Problem Statement

First-year students studying problem solving and Python typically
learn many small, foundational algorithms one at a time (swapping
values, computing a factorial, finding a GCD, reversing an array,
and so on), but rarely get a single place to run, compare, and
reflect on all of them together, along with their efficiency.
AlgorithmLab addresses this by building one command-line toolkit
that implements these algorithms from scratch and lets the user run
them interactively while also seeing a short complexity/approach
explanation for each one.

## Project Scope

- Implement, by hand, the fundamental algorithms and array
  techniques covered in CSE1021 Units 3, 4 and 5.
- Provide a menu-driven command-line interface (no GUI, no web, no
  database).
- Provide a basic algorithm-analysis reference for each algorithm
  (Unit 1 concepts: efficiency and analysis of algorithms).
- Validate user input so the program does not crash on ordinary
  mistakes.
- Provide automated tests (via Python's `unittest`) for the core
  algorithm functions.

Out of scope: GUI interfaces, web frameworks, databases, machine
learning, and anything requiring third-party/external packages.

## Target Users

- First-year Computer Science students learning Python and basic
  algorithms (the primary audience).
- Course evaluators who want to quickly verify that a syllabus-based
  algorithm project genuinely implements the required concepts.

## High-Level Features

- A main menu with 6 top-level options.
- Three algorithm submenus (Fundamental, Number & Factoring,
  Array/List Techniques), each with its own list of algorithms.
- An Algorithm Analysis module to browse complexity explanations
  directly, without running the algorithm.
- An Examples module showing sample inputs and expected outputs.
- Input validation throughout, so invalid input (empty strings,
  non-numeric text, out-of-range values) is handled gracefully.

## Expected Input

- Integers (positive, non-negative, or general, depending on the
  algorithm) typed at a terminal prompt.
- Space/comma separated lists of integers for array-based
  algorithms.
- Single characters for character-to-number conversion.
- Menu choices (numbers) to navigate between screens.

## Expected Output

- The computed result of the selected algorithm, clearly labeled.
- A short explanation of the algorithm's approach, time complexity,
  and space complexity, printed directly after the result.
- Clear, non-crashing error messages when the input is invalid.

## Major Functional Modules

1. **Fundamental Algorithms** - exchange values, counting,
   summation, factorial, Fibonacci sequence, reverse a number, base
   conversion, character-to-number conversion.
2. **Number & Factoring Algorithms** - square root, smallest
   divisor, GCD, prime generation, prime factorization, pseudo-random
   number generation, large power calculation, nth Fibonacci number.
3. **Array/List Techniques** - array reversal, counting, finding the
   maximum, removing duplicates from a sorted array, partitioning,
   finding the kth smallest element, and demonstrating lists,
   tuples, sets, and dictionaries.
4. **Algorithm Analysis** - a browsable reference of approach/time/
   space complexity for every algorithm implemented above.
