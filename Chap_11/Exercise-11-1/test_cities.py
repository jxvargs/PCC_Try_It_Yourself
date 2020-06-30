#!/usr/bin/env python3

# JulianV
# Jun 17, 2020.
# 11-1 Exercise
# Testing city_functions.py

import unittest
from city_functions import formatted_city_and_country

class CityCountryTestCase(unittest.TestCase):
# Testing city_functions.py
    def test_city_country(self):
        formatted_city_country = formatted_city_and_country('dallas', 'united states')
        self.assertEqual(formatted_city_country, 'Dallas, United States')

unittest.main()