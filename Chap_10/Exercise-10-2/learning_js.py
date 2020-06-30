#!/usr/bin/env python3

# JulianV
# May 19, 2020.
# 10-2 Exercise.
# Replace a any word using replace()

def readfile(file):
# open/read a file --> list    
    with open(file) as f:
        message = f.readlines()
    return message

def replace_text(phrases):
# It replaces a string with another string. --> list
    new_lines = []
    for line in phrases:
        new_lines.append(line.replace('Python', 'JavaScript').strip())
    return new_lines

def display_file_content(new_lines):
# Displaying the new content of the file.
    print('\n')
    print("This is my next programming language".center(60,'-'))
    for line in new_lines:
        print(line)

py_thoughts = 'learn_python.txt'

# A basic touch of functional programming.
lines = replace_text(readfile(py_thoughts))

#new_lines = replace_text(lines)

display_file_content(lines)