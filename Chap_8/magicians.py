#!/usr/bin/env python3.7

# JulianV
# Mar 4, 2020.
# Exercise 8-9
# Make a list of magicians
# using a function.

def display_magicians(magicians):
    # displaying magicians.
    print("")
    print("My favorite magicians.".center(30, '-'))
    print(f"{magicians}\n")

count = 1
limit = 3
magicians = []

# filling up the the list to be diplayed.
while count <= limit:
    magician = input("Enter your favorite magician: ")
    magicians.append(magician)
    count += 1

display_magicians(magicians)