#!/usr/bin/python3
"""Defines a Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ a square class"""

    def __init__(self, size, x=0, y=0, id=None):
        super.__init__(size, size, x, y, id)

    def __str__(self):
        """Return the print() and str() representation of the Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.size)
