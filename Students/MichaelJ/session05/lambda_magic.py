"""
A function that returns an input value with increasing incrementation.

Lambda and keyword magic

A function that returns a list of n functions. It will return the input
value with increasing incrementation.
"""

# (lambda example from online):
# def adder(x):
#   return lambda y: x + y
# add5 = adder(5)
# add5(1) = 6

# part 1


def function_builder(n):
    l = []
    for x in range(n):
        l.append(lambda y, x=x: x + y)
    return l

if __name__ == "__main__":

    assert len(function_builder(0)) == 0
    assert len(function_builder(1)) == 1
    assert len(function_builder(2)) == 2
    assert len(function_builder(10)) == 10

    the_list = function_builder(5)

    assert the_list[0](0) == 0
    assert the_list[0](1) == 1
    assert the_list[1](0) == 1
    assert the_list[1](1) == 2
    assert the_list[2](2) == 4

    print("all tests pass")
