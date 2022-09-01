#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for k, l in a_dictionary.items():
        a_dictionary[k] = l * 2
    return a_dictionary
