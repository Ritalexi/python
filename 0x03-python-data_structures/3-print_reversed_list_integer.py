#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lent = len(my_list) - 1
    if not my_list:
        return None
    while (lent >= 0):
        print("{}".format(my_list[lent]))
        lent -= 1
