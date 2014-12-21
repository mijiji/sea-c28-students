"""
Test whether series.py works

test_series.py

Can use the py.test to make sure that series.py works.
"""


import pytest
from series import fibonacci, lucas, sum_series


fib_vals = [

    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55)
]

luc_vals = [

    (0, 2),
    (1, 1),
    (2, 3),
    (3, 4),
    (4, 7),
    (5, 11),
    (6, 18),
    (7, 29),
    (8, 47),
    (9, 76),
    (10, 123)
]

sum_vals = [

    (0, 1, 0, 0),
    (0, 1, 1, 1),
    (0, 1, 2, 1),
    (0, 1, 3, 2),
    (0, 1, 4, 3),
    (0, 1, 5, 5),
    (2, 1, 0, 2),
    (2, 1, 1, 1),
    (2, 1, 2, 3),
    (2, 1, 3, 4),
    (2, 1, 4, 7),
    (2, 1, 5, 11)
]

for i, output in fib_vals:
    assert fibonacci(i) == output

for i, output in luc_vals:
    assert lucas(i) == output

for a, b, c, output in sum_vals:
    assert sum_series(a, b, c) == output
