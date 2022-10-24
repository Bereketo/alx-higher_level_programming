#!/usr/bin/python3
"""Defines a function to check if an object is an instance """


def is_same_class(obj, a_class):
    """checks if obj is an instance of the class """
    if type(obj) == a_class:
        return True
    return False
