#!/usr/bin/env python3

# JulianV
# May 19, 2020.
# 10-1 read your file entirely, and 
# loop through the lines.

# Reading the entire file once.
py_thoughts = ''
file_name = 'learn_python.txt'

with open(file_name) as file_object:
    py_thoughts = file_object.read()

print('\n')
print("Python Characteristics!".center(40, '-'))
print('-'.center(40,'-'))
print(py_thoughts)

# Reading the file line by line.
with open(file_name) as file_object:
    print("Python Characteristics!".center(40, '-'))
    for line in file_object:
        print(line)
        #print(line.rstrip())

# Making a llist of lines from a file.
with open(file_name) as file_object:
    lines = file_object.readlines()

thoughts = []
for line in lines:
    thoughts.append(line.strip())

print("\nthis is python in real world:".title())
for line in thoughts:
   print(f"\t{line}")