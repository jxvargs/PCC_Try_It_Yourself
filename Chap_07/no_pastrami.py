#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

# JulianV
# Jan 20 2020.
# Exercise 7-9
# No Pastrami.

sandwich_order = ['tuna sandwich', 'club sandwich', 'turkey sandwich', 'pastrami sandwich', 'BLT sandwich']
finished_sandwich = []

# Displaying the list order sandwiches
# and filling up the finished order list.
while sandwich_order:
    sandwich = sandwich_order.pop()
    print(f"{sandwich.title()} is ready.")
    finished_sandwich.append(sandwich)

print("")
# printing the list of done sandwiches.
print("sandwich done".center(32, '-'))
for sandwich in finished_sandwich:

    print(f"\t{sandwich.title()}")