#!/usr/bin/python3
""" Defines a rectangle class with setter and getter methods """


class Rectangle:
    """a rectangle class with a setter and getter methods """
    def __init__(self, height=0, width=0):
        """ a method to initialize """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ a method to return the width of rectangle """

        return self.__width

    @width.setter
    def width(self, value):
        """ a method to set the width of rectangle"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ a method to return the height of rectangle  """

        return self.__height

    @height.setter
    def height(self, value):
        """ a method to set the height of rectangle """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
