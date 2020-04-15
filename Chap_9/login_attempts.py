#!/usr/bin/env python3.7

# JulianV
# Apr 8, 2020.
# Exercise 9-5
# Login Attempts
# Based on exercise 9-3

class User:
    # Representing a user profile info.
    def __init__(self, user_name,first_name, 
                  last_name, email):
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        # Formatting a description user
        print("\nuser's info:")
        print(f"\t{self.user_name}")
        print(f"\t{self.first_name.title()} {self.last_name.title()}")
        print(f"\t{self.email}")

    def increment_login_attempts(self):
        # user login attemps
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        # Reseting login attempts
        self.login_attempts = 0
    def display_login_attempts(self):
        print(f"Login Attempts: {self.login_attempts}")

user = User('julianv', 'julian', 'vargas', 'julianv@example.com')
user.describe_user()
user.display_login_attempts()

# Incrementing login attempts
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Displaying login attemps
print(f"\nLogin attempts {str(user.login_attempts)}")

# Resetting login attemps and displaying resetting
user.reset_login_attempts()
print(f"Reseting login attempts: {str(user.login_attempts)}")