from __future__ import print_function


def fibonacci(n):
    """Return the nth value in the Fibonacci Series"""
    a, b = 0, 1  # Initialize Fibonacci Series
    for i in range(1, n):
        a, b = b, a + b  # Generate nth and nth + 1 value in Fibonacci Series
    return (a)


def lucas(n):
    """Return the nth value of the Lucas Numbers"""
    a, b = 2, 1  # Initialize Lucas Numbers
    for i in range(1, n):
        a, b = b, a + b  # Generate nth and nth + 1 value of the Lucas Numbers
    return (a)
