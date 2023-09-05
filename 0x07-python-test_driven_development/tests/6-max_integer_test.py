#!/usr/bin/python3

import unittest
from max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for the TestMaxInteger"""

    def test_max_integer(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertAlmostEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertAlmostEqual(max_integer([1]), 1)

    def test_empty_list(self):
        self.assertAlmostEqual(max_integer([]), None)

    def test_no_args(self):
        self.assertAlmostEqual(max_integer(), None)

    def test_type_errors(self):
        with self.assertRaises(TypeError):
            max_integer(23)
            max_integer("Hello")
            max_integer(None)

    def test_duplicate_max_values(self):
        self.assertEqual(max_integer([1, 2, 2, 1]), 2)

    def test_single_negative_number(self):
        self.assertEqual(max_integer([-5]), -5)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-5, 5]), 5)

    def test_floats(self):
        self.assertEqual(max_integer([-1.5, 2.3, 3.4, 2.5]), 3.4)

    def test_non_numeric_values(self):
        with self.assertRaises(TypeError):
            max_integer(['a', 'b', 'c'])

    def test_zero(self):
        self.assertEqual(max_integer([0, -1, -2, -3]), 0)

    def test_with_boolean(self):
        self.assertEqual(max_integer([True, False, 0, 1]), 1)


if __name__ == '__main__':
    unittest.main()
