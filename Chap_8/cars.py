#!usr/bin/env python3.7

# JulianV
# Mar 10, 2020.
# Exercise 8-14.
# Car's features.

def make_car(make, model, **car_features):
    desire_car = {}
    desire_car['make'] = make
    desire_car['model'] = model
    for key, value in car_features.items():
        desire_car[key] = value.title()
    return desire_car

my_car = make_car('honda', 'accord', color='metalic blue', GPS='yes', engine='2.4' )
print("Your car will be as follows".center(30,'-'))
print(my_car)