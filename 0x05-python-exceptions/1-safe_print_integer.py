#!/usr/bin/python3

def safe_print_integer(value):
    """ prints an integer if
        returns: true if integer, false if not integer
    """
    try:
        print("{:d}".format(value))
    except ValueError:
        break
    else:
       return false

    return  true 
