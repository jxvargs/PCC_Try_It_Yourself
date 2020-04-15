#!/usr/bin/env python3.7

# JulianV
# Apr 2, 2020.
# Exercise 9-2
# Creating instances,
# base on exercise 9-1.

class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        # Restaurant Description
        print(f"Description.")
        print(f"\t-{self.name.title()}")
        print(f"\t-{self.cuisine.title()}")

    def open_restaurant(self):
        # Restaurant hours.
        print("Status:")
        print(f"\t{self.name.title()}.")
        print("\tIt is OPEN")

mexico = Restaurant('aztecas', 'mexican')
usa = Restaurant('deli mornings', 'american breakfast')
viet = Restaurant('bahm mi viet', 'vietnamese bakery')

mexico.describe_restaurant()
usa.describe_restaurant()
viet.describe_restaurant()