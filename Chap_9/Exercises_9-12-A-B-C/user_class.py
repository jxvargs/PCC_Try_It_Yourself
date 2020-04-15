#!/usr/bin/env python3.7

# JulianV
# Apr 14, 2020.
# Exercise 9-12-A-B-C
# Multiple modules

class User():
    def __init__(self, user_name, first_name, 
            last_name, email):
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def describe_user(self):
        # formatting user output.
        print("\nUser information:")
        print(f"\tUser: {self.user_name}")
        print(f"\tFirst Name: {self.first_name}")
        print(f"\tLast name: {self.last_name}")
        print(f"\tEmail: {self.email}")
    