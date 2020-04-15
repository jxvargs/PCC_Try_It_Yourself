#!/usr/bin/env python3.7

# JulianV
# Apr 14, 2020.
# Exercise 9-10-A
# Imported Restaurant.

class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"Description.")
        print(f"\t-{self.name.title()}")
        print(f"\t-{self.cuisine.title()}")

    def open_restaurant(self):
        print("Status:")
        print(f"\t{self.name.title()}.")
        print("\tIt is OPEN")