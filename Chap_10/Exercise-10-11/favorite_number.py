#!/usr/bin/env python3

# JulianV
# Jun 4, 2020.
# 10-11 
# Write a program that it prompts
# the user for his/her favorite number
# and save in a json file.

import json

filename = 'favorite_number.json'

active = True
while active:
    try:
        fav_number = int(input("Enter your favorite number: "))
        if fav_number:
            active = False
    except ValueError:
        print("Try again - Number is required...")
    else:
        with open(filename, 'w') as f_obj:
            json.dump(fav_number, f_obj)
            print("Well done!")