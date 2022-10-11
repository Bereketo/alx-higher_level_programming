#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """ print x elements of a list
       Returns : number of elements printed
    """
    ans = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i], end=""))
            ans += 1
        except IndexError:
            break
    return ans
