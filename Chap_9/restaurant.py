#!/usr/bin/env python3.7

# JulianV
# Apr 2, 2020.
# Exercise 9-1
# Restaurant class, __init__, and 
# attributes.

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

mexico = Restaurant('aztecas', 'mexican')
print(f"Name of Restaurant: {mexico.name.title()}")
print(f"Style Cuisine: {mexico.cuisine.title()}")

mexico.describe_restaurant()
mexico.open_restaurant()


