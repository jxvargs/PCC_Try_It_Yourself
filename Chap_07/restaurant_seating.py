#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

# JulianV
# Jan 12 2020.
# Restaurant seating.
# Exercise 7-2

print("")
print('Welcome to Mexican Passion!'.center(50,'-'))
guests = int(input("How many people in your group? "))

if guests >= 8:
    print("\nWaiting time is 20 minutes!")
else:
    print("\nOk, your table is ready.")