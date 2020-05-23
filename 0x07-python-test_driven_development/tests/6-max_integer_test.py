#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer
    function
    """
    def test_max_pos(self):
        """Test max integer in positive numbers"""
        test_list = [88]
        self.assertEqual(max_integer(test_list), max(test_list))
        test_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(test_list), max(test_list))
        test_list = [1, 2, 10, 3, 4]
        self.assertEqual(max_integer(test_list), max(test_list))
        test_list = [99, 2540, 9999, float("inf")]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_max_neg(self):
        """Test max integer in negative numbers"""
        test_list = [-1, -2, -3, -4]
        self.assertEqual(max_integer(test_list), max(test_list))
        test_list = [-99, -2540, -9999, float("-inf")]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_max_both(self):
        """Test max integer in positive and negative numbers"""
        test_list = [-1, 2, -3, 4]
        self.assertEqual(max_integer(test_list), max(test_list))
        test_list = [99, -2540, -9999, 5000]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_max_raise(self):
        """Test max integer for raising TypeErrors"""
        test_list = [1, 2, 3, "a"]
        self.assertRaises(TypeError, max_integer, test_list)

    def test_max_none(self):
        """Test max void parameters"""
        self.assertIsNone(max_integer(), msg=None)
