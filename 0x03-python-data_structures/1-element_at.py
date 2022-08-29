#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range(0, len(my_list)):
        if (i == (idx - 1):
            return my_list[i]
        elif (idx < 0):
            return ("None")
        elif(idx > len(my_list)):
            return ("None")
