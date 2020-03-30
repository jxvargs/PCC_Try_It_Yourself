#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

# JulianV
# Jan 14 2020.
# exercise 7-5
# Ticket price base on customer's age.

active = True
print("\n")
print("Beyond Theater".center(50,"-"))
while active:
    age = int(input("How old are you? "))
    if age <= 3:
        print("Nice! Free ticket.")
    elif age > 3 and age <= 12:
        print("ticket price is $10.00 dls.")
    else: 
        print("ticket price $15.00 dls.")
    answer = input("\nEnter 'quit' to end the program: ")
    if answer == 'quit':
        active = False   
    print()