#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

# JulianV
# Jan 20 2020.
# Exercise 7-10
# prompt the user for his/her name and 
# his/her dream vaction place.

vacations = {}
# activate a flag.
active = True 

while active:
    name = input("\nWhat is your name? ")
    place = input("What is your dream vacation? ")
    vacations[name] = place

    answer = input("\nWould you like to Enter another one (yes/no) ")
    # checking for possile answers for 'no'
    if answer == 'no' or answer == 'n' or answer == 'No' or answer == 'NO':
        active = False # Deactivating the flag

print("") # formatting the output
print("Dream Vacation Palces".center(55,'-'))
for name, place in vacations.items():
    print(f"\t{name.title()} will tavel to {place.title()}.")