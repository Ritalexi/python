#!/usr/bin/python3
"""
Module for 1-my_list
"""

class MyList(list):
    """
    A class MyList that inherits from list
    """

    def print_sorted(self):
        """
        Public instance method
        that prints the list, but sorted
        Args: self - list
        """

        print(sorted(self))
