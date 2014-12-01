# Series Module
# This module contains three functions that all calculate a series where each 
# integer in the series is the sum of the previous two: Fibonacci Series 
# starts with 0 and then 1, Lucus Numbers start with 2 and 1 and Sum Series
# starts with any two number.

def fibonacci(n):
    """Return nth number in a fionacci series
       where n is an integer > 0.
       If n is less than 1, return None
    """
    if n == 1 :
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-2) + fibonacci(n-1)
    else:
        return None
print (fibonacci(3))
print (fibonacci(4))

def lucas(n):
    """Return nth number in a lucas number series
       where n is an integer >  0.
       If n is less than 1, return None
    """
    if n == 1 :
        return 2
    elif n == 2:
        return 1
    elif n > 2:
        return lucas(n-2) + lucas(n-1)
    else:
        return None
print (lucas(3))
print (lucas(4))

def sum_series(n, a = 0, b = 1):
    """Return nth number in a sum_series series
       where n is an integer >  0.
       If n is less than 1, return None
       a and b are the first and second numbers in the series.
    """
    if n == 1 :
        return a
    elif n == 2:
        return b
    elif n > 2:
        return sum_series(n-2, a, b) + sum_series(n-1, a, b)
    else:
        return None
print (sum_series(3))
print (sum_series(4))