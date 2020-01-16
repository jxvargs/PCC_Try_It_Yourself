#!/usr/bin/env python3.7
'''
    JulianV
    12/22/2019.
    Glosary program ver. 2 5 words follow by
    thier meaning.
'''
glosary = {'list': 
    'colletion of arbitrary objects, ordered, accessed by index, mutable, and dynamic.',
    'variable': 
    'name attaced to a particular object, variablesneed to be declared in advance.',
    'tuple':
    'A sequence of immutable python objects.',
    'method': 
    "It is a function that is available for a given object because object's type",
    'strings': 
    'strings are arrays of of bytes representing Unicode characters.',
    'dictionary':
    'It is an implementation of data structure that is more generally known as an associative array.',
    'if statatements':
    'It allows for conditional execution of a statement or group of statements based on the value of an expresion.'
    }

print("G l o s a r y .".center(88,' '))
print("---------------------------------------------------------------------------------")
for word, meaning in glosary.items():
    print(f"{word.title()}:\n   {meaning}")

'''    
print(f"List:\n {glosary['list']}")
print(f"Variable:\n  {glosary['variable']}")
print(f"Tuple:\n  {glosary['tuple']}")
print(f"Method:\n  {glosary['method']}")
print(f"string:\n  {glosary['strings']}")
'''
