#!/usr/bin/env python3.7

#   JulianV
#   1/02/2020
#   Cities. Exercise 6-11

# loading the information about the cities in a dictionary
cities = {
    'mexico city': {'country': 'mexico', 'population': '8 855 million', 'fact': 'It is known for its Templo Mayor'},
    'los angeles': {'country': 'united states', 'population': '4 million', 'fact': 'L.A is the entertainment capital of the world.'},
    'frankfurt': {'country': 'germany', 'population': '2.3 million', 'fact': "germany's financial capital"}
}
# Displaying every city information 
for city, info in cities.items():
    print(f"{city.title()}") # formatting output
    for basis, data in info.items():
        justify_txt = basis.title() # justifying the text 
        print(f"\t{justify_txt.rjust(10)}: {data.capitalize()}")