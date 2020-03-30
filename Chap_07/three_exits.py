#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

# JulianV
# Jan 15 2020.
# Exercise 7-6
# Three types of exit to terminate
# the program.

prompt = "\nEnter a message or 'quit' to exit: "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)