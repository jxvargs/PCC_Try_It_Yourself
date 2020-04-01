#!/usr/bin/env python3.7

# JulianV
# Mar 9, 2020.
# Exercise 8-12
# Write a function that it accepts
# a list of items.

def show_items(*ingredients):
    print("Items in your sandwiche".center(30,'-'))
    for ingredient in ingredients:
        print(f"\t- {ingredient}")

print("\n")
show_items('lettuce', 'tomato','bell pepper', 'olives')
show_items('ham', 'no onion', 'no chili')
show_items('jalapenos', 'grilled onion')