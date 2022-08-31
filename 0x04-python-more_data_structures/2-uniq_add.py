#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    ans = 0
    for i in new_list:
        ans += i
    return ans
