#!/usr/bin/env python3.7

# JulianV
# Feb 24 2020.
# Write a function that accepts
# one parameter. exercise 8-2
def favorite_book(title):
# string -> string
# It displays a message including the argument
    print(f"One of my favorite books is {title.title()}.")

book = input("Enter one of your preferred books: ")
favorite_book(book) # function call