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


def sum_series(n, a=0, b=1):
    """Return the nth value of a series determined by the optional arguments, a and b"""
    if a == 0 and b == 1:
        result = fibonacci(n)
    elif a == 2 and b == 1:
        result = lucas(n)
    else:
        print(u"That function is not available yet")
    return result

if __name__ == "__main__":
    test_values_fibonacci = [0, 1, 1, 2, 3, 5, 8, 13]
    test_values_lucas = [2, 1, 3, 4, 7, 11, 18, 29]
    test_values_sum_series = [[5, 0, 1, 3], [5, 2, 1, 7]]

    for n in range(7):
        assert fibonacci(n + 1) == test_values_fibonacci[n]
        assert lucas(n + 1) == test_values_lucas[n]

    for n in range(0, 1):
        print(test_values_sum_series[n][0:3])
        print(sum_series(test_values_sum_series[n][0:3]))
        assert sum_series(test_values_sum_series[n][0:3]) == test_values_sum_series[n][4]

    # If an assert fails, and exception will be thrown and this following print will not executre.
    print(u"All Tests Pass")
