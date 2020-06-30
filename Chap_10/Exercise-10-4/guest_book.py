#!/usr/bin/env python3

# JulianV
# May 21, 2020.
# 10-4 Guest book print a greeting
# and write it in a file.

filename = 'guest_book.txt'
active = True
# open the file as file object and write the message
# while it is active.
with open(filename, 'w') as file_object:
    while active: 
        name = input("Hello, enter your name: ")
        greeting = 'Welcome to Python world'
        print(f"{greeting} {name}.")
        file_object.write(f"{greeting} {name.title()}.\n")
        answer = input("More users (yes/no): ")
        if answer == 'no' or answer == 'No':
            active = False            