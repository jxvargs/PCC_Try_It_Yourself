#!/usr/bin/env python3

# JulianV
# May 31, 2020.
# 10-10 
# counting the common words in a text file.

print("Count the common word 'the' in a file.")
print("Enter 'q' to quit...")
content = []
common_word = 0
while True:
    filename = input("\nEnter file name: ")
    if filename == 'q':
        break
    try:
        with open(filename) as f_obj:
            for line in f_obj:
                content.append(line.rstrip())
            for new_line in content:
                common_word += new_line.lower().count('the')
            print(f"Result of common word is -> {common_word}.")
    except FileNotFoundError as err:
        print(f"{err} - No valid file...")
