"""
algorithms/array_algorithms.py

MODULE 3: Array/List Techniques
Covers CSE1021 Unit 5 concepts: array reversal, counting, finding the
maximum, removing duplicates from an ordered array, partitioning,
finding the kth smallest element, and demonstrating lists, tuples,
sets and dictionaries (including a simple time-tradeoff example).
"""

import time


def reverse_array(arr):
    """
    Reverse the order of elements in an array using the two-pointer
    swap technique (one pointer at the start, one at the end, moving
    towards the middle).

    Time complexity: O(n)
    Space complexity: O(1) extra (a copy is returned so the caller's
    original list is not silently mutated)
    """
    result = arr.copy()
    left = 0
    right = len(result) - 1
    while left < right:
        result[left], result[right] = result[right], result[left]
        left += 1
        right -= 1
    return result


def count_elements(arr, target):
    """
    Count how many times 'target' appears in arr, using a linear scan.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    count = 0
    for item in arr:
        if item == target:
            count += 1
    return count


def find_maximum(arr):
    """
    Find the maximum element in the array with a single linear scan,
    keeping track of the best value found so far.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    if not arr:
        raise ValueError("Cannot find the maximum of an empty array")

    maximum = arr[0]
    for item in arr[1:]:
        if item > maximum:
            maximum = item
    return maximum


def remove_duplicates_sorted(arr):
    """
    Remove duplicates from an ORDERED (already sorted) array.

    Approach:
    Because the array is sorted, any duplicate of a value must sit
    right next to it. So we only need to compare each element to the
    last element already kept in the result, instead of comparing
    against every previous element (which an unsorted approach would
    require).

    Time complexity: O(n)
    Space complexity: O(n), for the result list
    """
    if not arr:
        return []

    result = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != result[-1]:
            result.append(arr[i])
    return result


def partition_array(arr, pivot_index):
    """
    Partition an array around a pivot value using the Lomuto
    partition scheme (the classic approach that underlies quicksort
    and quickselect/kth-smallest algorithms).

    After partitioning:
      - all elements before the pivot's final position are < pivot
      - all elements after the pivot's final position are >= pivot

    Time complexity: O(n)
    Space complexity: O(1) extra (a copy is made first so the
    original array passed in is not mutated)

    Returns a tuple: (partitioned_array, final_index_of_pivot)
    """
    working = arr.copy()
    pivot_value = working[pivot_index]

    # move pivot to the end temporarily
    working[pivot_index], working[-1] = working[-1], working[pivot_index]

    store_index = 0
    for i in range(len(working) - 1):
        if working[i] < pivot_value:
            working[i], working[store_index] = working[store_index], working[i]
            store_index += 1

    # move pivot to its final sorted position
    working[store_index], working[-1] = working[-1], working[store_index]

    return working, store_index


def kth_smallest(arr, k):
    """
    Find the kth smallest element (1-indexed, so k=1 means the
    smallest element) using a straightforward sort-based approach.

    This is the simplest correct method and is presented first, as
    is common in an introductory course, before more advanced
    selection algorithms (like quickselect) are introduced.

    Time complexity: O(n log n), dominated by the sort
    Space complexity: O(n), for the sorted copy
    """
    if k < 1 or k > len(arr):
        raise ValueError("k is out of the valid range for this array")

    sorted_arr = sorted(arr)
    return sorted_arr[k - 1]


def demo_data_structures():
    """
    Demonstrate the four core Python data structures covered in
    Unit 5 (lists, tuples, sets, dictionaries), and show a simple
    time-tradeoff example: checking membership in a list vs a set.

    A list must be scanned element by element (O(n) average), while
    a set uses hashing and can check membership much faster on
    average (O(1) average case). This is the "time tradeoff" concept
    from the syllabus: sets use more setup/memory overhead in
    exchange for faster lookups.
    """
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    sample_tuple = (10, 20, 30)          # tuples are immutable
    sample_set = {5, 5, 6, 7, 8}         # duplicate 5 is automatically removed
    sample_dict = {"apple": 1, "banana": 2, "cherry": 3}

    # time tradeoff demonstration: list search vs set search
    big_list = list(range(100000))
    big_set = set(big_list)
    target = 99999  # a worst-case value for a list (near the end)

    start = time.perf_counter()
    _ = target in big_list
    list_search_time = time.perf_counter() - start

    start = time.perf_counter()
    _ = target in big_set
    set_search_time = time.perf_counter() - start

    return {
        "list": sample_list,
        "tuple": sample_tuple,
        "set": sample_set,
        "dict": sample_dict,
        "list_search_time": list_search_time,
        "set_search_time": set_search_time,
    }
