#!/usr/bin/env python3

import json

# JulianV
# Jun 4, 2020.
# 10-11 
# Loading your favorite number.

filename = 'favorite_number.json'

with open(filename) as f_obj:
    fav_number = json.load(f_obj)

print(f"I know your favorite number! {fav_number}.")