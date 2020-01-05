#!/usr/bin/env python3.7

# JulianV
# 12/22/2019.
# Exercise 6-5
# Rivers and their countries.

rivers = {'hudson':
    'It is a 316 mile river between New YorK city and Jersey city',
    'amazon':
    'The largest river in South America. Brazil, Peru, and Colombia.',
    'usumacinta': 'Named after the howler monkey is a river in southern Mexico and northern Guatemala.'
}
print("R I V E R S.".center(20,'_'))
for river in rivers.keys():
    print(f"- {river.title()}")

print("\n")
print("Location".center(80,'_'))
for location in rivers.values():
    print(f"-> {location.title()}")

