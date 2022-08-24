#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        r = "{}".format((number % -10) * -1)
        print(r, end="")
        return(r)
    else:
        r = "{}".format((number % 10))
        print(r, end="")
        return(r)
