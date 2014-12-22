"""
Prints the time taken to run code.

Timing Context Manager

Will record and print the time elapsed to run through code.
"""


import time


def sample():
    for i in range(100000):
        i = i ** 20
    return i


class timer(object):
    def __init__(self):
        self.start = time.time()

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        total_time = time.time() - self.start
        print 'time elapsed was {} seconds'.format(total_time)

with timer() as t:
    for i in range(100000):
        i = i ** 20
