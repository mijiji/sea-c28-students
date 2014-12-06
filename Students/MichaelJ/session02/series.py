# defining multiple mathematical series
# fibonacci series and lucas numbers


def fibonacci(n):
    if n < 0:
        return None
    # there is no negative values for n
    elif n == 0:
        return 0
    # first value of the series
    elif n == 1:
        return 1
    # second value of the series
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    # any other value is the sum of 2 previous sums

def lucas(n):
    if n < 0:
        return None
    elif n == 0:
    # first value of lucas series is different
        return 2
    elif n == 1:
        return 1
    # seconf value of lucas series is different
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)