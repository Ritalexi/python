#!/usr/bin/python3
def safe_print_division(a, b):
    ans = None
    try:
        ans = a / b
        return ans
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(ans))