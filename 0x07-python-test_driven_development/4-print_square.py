#!/usr/bin/python3
"""
A function that prints a square with the character #
"""


def print_square(size):
    """
    prints a square with the character #
    Args:
        size - an integer that determines the size length of the square
    raise:
        size must be an integer else raise TypeError.
        size must be greater than zero else raise ValueError.
        size should not be a float and less than zero,
        else raise TypeError.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    if (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
