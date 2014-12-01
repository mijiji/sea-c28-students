from __future__ import print_function


def fibonacci(n):
    """Return the nth number in the Fibonacci Series"""
    a, b = 0, 1  # Initialize Fibonacci Series
    for i in range(1, n):
        a, b = b, a + b  # Generate nth and nth + 1 number in Fibonacci Series
    return (a)
