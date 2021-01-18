#!/bin/python

import unittest
from unittest.mock import patch
from homework.tests_simple_employee import Employee

'''
To successfully Run this test module within 
systemwide Python3 environment from the root of 
the whole project you need to use following 
single-line command in terminal:
python -m homework.tests-hw.unittest_simple_employee
'''


class TestCase(unittest.TestCase):
    def setUp(self):
        self.testdata = Employee('Dmytro', 'Filippov', 1200)

    def test_email(self):
        self.assertEqual(self.testdata.email, 'Dmytro.Filippov@email.com')

    def test_fullname(self):
        self.assertEqual(self.testdata.fullname, 'Dmytro Filippov')

    def test_apply_raise(self):
        self.testdata.apply_raise()
        self.assertEqual(self.testdata.pay, 1260)

    def test_monthly_schedule(self):
        with patch('homework.tests_simple_employee.requests.get') as requests:
            requests.return_value.ok = True
            requests.return_value.text = 'some output'
            self.assertEqual(self.testdata.monthly_schedule(
                'January'), 'some output')

        with patch('homework.tests_simple_employee.requests.get') as requests:
            requests.return_value.ok = False
            self.assertEqual(self.testdata.monthly_schedule(
                'January'), 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
