#!/bin/python

import unittest
from homework.test_simple_calc import *


class TestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 6), 11)
        self.assertEqual(add(8, -17), -9)
        self.assertEqual(add(2.3, 4.5), 6.8)

    def test_substract(self):
        self.assertEqual(subtract(12, 3), 9)
        self.assertEqual(subtract(-22, 60), -82)
        self.assertEqual(subtract(75.98, 13.176), 62.804)

    def test_multiply(self):
        self.assertEqual(multiply(7, 6), 42)
        self.assertEqual(multiply(3, -15), -45)
        self.assertEqual(multiply(3.2, 5.1), 16.32)

    def test_devide(self):
        self.assertEqual(divide(100, 2), 50.0)
        self.assertEqual(divide(-6, 3), -2.0)
        self.assertEqual(divide(12, 8), 1.5)
        self.assertRaises(ValueError, lambda: divide(2, 0))


if __name__ == '__main__':
    unittest.main()
