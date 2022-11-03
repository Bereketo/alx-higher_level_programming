#!/usr/bin/python3
""" creating a base class  """


class Base:
   """The base class for other classes in this project
      __nb_objects is a class attribute
   """
    __nb_objects = 0
    def __init__(self, id=None):
        """initializes the base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects + = 1
            self.id =Base.__nb_objects
