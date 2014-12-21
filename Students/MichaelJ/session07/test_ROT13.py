"""
Test whether ROT13.py works

test_ROT13.py

Can use the py.test to make sure that ROT13.py works.
"""


import pytest
from ROT13 import rot13


def test_lower():
    assert rot13('rhsehthrhtsjnsjny') == 'eufrugueugfwafwal'


def test_upper():
    assert rot13('RETNDJE') == 'ERGAQWR'


def test_both_and_numbers():
    assert rot13('awaOVHU323') == 'njnBIUH323'
