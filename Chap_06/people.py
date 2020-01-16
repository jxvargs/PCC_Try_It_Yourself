#!/usr/bin/env python3.7
'''
    JulianV
    12/29/2019
    People exercise 6-7
'''
# Declaring an empty list.
people = []

# Three dictionaries thal will be filled up 
# in line 20.
person_info_one = {}
person_info_two = {}
person_info_three = {}

# The previous dictionaries are appended to
# the list people.
people.append(person_info_one)
people.append(person_info_two)
people.append(person_info_three)

# Filling up each dictionary with people's information 
for personal_info in people:
    personal_info['fname'] = input("Enter your first name: ")
    personal_info['lname'] = input("Enter your last name: ")
    personal_info['age'] = int(input("Enter your age: "))
    personal_info['city'] = input("What city do you live: ")
    print("".center(35,'-'))

# Displaying people's information.
for person in people:
    print(f"Hello my name is {person['fname'].capitalize()} {person_info_one['lname'].capitalize()}.")
    print(f"\tMy age is {person['age']}.")
    print(f"\tMy city is {person['city'].capitalize()}.")
    print("")