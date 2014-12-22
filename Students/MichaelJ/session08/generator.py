"""
A program to generate multiple series.

Generator

A program with multiple generators to produce multiple series.
"""


def intsum():
    a = 0
    b = 0
    while True:
        yield a
        b += 1
        a = a + b


def doubler():
    a = 0
    while True:
        yield a
        a = a * 2


def fib():
    a = 1
    b = 1
    while True:
        yield a
        a, b = b, a + b


def prime():
    a = 2
    while True:
        for i in range(2, a + 1):
            if a == i:
                yield a
            elif a % i == 0:
                break
        a += 1
