#!/usr/bin/env python3.7

# JulianV
# Feb 27, 2020.
# Exercise 8-4
# Default arguments

def make_tshirt(size='large', slogan='I love Python'):
    print("")
    print("\nOrder.")
    print(f"\tT-Shirt's size--> {size.capitalize()}")
    print(f"\tMessage--> {slogan}")
    print("")

print("")
print("xceed T-Shirts".center(40, '-'))
make_tshirt() # using default arguments
make_tshirt('medium')