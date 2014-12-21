"""
Test whether ack.py works

test_ack.py

Can use the py.test to make sure that ack.py works.
"""


import pytest
from ack import A


def test_A():
    AFunc = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 5, 7, 9], [5, 13, 29, 61]]
    for m in range(4):
        for n in range(4):
            assert A(m, n) == AFunc[m][n]
