#!/usr/bin/env python3.7

# JulianV
# Apr 8, 2020.
# Exercise 9-7
# Displaying admin privileges
# to a class method.

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
    
class Admin(User):
    #Initializing Admin Attributes
    def __init__(self, user_name, first_name,
            last_name, email):
        super().__init__(user_name, first_name, 
            last_name, email)
        self.admin = True
        self.privileges = ['can add post', 'can delete post',
                        'can band user', 'can edit post',
        ]

    def show_privileges(self):
        # Display Admin privileges.
        print("Admin Privileges:")
        print(f"\t-Admin: {self.admin}")
        for privilege in self.privileges:
            print(f"\t-{privilege}")




my_user = User('josev', 'jose', 'vargas', 'josev@example.com')
my_user.describe_user()

new_user = Admin('julianv', 'julian', 'vargas', 'julianv@example.com')
new_user.describe_user()
new_user.show_privileges()