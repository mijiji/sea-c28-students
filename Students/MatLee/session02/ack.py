def ackermann(m, n):
    """Return the Ackermann function evaluated for given values m and n."""
    if m is 0:
        return n+1
    elif (n is 0) and (m > 0):
        return "mode 2"
    else:
        return "mode 3"


