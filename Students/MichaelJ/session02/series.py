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
    """
    This computes the nth value of a series.
    n0 and n1 are optional values.
    If optional values are left alone, it is fibonacci.
    If the optional values are n0 = 2 and n1 = 1, the series is lucas.
    """
    if n < 0:
        return None
    if n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        return sum_series(n - 1, n0, n1) + sum_series(n - 2, n0, n1)


if __name__ == "__main__":

    assert fibonacci(-5) is None
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5