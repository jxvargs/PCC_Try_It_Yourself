#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

# JulianV
# Jan 13 2020.
# Multiples of ten.
# Exercise 7-3

print("\nLet's see if your number is multiple of ten.")
number = int(input("Enter a number: "))

# checking whether the number is multiple of ten
if number % 10 == 0:
    print(f"\nYeah! {number} is multiple of ten.")
else:
    print(f"\nAuh! {number} is not multiple of ten.")