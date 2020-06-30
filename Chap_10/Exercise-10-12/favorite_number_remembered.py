#!/usr/bin/env python3

# JulianV
# Jun 4, 2020.
# 10-12
# Combine the programs in 10-11 into one program
import json

filename = 'favorite_number.json'

active = True

try:
    with open(filename) as f_obj:
        fav_number = json.load(f_obj)
except FileNotFoundError:
    print(f"\nNo favorite number...\n")
    while active:
        try: 
            fav_number = int(input("Enter a favorite number: "))
            if fav_number:
                active = False
        except ValueError:
            print("Try again - number is required")
        else:
            with open(filename, 'w') as f_obj:
                json.dump(fav_number, f_obj)
                print("We'll remember your favorite number when you come back...")
else:
    print(f"Welcome back favorite number {fav_number}")
