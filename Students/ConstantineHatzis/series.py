from __future__ import print_function


def fibonacci(n):
    """Return the nth number in the Fibonacci Series"""
    a, b = 0, 1  # Initialize Fibonacci Series
    for i in range(n):
        a, b = b, a + b
        return (b)
