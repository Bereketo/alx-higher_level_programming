#!/usr/bin/python3
"""Defines a BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class """
    def area(self):
        """raise an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate value """
        if not isinstance(value, int):
            raise TypeError("{} value must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} value must be greater than 0".format(name))
