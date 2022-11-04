#!/usr/bin/python3
""" Defines a class rectangle that inherits from base"""


class Rectangle(Base):
    """a class rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the rectangle
           Args:
             width = width of the rectangle
             height = height of the rectangle
             x     = the x coordinate of the rectangle
             y     = the y coordinate of the rectangle
            id     = the id of the rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """sets/gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TyperError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """sets/gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """sets/gets the x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """sets/gets the y coordintates of the rectangle"""
        return self__.y

    @y.setter
    def y(self, y):
        if not isintance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
