#!/usr/bin/env python3.7

#   JulianV
#   12/30/2019
#   Favorite Numbers. Exercise 6-10

favorite_numbers = {
    'alan': [2, 4, 9], 
    'peter': [3, 5 ,7],
    'robert': [1, 3, 8, 9],
    'thuy': [6, 7],
    'jose': [3, 6, 9]
}
# Displaying title and colums' titles
print(f"Favorite Numbers".center(50,'-'))
print("Name" + "Numbers".rjust(8,' '))

# Iterating through dictonary information
# and formating it output
for name, numbers in favorite_numbers.items():
    print(f"{name.title()}")
    for number in numbers:
        print(f"\t{number}")