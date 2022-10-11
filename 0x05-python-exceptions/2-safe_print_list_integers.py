#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """ prints the first x elements which are integer
        return
    """
    m = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i], end=""))
            m += 1
        except (IndexError,ValueError, TypeError):
            continue
    print("")
    return m
