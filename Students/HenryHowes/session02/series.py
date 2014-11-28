def fibonacci(n):
    """"""
    if n < 1:
        raise ValueError('n must be greater than 0')

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci (n-2)


def lucas(n):
    """"""
    if n < 1:
        raise ValueError('n must be greater than 0')

    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n-1) + lucas (n-2)

def sum_series(n, first=0, second=1):
    if n < 1:
        raise ValueError('n must be greater than 0')
    #print second
    if n == 1:
        return first
    elif n == 2:
        return second
    else:
        return sum_series(n-1, first, second) + sum_series (n-2, first, second)

if __name__ == "__main__":
    #for number in range (3,8):
        #print fibonacci(8) # == fibonacci(3) + fibonacci(2)    
        #print lucas(0) # == lucas(4) + lucas(3)
        assert sum_series(6) == fibonacci(6)
        assert sum_series(5, 2, 1) == lucas(5)
        assert sum_series(3,first=5,second=4) == 9
        print("all tests passed")
#print(fibonacci(4))
#print(lucas(4))
#print(sum_series(4))
#print(sum_series(4, 2, 1))

