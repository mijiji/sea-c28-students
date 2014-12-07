"""
defining multiple mathematical series
fibonacci series and lucas numbers
"""


def fibonacci(n):

    """computes the fibonacci sequence"""

    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):

    """computes the lucas series"""

    if n < 0:
        return None
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def sum_series(n, n0=0, n1=1):
    if n < 0:
        return None
    if n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        return sum_series(n-1, n0, n1) + sum_series(n-2, n0, n1)