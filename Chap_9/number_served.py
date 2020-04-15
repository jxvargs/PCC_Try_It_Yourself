#!/usr/bin/env python3.7

# JulianV
# Apr 7, 2020.
# Exercise 9-4
# Attributes and methods

class Restaurant:
    def __init__(self, name, cuisine):
        # Initializing attributes.
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        # Describing restaurant and cuisine.
        print(f"Description.")
        print(f"\t-{self.name.title()}")
        print(f"\t-{self.cuisine.title()}")
        print(f"\t-Customers Served: {str(self.number_served)}")

    def open_restaurant(self):
        print("Status:")
        print(f"\t{self.name.title()}.")
        print("\tIt is OPEN")
    
    def set_number_served(self, customers):
        self.number_served = customers
        print(f"\tCustomer Served: {str(self.number_served)}")

    def increment_number_served(self, customers):
        self.number_served += customers
        print("\n")
        print(f"{self.number_served} customers have been served a day.")
        

    

mexico = Restaurant('aztecas', 'mexican')
print(f"Name of Restaurant: {mexico.name.title()}")
print(f"Style Cuisine: {mexico.cuisine.title()}")

mexico.describe_restaurant()
mexico.open_restaurant()

mexico.number_served = 5
mexico.describe_restaurant()

mexico.increment_number_served(0)