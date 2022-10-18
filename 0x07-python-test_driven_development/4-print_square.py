#!/usr/bin/python3
"""Prints a square with a character # """


def print_square(size):
    """ prints a square with a chararcter #
     Args:
        size: size of the length of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
