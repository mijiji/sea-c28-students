"""
Test whether CountEvens.py works

test_CountEvens.py

Can use the py.test to make sure that CountEvens.py works.
"""


import pytest
from CountEvens import count_evens


def test_evens():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert count_evens(a) == 6
