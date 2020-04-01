#!/usr/bin/env python3.7

# JulianV
# Mar 10, 2020.
# Exercise 8-13
# Your profile and a few more fields.

def build_profile(first, last, **user_info):
    # Build a dictionary containing everything we know
    # about the yourself.
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value.title()
    return profile

user_profile = build_profile('julian', 'vargas', 
                    location='garden grove', field='it', title='sysAdmin essentials')

print(user_profile)