"""
A method to creating new word combinations.

Trigram

Will use 3 adjacent words, the first 2 words will be a key and
the 3rd word will be the possible outcome. Thus its purpose is to create
pseudo books.
"""

import sys
import string
import random
from io import open


def import_text(the_file):
    open_text = open(the_file, 'r')
    read_text = open_text.read()
    text = []
    for word in read_text.split():
        word = word.lower()
        word = word.strip(string.punctuation + string.whitespace)
        word.append(word)
    return text

    trigram = {}
    for i in range(len(text) - 2):
        key = (text[i], text[i + 1])
        if trigram.__contains__(key):
            trigram[key].append(text[i + 2])
        else:
            trigram[key] = text[i + 2]
    return trigram

    new = ''
    for key, variable in trigram.items():
        variable = variable[random.randint(0, len(variable) - 1)]
        new += ' ' + variable
    return new

if __name__ == '__main__':
    def import_text()
