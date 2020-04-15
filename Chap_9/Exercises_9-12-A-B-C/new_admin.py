#!/usr/bin/env python3.7

# JulianV
# Apr 14, 2020.
# Exercise 9-12

from user_class import User
from admin_privilege_class import Admin


my_user = User('josev', 'jose', 'vargas', 'josev@example.com')
my_user.describe_user()

my_new_admin = Admin('jxvar6s', 'julian', 'vargas', 'jjulianv@example.com')
my_new_admin.describe_user()
my_new_admin.privileges.show_privileges()
