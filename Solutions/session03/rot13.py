#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A simple function to compute rot13 encoding

ROT13 encryption

Applying ROT13 to a piece of text merely requires examining its alphabetic
characters and replacing each one by the letter 13 places further along in
the alphabet, wrapping back to the beginning if necessary
"""

# note: the string translate() method would be the high-performance solution

import string

# a few handy constanst:
a = ord('a')
z = ord('z')
A = ord('A')
Z = ord('Z')


def rot13a(text):
    """
    my first solution
    """
    # loop through the letters
    new_text = []
    for c in text:
        # do upper and lower case separately
        if c in string.ascii_lowercase:
            o = ord(c) + 13
            if o > z:
                o = a-1 + o-z
        elif c in string.ascii_uppercase:
            o = ord(c) + 13
            if o > Z:
                o = A-1 + o-Z
        else:
            o = ord(c)
        new_text.append(chr(o))
    return "".join(new_text)


def rot13b(text):
    """
    A little smarter to use % to take care of the wrap-around
    """
    # loop through the letters
    new_text = []
    for c in text:
        # do upper and lower case separately
        if c in string.ascii_lowercase:
            o = a + ((ord(c) - a + 13) % 26)
        elif c in string.ascii_uppercase:
            o = A + ((ord(c) - A + 13) % 26)
        else:
            o = ord(c)
        new_text.append(chr(o))
    return "".join(new_text)

# Translation table for i byte string objects:
#   Faster if you build a translation table and use that
#   a translation table needs to be 256 characters long
#   -- all ord vales from 0 to 255

# build a translation table:
str_table = []
# loop through all possible ascii values
for c in range(256):
    # do upper and lower case separately
    if a <= c <= z:
        c = a + (c - a + 13) % 26
    elif A <= c <= Z:
        c = A + (c - A + 13) % 26
    str_table.append(chr(c))
str_table = "".join(str_table)

# Translation table for unicode objects.
#   Unicode has a LOT of code points, so you only specifiy the ones
#   that need changing in a Unicode translation table -- in a dict

uni_table = {}
# the lower-case letters
for c in range(a, z + 1):
    uni_table[c] = a + (c - a + 13) % 26
# the lower-case letters
for c in range(A, Z + 1):
    uni_table[c] = A + (c - A + 13) % 26


def rot13c(text):
    """
    This one uses str.translate() or unicode.translate()
    """
    if type(text) == str:
        return text.translate(str_table)
    elif type(text) == unicode:
        return text.translate(uni_table)


def rot13d(text):
    """This one uses the rot13 encoding provided by the Python Standard Lib
    """
    return text.encode('rot13')


if __name__ == "__main__":
    sample = "Magnetic from outside near corner"
    rot_sample = "Zntargvp sebz bhgfvqr arne pbeare"

    print rot13a(rot_sample)
    print rot13b(rot_sample)
    print rot13c(rot_sample)

    # rot13 should be reversible:

    assert rot13a(rot_sample) == sample

    text = "Some random text to try!"
    assert rot13a(rot13a(text)) == text

    assert rot13a(text) == rot13b(text) == rot13c(text)

    # And a Unicode test:

    text = u"Some random text to try!"
    print rot13a(text)

    assert rot13a(rot13a(text)) == text

    assert rot13a(text) == rot13b(text) == rot13c(text) == rot13d(text)

    print "All assertions pass"


# ## and some timings:
# In [12]: timeit rot13a('This is a pretty short string, but maybe long enough to test')
# 10000 loops, best of 3: 28.9 µs per loop

# In [13]: timeit rot13b('This is a pretty short string, but maybe long enough to test')
# 10000 loops, best of 3: 30.2 µs per loop

# In [14]: timeit rot13c('This is a pretty short string, but maybe long enough to test')
# 1000000 loops, best of 3: 426 ns per loop

# Note that that last one is nanoseconds!

