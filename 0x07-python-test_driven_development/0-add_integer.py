#!/usr/bin/python3
""" this is "0-add_integer module"
    this module supplies one function which is add(a, b)
"""


def add_integer(a, b=98):

    """ return the sum of two numbers """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b is must be an integer")
    result = int(a) + int(b)
    return result



