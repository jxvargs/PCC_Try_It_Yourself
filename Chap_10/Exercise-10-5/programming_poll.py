#!/usr/bin/env python3

# JulianV
# May 24, 2020.
# 10-5 Programming poll
# add user message to a file.

filename = 'poll.txt'
prompt = "\nWhy do you like programming? "
prompt += "\n(Enter 'quit' to finish.) "
active = True
with open(filename, 'a') as file_object:
    while active:
        reason = input(prompt)
        if reason == 'quit':
            break
        else:
            file_object.write(f"-{reason}.\n")

