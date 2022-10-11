#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 1
        while(i <= x):
            for m in my_list:
                i++
        return i
    except IndexError:
         print("index out of range")
