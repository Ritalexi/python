#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        while (i < x):
            print(my_list[i], end="")
            i += 1
        print()
        return x
    except:
        j = 0
        for s in my_list:
            j += 1
        print()
        return j
