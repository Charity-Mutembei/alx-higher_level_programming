#!/usr/bin/python3
"""Unittests for max_integer function"""

import unittest
import sys
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)
        self.assertEqual(max_integer([1, 3, 2, 5, 4]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_integer([-5, -4, -3, -2, -1]), -1)
        self.assertEqual(max_integer([-1, -3, -2, -5, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-5, 10, -3, 20, -1]), 20)
        self.assertEqual(max_integer([-5, -10, -3, -20, -1]), -1)
        self.assertEqual(max_integer([5, 10, 3, 20, 1]), 20)
        self.assertEqual(max_integer([-5, 10, 3, 20, 1]), 20)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([1, 1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([2, 2, 2, 2, 2]), 2)
        self.assertEqual(max_integer([3, 3, 3, 3, 3]), 3)


if __name__ == '__main__':
    unittest.main()
