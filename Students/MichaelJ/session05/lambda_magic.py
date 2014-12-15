"""
A function that returns an input value with increasing incrementation.

Lambda and keyword magic

A function that returns a list of n functions. It will return the input
value with increasing incrementation.
"""

# part 1
# (lambda example): g = lambda x: x**2
#                   print g(8) = 64


def function_builder(n):
    l = []
    for x in range(n):
        l.append(lambda y, x=x: x + y)
    return l

func_list = function_builder()
