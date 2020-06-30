#/usr/bin/env python3

# JulianV
# Jun 17, 2020.
# testing a function. (city, country and population)
# 11-2 Exercise
# using unittest

import unittest
from population_function import format_city_country_pop

class CityCountryPopTestCase(unittest.TestCase):    
    def test_city_country(self):        
        formatted_city_country_pop = format_city_country_pop('los angeles', 'united states')        
        self.assertEqual(formatted_city_country_pop, 'Los Angeles, United States')    
    
    def test_city_country_pop(self):        
        formatted_city_country_pop = format_city_country_pop(            
            'los angeles', 'united states', 12447000)        
        self.assertEqual(formatted_city_country_pop, 'Los Angeles, United States - Population=12447000')

unittest.main()