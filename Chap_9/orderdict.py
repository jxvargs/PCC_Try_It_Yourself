#!/usr/bin/env python3.7

# JulianV
# Apr 13, 2020.
# Exercise 9-13
# rewrite exercise 6-4
# using OrderDict class

from collections import OrderedDict

# JulianV
# 12/22/2019.
# Exercise 9-13
# Glosary program words follow by
# thier meaning.

glosary = OrderedDict()
glosary['list'] = 'colletion of arbitrary objects, ordered, accessed by index, mutable, and dynamic.'
glosary['variable'] = 'name attaced to a particular object, variablesneed to be declared in advance.'
glosary['tuple'] = 'A sequence of immutable python objects.'
glosary['method'] = "It is a function that is available for a given object because object's type"
glosary['strings'] = 'strings are arrays of of bytes representing Unicode characters.'
glosary['dictionary'] = 'It is an implementation of data structure that is more generally known as an associative array.'
glosary['if statatements'] = 'It allows for conditional execution of a statement or group of statements based on the value of an expresion.'

print("G l o s a r y .".center(88,' '))
print("---------------------------------------------------------------------------------")
for word, meaning in glosary.items():
    print(f"{word.title()}:\n   {meaning}")