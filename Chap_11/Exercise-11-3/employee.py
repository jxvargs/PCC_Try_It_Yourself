#!/usr/bin/env python3

# JulianV
# Jun 22, 2020.
# 11-3 Employee

class Employee():
    def __init__(self, f_name, l_name,  annual_salary):
        self.f_name = f_name
        self.l_name = l_name
        self.annual_salary = annual_salary

    def give_raise(self, salary_raise=5000):
        self.annual_salary += salary_raise

#my_employee = Employee('julian', 'vargas', 41000)
#my_employee.give_raise(3000)