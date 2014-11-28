def ack(m,n):
    """ """
    if m>=0 and n>=0:
        if not m:
            return n+1
        elif m > 0 and not n:
            return ack(m-1, 1)
        else:
            return ack(m-1, ack(m, n-1))
    else:
        return None




for m in range(4):
    for n in range(5):
        (ack(m,n))


