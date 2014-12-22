"""
Prints the time taken to run code.

Timing Context Manager

Will record and print the time elapsed to run through code.
"""


import time


def timed_function():
    for i in range(100000):
        i = i ** 20
    return i


