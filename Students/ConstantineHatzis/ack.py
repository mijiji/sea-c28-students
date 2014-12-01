def ack(m, n,):
    """Return the ouput of the Ackermann function for two numbers greater than zero."""
    if m < 0 or n < 0:
        return None
    elif m == 0:
        return n + 1
    elif m > 0 and n == 0:
        ack(m-1, 1)
    elif m > 0 and n > 0:
        ack(m-1, ack(m, n-1))
    else:
        return None

testValues = [[1, 2, 3, 4], [2, 3, 4, 5, 6], [3, 5, 7, 9, 11], [5, 13, 29, 61, 125]]
