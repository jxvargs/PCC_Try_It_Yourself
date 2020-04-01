#!/usr/bin/env python3.7

# JulianV
# Mar 4, 2020.
# Exercise 8-10
# Modify the list of magicians
# by adding "the Great" magician's name.

def show_magicians(magicians):
    print("")
    print("My favorite magicians.".center(60, '-'))
    print(f"{magicians}\n")

def make_great(magicians, great_magicians):
    while magicians:
        current_magician = magicians.pop()
        great_magicians.append(f"the Great {current_magician.title()}")

count = 1
magicians = []
great_magicians = []

while count <= 3:
    magician = input("Enter magian's name: ")
    magicians.append(magician)
    count += 1

make_great(magicians[:], great_magicians)
show_magicians(great_magicians)



