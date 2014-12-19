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


error = """Provide file to have white space removed.
If 2nd file is original, the original file will be overwritten.
If 2nd file is a new file, the new file will be written over.
"""


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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(error)
        sys.exit(1)

    elif len(sys.argv) > 2:
        print(error)
        sys.exit(1)

    elif len(sys.argv) == 2:
        original = sys.argv[1]
        try:
            new = sys.argv[2]
        except IndexError:
            new = original

    cleaner(original, new)
