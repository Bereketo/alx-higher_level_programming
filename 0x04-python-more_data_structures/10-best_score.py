#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        maxi = max(a_dictionary.values())
    else:
        return None
    for i in a_dictionary.keys():
        if a_dictionary[i] == maxi:
            return i
