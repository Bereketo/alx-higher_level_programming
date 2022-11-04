#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, var):
        if not isinstance(var, int):
            raise TypeError("width must be an integer")
        if var <= 0:
            raise ValueError("width must be > 0")
        self.__width = var

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, var):
        if not isinstance(var, int):
            raise TypeError("height must be an integer")
        if var <= 0:
            raise ValueError("height must be > 0")
        self.__height = var

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, var):
        if not isinstance(var, int):
            raise TypeError("x must be an integer")
        if var < 0:
            raise ValueError("x must be >= 0")
        self.__x = var

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, var):
        if not isinstance(var, int):
            raise TypeError("y must be an integer")
        if var < 0:
            raise ValueError("y must be >= 0")
        self.__y = var

    def area(self):
        """return the area of the rectangle """
        return self.width * self.height

    def display(self):
        """prints a rectangle with '#' symbol"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        for k in range(self.x):
            print("", end="")
        for m in range(self.y):
            print("")
        for a in range(self.height):
            for b in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """overrides the __str__ method
           to return the rectangle in different format
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute """
        if args and len(args) != 0:
            m = 0
            for arg in args:
                if m = 0:
                    self.id = arg
                elif m = 1:
                    self.width = arg
                elif m = 2:
                    self.height = arg
                elif m = 3:
                    self.x = arg
                elif m = 4:
                    self.y = arg
                m += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
