#!/usr/bin/env python3

# JulianV
# May 31, 2020.
# 10-6 addition catching the error.

print("\nEnter two numbers.")
try:
    num_one = input("Number one: ")
    num_one = int(num_one)
    
    num_two = input("Number two: ")
    num_two = int(num_two)
    result = num_one + num_two
except ValueError as Err:
    print(f"{Err} - must be a number (digit).")
else:
    print(f"Result->{result}")

