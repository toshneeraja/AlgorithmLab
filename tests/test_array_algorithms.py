"""
tests/test_array_algorithms.py

Unit tests for algorithms/array_algorithms.py
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from algorithms import array_algorithms


class TestArrayAlgorithms(unittest.TestCase):

    def test_reverse_array_normal(self):
        self.assertEqual(array_algorithms.reverse_array([1, 2, 3]), [3, 2, 1])

    def test_reverse_array_empty(self):
        self.assertEqual(array_algorithms.reverse_array([]), [])

    def test_reverse_array_does_not_mutate_original(self):
        original = [1, 2, 3]
        array_algorithms.reverse_array(original)
        self.assertEqual(original, [1, 2, 3])

    def test_count_elements_found(self):
        self.assertEqual(array_algorithms.count_elements([1, 2, 2, 3, 2], 2), 3)

    def test_count_elements_not_found(self):
        self.assertEqual(array_algorithms.count_elements([1, 2, 3], 9), 0)

    def test_find_maximum_normal(self):
        self.assertEqual(array_algorithms.find_maximum([3, 7, 1, 9, 2]), 9)

    def test_find_maximum_single_element(self):
        self.assertEqual(array_algorithms.find_maximum([42]), 42)

    def test_find_maximum_empty_raises(self):
        with self.assertRaises(ValueError):
            array_algorithms.find_maximum([])

    def test_remove_duplicates_sorted_normal(self):
        self.assertEqual(
            array_algorithms.remove_duplicates_sorted([1, 1, 2, 2, 3]), [1, 2, 3]
        )

    def test_remove_duplicates_sorted_empty(self):
        self.assertEqual(array_algorithms.remove_duplicates_sorted([]), [])

    def test_remove_duplicates_sorted_no_duplicates(self):
        self.assertEqual(
            array_algorithms.remove_duplicates_sorted([1, 2, 3]), [1, 2, 3]
        )

    def test_partition_array(self):
        arr = [8, 3, 5, 2, 9]
        partitioned, pivot_pos = array_algorithms.partition_array(arr, 2)  # pivot value = 5
        for i in range(pivot_pos):
            self.assertLess(partitioned[i], 5)
        for i in range(pivot_pos + 1, len(partitioned)):
            self.assertGreaterEqual(partitioned[i], 5)

    def test_kth_smallest_various_k(self):
        arr = [7, 2, 9, 1, 5]
        self.assertEqual(array_algorithms.kth_smallest(arr, 1), 1)
        self.assertEqual(array_algorithms.kth_smallest(arr, 3), 5)
        self.assertEqual(array_algorithms.kth_smallest(arr, 5), 9)

    def test_kth_smallest_invalid_k_too_low_raises(self):
        with self.assertRaises(ValueError):
            array_algorithms.kth_smallest([1, 2, 3], 0)

    def test_kth_smallest_invalid_k_too_high_raises(self):
        with self.assertRaises(ValueError):
            array_algorithms.kth_smallest([1, 2, 3], 4)

    def test_demo_data_structures_keys(self):
        result = array_algorithms.demo_data_structures()
        expected_keys = {
            "list", "tuple", "set", "dict",
            "list_search_time", "set_search_time",
        }
        self.assertEqual(set(result.keys()), expected_keys)

    def test_demo_data_structures_set_removes_duplicates(self):
        result = array_algorithms.demo_data_structures()
        # sample_set was built from {5, 5, 6, 7, 8} -> duplicates removed
        self.assertEqual(result["set"], {5, 6, 7, 8})


if __name__ == "__main__":
    unittest.main()
