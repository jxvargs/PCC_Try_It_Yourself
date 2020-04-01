#!/usr/bin/env python3.7

# JulianV
# Mar 2, 2020.
# Exercise 8-8
# Use a while loop to enter
# an album's artist and title.
def make_album(artist, album_title):
# input string, int -> dictionary
# the function builds a dictionary.
    # building the dictionary
    album = {'Singer': artist.title(), 'Album': album_title.title()}
    return album 

while True:
    print("Enter Album's information.")
    print("(enter 'q' at any time to quit)")
    artist = input("Enter artist name: ")
    if artist == 'q':
        break # exit the loop
    title = input("Enter album's title: ")
    if title == 'q':
        break # exit the loop
    # funcntion call
    album_info = make_album(artist, title)
    # Formatting the output
    print(f"\n\t{album_info}\n")