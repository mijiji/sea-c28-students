'''
Ackermann function

'''


def A(m, n):
    # computes ackermann function
    if m < 0 or n < 0:
        return None
    # ackermann function does not account for negative numbers in input
    if m == 0:
        return n + 1
    elif n == 0:
        return A(m - 1, 1)
    elif m > 0 and n > 0:
        return A(m - 1, A(m, n - 1))

if __name__ == "__main__":

    # Some basic tests

    assert A(0, 0) == 1
    assert A(0, 3) == 4
    assert A(1, 0) == 2
    assert A(1, 4) == 6
    assert A(2, 2) == 7
    assert A(3, 3) == 61
    # if m is >= 4, end value is extremly large
    assert A(-1, -1) is None
    assert A(0, -1) is None

    print u"all tests passed"
