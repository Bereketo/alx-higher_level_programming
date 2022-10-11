#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0
    for i in my_list_1 and for j in my_list_2:
        try:
            new_list[i] = i/j
        except IndexError:
            print("out of  range")
        except (TypeError, ValueError):
            print("Wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            new_list[i] = 0
    return new_list
