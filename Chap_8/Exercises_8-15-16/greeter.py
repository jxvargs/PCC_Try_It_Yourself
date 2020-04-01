#!/usr/bin/env/ python3.7
import greetings
from greetings import greeter
from greetings import course_taken
import greetings as gct
from greetings import *

# JulianV
# Mar 31, 2020.
# Exercise 8-16-b
# Imports

courses = ['Python', 'Java', 'JavaScript']
greeter(name = input("\nWhat is your name: "))
print(f"\n\t{courses}")
course_taken(course = input("Which course from the list, are you taking: "))

courses = ['Python', 'Java', 'JavaScript']
gct.greeter(name = input("\nWhat is your name: "))
print(f"\n\t{courses}")
gct.course_taken(course = input("Which course from the list, are you taking: "))
