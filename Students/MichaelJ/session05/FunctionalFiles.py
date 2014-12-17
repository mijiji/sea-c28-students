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


def cleaner(original, new):
    x = io.open(original).readlines()
    y = map(string.strip, x)
    newfile = io.open(new, 'whitespaceremoved')
    for text in y:
        newfile.write(text + "\n")


def cleaner2(original, new):
    x = io.open(original).readlines()
    y = [text.strip() + "\n" for text in x]
    io.open(new, "whitespaceremoved").writelines(y)
