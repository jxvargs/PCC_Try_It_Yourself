#!/usr/bin/env python3.7

# JulianV
# Feb 27, 2020.
# Exercise 8-5
# Write a function call describe_city()
# that it accepts two parameters.

def describe_city(city, country='usa'):
    print(f"{city.title()} is in {country.upper()}")

describe_city('los angeles')
describe_city('san diego')
describe_city('guadalajara', 'mexico')