#!/usr/bin/python3
"""Defines a class and inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """a function that check if obj is instance of a_class
       or if it is inherited from a_class
    """
    if isinstance(obj, a_class) or issubclass(obj, a_class):
        return True
    return False
