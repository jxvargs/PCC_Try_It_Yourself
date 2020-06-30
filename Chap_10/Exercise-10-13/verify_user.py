#!/usr/bin/env python3

# JulianV
# Jun 8, 2020.
# 10-13 
# verify user

import json

def get_store_username():
# Get stored username if available.
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    # Prompting for a new user
    username = input("What is your  name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
# Greet user by name."
    username = get_store_username()
    if username:
        correct_answer = input(f"Hi, are you {username} (y/n) ")
        if correct_answer == 'y':
            print(f"Welcome back, {username.title()}.")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username.title()}.")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username.title()}.")

greet_user()