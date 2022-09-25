#!/usr/bin/python3
def no_c(my_string):
    my_string.translate({ord('c'):" "})
    my_string.translate({ord('C'):None})
    return my_string
