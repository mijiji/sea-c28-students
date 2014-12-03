from __future__ import print_function  # For Python 3 compatibility
from string import maketrans  # To make using str.translate easier

# Refernce alphabet
alphabet = u"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Encrypted alphabet
key13 = u"nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
# Translation table
table13 = maketrans(alphabet, key13)
# Example text
plain_text = u"""For instance, on the planet Earth, man had always assumed that the was more intelligent than dolphins because he had achieved so much - the wheel, New York, wars and so on - whilst all the dolphins had ever done was muck about in the water having a good time. But conversely, the dolphins had always believed that they were far more intelligent than man - for precisely the same reasons."""

# Encryption via str.translate()
print(plain_text)


def rot13_encrypt(text, table):
    """ Encryption via the translate method for strings"""
    encrypted_text = text.translate(table13)
    return encrypted_text

encrypted_text = rot13_encrypt(plain_text, table13)
print(encrypted_text)
