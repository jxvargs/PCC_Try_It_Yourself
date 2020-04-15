#!/usr/bin/env python3.7

# JulianV
# Apr 14, 2020.
# Exercise 9-14
# Generate a random number
# using random and randint

from random import randint

class Die():
    def __init__(self, number):
        # Initializing Attributes
        self.number = number

    def roll_die(self):
        start_number = 1
        number = randint(start_number, self.number)
        return number

six_sides = Die(6)
ten_sides = Die(10)
twenty_sides = Die(20)
print(f"Your number is -> {six_sides.roll_die()}")
print(f"Your number is -> {six_sides.roll_die()}")
print(f"Your number is -> {six_sides.roll_die()}")
print(f"Your number is -> {six_sides.roll_die()}")
print(f"Your number is -> {six_sides.roll_die()}")
print(f"Your number is -> {six_sides.roll_die()}")
print(f"Your number is -> {six_sides.roll_die()}")
print(f"Your number is -> {six_sides.roll_die()}")
print(f"Your number is -> {six_sides.roll_die()}")
print(f"Your number is -> {six_sides.roll_die()}")
print("")
print(f"Your number is -> {ten_sides.roll_die()}")
print(f"Your number is -> {ten_sides.roll_die()}")
print(f"Your number is -> {ten_sides.roll_die()}")
print(f"Your number is -> {ten_sides.roll_die()}")
print(f"Your number is -> {ten_sides.roll_die()}")
print(f"Your number is -> {ten_sides.roll_die()}")
print(f"Your number is -> {ten_sides.roll_die()}")
print(f"Your number is -> {ten_sides.roll_die()}")
print(f"Your number is -> {ten_sides.roll_die()}")
print(f"Your number is -> {ten_sides.roll_die()}")
print("")
print(f"Your number is -> {twenty_sides.roll_die()}")
print(f"Your number is -> {twenty_sides.roll_die()}")
print(f"Your number is -> {twenty_sides.roll_die()}")
print(f"Your number is -> {twenty_sides.roll_die()}")
print(f"Your number is -> {twenty_sides.roll_die()}")
print(f"Your number is -> {twenty_sides.roll_die()}")
print(f"Your number is -> {twenty_sides.roll_die()}")
print(f"Your number is -> {twenty_sides.roll_die()}")
print(f"Your number is -> {twenty_sides.roll_die()}")
print(f"Your number is -> {twenty_sides.roll_die()}")


