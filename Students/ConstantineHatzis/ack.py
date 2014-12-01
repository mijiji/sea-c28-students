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
