"""
An example exception to apply in mailroom.

Exceptions, safe_input.py

Creates a function that can generate 2 exceptions.
"""


def safe_input():
    try:
        return raw_input(u"insert text: ")

    except (KeyboardInterrupt, EOFError):
        return None

y = safe_input()

print(y)
