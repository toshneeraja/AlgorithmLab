"""
This is the Main program for AlgorithmLab.
Handles the menus and connects user input with the algorithm modules.
"""

from algorithms import fundamental
from algorithms import conversions
from algorithms import number_algorithms
from algorithms import array_algorithms
from analysis import complexity
from utils import input_validation
from utils import display


def menu_fundamental():
    options = [
        "Exchange values",
        "Counting elements in a list",
        "Summation of first n numbers",
        "Factorial (iterative)",
        "Fibonacci sequence",
        "Reverse a number",
        "Base conversion",
        "Character <-> Number conversion",
    ]

    while True:
        display.print_header("MODULE 1: FUNDAMENTAL ALGORITHMS")
        display.print_menu(options)

        choice = input_validation.get_menu_choice(
            "Enter your choice: ",
            [str(i) for i in range(1, len(options) + 2)],)

        if choice == "1":
            a = input_validation.get_integer("Enter first value: ")
            b = input_validation.get_integer("Enter second value: ")

            new_a, new_b = fundamental.exchange_values(a, b)

            display.print_result("Swapped values", f"a={new_a}, b={new_b}")
            display.print_explanation(
                complexity.get_complexity_info("exchange_values"))

        elif choice == "2":
            numbers = input_validation.get_integer_list(
                "Enter numbers separated by spaces: ")

            print("Condition options: even, odd, positive, negative")
            condition = input("Enter condition: ").strip().lower()
            result = fundamental.counting(numbers, condition)
            display.print_result(f"Count of {condition} numbers", result)

        elif choice == "3":
            n = input_validation.get_non_negative_integer("Enter n: ")
            result = fundamental.summation(n)
            display.print_result("Sum of first n numbers", result)

        elif choice == "4":
            n = input_validation.get_non_negative_integer("Enter n: ")

            result = fundamental.factorial(n)

            display.print_result("Factorial", result)

        elif choice == "5":
            n = input_validation.get_positive_integer( "How many Fibonacci terms? " )
            result = fundamental.fibonacci_sequence(n)
            display.print_result("Fibonacci sequence", result)

        elif choice == "6":
            n = input_validation.get_integer(
                "Enter a number to reverse: ")

            result = fundamental.reverse_number(n)

            display.print_result("Reversed number", result)
            display.print_explanation(
                complexity.get_complexity_info("reverse_number"))

        elif choice == "7":
            base_conversion_menu()

        elif choice == "8":
            char_num_menu()

        elif choice == str(len(options) + 1):
            break


def base_conversion_menu():

    display.print_header("BASE CONVERSION")

    print("1. Decimal to another base")
    print("2. Another base to Decimal")

    sub_choice = input_validation.get_menu_choice(
        "Enter your choice: ",
        ["1", "2"],)

    try:
        if sub_choice == "1":
            n = input_validation.get_non_negative_integer(
                "Enter decimal number: ")

            base = input_validation.get_integer(
                "Enter target base (2-16): ")

            if base < 2 or base > 16:
                print("Base must be between 2 and 16.")
                return

            result = conversions.decimal_to_base(n, base)

            display.print_result(f"{n} in base {base}", result)

        else:
            num_str = input( "Enter the number (as text): ").strip()

            base = input_validation.get_integer("Enter its base (2-16): " )

            if base < 2 or base > 16:
                print("Base must be between 2 and 16.")
                return

            result = conversions.base_to_decimal(num_str, base)

            display.print_result(
                f"{num_str} (base {base}) in decimal",
                result,
            )

        display.print_explanation(complexity.get_complexity_info("decimal_to_base"))

    except ValueError as error:
        print(f"Invalid input: {error}")


def char_num_menu():
    display.print_header("CHARACTER <-> NUMBER CONVERSION")

    print("1. Character to number")
    print("2. Number to character")

    sub_choice = input_validation.get_menu_choice(
        "Enter your choice: ", ["1", "2"],)

    if sub_choice == "1":
        ch = input("Enter a single character: ").strip()

        try:
            result = conversions.char_to_number(ch)
            display.print_result("ASCII/Unicode value", result)

        except ValueError as error:
            print(f"Invalid input: {error}")

    else:
        code = input_validation.get_non_negative_integer(
            "Enter a numeric code (0-1114111): " )

        try:
            result = conversions.number_to_char(code)
            display.print_result("Character", result)

        except ValueError:
            print("Invalid code point. Please enter a valid Unicode code point.")

    display.print_explanation(
        complexity.get_complexity_info("char_to_number")
    )


def menu_number():
    options = [
        "Square root (Newton's method)",
        "Smallest divisor",
        "GCD of two numbers",
        "Generate prime numbers up to n",
        "Prime factorization",
        "Generate pseudo-random numbers",
        "Raise a number to a large power",
        "nth Fibonacci number",]

    while True:
        display.print_header("MODULE 2: NUMBER & FACTORING ALGORITHMS")
        display.print_menu(options)

        choice = input_validation.get_menu_choice(
            "Enter your choice: ",
            [str(i) for i in range(1, len(options) + 2)],)

        if choice == "1":
            n = input_validation.get_non_negative_integer("Enter a non-negative number: ")

            try:
                value, iterations = number_algorithms.square_root_newton(n)

                display.print_result(
                    "Square root (approx.)",
                    round(value, 6),)

                print(f"(Converged in {iterations} iterations)")

            except ValueError as error:
                print(f"Invalid input: {error}")

            display.print_explanation(
                complexity.get_complexity_info("square_root_newton")
            )

        elif choice == "2":
            n = input_validation.get_positive_integer("Enter n (2 or greater recommended): ")

            result = number_algorithms.smallest_divisor(n)

            display.print_result("Smallest divisor", result)
            display.print_explanation(
                complexity.get_complexity_info("smallest_divisor"))

        elif choice == "3":
            a = input_validation.get_integer("Enter first number: ")
            b = input_validation.get_integer("Enter second number: ")

            result = number_algorithms.gcd_euclidean(a, b)

            display.print_result("GCD", result)

        elif choice == "4":
            limit = input_validation.get_positive_integer("Enter upper limit: ")

            result = number_algorithms.generate_primes(limit)

            display.print_result("Primes", result)
            display.print_explanation(
                complexity.get_complexity_info("generate_primes"))

        elif choice == "5":
            n = input_validation.get_positive_integer( "Enter a number: ")

            result = number_algorithms.prime_factors(n)

            display.print_result("Prime factors", result)

        elif choice == "6":
            seed = input_validation.get_non_negative_integer("Enter a seed value: ")

            count = input_validation.get_positive_integer("How many numbers to generate? " )

            result = number_algorithms.pseudo_random_lcg(seed,count,)

            display.print_result("Pseudo-random numbers", result)
            display.print_explanation(
                complexity.get_complexity_info("pseudo_random_lcg"))

        elif choice == "7":
            base = input_validation.get_integer("Enter base: ")

            exponent = input_validation.get_non_negative_integer("Enter exponent (0 or greater): ")

            try:
                result = number_algorithms.power_fast(
                    base,
                    exponent,)

                display.print_result(
                    f"{base}^{exponent}",
                    result, )

            except ValueError as error:
                print(f"Invalid input: {error}")

            display.print_explanation(
                complexity.get_complexity_info("power_fast"))

        elif choice == "8":
            n = input_validation.get_non_negative_integer(
                "Enter n: "  )

            result = number_algorithms.nth_fibonacci_iterative(n)

            display.print_result(
                f"{n}th Fibonacci number",
                result,)

            display.print_explanation(
                complexity.get_complexity_info(
                    "nth_fibonacci_iterative"))

        elif choice == str(len(options) + 1):
            break


def menu_array():
    options = [
        "Reverse an array",
        "Count occurrences of a value",
        "Find maximum element",
        "Remove duplicates from a sorted array",
        "Partition an array around a pivot",
        "Find the kth smallest element",
        "Demonstrate lists, tuples, sets, dictionaries",
    ]

    while True:
        display.print_header("MODULE 3: ARRAY/LIST TECHNIQUES")
        display.print_menu(options)

        choice = input_validation.get_menu_choice(
            "Enter your choice: ",
            [str(i) for i in range(1, len(options) + 2)],)

        if choice == "1":
            arr = input_validation.get_integer_list("Enter array elements: " )

            result = array_algorithms.reverse_array(arr)

            display.print_result("Reversed array", result)
            display.print_explanation(
                complexity.get_complexity_info("reverse_array") )

        elif choice == "2":
            arr = input_validation.get_integer_list("Enter array elements: ")

            target = input_validation.get_integer( "Enter value to count: ")

            result = array_algorithms.count_elements(
                arr,
                target,)

            display.print_result("Occurrences", result)
            display.print_explanation(
                complexity.get_complexity_info("count_elements"))

        elif choice == "3":
            arr = input_validation.get_integer_list(
                "Enter array elements: ")

            try:
                result = array_algorithms.find_maximum(arr)

                display.print_result(
                    "Maximum element",
                    result,)

            except ValueError as error:
                print(f"Invalid input: {error}")

            display.print_explanation(
                complexity.get_complexity_info("find_maximum") )

        elif choice == "4":
            print("Note: this algorithm assumes the array is already sorted.")

            arr = input_validation.get_integer_list("Enter sorted array elements: ")

            result = array_algorithms.remove_duplicates_sorted(arr)

            display.print_result("Array without duplicates",result,)

            display.print_explanation(complexity.get_complexity_info("remove_duplicates_sorted"))

        elif choice == "5":
            arr = input_validation.get_integer_list("Enter array elements: ")

            pivot_index = input_validation.get_non_negative_integer(f"Enter pivot index (0 to {len(arr) - 1}): ")

            if pivot_index >= len(arr):
                print("Pivot index out of range.")

            else:
                partitioned, final_pos = array_algorithms.partition_array(arr,pivot_index,)
                display.print_result("Partitioned array",partitioned,)
                print(f"(Pivot ended up at index {final_pos})")

            display.print_explanation(complexity.get_complexity_info("partition_array") )

        elif choice == "6":
            arr = input_validation.get_integer_list(
                "Enter array elements: ")

            k = input_validation.get_positive_integer(
                "Enter k: ")

            try:
                result = array_algorithms.kth_smallest(arr,k,)

                display.print_result(f"{k}th smallest element", result,)

            except ValueError as error:
                print(f"Invalid input: {error}")

            display.print_explanation(
                complexity.get_complexity_info("kth_smallest")
            )

        elif choice == "7":
            result = array_algorithms.demo_data_structures()

            print("\nList  :", result["list"])
            print("Tuple :", result["tuple"])
            print("Set   :", result["set"])
            print("Dict  :", result["dict"])

            print("\nTime tradeoff demo (membership test on 100000 items):")
            print(
                f"  List search time : "
                f"{result['list_search_time']:.8f} seconds")

            print(
                f"  Set  search time : "
                f"{result['set_search_time']:.8f} seconds")

            print( " Sets generally give faster average-case membership")
            print( " tests than lists because they use hashing.")

        elif choice == str(len(options) + 1):
            break


def menu_analysis():
    all_algorithms = complexity.list_all_algorithms()

    display.print_header("MODULE 4: ALGORITHM ANALYSIS")

    for index, name in enumerate(all_algorithms, start=1):
        print(f"{index}. {name}")

    print(f"{len(all_algorithms) + 1}. Back")

    choice = input_validation.get_menu_choice(
        "Select an algorithm to see its analysis: ",
        [str(i) for i in range(1, len(all_algorithms) + 2)],)

    if choice == str(len(all_algorithms) + 1):
        return

    selected_name = all_algorithms[int(choice) - 1]

    info = complexity.get_complexity_info(selected_name)

    display.print_header(f"ANALYSIS: {selected_name}")
    display.print_explanation(info)


def menu_examples():

    display.print_header("EXAMPLES")

    try:
        with open("sample_inputs/examples.txt", "r") as file:
            content = file.read()

        print(content)

    except FileNotFoundError:
        print(
            "Example file not found. Make sure "
            "sample_inputs/examples.txt exists "
            "and that you are running main.py "
            "from the project's root folder." )


def main():

    while True:
        display.print_title()

        print()
        print("1. Fundamental Algorithms")
        print("2. Number & Factoring Algorithms")
        print("3. Array/List Techniques")
        print("4. Algorithm Analysis")
        print("5. Examples")
        print("6. Exit")
        print()

        choice = input_validation.get_menu_choice(
            "Enter your choice: ",
            ["1", "2", "3", "4", "5", "6"],)

        if choice == "1":
            menu_fundamental()

        elif choice == "2":
            menu_number()

        elif choice == "3":
            menu_array()

        elif choice == "4":
            menu_analysis()

        elif choice == "5":
            menu_examples()

        elif choice == "6":
            print("Thank you for using AlgorithmLab. Goodbye!")
            break


if __name__ == "__main__":
    try:
        main()

    except (EOFError, KeyboardInterrupt):
        # Exit safely if the user interrupts the program.
        print(
            "\n\nInput interrupted. "
            "Exiting AlgorithmLab. Goodbye!")
