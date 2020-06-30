#!/usr/bin/env python3

# JulianV
# Jun 17, 2020.
# testing a function. (city and country)
# 11-1 Exercise
# using unittest

def formatted_city_and_country(city, country):
# Generate a formatted city and country.
    city_and_country = f"{city}, {country}"
    return city_and_country.title()