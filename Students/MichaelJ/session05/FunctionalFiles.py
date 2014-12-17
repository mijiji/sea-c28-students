"""
Cleans the file by removing the white space.

Functional Files


Reads through a file and removes leading and trailing wite space
from each file.
"""

import string
import io
import sys
filename = sys.argv[1]


def cleaneer(original, new):
    x = io.open(original).readlines()
    y = map(string.strip, x)

