#!/usr/bin/python3
""" Defines a derived class Mylist"""


class Mylist(list):
    """ Mylist class which inherits from list parent class """
    def print_sorted(self):
        """ a function that prints a sorted list """
        print(sorted(self))
