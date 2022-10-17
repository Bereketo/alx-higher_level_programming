#!/usr/bin/python3
""" Defines a rectangle class with setter and getter methods """


class Rectangle:
    """a method to initialize """
    def __init__(self, height, width):
        self.__width = width
        self.__height = height

    """ a method to return the width of rectangle """
    def width(self):
        return self.__width

    """ a method to set the width of rectangle"""
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    """ a method to return the height of rectangle  """
    def height(self):
        return self.__height

    """ a method to set the height of rectangle """
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
