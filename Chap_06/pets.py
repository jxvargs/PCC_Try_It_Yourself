#!/usr/bin/env python3.7

#   JulianV
#   12/30/2019
#   Pets exercise 6-8

# dogs information stored in a dictionary
rocky = {'breed': 'labrador', 'har': 'black', 'owner': 'peter pan' }
baloo = {'breed': 'belgian shepherd', 'hair': 'brown/black', 'owner': 'don bracho'}
luiggi = {'breed': 'terrier', 'hair': 'white gray black', 'owner': 'bryan'}
amy = {'breed': 'shar pei', 'hair': 'brown', 'owner': 'demian'}
dydy = {'breed': 'scotish terrier', 'hair': 'black', 'owner': 'joanna'}

pets = [rocky, baloo, luiggi, amy, dydy] # List of dictionaries

# Displaying information about the dogs.
print("DOGS".center(80,'-'))
for dog in pets:
    print(f"{dog}")