#!/usr/bin/env python3.7

# JulianV
# Feb 27, 2020.
# Returning a dictionary.
# This function will build a dictionary
# Exercise 8-7

def make_album(artis, album_title, num_tracks=0):
# input string, int -> dictionary
# the function builds a dictionary.
    album = {'Singer': artis, 'album': album_title}
    if num_tracks:
        album['tracks'] = num_tracks
    return album

musician = make_album('3 Doors Down', 'Away from the Sun')
print(musician)

musician = make_album('Shakira', 'Donde Estan Los Ladrones', 12)
print(musician)