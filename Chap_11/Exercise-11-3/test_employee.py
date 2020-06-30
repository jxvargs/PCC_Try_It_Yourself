#!/usr/bin/env python3

# JulianV
# Jun 22, 2020.
# 11-3 Testing Employee class

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
# Testing for the class Employee
    def setUp(self):
        self.my_employee = Employee('Julian', 'Vargas', 41000)

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 46000)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(3000)
        self.assertEqual(self.my_employee.annual_salary, 44000)

unittest.main()