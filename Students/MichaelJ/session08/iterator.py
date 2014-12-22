#!/usr/bin/env python

"""
Simple iterator examples
"""


class IterateMe_1(object):
    """
    About as simple an iterator as you can get:
    returns the sequence of numbers from zero to 4
    ( like xrange(4) )
    """
    def __init__(self, stop=5):
        self.current = -1
        self.stop = stop

    def __iter__(self):
        return self

    def next(self):
        self.current += 1
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


class IterateMe_2(object):
    """
    About as simple an iterator as you can get:
    returns the sequence of numbers from zero to 4
    ( like xrange(4) )
    """
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = 1
        self.current = start - step

    def __iter__(self):
        return IterateMe_2(self.start, self.stop, self.step)

    def next(self):
        self.current += 1
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


if __name__ == "__main__":

    print("first version")
    it = IterateMe_2(1, 5, 1)
    for i in it:
        if i > 2:
            break
        print(i)
    for i in it:
        print(i)

    xran = xrange(5)
    for i in xran:
        if i > 2:
            break
        print(i)
    for i in xran:
        print(i)