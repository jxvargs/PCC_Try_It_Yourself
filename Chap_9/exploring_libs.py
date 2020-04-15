#!/usr/bin/env python3.7

# JulianV
# Apr 14, 2020.
# Exercise 9-15
# Exploring Python standard library.

import glob

class Globing():
    def __init__(self, pattern):
        self.pattern = pattern

    def display_files(self):
        # Displaying files with a pattern
        print("Files:")
        for file in sorted(glob.glob(self.pattern)):
            print(f"\t{file}")

my_file = Globing('elec*.py')
my_file.display_files()