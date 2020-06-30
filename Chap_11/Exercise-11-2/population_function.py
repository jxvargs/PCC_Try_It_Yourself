#!/usr/bin/env python3

# JulianV
# Jun 17, 2020.
# testing a function. (city, country and population)
# 11-2 Exercise
# using unittest

def format_city_country_pop(city, country, pop=0):
# Generate a formatted city and country.
    if pop:
        city_country_pop = f"{city.title()}, {country.title()} - Population={str(pop)}"
    else:
        city_country_pop = f"{city.title()}, {country.title()}"
    return city_country_pop