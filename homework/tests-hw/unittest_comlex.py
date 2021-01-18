#!/bin/python

import unittest
from homework.tests_complex import *


'''
To successfully Run this test module within 
systemwide Python3 environment from the root of 
the whole project you need to use following 
single-line command in terminal:
python -m homework.tests-hw.unittest_complex
'''


class TestCase(unittest.TestCase):

    def setUp(self):
        self.testClass = Test()

    def tearDown(self):
        pass

    def test_function_enter(self):
        self.assertIs(self.testClass.__enter__(), self.testClass)

    @mock.patch('testClass.__exit__', return_value=True)
    def test_function_exit(self):
        self.assertEqual(self.testClass.__exit__(0, 9, 8), True)

    def test_function_hello(self):
        self.assertEqual(self.testClass.hello(), 1)

    @mock.patch('testClass.hello', return_value=33)
    def test_function_hello_mock(self):
        self.assertEqual(self.testClass.hello(), 33)

    def test_new_test(self):
        self.assertIsInstance(new_test(), Test)

    def test_func(self):
        self.assertEqual(func(), self.testClass.hello())


if __name__ == '__main__':
    unittest.main()
