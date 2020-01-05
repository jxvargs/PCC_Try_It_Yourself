#!/usr/bin/env python3.7
'''
    JulianV
    12/22/2019.
    Exercise 6-6
    Polling, check if the members of the list
    have taken the poll.
'''
poll = {'jen': True,
    'sarah': False,
    'edward': False,
    'phil': True,
    'peter': True,
    'ryan': False,
    'pedro': True
}
for user, value in poll.items():
    if value == True:
        print(f"{user.title()} thanks for taking the poll.")
    else:
        print(f"{user.title()}, please take the poll.")
