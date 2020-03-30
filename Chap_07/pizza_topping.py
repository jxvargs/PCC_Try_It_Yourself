#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

# JulianV
# Jan 14 2020.
# exercise 7-4
# It prompts user to enter a pizza
# topping and it displays the topping
# on the screen. Enter quit to finish.

active = True # activating the flag
print("\n")

# formatting title.
print("Welcome to Desire Pizza".center(50,'-'))
prompt = "Enter your topping or (quit) to exit: "

while active: # while active is true
    topping = input(prompt)
    if topping == 'quit':
        active = False # changing flag status
    else: # displaying topping on the screen.
        print(f"{topping} added to your pizza...\n")