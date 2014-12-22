"""
A decorator at add to a function.

P-Wrapper decorator

A wrapper to add to a function that returns a string.
"""


def p_wrapper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result = "<p> %n </p>" % result
        return result
    return wrapper


@p_wrapper
def return_a_string(string):
    return string
