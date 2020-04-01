#!/usr/bin/env python3.7

# JulianV
# Feb 28, 2020.
# Exercise 8-6
# write a function en format the 
# output

def city_country(city, country):
# input string -> string. It takes
# two arguments and it returns a formatted
# string.
    print(''.center(40, '_'))
    print(f'\t"{city.title()}, {country.title()}"')
    print(''.center(40, '_'))

city_country('paris', 'france')
city_country('berlin', 'germany')
city_country('cuernavaca', 'mexico')