#!/usr/bin/env python3.7

# JulianV
# Apr 2, 2020.
# Exercise 9-3
# Creat a class call user
# to store profile attributes.

class User:
    # Representing a user profile info.
    def __init__(self, user_name,first_name, 
                  last_name, email):
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def describe_user(self):
        # Formatting a description user
        print("\nuser's info:")
        print(f"\t{self.user_name}")
        print(f"\t{self.first_name.title()} {self.last_name.title()}")
        print(f"\t{self.email}")

flag = True

while flag:
    user_name = input("\nEnter a username: ")
    f_name = input("Enter your first name: ")
    l_name = input("Enter your last name: ")
    email = input("Enter your email: ")

    user = User(user_name, f_name, l_name, email)
    user.describe_user()
    
    answer = input("\nOne more user (yes/Yes/Y/y)?: ")
    if answer == 'Yes' or answer == 'yes' or answer == 'y' \
                 or answer == 'Y':
        flag = True
    else:
        flag = False
        print("\nThaks for your participation...\n")