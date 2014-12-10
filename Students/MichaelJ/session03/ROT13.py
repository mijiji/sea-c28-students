"""
A function to encrypt and make codes

ROT13

The function will replace a letter with another letter that is
13 letters away.  It will wrap around the alphabet.
"""

import string

A = ord('A')
Z = ord('Z')
a = ord('a')
z = ord('z')


def rot13(message):
    encrypt = []
    for letter in message:
        if letter in string.ascii_uppercase:
