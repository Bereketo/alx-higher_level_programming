#!/usr/bin/python3
"""Defines a Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ a square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """ initializes a new square"""
        super.__init__(size, size, x, y, id)
    @property
    def size(self):
        """get/set size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return the print() and str() representation of the Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.size)
   def update(self, *args, **kwargs)
        """Update the class Square
           *args is the list of arguments - no-keyworded arguments

             1st argument should be the id attribute
             2nd argument should be the size attribute
             3rd argument should be the x attribute
             4th argument should be the y attribute
             **kwargs as key/value (keyworded arguments)
        """
        if args and len(args) != 0:
            m = 0
            for arg in args:
               if m == 0:
                   if arg is None:
                       self.__init__(self.size, self.x, self.y)
                   else:
                       self.id = arg
               elif m == 1:
                   self.size = arg
               elif m == 2:
                   self.x = arg
               elif m == 3:
                   self.y = arg
               m += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y) 
                    else:
                        self.id = v
                elif k == "size"
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
