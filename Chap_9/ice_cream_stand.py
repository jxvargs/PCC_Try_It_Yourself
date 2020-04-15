#!/usr/bin/env python3.7

# JulianV
# Apr 8, 2020.
# Exercise 9-6
# Inheritance

class Restaurant:
    def __init__(self, name, cuisine):
        # Attributes initialization
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        # Restaurant description output
        print(f"Description.")
        print(f"\t-{self.name.title()}")
        print(f"\t-{self.cuisine.title()}")

    def open_restaurant(self):
        # Restaurant status
        print("Status:")
        print(f"\t{self.name.title()}.")
        print("\tIt is OPEN")

class IceCreamStand(Restaurant):
    #Representing the icream stand in the restaurant
    def __init__(self, name, cuisine):
        # Initializing attributes.
        super().__init__(name, cuisine)
        self.flavors = ['chocolate', 'strawberry', 'vanilla']

    def ice_cream_flavors(self):
        # Displaying flavor's list
        print("\n")
        print(f"Ice Cream Flavors".center(50, '-'))
        print(f"\t{self.flavors}")


new_restaurant = IceCreamStand('aztecs', 'mexican')
new_restaurant.describe_restaurant()
new_restaurant.ice_cream_flavors()