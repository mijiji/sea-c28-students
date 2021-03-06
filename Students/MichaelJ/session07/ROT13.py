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
            b = A + ((ord(letter) - A + 13) % 26)
        elif letter in string.ascii_lowercase:
            b = a + ((ord(letter) - a + 13) % 26)
        else:
            b = ord(letter)
        encrypt.append(chr(b))
    return "".join(encrypt)

if __name__ == "__main__":

    print rot13("Apple")
    assert rot13("Apple") == "Nccyr"

    print rot13("Hello!")
    assert rot13("Hello1!") == "Uryyb1!"

    print "all tests pass"
