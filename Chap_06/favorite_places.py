#!/usr/bin/env python3.7

#   JulianV
#   12/30/2019
#   Favorite Places. Exercise 6-9

# filling up the favorite places dictionary: key: name, value: favorite places.
favorite_places = {'peter': ['vietnam', 'south korea', 'china'],
    'julian': ['washintong dc', 'germany', 'islandia'],
    'alan': ['canada', 'brasil', 'japon'],
    'jorge': ['san francisco', 'las vegas', 'mexico'],
    'anthony': ['costa rica', 'puerto rico', 'las vegas']
}
# Formatting title.
print("Favorite Places".center(30,'_'))

# Displayaing each name information.
for name, places in favorite_places.items():
    print(f"* {name.title()}")
    for place in places:
        print(f"\t- {place.title()}")
