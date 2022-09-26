#!/usr/bin/python3
def max_integer(my_list=[]):
    leng = len(my_list)-1
    if len(my_list) == 0:
        return None
    max = my_list[0]
    for i in range(leng):
        if max < my_list[i+1]:
            max = my_list[i]
    return max
