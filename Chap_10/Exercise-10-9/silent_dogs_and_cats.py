#!/usr/bin/env python3

# JulianV
# May 31, 2020.
# 10-9
# Catch FileNotFound
# Failing silently.

def read_file_content(filename): 
    try:
        with open(filename) as f_obj:
            names = f_obj.readlines()
    except FileNotFoundError:
        # Failing Silently  according to the book.
        pass
    else:
        if filename == 'cats.txt':
            print("C a t s:")
        else:
            print("D o g s:")
        for name in names:
            print(f"\t{name.rstrip()}")

def prompt():
# prompt user for file names.
    count = 1
    filenames = []
    while count <= 2:
        file = input("Enter your file name: ")
        filenames.append(file)
        count += 1
    return filenames

lst_files = prompt()

for filename in lst_files:
    read_file_content(filename)