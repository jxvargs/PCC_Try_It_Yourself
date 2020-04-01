#!/usr/bin/env python3.7

# JulianV
# Feb 27, 2020.
# Exercise 8.3 function calls.
# positional arguments and keyword arguments.

def make_tshirt(size, slogan):
# string input -> It display the size and
# the message on your T-Shirt
    print("\nOrder.")
    print(f"\tT-Shirt size--> {size}")
    print(f"\tMessage--> {slogan}")
    print("")

print("")
print("xceed T-Shirts".center(40, "-"))
t_shirt_size = input("Enter your size (small-p/small/medium/large/x-large): ")
message = input("Enter your message: ")

# Positional and keyword arguments.
make_tshirt(t_shirt_size, message)
make_tshirt(size=t_shirt_size, slogan=message)