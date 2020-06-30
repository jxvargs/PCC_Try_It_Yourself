#!/usr/bin/env python3

# JulianV
# May 31, 2020.
# 10-7 Exercise
# Enter two numbers and catch the valueError

print("\nAdding two numbers.")
print("Or 'q' to quit the program.")

while True:
    num_one = input("\nFirst number: ")
    if num_one == 'q':
        print("\nProgram stops...")
        break
    num_two = input("Second number: ")
    if num_two == 'q':
        print("\nProgram stops...")
        break
    try:
        answer = int(num_one) + int(num_two)
    except ValueError:
        print("- you need a number (digit).")
    else:
        print(f"Result-> {answer}")