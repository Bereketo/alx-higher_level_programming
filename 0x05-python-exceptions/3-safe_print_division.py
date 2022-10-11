#!/usr/bin/python3

def safe_print_division(a, b):
    """ return a/b
    """
    try:
        res = a/b
    except ZeroDivisonError:
        break
    finally:
        return res
