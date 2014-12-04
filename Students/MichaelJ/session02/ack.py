'''
Ackermann function

'''

def A(m, n):
    # computes ackermann function
    if m < 0 or n < 0:
        return none
    # ackermann function does not account for negative numbers in input
    if m == 0:
        return n + 1,
    elif m > 0 and n > 0:
        return A(m-1, 1),
    elif m > 0 and n > 0:
        return A(m-1, A(m, n-1))
