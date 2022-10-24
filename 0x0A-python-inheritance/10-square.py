#!/usr/bin/python3
"""Defines a class square """
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A square class which inherites from rectangle"""
    def __init__(self, size):
        """ initializes size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
