#!/usr/bin/python3
"""Defines a rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a rectangle class which inherites from basegeometry"""
    def __init__(self, width, height):
        """initializes the width and height """
        self.integer_validatory("width", width)
        self.__width = width
        self.integer_validatory("height", height)
        self.__height = height
