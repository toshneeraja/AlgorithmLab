"""
utils/display.py
Handles UI rendering, including menus, headings, results, and algorithm explanations, ensuring a clean and consistent user experience.
"""

def print_title():
    print("=" * 50)
    print("ALGORITHMLAB".center(50))
    print("Fundamental Algorithm Toolkit".center(50))
    print("=" * 50)


def print_header(title):

    print("\n" + "-" * 50)
    print(title.center(50))
    print("-" * 50)


def print_menu(options):
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

    print(f"{len(options) + 1}. Back")


def print_result(label, value):
    print(f"\nResult -> {label}: {value}")

def print_explanation(info):
    print("\nExplanation:")
    print(f"  Approach          : {info.get('approach')}")
    print(f"  Time complexity   : {info.get('time_complexity')}")
    print(f"  Space complexity  : {info.get('space_complexity')}")