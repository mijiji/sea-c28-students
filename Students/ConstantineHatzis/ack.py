from __future__ import print_function


def ack(m, n):
    """Return the ouput of the Ackermann function for two numbers greater than zero."""
    print(m, n)
    if m < 0 or n < 0:
        print(u"m < 0 and n < 0: ", m, n)
        return None
    elif m == 0:
        print(u"m == 0: ", m, n, n + 1)
        return n + 1
    elif m > 0 and n == 0:
        print(u"m > 0 and n == 0: ", m, n)
        ack(m-1, 1)
    elif m > 0 and n > 0:
        print(u"m > 0 and n > 0: ", m, n)
        ack(m-1, ack(m, n-1))

print(u"Answer = ", ack(2, 0))

if __name__ == "__main__":
    testValues = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 5, 7, 9, 11], [5, 13, 29, 61, 125]]
