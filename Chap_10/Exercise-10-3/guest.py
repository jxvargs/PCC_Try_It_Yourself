#!/usr/bin/env python3

# JulianV
# May 21, 2020.
# 10-3 Guest. 
# Prompt a user and write their 
# name to a file.

def write_file(name, file):
# name will be written in a file.
    with open(file, 'w') as file_object:
        file_object.write(f"Welcome, {name.title()}.")


file_name = 'guest.txt'
name = input("Hello, what is your name: ")

write_file(name, file_name)