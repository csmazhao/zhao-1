# -*- coding: utf-8 -*-

import unittest
from mathfunc import *


class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""


    @classmethod
    def setUpClass(cls):
        print("3333333333333333333.")

    @classmethod
    def tearDownClass(cls):
        print ("444444444444444444444444.")
    def test_add(self):
        """Test method add(a, b)"""
        self.assertEqual(3, add(1, 2))

    def test_minus(self):
        """Test method minus(a, b)"""
        self.assertEqual(1, minus(3, 2))

    def test_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(6, multi(2, 3))


    def test_divide(self):
        """Test method divide(a, b)"""
        self.assertEqual(3, divide(6, 2))
        self.assertEqual(2.6, divide(5, 2))

if __name__ == '__main__':
    unittest.main()