"""
utils/input_validation.py
This module provides basic validation utilities to safeguard the application against invalid user inputs. These checks ensure the system gracefully handles common edge cases, such as empty fields or incorrect data types, preventing unexpected runtime errors.
"""

def get_integer(prompt):
    while True:
        user_input = input(prompt).strip()

        if user_input == "":
            print("Input cannot be empty. Please try again.")
            continue

        try:
            return int(user_input)

        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_positive_integer(prompt):

    while True:
        value = get_integer(prompt)

        if value <= 0:
            print("Please enter a positive integer.")
            continue

        return value


def get_non_negative_integer(prompt):

    while True:
        value = get_integer(prompt)

        if value < 0:
            print("Please enter 0 or a positive integer.")
            continue

        return value


def get_integer_list(prompt):
    while True:
        raw = input(prompt).strip()

        if raw == "":
            print("Input cannot be empty. Please try again.")
            continue
        tokens = raw.replace(",", " ").split()

        try:
            numbers = [int(token) for token in tokens]

        except ValueError:
            print(
                "Invalid input. Please enter numbers separated "
                "by spaces or commas." )
            continue

        if len(numbers) == 0:
            print("Please enter at least one number.")
            continue

        return numbers


def get_menu_choice(prompt, valid_choices):

    while True:
        choice = input(prompt).strip()

        if choice in valid_choices:
            return choice

        print("Invalid choice. Please select a valid menu option.")


def safe_divide(numerator, denominator):
    try:
        return numerator / denominator

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
