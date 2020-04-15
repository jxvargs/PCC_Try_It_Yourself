#!/usr/bin/env python3.7

# JulianV
# Apr 14, 2020.
# Exercise 9-12-A-B-C
from user_class import User

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