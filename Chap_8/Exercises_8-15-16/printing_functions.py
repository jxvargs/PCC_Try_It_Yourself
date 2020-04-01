#!/usr/bin/env python3.7

# JulianV
# Mar 30, 2020.
# Writing an import statement.
# Exercise 8-15-a

# Managing data.
def print_models(unprinted_designs, completed_models):
    print("Unprinted Designs".center(30,'-'))
    for design in unprinted_designs:
        print(f"\t{design}")
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("")
    print("The following models have been printed.")
    for complete_model in completed_models:
        print(f"\t{complete_model}")
