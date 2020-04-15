#!/usr/bin/env python3.7

# JulianV
# Apr 14, 2020.
# Exercise 9-11-A
# Storing Admmin classes 
# and import them from a different
# file.

class User():
    def __init__(self, user_name, first_name, 
            last_name, email):
        # Initializing User Attributes.
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
    
class Admin(User):
    #Initializing Admin Attributes
    def __init__(self, user_name, first_name,
            last_name, email):
        super().__init__(user_name, first_name, 
            last_name, email)
        self.admin = True
        # This Attribute connects to Privilege Class.
        self.privileges = Privileges()

class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = ['can add post', 'can delete post',
                        'can band user', 'can edit post',
                ]

    def show_privileges(self):
        # Display Admin privileges.
        print("Admin Privileges:")
        for privilege in self.privileges:
            print(f"\t-{privilege}")
