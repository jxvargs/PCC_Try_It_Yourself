#!/usr/bin/env python3.7

# JulianV
# Mar 31, 2020.
# Exercise 8-16-a
# greeter program

def greeter (name):
    print(f"\nHello, nice to meet you, {name.title()}")

def course_taken(course):
    new_course = course.upper()
    if new_course == "Python":
        print(f"Great {new_course} is a tremendous option.")
    else:
        print(f"{new_course} is a good option")
